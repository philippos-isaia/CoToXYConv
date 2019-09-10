# CoToXYConv
A python script which can convert latitude and longitude to X and Y cartesian system. 
The result can be used in simulators which prefer X and Y coordinates.

It uses JSON and SUMOLib, therefore SUMO simulator has to be installed on the host machine.

The user can execute the code as follows:

python CoordinatesCalculator.py --sumo sumonetfile.net --netin input.json --netout output.json
