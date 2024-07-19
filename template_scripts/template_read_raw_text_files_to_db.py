# -*- coding: utf-8 -*-
"""template script of how to read raw data from .txt files to a database"""
import hsr1

data_filepath = "directory/containing/data/to/be/loaded"
deployment_metadata_filepath = "filepath/to/deployment.ini"
db_filepath = "the/name/and/location/of/the/new/database.db"

db_driver = hsr1.RawDbDriver(db_filepath)

##### start and end time are inclusive for read_txt
data, deployment_metadata = hsr1.read_txt.read_raw_txt(data_filepath, "2000-05-17", "2050-05-17", deployment_metadata_filepath)
db_driver.db_store.store(data, deployment_metadata)