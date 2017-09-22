# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:22:35 2017

@author: agail
"""

import sqlalchemy
from sqlalchemy import (create_engine, select, Table, MetaData, and_, desc,
                        func, Table, Column, String, Integer, Float, Boolean,
                        insert)
import psycopg2
import csv


# Create an engine to the census database
engine = create_engine('postgresql+psycopg2://postgres:052587@localhost/Learning')

metadata = MetaData()

customers = Table('customers', metadata, autoload=True, autoload_with=engine)

#set up connection
connection = engine.connect()

## Use the .table_names() method on the engine to print the table names
#print(engine.table_names())
#
#stmt = select([customers])
#
#results = connection.execute(stmt).fetchall()
#
#print(results)
#
#rev_stmt = stmt.order_by(customers.columns.id)
#
#rev_results = connection.execute(stmt).fetchall()
#
#print(rev_results) 
#
#
# Define a new table with a name, count, amount, and valid column: data
data = Table('data', metadata,
             Column('value', String(255)),
             Column('customs_districts_label', String(255)),
             Column('location_chinese_trader', String(255)),
             Column('trader_zone', String(255)),
             Column('customs_regime', String(255)),
             Column('country_of_destination', String(255)),
             Column('country_of_consumption', String(255)),
             Column('location_chinese_producer', String(255)),
             Column('producer_zone', String(255)),
             Column('transportation_modes', String(255)),
             Column('china_hs8', String(255)),
             Column('quantity_unit', String(255)),
             Column('quantity', String(255))
)

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))


##Import the CSV
#preview_data = []
#with open('data/previews.csv') as csv_reader:
#    spamreader = csv.reader(csv_reader, delimiter = ',')
#    next(spamreader, None)
#    for row in spamreader:
#        preview_data.append(', '.join(row))
        
        
# read CSV file & load into list
with open("data/previews.csv", 'r') as my_file:
    reader = csv.reader(my_file, delimiter=',')
    preview_data = list(reader)
        
        
#with open('data/previews.csv', 'r') as f:    
#    cursor = engine.cursor()
#    cmd = 'COPY tbl_name(value,customs_districts_label,location_chinese_trader,trader_zone,customs_regime,country_of_destination,country_of_consumption,location_chinese_producer,producer_zone,transportation_modes,china_hs8,quantity_unit,quantity) FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
#    cursor.copy_expert(cmd, f)
#    engine.commit()

#Loading a CSV into a Table

# Create a insert statement for census: stmt
stmt = insert(data)

# Create an empty list and zeroed row count: values_list, total_rowcount
values_list = []
total_rowcount = 0

# Enumerate the rows of csv_reader
for idx, row in enumerate(preview_data[1:]):
    #create data and append to values_list
    data = {'value': row[0], 'customs_districts_label': row[1], 'location_chinese_trader': row[2],
            'trader_zone': row[3],'customs_regime': row[4],'country_of_destination': row[5],
            'country_of_consumption': row[6],'location_chinese_producer': row[7],
            'producer_zone': row[8],'transportation_modes': row[9],'china_hs8': row[10],
            'quantity_unit': row[11],'quantity': row[12]}
    values_list.append(data)

    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = connection.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []

# Print total rowcount
print(total_rowcount)



