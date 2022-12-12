from . import plot
from . import calc
import xarray as xr


def height_year(data, year, min_bool):
    data = calc.mean_year(data, year)
    data_yearly_height = calc.calc_height(data, variable="ozone", min=min_bool)
    plot.singleplot(
        data_yearly_height.altitude_of_interest,
        "Mean over year {0}".format(year),
    )


def height_mean(data, min_bool):
    data_mean = data.mean(dim=["time"], skipna=True)
    data_height = calc.calc_height(data_mean, variable="ozone", min=min_bool)
    plot.singleplot(data_height.altitude_of_interest, "Mean over whole time")


def height_mean_seasons(data, min_bool):
    seasonal_data = calc.group_seasons(data)
    data_seasonal_heights = calc.mean_seasons(seasonal_data, min_bool)
    plot.multiplot(data_seasonal_heights, "season")


def vertical_concentrations(data, glob, trop, highlat, midlat):
    # global, tropics, high latitude,mid-lats

    if glob:
        data_global_mean = calc.mean_vertical(data, slice(-90, 90))
        plot.plot_vertical(data_global_mean, "Global vertical profile")

    if trop:
        data_tr_mean = calc.mean_vertical(data, slice(-23.43631, 23.43631))
        plot.plot_vertical(data_tr_mean, "Vertical profile for tropics")

    if highlat:
        data_highlat1 = data.sel(latitude_bins=slice(-90, -66.55))
        data_highlat2 = data.sel(latitude_bins=slice(66.55, 90))
        data_highlat = xr.merge([data_highlat1, data_highlat2])
        data_highlat_mean = calc.mean_vertical(data_highlat, slice(-90, 90))
        plot.plot_vertical(data_highlat_mean, "Vertical profile for high latitudes")

    if midlat:
        data_midlat_mean = calc.mean_vertical(data, slice(-66.55, 66.55))
        plot.plot_vertical(data_midlat_mean, "Vertical profile for mid-latitudes")


def seasonal_concentrations(data, season):
    # group by seasons since 1991
    dict_season = {
        "winter": [12, 1, 2],
        "spring": [3, 4, 5],
        "summer": [6, 7, 8],
        "autumn": [9, 10, 11],
    }

    # selecting nothern polar circle, which includes the ozone hole
    data = data.sel(latitude_bins=slice(66.55, 90))
    data = data.mean(dim=["altitude", "latitude_bins", "longitude_bins"], skipna=True)

    if season == "all":
        plot.plot_timeseries(data.ozone, "Northern polar circle, all seasons")

    # seasons:
    else:
        season_data = data.sel(time=data.time.dt.month.isin(dict_season[season]))
        plot.plot_timeseries(
            season_data.ozone, "Northern polar circle, {0}".format(season)
        )
