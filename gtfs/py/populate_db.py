import csv
import os
import psycopg2 as pypg

from gtfs_spec import gtfs_spec

class DBManager:

  def __init__(self):
    self.conn = pypg.connect("dbname=mobility host=localhost port=5432 user=orzo password=Contrasenya1992_")
    self.cur = self.conn.cursor()
    self.gtfs_specs = gtfs_spec
    
  
  def initialize_schema(self, schema):
     query = "CREATE SCHEMA IF NOT EXISTS " + schema + ";"
     self.cur.execute(query)
    
    
  def get_field_type(self, table, field):
    table = self.gtfs_specs[table] if table in self.gtfs_specs.keys() else None
    type = table[field] if table and field in table.keys() else None
    return type if type else "varchar"
  
  
  def gen_table_by_name(self, schema, tablename, fieldnames):
    
    clean_query = "DROP TABLE IF EXISTS %s.%s;" % (schema, tablename)
    self.cur.execute(clean_query)
    
    query = "CREATE TABLE IF NOT EXISTS %s.%s (" % (schema, tablename)
    
    tablefields = list()
    
    for fieldname in fieldnames:
      field_str_name = "%s " + self.get_field_type(tablename, fieldname) 
      tablefields.append(field_str_name)
      
    tablefields = ",".join(tablefields) % tuple(fieldnames)
    
    query = query + tablefields + ');'
    
    print('\nCREATE TABLE ' + schema + '.' + tablename)
    self.cur.execute(query)
    
    
  def populate_table_by_name(self, schema, tablename, fieldnames, values):
    query = "INSERT INTO %s.%s (" % (schema, tablename)
    
    tablefields = list()
    
    for name in fieldnames:
      tablefields.append("%s")
      
    tablefields = ",".join(tablefields) % tuple(fieldnames) + ')'
    
    queryvalues = [None]*len(fieldnames)
    
    for index in range(len(fieldnames)):
      queryvalues[index] = "%s"
      
    queryvalues = "(" + ",".join(queryvalues) + ")"
    
    query = query + tablefields + ' VALUES ' + queryvalues
    
    values = list(map(lambda val: val if val else None, values))
    self.cur.execute(query, values)
    
    
  def commit( self ):
    self.conn.commit()
    self.cur.close()
    self.conn.close()
  

cwd = os.getcwd()
dbman = DBManager()

for folder in os.listdir(cwd):
  if 'gtfs' in folder:
    dbman.initialize_schema(folder)
    for file in os.listdir(os.path.join(cwd,folder)):
      rowIdx = 0
      table_fileds = None
      table_name = file.replace('.txt','')
      reader = csv.reader(open(os.path.join(cwd,folder,file), encoding='Latin1'), delimiter=',')
      for row in reader:
        if rowIdx == 0:
          table_fields = row
          dbman.gen_table_by_name(folder, table_name, table_fields)
        elif len(row):
          dbman.populate_table_by_name(folder, table_name, table_fields, row)
        
        rowIdx += 1
    
dbman.commit()
 
