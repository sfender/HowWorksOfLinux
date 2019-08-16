import os.path
import pandas as pd
import numpy as np
import holoviews as hv
import argparse

hv.extension('matplotlib')
parser = argparse.ArgumentParser()

def plot_and_save_cache_access_time_graph(df, filename):
        
    scatter = hv.Scatter(
                    (df.index + 2, df["access"])
                ).opts(
                    xticks=[2,4,6,8,10,12,14,16],   
                    xlabel="memory size: 2x [KB]",
                    ylabel="access time [ns/count]"
                )
    scatter_log = hv.Scatter(
                    (df.index + 2, df["access"])
                ).opts(
                    logy = True, 
                    xticks=[2,4,6,8,10,12,14,16],
                    xlabel="memory size: 2x [KB]",
                    ylabel="log access time [ns/count]"
                )
    access = scatter + scatter_log

    renderer = hv.renderer('matplotlib')
    renderer.save(access, 'cache_access_time')

if __name__ == "__main__":

    parser.add_argument("--filename", type=str, 
                        help="output filename made by cache.c forloop")
    args = parser.parse_args()
    df = pd.read_csv(args.filename, skiprows=0, names=['access'])
    filename, _ = os.path.splitext(args.filename)

    plot_and_save_cache_access_time_graph(df, filename)
