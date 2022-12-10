import xarray as xr


def mean_seasons(data):
    print("mean season")
    print(data)

    #season_bins = [1,4,7,10,12]
    #seasons_labels=["winter", "spring", "summer", "autumn"]
    #data = data.groupby_bins("time.month", season_bins, labels =seasons_labels).mean()
    groups = data.groupby("time.month")
    keys = groups.groups.keys()
    print(keys)
    for i in keys:
        print(i)
        print(groups[i])
        print("\n")

    return data


def mean_year(data, year):
    data = data.sel(time=slice("{0}-01-01".format(year),"{0}-12-31".format(year)))
    data = data.mean(dim=["time"], skipna=True)

    return data


def calc_height(data, variable, min):
    """Calculate the height of the max/min value of variable
    (for example ozone concentration). Adds these values to dataset"""

    if min == True:
        comparison = data[variable].min(dim=["altitude"])
    else:
        comparison = data[variable].max(dim=["altitude"])
    mask = xr.where(data[variable] == comparison, data["altitude"], 0)

    # reducing with sum()
    altitudes = mask.sum(dim="altitude")
    data = data.assign(altitude_of_interest=altitudes)
    return data
