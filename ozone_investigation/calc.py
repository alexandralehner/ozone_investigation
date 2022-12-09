import xarray as xr


def mean_seasons(data):
    return data

def mean_year(data, year):
    print(year)
    return data
def calc_height(data, variable, max):
    '''Calculate the height of the max/min value of variable
    (for example ozone concentration). Adds these values to dataset'''

    if max==True:
        comparison = data[variable].max(dim=["altitude"])
    else:
        comparison = data[variable].min(dim=["altitude"])
    mask = xr.where(data[variable] ==
                          comparison,
                          data["altitude"], 0)

    # reducing with sum()
    altitudes = mask.sum(dim="altitude")
    data = data.assign(altitude_of_interest=altitudes)
    return data

