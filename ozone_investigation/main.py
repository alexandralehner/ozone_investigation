import argparse
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
        "--compute_height",
        dest="compute_height",
        type=str,
        help="Which data to use for height of max/min level of ozone: "
        "mean=mean over total time range, "
        "mean_seasons=use mean per season for whole time range, "
        "or year=mean over a specific year, further specify with --year",
    )
    parser.add_argument(
        "--year",
        dest="year",
        type=str,
        required=False,
        help="Include a specific year, "
        "for example '1991' when using '--compute year'",
    )
    parser.add_argument(
        "--min",
        dest="min",
        action="store_true",
        help="plot minimum value? " "Else, maximum value is used for calculations",
    )

    parser.add_argument(
        "--vertical_global",
        dest="vertical_global",
        action="store_true",
        help="Compute and plot global vertical profiles of mean ozone concentration?",
    )
    parser.add_argument(
        "--vertical_tropical",
        dest="vertical_tropical",
        action="store_true",
        help="Compute and plot tropical vertical profiles of mean ozone concentration?",
    )
    parser.add_argument(
        "--vertical_highlat",
        dest="vertical_highlat",
        action="store_true",
        help="Compute and plot vertical profiles of mean ozone concentration in the high latitudes?",
    )
    parser.add_argument(
        "--vertical_midlat",
        dest="vertical_midlat",
        action="store_true",
        help="Compute and plot vertical profiles of mean ozone concentration in the mid latitudes?",
    )
    parser.add_argument(
        "--seasonal_pattern",
        dest="seasonal_pattern",
        type=str,
        required=False,
        help="Plot seasonal patterns as a time series - specify season: "
        "winter, spring, summer, autumn, all",
    )

    args = parser.parse_args()

    if not Path(args.file).exists():
        parser.error(f"File {args.file} does not exist.")

    filename = args.file
    # breakpoint()
    data = file_handler.read_in_file(filename)

    first_year = data.coords["time"].values[0].astype(str)[:4]
    last_year = data.coords["time"].values[-1].astype(str)[:4]
    if args.compute_height == "year":
        if args.year is None:
            parser.error("No year given. Please try again and specify year with --year")
        if int(args.year) < int(first_year) or int(args.year) > int(last_year):
            parser.error(
                "Year given does not exist in the dataset. "
                "Please try again with a year between {0} and {1}".format(
                    first_year, last_year
                )
            )
        else:
            data_handler.height_year(data, args.year, args.min)
    elif args.compute_height == "mean":
        data_handler.height_mean(data, args.min)
    elif args.compute_height == "mean_seasons":
        data_handler.height_mean_seasons(data, args.min)
    elif (
        args.vertical_global
        or args.vertical_tropical
        or args.vertical_highlat
        or args.vertical_midlat
    ):
        data_handler.vertical_concentrations(
            data,
            args.vertical_global,
            args.vertical_tropical,
            args.vertical_highlat,
            args.vertical_midlat,
        )
    elif args.seasonal_pattern is not None:
        data_handler.seasonal_concentrations(data, args.seasonal_pattern)
    else:
        parser.error(
            "There was an error with your request. " "Check your spelling and try again"
        )
