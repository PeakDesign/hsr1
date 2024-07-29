# -*- coding: utf-8 -*-
"""template script of how to read raw data from .txt files to a database"""
import hsr1

data_filepath = "location/of/data/to/be/read"
deployment_metadata_filepath = "location/of/deployment/metadata.ini"
db_filepath = "where/the/database/will/be/stored.db"

db_driver = hsr1.DBDriver(db_filepath)

##### start and end time are inclusive for read_txt
data, deployment_metadata = hsr1.read_txt.read_raw_txt(data_filepath, "2000-05-17", "2023-06-04", deployment_metadata_filepath)
db_driver.store_raw(data, deployment_metadata)