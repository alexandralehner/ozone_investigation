import argparse
from . import file_handler
from . import data_handler


def entry_point():
    """Entry point for the project"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file",
        required=True,
        type=str,
        help="path to netCDF-file with climate data",
    )
    args = parser.parse_args()
    filename = args.file
    #breakpoint()
    data = file_handler.read_in_file(filename)

    data_handler.maxozone(data)
