# -*- coding: utf-8 -*-
"""template script for calibrating a raw dataset"""
import hsr1


db_name = "location/of/the/database.db"
output_loc = "where/to/store/the/output.txt"
calibration_file = "location/of/the/existing/calibration.txt"

db = hsr1.DBDriver(db_name)
raw_data = db.load_raw()

dataset = hsr1.utils.spectrum.RawDataset(raw_data, calibrations_filepath=calibration_file, spectrum_type="wavelength")

new_cals = dataset.find_all_calibrations(file_output=output_loc, plot_summary=True)