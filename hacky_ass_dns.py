# Hacky ass dyndns

#link to export as JSON: https://www.myfritz.net/action/export/json

import json
import glob
import pandas

list_json_files = glob.glob("C:\\Users\\<YOIRUSERNAME>\\Downloads\\*.json")

for json_file in list_json_files:
    with open(json_file) as json_as_list:  
        data = json.load(json_as_list)
        data = data[0]

    print("Name       : {}".format(data["name"]))
    print("Model      : {}".format(data["model"]))
    print("Provider   : {}".format(data["provider"]))
    print("Firmware   : {}".format(data["firmware_version"]))
    print("Last Active: {}".format(data["last_active"]))
    print("IPv4       : {}".format(data["ipv4_address"]))
    print("Myfritz URL: {}".format(data["myfritz_url"]))
    print("----------------------------------------------------")
