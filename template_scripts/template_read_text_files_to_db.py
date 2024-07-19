# -*- coding: utf-8 -*-
""""""
import hsr1

data_filepath = "directory/containing/data/to/be/loaded"
deployment_metadata_filepath = "filepath/to/deployment.ini"
db_filepath = "the/name/and/location/of/the/new/database.db"


db_driver = hsr1.DBDriver(db_filepath)

##### start and end time are inclusive for read_txt
data = hsr1.read_txt.read(data_filepath, "2000-01-01", "2023-06-05", deployment_metadata_filepath=deployment_metadata_filepath)
db_driver.store(data)





