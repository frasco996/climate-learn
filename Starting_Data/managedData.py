import os
import numpy as np
import netCDF4 as nc

base_path_2 = os.path.join('./', '2m_temperature/')
base_path_850 = os.path.join('./', 'temperature_850/')
base_path_500 = os.path.join('./', 'geopotential_500/')
base_path_ru = os.path.join('./', 'relative_humidity/')
base_path_solar = os.path.join('./', 'toa_incident_solar_radiation/')
base_path_temp = os.path.join('./', 'temperature/')  # Path for temperature data
base_path_geo = os.path.join('./', 'geopotential/')  # Assuming a path for geopotential data

# Define the years you want to include
years = range(2013, 2019)

# List to store the data for each year
levels_of_interest = [50, 600, 925]
all_data = []

for year in years:
    file_path_2 = os.path.join(base_path_2, f'2m_temperature_{year}_5.625deg.nc')
    file_path_850 = os.path.join(base_path_850, f'temperature_850hPa_{year}_5.625deg.nc')
    file_path_500 = os.path.join(base_path_500, f'geopotential_500hPa_{year}_5.625deg.nc')
    file_path_ru = os.path.join(base_path_ru, f'relative_humidity_{year}_5.625deg.nc')
    file_path_solar = os.path.join(base_path_solar, f'toa_incident_solar_radiation_{year}_5.625deg.nc')
    file_path_temp = os.path.join(base_path_temp, f'temperature_{year}_5.625deg.nc')
    file_path_geo = os.path.join(base_path_geo, f'geopotential_{year}_5.625deg.nc')  # Assuming this file contains geopotential data at multiple levels

    # Load and process geopotential 500 data
    dataset_500 = nc.Dataset(file_path_500, 'r')
    geopotential_500_data = dataset_500.variables['z'][:]
    geopotential_500_data = geopotential_500_data.filled(np.nan)

    # Load and process temperature 850 data
    dataset_850 = nc.Dataset(file_path_850, 'r')
    temperature_850_data = dataset_850.variables['t'][:]
    temperature_850_data = temperature_850_data.filled(np.nan)

    # Load and process temperature 2m data
    dataset_2 = nc.Dataset(file_path_2, 'r')
    t2m_data = dataset_2.variables['t2m'][:]
    t2m_data = t2m_data.filled(np.nan)

    # Load and process relative humidity data
    dataset_ru = nc.Dataset(file_path_ru, 'r')
    variable = dataset_ru.variables['r']  # shape is (8760, 13, 32, 64)
    levels = dataset_ru.variables['level'][:]  # Assuming this contains level values

    # Identify the indices of the levels you want (e.g., levels 50, 600, 925)
    level_indices = [np.where(levels == lvl)[0][0] for lvl in levels_of_interest]
    sliced_variable = variable[:, level_indices, :, :]

    # Reshape sliced variable data from (8760, 3, 32, 64) to (8760, 3, 32, 64)
    sliced_variable_data = sliced_variable.filled(np.nan)

    # Load and process temperature data at the specified levels
    dataset_temp = nc.Dataset(file_path_temp, 'r')
    temp_variable = dataset_temp.variables['t'][:]  # Assume 'temperature' is the variable name
    temp_levels = dataset_temp.variables['level'][:]  # Levels corresponding to temperature

    # Ensure temperature data has the same levels
    temp_level_indices = [np.where(temp_levels == lvl)[0][0] for lvl in levels_of_interest]
    temp_sliced_variable = temp_variable[:, temp_level_indices, :, :]

    # Reshape temperature data if needed
    temp_sliced_variable_data = temp_sliced_variable.filled(np.nan)
    
    # Load and process geopotential data at the specified levels
    dataset_geo = nc.Dataset(file_path_geo, 'r')
    geo_variable = dataset_geo.variables['z'][:]  # Assume 'z' is the variable name for geopotential
    geo_levels = dataset_geo.variables['level'][:]  # Levels corresponding to geopotential

    # Ensure geopotential data has the same levels
    geo_level_indices = [np.where(geo_levels == lvl)[0][0] for lvl in levels_of_interest]
    geo_sliced_variable = geo_variable[:, geo_level_indices, :, :]

    # Reshape geopotential data if needed
    geo_sliced_variable_data = geo_sliced_variable.filled(np.nan)

    # Load and process TOA incident solar radiation data
    dataset_solar = nc.Dataset(file_path_solar, 'r')
    solar_data = dataset_solar.variables['tisr'][:]
    solar_data = solar_data.filled(np.nan)

    # Combine data along the second dimension (channel dimension)
    combined_data = np.concatenate([geopotential_500_data[:, np.newaxis, :, :],
                                    temperature_850_data[:, np.newaxis, :, :],
                                    t2m_data[:, np.newaxis, :, :],
                                    sliced_variable_data,
                                    temp_sliced_variable_data,
                                    geo_sliced_variable_data,
                                    solar_data[:, np.newaxis, :, :]], axis=1)

    all_data.append(combined_data)

# Combine all years' data into a single NumPy array
reshaped_data = np.concatenate(all_data, axis=0)
np.save('./tensor.npy', reshaped_data)
print("Combined data shape:", reshaped_data.shape)

