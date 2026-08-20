import os

import pandas as pd
import numpy as np

import hsr1


class TestDatabase:
    def test_can_create_database(self):
        data_filepath = "tests/res/NOAA 2025"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/my_database.db"

        db_driver = hsr1.DBDriver(database_location)

        if os.path.exists(database_location):
            os.remove(database_location)

        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        db_driver.store(data)

        assert(os.path.exists(database_location))
        assert(os.path.getsize(database_location) > 100)


    
    def test_can_read_from_database(self):
        data_filepath = "tests/res/NOAA 2025"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/databases/my_database.db"

        db_driver = hsr1.DBDriver(database_location)

        if os.path.exists(database_location):
            os.remove(database_location)


        txt_data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)

        db_driver.store(txt_data)
        db_data = db_driver.load()

        assert(type(db_data) == pd.DataFrame)
        assert("pc_time_end_measurement" in db_data.columns)
        
        assert("global_integral" in db_data.columns)
        assert("diffuse_integral" in db_data.columns)
        assert("global_spectrum" in db_data.columns)

        assert(txt_data[0]["global_spectrum"].equals(db_data["global_spectrum"]))

    def test_can_load_system_data_correctly(self):
        data_filepath = "tests/res/Tara 2023"
        deployment_metadata_filepath = "tests/res/short_tara_2023/Tara 2023 Deployment.ini"

        database_location = "tests/temp/databases/my_database.db"

        if os.path.exists(database_location):
            os.remove(database_location)

        db_driver = hsr1.DBDriver(database_location)

        txt_data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath, end_date="2023-06-05")

        db_driver.store(txt_data)

        # data = db_driver.load(["gps_altitude"], end_time="2023-06-05 14:00:00")
        # x = "SELECT system_data.pc_time_end_measurement, system_data.gps_altitude FROM spectral_data LEFT JOIN system_data ON spectral_data.sample_id = system_data.sample_id LEFT JOIN precalculated_values ON spectral_data.sample_id = precalculated_values.sample_id ORDER BY STRFTIME('%s', spectral_data.pc_time_end_measurement)"
        # data = db_driver.db_load.load_sql(x)
        # print(data[1500:])
        data = db_driver.load(["pc_time_end_measurement", "gps_altitude"])
        # data = db_driver.db_load.load_sql("SELECT pc_time_end_measurement, gps_altitude FROM system_data")
        # print(data[1500:])

    def test_can_read_from_database_accessory(self):
        data_filepath = "tests/res/NOAA 2025"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/databases/my_database.db"

        db_driver = hsr1.DBDriver(database_location)

        if os.path.exists(database_location):
            os.remove(database_location)

        txt_data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)

        db_driver.store(txt_data)
        
        db_data = db_driver.load(["pc_time_end_measurement", "global_integral"])
        db_data = db_driver.load(["pc_time_end_measurement", "_15Vin"])
        assert("_15Vin" in db_data.columns)
        assert(len(db_data) > 10)

        

    def test_can_handle_invalid_accessory_dates(self):

        data_filepath = "tests/res/Tara 2023_mod/invalid_date"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/databases/my_database.db"

        db_driver = hsr1.DBDriver(database_location)

        if os.path.exists(database_location):
            os.remove(database_location)

        txt_data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)

        db_driver.store(txt_data)
        g = hsr1.Graph(db_driver, block=False)
        g.plot_gps()


    # def test_deployment_metadata_is_shared_if_same_raw(self):
    #     data_filepath = "tests/res/Tara 2023"
    #     deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"
    #
    #     database_location = "tests/temp/databases/my_database.db"
    #
    #     db_driver = hsr1.DBDriver(database_location)
    #
    #     if os.path.exists(database_location):
    #         os.remove(database_location)
    #
    #     raw_txt_data = hsr1.read_txt.read_raw_txt(data_filepath, 
    #                                       deployment_metadata_filepath=deployment_metadata_filepath,
    #                                       end_date="2023-06-04")
    #     db_driver.store_raw(raw_txt_data)
    #
    #
    #     raw_txt_data = hsr1.read_txt.read_raw_txt(data_filepath, 
    #                                               deployment_metadata_filepath=deployment_metadata_filepath,
    #                                               start_date="2023-06-05",
    #                                               end_date="2023-06-05")
    #     db_driver.store_raw(raw_txt_data)
    #
    #     raw_txt_data = hsr1.read_txt.read_raw_txt(data_filepath, 
    #                                               deployment_metadata_filepath=deployment_metadata_filepath,
    #                                               start_date="2023-06-06",
    #                                               end_date="2023-06-06")
    #     db_driver.store_raw(raw_txt_data)
    #
    #
    #     data = db_driver.load_metadata()
    #     assert(len(data.index) == 1)
    #
    #
    def test_deployment_metadata_is_shared_if_same(self):
        data_filepath = "tests/res/Tara 2023"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/my_database.db"

        db_driver = hsr1.DBDriver(database_location)

        if os.path.exists(database_location):
            os.remove(database_location)

        txt_data = hsr1.read_txt.read(data_filepath, 
                                          deployment_metadata_filepath=deployment_metadata_filepath,
                                          end_date="2023-06-04")
        db_driver.store(txt_data)

        txt_data = hsr1.read_txt.read(data_filepath, 
                                          deployment_metadata_filepath=deployment_metadata_filepath,
                                        start_date="2023-06-05",
                                          end_date="2023-06-05")
        db_driver.store(txt_data)


        data = db_driver.load_metadata()
        assert(len(data.index) == 1)

    def test_database_sort_parameter(self):
        data_filepath = "tests/res/Tara 2023"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/my_database.db"

        db_driver = hsr1.DBDriver(database_location)

        if os.path.exists(database_location):
            os.remove(database_location)


        txt_data = hsr1.read_txt.read(data_filepath, 
                                          deployment_metadata_filepath=deployment_metadata_filepath,
                                        start_date="2023-06-05",
                                          end_date="2023-06-05")
        db_driver.store(txt_data)

        txt_data = hsr1.read_txt.read(data_filepath, 
                                          deployment_metadata_filepath=deployment_metadata_filepath,
                                          end_date="2023-06-04")

        db_driver.store(txt_data)


        unsorted_data = db_driver.load(["pc_time_end_measurement", "global_integral"], sort=False)
        times = pd.to_datetime(unsorted_data["pc_time_end_measurement"]).astype(int)
        sorted = (np.diff(times) > 0).all()
        assert(not sorted)
        
        unsorted_data = db_driver.load(["pc_time_end_measurement", "global_integral"], sort=True)
        times = pd.to_datetime(unsorted_data["pc_time_end_measurement"]).astype(int)
        sorted = (np.diff(times) > 0).all()
        assert(sorted)




