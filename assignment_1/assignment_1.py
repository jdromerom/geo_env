# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pdb
import xarray as xr


# Loading the dataset using xarray
dset = xr.open_dataset(r'../data/N21E039.SRTMGL1_NC.nc')  # Opening a NetCDF file containing DEM data

# Setting a breakpoint for debugging
pdb.set_trace()  # The execution will pause here, allowing for interactive debugging

# Extracting the DEM (Digital Elevation Model) data from the dataset(dset)
DEM = np.array(dset.variables['SRTMGL1_DEM'])  # Converting the DEM data to a NumPy array
print('DEM shape:', DEM.shape)  # Printing the shape of the DEM data

# Setting another breakpoint for debugging
pdb.set_trace() 

# Plotting the DEM data
plt.imshow(DEM)                 
cbar = plt.colorbar()           
cbar.set_label('Elevation (m asl)')  

# Displaying and saving the plot
# plt.show()                     
plt.savefig('assignment_1.png', dpi=300)  

