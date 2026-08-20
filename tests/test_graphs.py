import os

import hsr1

class TestGraphs:

    def test_should_plot_main_graphs(self):
        # data_filepath = "tests/res/databases/Ispra 10s"
        # deployment_metadata_filepath = "tests/res/databases/Ispra 10s/HSR1-005 ISRC 2024 Deployment.ini"
        # database_location = "tests/temp/databases/ispra_database.db"
        # database_location = "/home/albie/PeakDesign/Albie datasets/Quest 2025/databases/HSR1-004 PML Quest 2025.db"
        # deployment_metadata_filepath = "~/PeakDesign/Albie datasets/Quest 2025/HSR1-004 2025 Deployment.ini"
        # database_location = "tests/temp/databases/quest_database.db"
        data_filepath = "tests/res/Tara 2023"
        deployment_metadata_filepath = "tests/res/short_tara_2023/Tara 2023 Deployment.ini"
        database_location = "tests/temp/databases/tara_2023.db"

        if os.path.exists(database_location):
            os.remove(database_location)

        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        driver = hsr1.DBDriver(db_name=database_location)
        driver.store(data)
        
        g = hsr1.Graph(driver, block=False)

        g.plot_integral(flag=True)
        g.plot_gps()
        g.plot_accessory()
        g.daily_integrals(flag=True)
        

    def test_should_respect_timezones(self):
        data_filepath = "tests/res/SGP 2022"
        deployment_metadata_filepath = "tests/res/SGP 2022/SGP 2022 Deployment.ini"
        database_location = "tests/temp/databases/my_database.db"
        # database_location = "/home/albie/PeakDesign/Albie datasets/Quest 2025/databases/HSR1-004 PML Quest 2025.db" 
        # deployment_metadata_filepath = "~/PeakDesign/Albie datasets/Quest 2025/HSR1-004 2025 Deployment.ini"
        # database_location = "tests/temp/databases/quest_database.db"

        if os.path.exists(database_location):
            os.remove(database_location)

        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        driver = hsr1.DBDriver(db_name=database_location)
        driver.store(data)
        
        g = hsr1.Graph(driver, timezone="-06:00", block=False)

        g.plot_integral(flag=True)
        g.plot_gps()
        g.plot_accessory()
        g.daily_integrals(flag=True)

    def test_should_respect_timezones_when_plotting_from_dataframe(self):
        data_filepath = "tests/res/SGP 2022"
        deployment_metadata_filepath = "tests/res/SGP 2022/SGP 2022 Deployment.ini"
        database_location = "tests/temp/databases/my_database.db"

        if os.path.exists(database_location):
            os.remove(database_location)

        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        driver = hsr1.DBDriver(db_name=database_location)
        driver.store(data)

        loaded_data = driver.load(["global_integral", "diffuse_integral", "sza", "gps_longitude", "gps_latitude", "gps_altitude", "pc_time_end_measurement", "azimuth", "toa_hi", "sed"])

        
        # g = hsr1.Graph(timezone="-06:00", block=True)
        g = hsr1.Graph(timezone="-06:00", block=False)

        g.plot_integral(dataframe=loaded_data, flag=True)

    def test_should_load_data_correctly(self):
        data_filepath = "tests/res/SGP 2022"
        deployment_metadata_filepath = "tests/res/SGP 2022/SGP 2022 Deployment.ini"
        database_location = "tests/temp/databases/my_database.db"

        if os.path.exists(database_location):
            os.remove(database_location)

        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        driver = hsr1.DBDriver(db_name=database_location)
        driver.store(data)

        # this is missing sed for plot_integral. testing if ignore_missing works
        loaded_data = driver.load(["global_integral", "diffuse_integral", "sza", "gps_longitude", "gps_latitude", "gps_altitude", "pc_time_end_measurement", "azimuth", "toa_hi"])

        
        # g = hsr1.Graph(timezone="-06:00", block=True)
        g = hsr1.Graph(timezone="-06:00", block=False)

        g.plot_integral(dataframe=loaded_data, flag=True)

