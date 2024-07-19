# -*- coding: utf-8 -*-
"""template script for calibrating a raw dataset"""
import hsr1


db_name = "database/to/be/calibrated"

output_loc = "calibrations/new_calibration.txt"

calibration_file = "exsisting/calibration/file.txt"

raw_driver = hsr1.RawDbDriver(db_name)
raw_data = raw_driver.load()

dataset = hsr1.utils.spectrum.RawDataset(raw_data, calibrations_filepath=calibration_file, spectrum_type="wavelength")

new_cals = dataset.find_all_calibrations(file_output=output_loc, plot_summary=True)