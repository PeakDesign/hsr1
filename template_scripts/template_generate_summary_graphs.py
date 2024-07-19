# -*- coding: utf-8 -*-
"""template script for generating graphs from a database using the hsr1 library"""
import hsr1


db_filepath = "your/database/here.db"

db = hsr1.DBDriver(db_filepath)
graph = hsr1.Graph(db, timezone="00:00", dpi=100)


graph.daily_aod_cimel()

graph.daily_integrals()

graph.plot_integral(True)
graph.plot_gps()
graph.plot_dips_summary()
