import simplejson as json
from pymongo import MongoClient

from .table import table # .?¿

client = MongoClient()
db = client.mobility

criteria = json.load(open('criteria.json'))
# table = json.load(open('table.json'))
# for row in table["data"]:
#   row["fn"]=eval(row["fn"])

data = [
  doc for doc in list(db.highways.find({}, {"_id": False})) #_id entre comes?
  if (doc["geometry"]["type"] == "LineString" or doc["geometry"]["type"] == "MultiLineString")
  and doc["properties"]["tags"].get("highway", None)
]


def classify():
  for doc in data:
    doc["modes"] = doc.get("modes", dict())
    for mode_idx in range(len(table["columns"])):
      mode_value = 0
      mode_name = table["columns"][mode_idx]
      for row_idx in range(len(table["rows"])):   
        dimension = table["data"][row_idx]
        dimension_name = table["rows"][row_idx]
        weight = dimension["weight"][mode_idx]
        formula = dimension["fn"]
        dim_value = formula(doc, weight, mode_idx, criteria[dimension_name])
        if dim_value:
          mode_value += dim_value
        
      doc["modes"][mode_name] = mode_value
      
    print(doc["modes"])

if __name__ == '__main__':
  classify()