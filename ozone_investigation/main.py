import argparse
import numpy as np
from pathlib import Path
from . import file_handler
from . import data_handler


def entry_point():
    """Entry point for the project"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        dest="file",
        type=str,
        required=True,
        help="path to netCDF-file with climate data",
    )

    parser.add_argument(
        "--plot_heights",
        dest="plot_heights",
        action="store_true",
        help="Plot the height of the max/min level of ozone? Further specify with --max, else minimum levels are used"
    )

    parser.add_argument(
        "--max",
        dest="max",
        action="store_true",
        help="plot maximum value? If False, minimum value is used for calculations"
    )

    parser.add_argument(
        "--plot_vertical",
        dest="plot_vertical",
        action="store_true",
        help="Plot vertical profiles of mean ozone concentration?"
    )
    parser.add_argument(
        "--plot_seasonal_pattern",
        dest="plot_seasonal_pattern",
        action="store_true",
        help="Plot seasonal patterns as a time series?"
    )
    parser.add_argument(
        "--compute",
        dest="compute",
        type=str,
        required=True,
        help="Which data to use: mean=mean over total time range, mean_seasons=use mean over 4 seasons, or year=mean over a specific year, specify with --year"
    )
    parser.add_argument(
        "--year",
        dest="year",
        type=str,
        required=False,
        help="Include a specific year, for example '1991' when using '--compute year'"
    )
    args = parser.parse_args()

    if not Path(args.file).exists():
            parser.error(f"File {args.file} does not exist.")

    filename = args.file
    # breakpoint()
    data = file_handler.read_in_file(filename)

    if args.compute=="year":
        if (args.year is None):
            parser.error("No year given. Please try again.")
    data_handler.make_min_max_dataset(data, args.compute, args.year, args.max)
