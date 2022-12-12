import xarray as xr


def calc_height(data, variable, min):
    """Calculate the height of the max/min value of variable
    (for example ozone concentration). Adds these values to dataset"""

    if min:
        comparison = data[variable].min(dim=["altitude"])
        minmax = "min"
    else:
        comparison = data[variable].max(dim=["altitude"])
        minmax = "max"
    mask = xr.where(data[variable] == comparison, data["altitude"], 0)

    # reducing with sum()
    altitudes = mask.sum(dim="altitude")
    data = data.assign(altitude_of_interest=altitudes)
    data.altitude_of_interest.attrs[
        "long_name"
    ] = "Altitude of {0} ozone concentration above geoid".format(minmax)
    return data


def group_seasons(data):
    season_bins = [1, 4, 7, 10, 12]
    season_labels = ["winter", "spring", "summer", "autumn"]
    data = data.groupby_bins(
        "time.month", season_bins, labels=season_labels
    ).mean()
    return data


def mean_seasons(data, min_bool):
    seasonal_data = []
    for coordinate, sub_arr in data.groupby("month_bins"):
        data_mean = sub_arr.mean(dim=["month_bins"], skipna=True)
        data_height = calc_height(data_mean, variable="ozone", min=min_bool)
        data_height.attrs["season"] = coordinate
        seasonal_data.append(data_height)
    return seasonal_data


def mean_year(data, year):
    data = data.sel(
        time=slice("{0}-01-01".format(year), "{0}-12-31".format(year))
    )
    data = data.mean(dim=["time"], skipna=True)

    return data

def mean_vertical(data, latitudes):
    data_selection = data.sel(latitude_bins=latitudes)
    data_mean = data_selection.mean(
        dim=["latitude_bins", "longitude_bins"], skipna=True)
    return data_mean