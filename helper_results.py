#!usr/bin/env python3
#
##############################################################################
# AUTHOR(S):    Anna Petrasova
#               Adapted from  FUTURES_v3 case study validation.ipynb. Accessed here:
#               https://colab.research.google.com/drive/1mTEJanqihKwHAAnjhQpfegURq1whnq-G#scrollTo=15pC4nfQldCA
# PURPOSE: Helper functions to report results from FUTURES simulation
#          - Reformats metrics dictionary into pandas dataframe
#          - Plots results as hits, misses and false alarms
#          - and/or plots results as allocation and quantity disagreement
##############################################################################

import pandas as pd
import matplotlib.pyplot as plt


# Function used to create metrics table from dictionary
# takes metrics dictionary as input parameter
def results_table(metrics):
    tab = pd.DataFrame.from_records(metrics)
    tab["hits"] *= 100
    tab["misses"] *= 100
    tab["false_alarms"] *= 100
    tab["figure_of_merit"] *= 100
    tab["null_successes"] *= 100
    tab["initially_developed"] *= 100
    tab["quantity_error"] = tab["misses"] - tab["false_alarms"]
    tab["total_error"] = tab["misses"] + tab["false_alarms"]
    tab["allocation_error"] = tab["total_error"] - tab["quantity_error"]
    return tab


# Function used to plot hits, misses, and false alarms
# takes matplotlib axis, Pandas dataframe, and color object as input params
def plot_hit_miss(ax, tab, cmap):
    width = 0.1
    ax.set_prop_cycle(color=cmap.colors)
    ax.bar([""], tab["misses"].mean(), width, label="Misses")
    ax.bar(
        [""],
        tab["false_alarms"].mean(),
        width,
        bottom=tab["misses"].mean(),
        label="false alarms",
    )
    ax.bar(
        [""],
        tab["hits"].mean(),
        width,
        bottom=tab["misses"].mean() + tab["false_alarms"].mean(),
        label="Hits",
    )
    ax.bar(
        [""],
        tab["null_successes"].mean(),
        width,
        bottom=tab["misses"].mean() + tab["false_alarms"].mean() + tab["hits"].mean(),
        label="Null successes",
    )
    ax.bar(
        [""],
        tab["initially_developed"].mean(),
        width,
        bottom=tab["misses"].mean()
        + tab["false_alarms"].mean()
        + tab["hits"].mean()
        + tab["null_successes"].mean(),
        label="Initially_developed",
    )
    ax.text(-0.03, 1, f'{tab["misses"].mean():.2f}%', color="black")
    ax.text(-0.03, 4.2, f'{tab["false_alarms"].mean():.2f}%', color="black")
    ax.text(0.03, 5.3, f'{tab["hits"].mean():.2f}%', color="black")
    ax.text(-0.03, 45, f'{tab["null_successes"].mean():.2f}%', color="black")
    ax.text(-0.03, 90, f'{tab["initially_developed"].mean():.2f}%', color="black")
    return ax


# Function used to plot quantity and allocation error
# takes matplotlib axis, Pandas dataframe, and color object as input params
def plot_quant_alloc_error(ax, tab):
    cmap = plt.cm.get_cmap("viridis", 3)
    width = 0.1
    ax.set_prop_cycle(color=cmap.colors)
    ax.bar([""], tab["quantity_error"].mean(), width, label="Quantity error")
    ax.bar(
        [""],
        tab["allocation_error"].mean(),
        width,
        bottom=tab["quantity_error"].mean(),
        label="Allocation error",
    )
    ax.text(-0.02, 0.5, f'{tab["quantity_error"].mean():.2f}%', color="black")
    ax.text(-0.02, 2.7, f'{tab["allocation_error"].mean():.2f}%', color="black")
    return ax
