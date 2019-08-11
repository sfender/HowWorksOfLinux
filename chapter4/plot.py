import os.path
import pandas as pd
import numpy as np
import holoviews as hv
import argparse

hv.extension('bokeh')
parser = argparse.ArgumentParser()

def plot_and_save_process_graph(holoviews_table, filename):
    '''plot and save process graph from outout file made by loop.py
    '''

    process = hv.Scatter(holoviews_table, 'ms', 'process')
    renderer = hv.renderer('matplotlib')
    renderer.save(process, 'process_' + filename)

if __name__ == "__main__":

    parser.add_argument("--filename", type=str, 
                        help="output filename made by loop.py")
    args = parser.parse_args()

    df = pd.read_csv(args.filename, delimiter='\t', skiprows=2, names=['process', 'ms', 'progress'])
    tab = hv.Table(df)
    filename, _ = os.path.splitext(args.filename)

    plot_and_save_process_graph(tab, filename)
