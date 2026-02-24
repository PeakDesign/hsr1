import os

import hsr1


class TestRawDatabase:
    def test_can_read_raw_data_and_store(self):
        data_filepath = "tests/res/NOAA 2025"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/my_database.db"

        db_driver = hsr1.DBDriver(database_location)

        
        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        db_driver.store(data)

        data= hsr1.read_txt.read_raw_txt(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        db_driver.store_raw(data)

        assert(os.path.exists(database_location))
        assert(os.path.getsize(database_location) > 100)

    def test_adding_raw_data_dosent_confuse_existing_methods(self):
        data_filepath = "tests/res/NOAA 2025"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/my_database.db"

        db_driver = hsr1.DBDriver(database_location)

        
        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        db_driver.store(data)
        
        loaded_data = db_driver.load()

        # data= hsr1.read_txt.read_raw_txt(data_filepath, deployment_metadata_filepath=
        #                           deployment_metadata_filepath)
        # db_driver.store_raw(data)
        #
        # new_loaded_data = db_driver.load()
        # assert(loaded_data.equals(new_loaded_data))


    def test_can_load_raw_data_using_regular_load_method(self):
        data_filepath = "tests/res/NOAA 2025"
        deployment_metadata_filepath = "tests/res/NOAA 2025/HSR1-009 NOAA 2025 Deployment.ini"

        database_location = "tests/temp/databases/my_database.db"

        if os.path.exists(database_location):
            os.remove(database_location)

        db_driver = hsr1.DBDriver(database_location)

        
        data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        db_driver.store(data)

        data = hsr1.read_txt.read_raw_txt(data_filepath, deployment_metadata_filepath=
                                  deployment_metadata_filepath)
        db_driver.store_raw(data)


        loaded_data = db_driver.load(table="raw_data")
        original_loaded_data = db_driver.db_load.old_load_raw()

        # methods use different time formats (load includes timezone). Check the rest of the data is the same.
        original_loaded_data["pc_time_end_measurement"] = loaded_data["pc_time_end_measurement"]
        assert(loaded_data.equals(original_loaded_data))


        loaded_data = db_driver.load(table="raw_data", columns=["channel_1"])
        original_loaded_data = db_driver.db_load.old_load_raw(columns=["channel_1"])
        original_loaded_data.index = loaded_data.index

        assert(loaded_data.equals(original_loaded_data))


        loaded_data = db_driver.load(table="raw_data", start_time="2025-03-20 21:00:00", end_time="2025-03-20 22:00:00", timezone="+01:00")



