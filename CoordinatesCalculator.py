import os, sys
import argparse
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

# import sumo library
import sumolib
# import json library
import json

parser = argparse.ArgumentParser()
parser.add_argument("--sumo", help="SUMO Simulator Network File Path (path and filename)")
parser.add_argument("--netin", help="4G Antennas JSON Input File Path (path and filename)")
parser.add_argument("--netout", help="4G Antennas JSON Output File Path (path and filename)")
args = parser.parse_args()

if args.sumo and args.netin and args.netout:	
	# parse the sumo network file (to be provided as an argument)
	net = sumolib.net.readNet(args.sumo)

	data = {}
	data['4Gantennas'] = []
	# parse Telecommunications JSON file (to be provided as an argument)
	with open(args.netin) as json_file:
		telco = json.load(json_file)
		for val in telco['4Gantennas']:
			#Calculate X and Y using lon and lat provided in the input file
			x, y = net.convertLonLat2XY(val['lon'], val['lat'])
			data['4Gantennas'].append({
			"name":val['name'], 
			"provider": val['provider'], 
			"lat": val['lat'], 
			"lon": val['lon'], 
			"gsm_cells": val['gsm_cells'],
			"dcs_cells": val['dcs_cells'],
			"ant_height": val['ant_height'],
			"x_coor": x,
			"y_coor": y,
			})

	with open(args.netout, 'w') as outfile:
		json.dump(data, outfile)
else:
	if not args.sumo:
		print("Please define the SUMO Simulator Network File Path")
	if not args.netin:
		print("Please define the 4G Antennas JSON Input File Path")
	if not args.netout:
		print("Please define the 4G Antennas JSON Output File Path")