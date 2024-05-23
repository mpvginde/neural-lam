# Third-party
import cartopy
import numpy as np

WANDB_PROJECT = "neural-lam"

SECONDS_IN_YEAR = (
    365 * 24 * 60 * 60
)  # Assuming no leap years in dataset (2024 is next)

# Log prediction error for these lead times
VAL_STEP_LOG_ERRORS = np.array([1, 2, 3, 5, 10, 15, 19])

# Log these metrics to wandb as scalar values for
# specific variables and lead times
# List of metrics to watch, including any prefix (e.g. val_rmse)
METRICS_WATCH = []
# Dict with variables and lead times to log watched metrics for
# Format is a dictionary that maps from a variable index to
# a list of lead time steps
VAR_LEADS_METRICS_WATCH = {
    6: [2, 19],  # t_2
    14: [2, 19],  # wvint_0
    15: [2, 19],  # z_1000
}

# Variable names
PARAM_NAMES = [
    "pres_heightAboveGround_0_instant",
    "pres_heightAboveSea_0_instant",
    "strd_heightAboveGround_0_accum",
    "ssrd_heightAboveGround_0_accum",
    "r_heightAboveGround_2_instant",
    "r_isobaricInhPa_925_instant",
    "t_heightAboveGround_2_instant",
    "t_isobaricInhPa_925_instant",
    "t_isobaricInhPa_850_instant",
    "t_isobaricInhPa_500_instant",
    "u_heightAboveGround_2_instant",
    "u_isobaricInhPa_850_instant",
    "v_heightAboveGround_2_instant",
    "v_isobaricInhPa_850_instant",
    "tcolw_entireAtmosphere_0_instant",
    "z_isobaricInhPa_1000_instant",
    "z_isobaricInhPa_500_instant",
]

PARAM_NAMES_SHORT = [
    "sp",
    "msl",
    "strd",
    "ssrd",
    "rh2m",
    "rh925",
    "t2m",
    "t925",
    "t850",
    "t500",
    "u2m",
    "u850",
    "v2m",
    "v850",
    "tcolw",
    "z1000",
    "z500",
]
PARAM_UNITS = [
    "Pa",
    "Pa",
    "W/m\\textsuperscript{2}",
    "W/m\\textsuperscript{2}",
    "-",  # unitless
    "-",
    "K",
    "K",
    "K",
    "K",
    "m/s",
    "m/s",
    "m/s",
    "m/s",
    "kg/m\\textsuperscript{2}",
    "m\\textsuperscript{2}/s\\textsuperscript{2}",
    "m\\textsuperscript{2}/s\\textsuperscript{2}",
]

# Projection and grid
# Hard coded for now, but should eventually be part of dataset desc. files
GRID_SHAPE = (548, 548)  # (y, x)

LAMBERT_PROJ_PARAMS = {
    "a": 6371229,
    "b": 6371229,
    "lat_0": 50.8,
    "lat_1": 50.8,
    "lat_2": 50.8,
    "lon_0": 4.55,
    "proj": "lcc",
}

GRID_LIMITS = [  # In projection
    -355550,  # min x
    355550,  # max x
    -355550,  # min y
    355550,  # max y
]

# Create projection
LAMBERT_PROJ = cartopy.crs.LambertConformal(
    central_longitude=LAMBERT_PROJ_PARAMS["lon_0"],
    central_latitude=LAMBERT_PROJ_PARAMS["lat_0"],
    standard_parallels=(
        LAMBERT_PROJ_PARAMS["lat_1"],
        LAMBERT_PROJ_PARAMS["lat_2"],
    ),
)

# Data dimensions
GRID_FORCING_DIM = 5 * 3 + 1  # 5 feat. for 3 time-step window + 1 batch-static
GRID_STATE_DIM = 17
