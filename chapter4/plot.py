import os.path
import pandas as pd
import numpy as np
import holoviews as hv
import argparse

hv.extension('bokeh')
parser = argparse.ArgumentParser()

def plot_and_save_process_graph(holoviews_table, filename):
    '''plot and save process graph from output file made by loop.py
    '''

    process = hv.Scatter(holoviews_table, 'ms', 'process')
    renderer = hv.renderer('matplotlib')
    renderer.save(process, 'process_' + filename)

def plot_and_save_progress_graph(holoviews_table, filename, process_list):
    '''plot and save process graph from output file made by loop.py
    '''

    progress_dict = {process:hv.Scatter(holoviews_table.select(process=process), 'ms', 'progress')
                        for process in process_list}
    ndoverlay = hv.NdOverlay(progress_dict, kdims='process')
    renderer = hv.renderer('matplotlib')
    renderer.save(ndoverlay, 'progress_' + filename)

if __name__ == "__main__":

    parser.add_argument("--filename", type=str, 
                        help="output filename made by loop.py")
    args = parser.parse_args()

    df = pd.read_csv(args.filename, delimiter='\t', skiprows=2, names=['process', 'ms', 'progress'])
    process_list = df['process'].unique().tolist()
    holoviews_table = hv.Table(df)
    filename, _ = os.path.splitext(args.filename)

    plot_and_save_process_graph(holoviews_table, filename)
    plot_and_save_progress_graph(holoviews_table, filename, process_list)
