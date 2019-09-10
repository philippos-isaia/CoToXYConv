# CoToXYConv
A python script which can convert latitude and longitude to X and Y cartesian system using SUMO network file. 
The result can be used in simulators which prefer X and Y coordinates.

It uses JSON and SUMOLib, therefore SUMO simulator has to be installed on the host machine.

The user can execute the code as follows:

python CoordinatesCalculator.py --sumo sumonetfile.net --netin input.json --netout output.json

--sumo sumonetfile.net -> SUMO Simulator Network File Path (path and filename)
--netin input.json -> JSON Input File Path (path and filename)
--netout output.json -> JSON Output File Path (path and filename)

Input JSON File Structure

{"4Gantennas": [
	{"name": "MTN_LIM_002_C5", "provider": "MTN", "lat": 34.68208, "lon": 33.05428, "gsm_cells": 3, "dcs_cells": 0, "ant_height": 4}, 
	{"name": "MTN_LIM_003_C10", "provider": "MTN", "lat": 34.69278, "lon": 33.06528, "gsm_cells": 3, "dcs_cells": 0, "ant_height": 6}, 
]}

Output JSON File Structure

{"4Gantennas": [
    {"name": "MTN_LIM_002_C5", "provider": "MTN", "lat": 34.68208, "lon": 33.05428, "gsm_cells": 3, "dcs_cells": 0, "ant_height": 4, "x_coor": 1275.2612441905658, "y_coor": 1045.4090951508842}, 
    {"name": "MTN_LIM_003_C10", "provider": "MTN", "lat": 34.69278, "lon": 33.06528, "gsm_cells": 3, "dcs_cells": 0, "ant_height": 6, "x_coor": 2282.127144841652, "y_coor": 2232.5358261852525}, 
]}
