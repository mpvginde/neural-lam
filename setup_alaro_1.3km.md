## Setup used for the ALARO 1.3 km version

1. Variables used

| #     |**Abbreviation**       | **Quantity**  | **Vertical Level**    | **In Original Paper** | **Unit**      | **FA-name**   |
|--     |--                     |--             |--                     |--                     |--             |--             |
|1      |`psfc`                 | Pressure      | Surface               | YES                   | Pa            | `SURFPRESSION`  | 
|2      |`mslp`                 | Pressure      | Sea level             | YES                   | Pa            | `MSLPRESSURE`   |
|--     |--                     |--             |--                     |--                     |--             |--             |
|3      |`dlwrs`                | Downward Longwave Radiation flux | Surface     | NO                   | W/m^2         | `SURFRAYT THER DE`      |
|4      |`dswrs`                | Downward Shortwave Radioation flux | Surface   | NO                   | W/m^2         | `SURFRAYT SOLA DE`      |
|--     |--                     |--             |--                     |--                     |--             |--             |
|5      |`t2m`                  | Temperature   | 2 meter ab. surface   | YES                   | K             | `CLSTEMPERATURE`        |
|6      |`t850`                 | Temperature   | 850 hPa               | YES                   | K             | `P85000TEMPERATUR`      |
|7      |`t500`                 | Temperature   | 500 hPa               | YES                   | K             | `P50000TEMPERATUR`      |
|--     |--                     |--             |--                     |--                     | --            |--                     |
|8      | `u2m`                   | Zonal wind    | 2 meter ab. surface   | NO                    | m/s           | `CLSVENT.ZONAL` |
|10      | `v2m`                   | Meridional wind | 2 meter ab. surface | NO                    | m/s           | `CLSVENT.MERIDIEN`      |
|      |`u850`                 | Zonal wind    | 850 hPa               | YES                   | m/s           | `P85000VENT_ZONAL`      |
|11     |`v850`                  | Meridional wind       | 850 hPa       | YES                   | m/s           | `P85000VENT_MERID`      |
|--     |--                     |--             |--                     | --                    | --            | --                    |
|12     |`rh2m`                 | Relative Humidity     | 2 meter ab. surface   | YES           | -             | `CLSHUMI.RELATIVE`      |
|--     |--                     |--             |--                     | --                    |--             | --                    |
|13     | `cltvi`               | Grid-column integrated precipitable water     | All   | YES           | kg/m^2        | `ATMOHUMI TOTALE`       |
|--     |--                     |--             |--                     | --                    |--             | --                    |
|14     | `z1000`               | Geopotential Height  | 1000 hPa              | NO                   | m       | `P00000GEOPOTENTI`      |
|15     | `z500`                | Geopotential Height  | 500 hPa               | NO                   | m       | `P85000GEOPOTENTI`      |
