## Setup used for the ALARO 1.3 km version

1. Variables used

| #     |**Abbreviation**       | **Quantity**  | **Vertical Level**    | **In Original Paper** | **Unit**      | **FA-name**   |
|--     |--                     |--             |--                     |--                     |--             |--             |
|1      |`psfc`                 | Pressure      | Surface               | YES                   | Pa            | `SURFPRESSION`  | 
|2      |`mslp`                 | Pressure      | Sea level             | YES                   | Pa            | `MSLPRESSURE`   |
|--     |--                     |--             |--                     |--                     |--             |--             |
|3      |`nlwrs`                | Longwave Radiation flux | Surface     | YES                   | W/m^2         | `SURFFLU.RAY.SOLA`      |
|4      |`nswrs`                | Shortwave Radioation flux | Surface   | YES                   | W/m^2         | `SURFFLU.RAY.THER`      |
|--     |--                     |--             |--                     |--                     |--             |--             |
|5      |`t2m`                  | Temperature   | 2 meter ab. surface   | YES                   | K             | `CLSTEMPERATURE`        |
|6      |`t850`                 | Temperature   | 850 hPa               | YES                   | K             | `P85000TEMPERATUR`      |
|7      |`t500`                 | Temperature   | 500 hPa               | YES                   | K             | `P50000TEMPERATUR`      |
|--     |--                     |--             |--                     |--                     | --            |--                     |
|8      | `u2m`                   | Zonal wind    | 2 meter ab. surface   | NO                    | m/s           | `CLSVENT.ZONAL` |
|9      | `v2m`                   | Meridional wind | 2 meter ab. surface | NO                    | m/s           | `CLSVENT.MERIDIEN`      |
|8      |`u850`                 | Zonal wind    | 850 hPa               | YES                   | m/s           | `P85000VENT_ZONAL`      |
|9      |`v850`                  | Meridional wind       | 850 hPa       | YES                   | m/s           | `P85000VENT_MERID`      |
|--     |--                     |--             |--                     | --                    | --            | --                    |
|10     |`rh2m`                 | Relative Humidity     | 2 meter ab. surface   | YES           | -             | `CLSHUMI.RELATIVE`      |
|--     |--                     |--             |--                     | --                    |--             | --                    |
|11     | `wvint`               | Grid-column integrated water vapour   | All   | YES           | kg/m^2        | `ATMOHUMI TOTALE`       |
|--     |--                     |--             |--                     | --                    |--             | --                    |
|12     | `z1000`               | Geopotential  | 1000 hPa              | YES                   | m^2/s^2       | `P00000GEOPOTENTI`      |
|13     | `z500`                | Geopotential  | 500 hPa               | YES                   | m^2/s^2       | `P85000GEOPOTENTI`      |
