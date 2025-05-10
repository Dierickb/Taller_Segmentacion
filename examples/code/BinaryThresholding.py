import sys
sys.path.append('lib/python3')


import argparse
import PIM_T3 # type: ignore

# -- Parser command line arguments
parser = argparse.ArgumentParser(description="Binary Thresholding")
parser.add_argument("input_image", help="Input image path")
parser.add_argument("lower_threshold", type=float, help="Lower threshold")
parser.add_argument("upper_threshold", type=float, help="Upper threshold")
parser.add_argument("outside_value", type=int, help="Outside value")
parser.add_argument("inside_value", type=int, help="Inside value")
args = parser.parse_args()


try:
    args = parser.parse_args()
except BaseException as e:
    sys.exit(1)

filtro = PIM_T3.BinaryThresholding(
    input_image_path=args.input_image,
    lower_threshold=args.lower_threshold,
    upper_threshold=args.upper_threshold,
    outside_value=args.outside_value,
    inside_value=args.inside_value,
    file_executed=sys.argv[0]
)

filtro.threshold_image()