import os

import hsr1

class TestGraphs:

    def test_should_plot_integral_summary_graph(self):
        data_filepath = "tests/res/Tara 2023"
        deployment_metadata_filepath = "tests/res/SGP 2022/SGP 2022 Deployment.ini"
        database_location = "tests/temp/databases/tara_2023.db"

        png_save_location = "tests/temp/plots"

        if os.path.exists(database_location):
            os.remove(database_location)
        
        for f in os.listdir(png_save_location):
            os.remove(os.path.join(png_save_location, f))

        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        driver = hsr1.DBDriver(db_name=database_location)
        driver.store(data)
        
        g = hsr1.Graph(driver, block=False, output_location=png_save_location)

        g.plot_daily_line(["global_integral"], period=1)
        
