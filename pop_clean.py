#!usr/bin/env python3
########################################
# PURPOSE:
#       Process population data for usage in FUTURES simulation (DEMAND submodule)
#       Exports two .csv files with historical population trend and population projections
# USAGE:
#       python pop_clean.py
#       --sim_start [start year of simulation]
#       --sim_end [end year of simulation]
#       --study_area [string of counties to be included separated by comma]
#       --wd [working directory, location of population inputs and outputs]
#       ex: python pop_clean.py --sim_start 2012 --sim_end 2021 --study_area "37,63,101,105,125,135,183" --wd "D:\\Zoning_Development\\input_data"
# ASSUMPTIONS:
#       Population and counties located in North Carolina (FIPS = 37)
#       NLCD years based on data availability in November, 2023
########################################

import pandas as pd
import os
import argparse

# available NLCD years
nlcd_years = [2001, 2004, 2006, 2008, 2011, 2013, 2016, 2019, 2021]


# Custom argument to parse string of counties into list of integers
def list_of_int(arg):
    return list(map(int, arg.split(",")))


# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add an argument for the list of strings
parser.add_argument("--sim_start", type=int)
parser.add_argument("--sim_end", type=int)
parser.add_argument("--study_area", type=list_of_int)
parser.add_argument("--wd", type=str)

# Parse the command-line arguments
args = parser.parse_args()

# save arguments
counties = args.study_area
sim_start = args.sim_start
sim_end = args.sim_end
wd = args.wd

train_years = [yr for yr in nlcd_years if yr < sim_start]

pop = pd.read_csv(os.path.join(wd, "population.csv"))

pop["fips"] = pop["fips"].astype("string")

# '^' indicates start of string so we don't delete 37 in FIPS such as 37037
pop = pop.replace("^37", "", regex=True)

# limit to necessary columns
pop_subset = pop[["fips", "total", "year"]]

# turn back into int
pop_subset.loc[:, "fips"] = pop_subset["fips"].astype("int64")

# reshape table to have column for each county and row for each year
pop_pivot = pop_subset.pivot_table(index="year", columns="fips", values="total")

# export population projection
pop_pivot.loc[sim_start:sim_end, counties].to_csv(
    os.path.join(wd, "population_projection_test.csv")
)

# export population trend
pop_pivot.loc[train_years, counties].to_csv(
    os.path.join(wd, "population_trend_test.csv")
)
