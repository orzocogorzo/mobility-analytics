import simplejson as json
from pymongo import MongoClient

client = MongoClient()
db = client.mobility

criteria = json.load(open('criteria.json'))
table = json.load(open('table.json'))
data = [
  doc for doc in list(db.highways.find({}, {"_id": False})) 
  if (doc["geometry"]["type"] == "LineString" or doc["geometry"]["type"] == "MultiLineString")
  and doc["properties"]["tags"].get("highway", None)
]

def classify():
  for doc in data:
    doc["modes"] = doc.get("modes", dict())
    mode_idx = 0
    for mode_name in table["columns"]:
      mode_value = 0
      for row_idx in range(len(table["rows"])):
        if len(table["data"]) > row_idx:
          dimension = table["data"][row_idx]
          dimension_name = table["rows"][row_idx]
          weight = dimension["weight"]
          formula = eval(dimension["fn"])
          dim_value = formula(doc, weight, mode_idx, criteria[dimension_name])
          if dim_value:
            mode_value += dim_value
        
      doc["modes"][mode_name] = mode_value
      mode_idx += 1
      
    print(doc["modes"])