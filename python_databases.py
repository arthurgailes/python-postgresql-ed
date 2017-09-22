# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:22:35 2017

@author: agail
"""

import sqlalchemy
from sqlalchemy import (create_engine, select, Table, MetaData, and_, desc,
                        func)
import psycopg2


# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://postgres:052587@localhost/Learning')

metadata = MetaData()

customers = Table('customers', metadata, autoload=True, autoload_with=engine)

#set up connection
connection = engine.connect()

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())

stmt = select([customers])

results = connection.execute(stmt).fetchall()

print(results)

rev_stmt = stmt.order_by(customers.columns.id)

rev_results = connection.execute(stmt).fetchall()

print(rev_results) 