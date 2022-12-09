from . import plot
from . import calc
import xarray as xr
import numpy as np




def make_min_max_dataset(data, compute, year, max_bool):
    if compute == "mean":
        data = data.mean(dim=["time"], skipna=True)
    if compute == "mean_seasons":
        data = calc.mean_seasons(data)
    if compute == "year":
        data = calc.mean_year(data, year)

    data = calc.calc_height(data, variable="ozone",max=max_bool)

    print(data.altitude_of_interest)

    plot.plot_world(data.altitude_of_interest)
