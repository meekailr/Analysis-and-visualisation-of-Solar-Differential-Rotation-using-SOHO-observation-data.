# Analysis-and-visualisation-of-Solar-Differential-Rotation-using-SOHO-observation-data.
Estimating the angular velocity of multiple sunspots by transforming image coordinates into heliographic coordinates and fitting longitudinal motion over time.
Thus producing an estimate of the angular velocity of the surface of the sun at differing latitudes.
With this we can determine the differential rotation of the sun's surface, which points towards a better model of its surface behaving as a plasma as opposed to a rigid body.

Datasets used:
--------------
SOHO/SDA data - https://sdo.gsfc.nasa.gov/assets/img/browse/
HELIOS data -  HELIO software (version 3.2 to 4.2)


Usage of sunspot_analysis.py
-------------------------
input data:
X and Y positions of solar feature centre and B_0 data for that day in the format shown in "sunspot_position_and_B_0_values_2024_05_28-06_01.txt".
Used formulae to convert into:
radius to sunspot
angle to sunspot from central origin
angular radius

output data:
heliographic latitudes and heliographic longitudes of sunspots

