import sys
sys.path.append('lib/python3')

import argparse
import PIM_T3  # type: ignore

# -----------------------------
# Parser de argumentos
# -----------------------------
parser = argparse.ArgumentParser(description="Fast Marching Segmentation")

parser.add_argument("input_image", help="Ruta de la imagen de entrada")
parser.add_argument("sigma", type=float, help="Sigma para el filtro de gradiente")
parser.add_argument("x", type=int, help="Coordenada X de la semilla")
parser.add_argument("y", type=int, help="Coordenada Y de la semilla")
parser.add_argument("z", type=int, help="Coordenada Z de la semilla")
parser.add_argument("stopping_value", type=float, help="Valor de parada para el fast marching")
parser.add_argument("time_threshold", type=float, help="Umbral para el filtro binario")

# Opcionales: sigmoide
parser.add_argument("--alpha_sigmoid", type=float, default=None, help="Valor de alpha para el sigmoide (por defecto auto)")
parser.add_argument("--beta_sigmoid", type=float, default=None, help="Valor de beta para el sigmoide (por defecto auto)")
parser.add_argument("--auto_sigmoid", action="store_true", help="Activar ajuste automático de alpha y beta")

# Opcional: salida
parser.add_argument("--printing", action="store_true", help="Imprimir información de procesamiento")

# -----------------------------
# Ejecutar filtro
# -----------------------------
try:
    args = parser.parse_args()
except Exception as e:
    print(f"Error en argumentos: {e}")
    sys.exit(1)

filtro = PIM_T3.FastMarchingImageFilter(
    input_image_path=args.input_image,
    file_executed=sys.argv[0],
    sigma=args.sigma,
    alpha_sigmoid=args.alpha_sigmoid,
    beta_sigmoid=args.beta_sigmoid,
    x_position=args.x,
    y_position=args.y,
    z_position=args.z,
    stop=args.stopping_value,
    time_threshold=args.time_threshold,
    auto_sigmoid=args.auto_sigmoid,
    printing=args.printing
)

filtro.fast_marching_image()
