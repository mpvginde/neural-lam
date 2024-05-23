## Setup used for the ALARO 1.3 km version

1. Variables used

| #     |**Abbreviation**       | **Quantity**  | **Vertical Level**    | **In Original Paper** | **Unit**      | **FA-name**   |
|--     |--                     |--             |--                     |--                     |--             |--             |
|1      |`sp`                   | Pressure      | Surface               | YES                   | Pa            | `SURFPRESSION`  | 
|2      |`msl`                  | Pressure      | Sea level             | YES                   | Pa            | `MSLPRESSURE`   |
|--     |--                     |--             |--                     |--                     |--             |--             |
|3      |`strd`                 | Downward Longwave Radiation flux | Surface     | NO                   | W/m^2         | `SURFRAYT THER DE`      |
|4      |`ssrt`                 | Downward Shortwave Radioation flux | Surface   | NO                   | W/m^2         | `SURFRAYT SOLA DE`      |
|--     |--                     |--             |--                     |--                     |--             |--             |
|5      |`rh2m`                 | Relative Humidity     | 2 meter ab. surface   | YES           | -             | `CLSHUMI.RELATIVE`      |
|6      |`rh925`                | Relative Humidity     | 2 meter ab. surface   | YES           | -             | `CLSHUMI.RELATIVE`      |
|--     |--                     |--             |--                     | --                    | --            | --                    |
|7      |`t2m`                  | Temperature   | 2 meter ab. surface   | YES                   | K             | `CLSTEMPERATURE`        |
|8      |`t925`                 | Temperature   | 2 meter ab. surface   | YES                   | K             | `CLSTEMPERATURE`        |
|9      |`t850`                 | Temperature   | 850 hPa               | YES                   | K             | `P85000TEMPERATUR`      |
|10     |`t500`                 | Temperature   | 500 hPa               | YES                   | K             | `P50000TEMPERATUR`      |
|--     |--                     |--             |--                     |--                     | --            |--                     |
|11     |`u2m`                  | Zonal wind    | 2 meter ab. surface   | NO                    | m/s           | `CLSVENT.ZONAL` |
|12     |`u850`                 | Zonal wind    | 850 hPa               | YES                   | m/s           | `P85000VENT_ZONAL`      |
|13     |`v2m`                  | Meridional wind | 2 meter ab. surface | NO                    | m/s           | `CLSVENT.MERIDIEN`      |
|14     |`v850`                 | Meridional wind       | 850 hPa       | YES                   | m/s           | `P85000VENT_MERID`      |
|--     |--                     |--             |--                     | --                    |--             | --                    |
|15     | `cltvi`               | Grid-column integrated precipitable water     | All   | YES           | kg/m^2        | `ATMOHUMI TOTALE`       |
|--     |--                     |--             |--                     | --                    |--             | --                    |
|16     | `z1000`               | Geopotential Height  | 1000 hPa              | NO                   | m       | `P00000GEOPOTENTI`      |
|17     | `z500`                | Geopotential Height  | 500 hPa               | NO                   | m       | `P85000GEOPOTENTI`      |
