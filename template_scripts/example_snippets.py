# -*- coding: utf-8 -*-



"""------------------
read .txt files to db
------------------"""
# import hsr1

# data_filepath = "../Datasets/Small Tara 2023"
# deployment_metadata_filepath = "../Datasets/Tara 2023/Tara 2023 Deployment.ini"

# database_location = "databases/my_database.db"

# db_driver = hsr1.DBDriver(database_location)

# data = hsr1.read_txt.read(data_filepath, deployment_metadata_filepath=deployment_metadata_filepath)
# db_driver.store(data)


"""------------------
loading data from the database
------------------"""
# import hsr1

# database_location = "databases/my_database.db"
# db_driver = hsr1.DBDriver(database_location)
# data = db_driver.load(["pc_time_end_measurement", "global_integral"],
# 		   	  condition="sza < 1.57")

"""------------------
loading data from the database-accessory
------------------"""
# import hsr1

# database_location = "databases/my_database.db"
# db_driver = hsr1.DBDriver(database_location)

# # data from accessory_data
# accessory_data = db_driver.load_accessory(["pc_time_end_measurement", "Yaw"])

# # data from spectral_data and precalculated_values
# data = db_driver.load(["global_integral", "azimuth"])

"""------------------
loading data from the database-metadata
------------------"""
# import hsr1

# database_location = "databases/my_database.db"
# db_driver = hsr1.DBDriver(database_location)
# data = db_driver.load_metadata(["owner_contact", "operator_contact"])

"""------------------
loading data from the database-spectrum
------------------"""
# import hsr1

# database_location = "databases/my_database.db"
# db_driver = hsr1.DBDriver(database_location)

# global_spectrum = db_driver.load_spectrum("global_spectrum")

"""------------------
graphing data
------------------"""
# import hsr1

# database_location = "databases/my_database.db"

# graph = hsr1.Graph(database_location)

# graph.plot_integral()
# graph.plot_gps()
# graph.plot_dips_summary()
# graph.plot_accessory()

# graph.plot_daily_line(["global_integral", "diffuse_integral"])
# graph.plot_daily_hist(["rh", "pressure"])

"""------------------
graphing data
------------------"""
# import hsr1

# existing_database = "databases/my_database.db"
# db_driver = hsr1.DBDriver(existing_database)

# db_driver.combine_database("databases/tara.db")

"""------------------
graph example
------------------"""
import hsr1

database_location = "databases/my_database.db"
graph = hsr1.Graph(database_location, start_time="2024-06-17", end_time="2024-06-18", 
                   dpi=300, timezone="+06:00", 
                   output_location="../hsr1_debug_images/")