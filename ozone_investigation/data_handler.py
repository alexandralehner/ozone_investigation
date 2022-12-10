from . import plot
from . import calc
import xarray as xr
import numpy as np


def make_min_max_dataset(data, compute, year, min_bool):
    if compute == "mean":
        data = data.mean(dim=["time"], skipna=True)
        data = calc.calc_height(data, variable="ozone", min=min_bool)
    if compute == "mean_seasons":
        data = calc.mean_seasons(data)
        #for month in data.coords["month_bins"]:
        #    print(month)
        #    data=calc.calc_height(data.sel(month_bins=month), variable="ozone", min=min_bool)

        #for i in range(0:12)

#    data.coords["time"].values[0].astype(str)[:4]
    if compute == "year":
        data = calc.mean_year(data, year)
        data = calc.calc_height(data, variable="ozone", min=min_bool)

#    data = calc.calc_height(data, variable="ozone", min=min_bool)

    print(data.altitude_of_interest)

    plot.plot_world(data.altitude_of_interest)
