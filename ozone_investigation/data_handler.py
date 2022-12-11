from . import plot
from . import calc
import xarray as xr
import numpy as np

def  height_year(data,year,min_bool):
    data = calc.mean_year(data, year)
    data_yearly_height = calc.calc_height(data, variable="ozone", min=min_bool)
    plot.singleplot(data_yearly_height.altitude_of_interest, "Mean over year {0}".format(year))
def height_mean(data, min_bool):
    data_mean = data.mean(dim=["time"], skipna=True)
    data_height = calc.calc_height(data_mean, variable="ozone", min=min_bool)
    plot.singleplot(data_height.altitude_of_interest, "Mean over whole time")
def height_mean_seasons(data, min_bool):
    seasonal_data = calc.group_seasons(data)
    data_seasonal_heights = calc.mean_seasons(seasonal_data, min_bool)
    plot.multiplot(data_seasonal_heights, "season")
def vertical_concentrations(data):
    #global, tropics, high latitude,mid-lats
    print(data)
    data_global = data.mean(dim=["latitude_bins","longitude_bins"], skipna=True)
    print(data_global)
    plot.plot_vertical(data_global)