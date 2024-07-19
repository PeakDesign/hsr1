# -*- coding: utf-8 -*-
"""template script for calibrating an instrument from one pixel spectrum reading"""

import numpy as np

import hsr1


data_file = "the/pixel/spectrum/being/calibrated.txt"

output_file = "new_calibration.txt"

pixel_dataset = hsr1.read_txt.read_raw_pixels(data_file, 0)

reference_dip_locations = [374, 384, 393, 430, 487, 517, 590, 657, 688, 719, 761, 817, 900, 910, 936, 976]

dataset = hsr1.spectrum.RawDataset(pixel_dataset, amplitude_calibration=np.ones(801), spectrum_type="pixel")

new_cals = dataset.find_all_calibrations(file_output=output_file, reference_dip_locations=reference_dip_locations,
                                         plot_total_output=True, plot_summary=True, plot_individual_results=False, plot_debug=False)

dataset.plot_calibration(new_cals)
