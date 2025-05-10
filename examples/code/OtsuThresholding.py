import sys
sys.path.append('lib/python3')


import argparse
import PIM_T3 # type: ignore

# -- Parser command line arguments
parser = argparse.ArgumentParser(description="Otsu thresholding")
parser.add_argument("input_image", help="Input image path")
parser.add_argument("num_bins", type=int, help="Number of bins")
parser.add_argument("num_thresholds", type=int, help="Number of thresholds")
parser.add_argument("label_offset", type=float, help="label offset")
args = parser.parse_args()


try:
    args = parser.parse_args()
except BaseException as e:
    sys.exit(1)

dierick = PIM_T3.OtsuThresholding(
    input_image_path=args.input_image,
    file_executed=sys.argv[0],
    num_bins=args.num_bins,
    label_offset=args.label_offset,
    num_thresholds=args.num_thresholds,
)

dierick.otsu_threshold_image()