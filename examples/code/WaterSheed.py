import sys
sys.path.append('lib/python3')


import argparse
import PIM_T3 # type: ignore

# -- Parser command line arguments
parser = argparse.ArgumentParser(description="Watershed")
parser.add_argument("input_image", help="Input image path")
parser.add_argument("threshold", type=float, help="Threshold")
parser.add_argument("level", type=float, help="Level")
args = parser.parse_args()


try:
    args = parser.parse_args()
except BaseException as e:
    sys.exit(1)

dierick = PIM_T3.WaterSheed(
    input_image_path=args.input_image,
    file_executed=sys.argv[0],
    threshold=args.threshold,
    level=args.level,
)

dierick.watershed_image()