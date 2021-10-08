import json
import csv

json_fp = open("input.json", "r", encoding='utf-8')
csv_fp = open("output.csv", "w", encoding='utf-8', newline='')

data_list = json.load(json_fp)
sheet_title = data_list[0].keys()
sheet_data = []

for data in data_list:
    sheet_data.append(data.values())

writer = csv.writer(csv_fp)

writer.writerow(sheet_title)

writer.writerows(sheet_data)

json_fp.close()
csv_fp.close()
