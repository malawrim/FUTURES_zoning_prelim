# FUTURES_zoning_prelim
Repository for scripts to run FUTURES for written preliminary exam

GRASS location information
name: FUTURES_zoning_prelim
epsg:32119 (NAD83/NC)

Description of Contents:  

Helper scripts
- helper.py
    - Contains helper functions written by Anna Petrasova to initialize GRASS environment and display GRASS maps in Jupyter Notebook either statically or interactively
- validation.py
    - Development version of GRASS tool r.futures.validation written by Anna Petrasova to compute validation metrics from FUTURES simulation including hits, misses, allocation disagreement, - quantity disagreement
- pop_clean.py
    - Process population data for usage in FUTURES simulation (DEMAND submodule). Exports two .csv files with historical population trend and population projections
Pre-processing
- futures_preprocess.ipynb
    - Used to process necessary predictors for FUTURES simulations (including slope, land cover composition, transportation, and zoning)
    - Calculate development pressure based on historical development patterns
FUTURES simulation
- futures_potential.ipynb
    - Computes FUTURES POTENTIAL submodel. Includes parameterization under three scenarios of available predictors (no zoning predictor, core-district zoning predictors, sub-district zoning predictors).
- futures_demand.ipynb
    - Computes FUTURES DEMAND submodel. Calculates demand based on population and development data from 2001-2011.
futures_pga.ipynb
    - Computes FUTURES simulation (Patch Growth Algorithm; PGA). Includes calibration of patch characteristics, FUTURES simulation, and exporting of results.
Post-processing
- Futures_postprocess.ipynb
    - Report results from FUTURES simulations. Compares results with and without zoning predictors.
Environment
- futures_zoning.yml - conda environment for FUTURES simulations (does not work on Windows with GRASS and Jupyter Notebook)

GRASS_Jupyter_Windows_VSCode.mov - Instructional video for running GRASS through Jupyter Notebook on Windows in VS Code 
