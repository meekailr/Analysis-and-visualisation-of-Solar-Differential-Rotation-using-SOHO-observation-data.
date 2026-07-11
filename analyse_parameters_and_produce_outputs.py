import pandas as pd
import numpy as np
import math

L_0 = 0
data1 = []
radius = []
angle = []
angularradius = []
B_0 = []
B_0rad = []
hel_lat = []
hel_long = []

# - Clean data (strip whitespace and columns), find length of data
df=pd.read_csv("sunspot_positions_and_B_0.txt", sep="\t")
df_length=len(df)

# - Functions / formulae
#Magnitude function
def Mag(array):
    return round((math.sqrt(array[0]**2 + array[1]**2)), 2)
#Angle function
def anglefinder(array):
    return round((math.atan2(array[1], array[0])),2)
#Angular radius function
def angularradiusfinder(r):
    R = 453.233542 # Radius of the solar disc in px
    return round(math.asin(r / R) - (0.53 * math.pi / 180) * (r / (2 * R)), 2)
#Latitude of solar feature
def hel_latfinder(angularradtemp, angletemp, B_0radtemp):
    return round(math.asin(math.sin(B_0radtemp) * math.cos(angularradtemp) + math.cos(B_0radtemp) * math.sin(angularradtemp) * math.cos(angletemp)), 2)
#Longitude of solar feature
def hel_longfinder(angularradtemp, hel_lattemp, angletemp):
    return round(math.asin(((-math.sin(angularradtemp) * math.sin(angletemp)/(math.cos(hel_lattemp)))) + L_0), 2)

# - Extract data from cleaned table
#sunspot position table
for i in range(df_length):
    abc = df.iloc[i].values
    ab = [float(abc[0]),float(abc[1])]
    c = float(abc[2])
    data1.append(ab)
    B_0.append(c)
    B_0rad.append(c*(math.pi / 180))
    
xy = np.array(data1)



# - set central origin
translatedxy = xy-512


# - Iteration over all data
for i in range(df_length):
    selected_xy = translatedxy[i]
    B_0rad_i = B_0rad[i]
    #print(selected_xy)
    radius_i = Mag(selected_xy)
    radius.append(radius_i)
# - Produces radii using Mag function
    angle_i = anglefinder(selected_xy)
    angle.append(angle_i)
# - Produce angles from centre using X,Y positional values
    angular_radius_i = angularradiusfinder(radius_i)
    angularradius.append(angular_radius_i)
# - Produce angular radii from position of solar feature
    hel_lat_i = hel_latfinder(angular_radius_i, angle_i, B_0rad_i)
    hel_lat.append(hel_lat_i)
# - Produce heliographic latitude of solar feature
    hel_long_i = hel_longfinder(angular_radius_i, hel_lat_i, angle_i)
    hel_long.append(hel_long_i)
# - Produce heliographic longitude of solar feature
    


print(radius)
print(angle)
print(angularradius)
print(hel_lat)
print(hel_long)
# - output variables
