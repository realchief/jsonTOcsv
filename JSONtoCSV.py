

import os
import json
import csv

json_file = 'facebook.da.influencers.json'
csv_file = 'facebook.da.influencers.csv'

if os.path.exists(json_file):

    json_file_object = open(json_file, 'r')

    # Load JSON file data to a python dict object.
    table_dict = json.load(json_file_object)

    header_field_names_list = []

    dict_keys = list(table_dict.keys())

    dict_keys_length = len(dict_keys)
    row_dicts = []
    c = 0

    for dict_key in dict_keys:
        row_dict_temp = []
        for row in table_dict[dict_key]:
            row_dict_temp.append(table_dict[dict_key][row])
        row_dicts.append(row_dict_temp)

    csv_file_object = open(csv_file, 'w')
    csv_dict_file_writer = csv.DictWriter(csv_file_object, fieldnames=dict_keys)

    csv_dict_file_writer.writeheader()

    for index, row_dict in enumerate(row_dicts[0]):
        # Write each row dict data to the csv file.
        row = {}
        for index_temp, dict_key in enumerate(dict_keys):
            row[dict_key] = row_dicts[index_temp][index]
        csv_dict_file_writer.writerow(row)

    print("Convert " + json_file + " to " + csv_file + " success.")
else:
    print(json_file + " do not exist. ")