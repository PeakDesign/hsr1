# -*- coding: utf-8 -*-
"""template script for combining several databases into one"""
import os

import hsr1


main_db = "your/main/database.db"
db_file_or_dir_to_merge = "the/database/that/will/be/merged/into/the/main_db.db"


db_driver = hsr1.DBDriver(main_db)

# checks if db_file_or_dir_to_merge is a directory of databases or just one database that will be merged
# if you know what you are merging, you can skip the if statement and just use the appropriate function
if os.path.isdir(db_file_or_dir_to_merge):
    print("directory")
    db_driver.db_store.combine_database_folder(db_file_or_dir_to_merge, delete=False)

elif os.path.isfile(db_file_or_dir_to_merge):
    print("file")
    db_driver.db_store.combine_database(db_file_or_dir_to_merge)

else:
    print("path was not a file or a folder")