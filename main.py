import argparse
import os
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SCENES_DIR = PROJECT_ROOT / "src" / "scenes"
MEDIA_DIR = PROJECT_ROOT / "media" / "videos"

SCENE_MAP = {
    "1": ("scene1_riemann_motivation.py", "Scene1RiemannMotivation", "Paso 1: Sumas de Riemann"),
    "2": ("scene2_accumulation_tfc1.py", "Scene2AccumulationTFC1", "Paso 2: Acumulación y TFC 1"),
    "3": ("scene3_antiderivative_theory.py", "Scene3AntiderivativeTheory", "Paso 3: Familia de Antiderivadas"),
    "4": ("scene4_barrow_deduction.py", "Scene4BarrowDeduction", "Paso 4: Deducción de Barrow (TFC II)"),
    "5": ("scene5_example_calculation.py", "Scene5ExampleCalculation", "Paso 5: Ejemplo Numérico y Verificación"),
}

QUALITY_FLAGS = {
    "low": "-ql",
    "med": "-qm",
    "high": "-qh",
}

QUALITY_SUBFOLDERS = {
    "low": "480p15",
    "med": "720p30",
    "high": "1080p60",
}

def render_scene(key: str, quality: str = "med", preview: bool = False) -> bool:
    if key not in SCENE_MAP:
        print(f"[ERROR] Escena '{key}' no reconocida.")
        return False

    script_name, class_name, description = SCENE_MAP[key]
    script_path = SCENES_DIR / script_name
    q_flag = QUALITY_FLAGS.get(quality, "-qm")

    cmd = ["uv", "run", "manim", q_flag]
    if preview:
        cmd.append("-p")
    cmd.extend([str(script_path), class_name])

    print(f"\n🎬 Renderizando: {description}")
    print(f"   Clase: {class_name} | Calidad: {quality} ({q_flag})\n")

    env = {**os.environ, "PYTHONPATH": str(PROJECT_ROOT)}
    result = subprocess.run(cmd, cwd=str(PROJECT_ROOT), env=env)
    return result.returncode == 0

def render_all(quality: str = "med") -> bool:
    print(f"\n🚀 Iniciando renderizado secuencial (calidad: {quality})...")
    for key in sorted(SCENE_MAP.keys()):
        if not render_scene(key, quality=quality, preview=False):
            print(f"[ALERTA] Falló el renderizado de la escena {key}.")
            return False
    print("\n✅ ¡Todas las escenas fueron renderizadas exitosamente!")
    return True

def merge_scenes(quality: str = "med") -> None:
    subfolder = QUALITY_SUBFOLDERS.get(quality, "720p30")
    video_files = []

    for key in sorted(SCENE_MAP.keys()):
        script_name, class_name, _ = SCENE_MAP[key]
        module_name = script_name.replace(".py", "")
        expected_path = MEDIA_DIR / module_name / subfolder / f"{class_name}.mp4"

        if not expected_path.exists():
            print(f"[ERROR] Archivo no encontrado: {expected_path}")
            print("Renderice las escenas primero ejecutando: uv run python main.py --all")
            return

        video_files.append(expected_path)

    concat_file = PROJECT_ROOT / "concat_list.txt"
    concat_file.write_text("\n".join(f"file '{v.resolve()}'" for v in video_files) + "\n")

    output_file = PROJECT_ROOT / f"MAT1188_Grupo9_EID_Completo_{quality}.mp4"
    print(f"\n🎞️ Concatenando escenas en: {output_file}")

    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(output_file)
    ]
    result = subprocess.run(cmd)

    if concat_file.exists():
        concat_file.unlink()

    if result.returncode == 0:
        print(f"✨ ¡Video final generado con éxito!: {output_file}")
    else:
        print("❌ Error al unir los videos con ffmpeg.")

def main() -> None:
    parser = argparse.ArgumentParser(description="Orquestador de Manim para MAT1188-EID Grupo 9")
    parser.add_argument("--scene", "-s", choices=["1", "2", "3", "4", "5"], help="Número de escena (1-5)")
    parser.add_argument("--all", "-a", action="store_true", help="Renderizar todas las escenas en lote")
    parser.add_argument("--quality", "-q", choices=["low", "med", "high"], default="med", help="Calidad del video")
    parser.add_argument("--preview", "-p", action="store_true", help="Abrir reproductor al finalizar")
    parser.add_argument("--merge", "-m", action="store_true", help="Unir escenas renderizadas en MP4 final")

    args = parser.parse_args()

    if args.merge:
        merge_scenes(quality=args.quality)
    elif args.all:
        render_all(quality=args.quality)
    elif args.scene:
        render_scene(args.scene, quality=args.quality, preview=args.preview)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

