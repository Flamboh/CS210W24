import json
import matplotlib.pyplot as plt
from pop_stats import *

def plot_pop_data(pop, lat, lon) -> None:
    dot_size = [x/1000 for x in pop]
    plt.scatter(lon, lat, dot_size)
    plt.show()


def plot_hist(data, n_bins=10) -> None:
    plt.hist(data, bins=n_bins)
    plt.show()

if __name__ == "__main__":
    file_name = "population.json"
    
    [pop, lat, lon, growth, dens] = read_data(file_name, \
        ["pop2023", "lat", "lng", "growth", "density"])
    
    plot_pop_data(pop, lat, lon)
    
    pop = filter_arr(pop, 10000)

    plot_hist(dens)

    