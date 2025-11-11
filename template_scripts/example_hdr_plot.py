import os

import pandas as pd

import hsr1


def read_calibration_file(filepath):
    rows = []
    with open(filepath) as f:
        for line in f.readlines():
            if line[:8] == "Sequence":
                row = line.split("\t")
                for i in range(len(row)):
                    if row[i][-1:] == "\n":
                        row[i] = row[i][:-1]

                    try:
                        row[i] = float(row[i])
                    except ValueError:
                        pass
                rows.append(row)

    cal_data = pd.DataFrame(data=rows, columns=["sequence", "number", "int_time", "gain", "slope", "offset"])
    cal_data = cal_data[["number", "int_time", "gain", "slope", "offset"]]
    return cal_data

data_filepath = "/home/albie/PeakDesign/Albie datasets/SGP 2022"
deployment_metadata_filepath = "/home/albie/PeakDesign/Albie datasets/SGP 2022/SGP 2022 Deployment.ini"
calibration_filepath = "/home/albie/Downloads/dropbox-copy/Albie (1)/Wavelength calibration/Calibration files SGP/Baumer 700004143714 CameraCalibration 20ms 4seq.txt"
database_location = "dev/res/databases/hdr_database.db"

db = hsr1.DBDriver(database_location)

if not os.path.exists(database_location):
    data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=deployment_metadata_filepath)
    db.store(data)



loaded_data = db.load(table="hdr")

cal_data = read_calibration_file(calibration_filepath)
# remove the first scale and offset values because those arent used and are just default values
cal_data = cal_data.iloc[1:].reset_index()

for i in range(len(cal_data)):
    col_name = "reference "
    loaded_data[col_name+"scale "+str(i+1)] = cal_data.loc[i, "slope"]
    loaded_data[col_name+"offset "+str(i+1)] = cal_data.loc[i, "offset"]

to_plot_columns = [col for col in loaded_data.columns if not col in ["pc_time_end_measurement", "dataseries_id"]]

g = hsr1.Graph()
g.plot_daily_line(columns=to_plot_columns, dataframe=loaded_data, period=1, title_prefix="hdr values with calibration reference in ", min_limit=-0.2)

