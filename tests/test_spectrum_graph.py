import os

import hsr1
import numpy as np
import pandas as pd

class TestSpectrumGraph:
    def test_spectrum_graph_plots(self):
        data_filepath = "tests/res/NOAA 2025"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/my_database.db"

        if os.path.exists(database_location):
            os.remove(database_location)

        db_driver = hsr1.DBDriver(database_location)

        txt_data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)

        db_driver.store(txt_data)

        g = hsr1.Graph(db_driver, timezone="-04:00", output_location="tests/temp/plots", block=False)

        g.plot_spectrum_day()
