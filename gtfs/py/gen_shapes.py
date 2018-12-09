import shapefile as shp
import csv, os
import requests as req

class ShpGenerator():

  def __init__(self, filepath, shapeType=3):
    self.fields_spec = {
      "shape_id": {
        "type": "C",
        "size": "255"
      },
      "shape_pt_lat": {
        "type": "N",
        "decimal": "10"
      },
      "shape_pt_lon": {
        "type": "N",
        "decimal": "10"
      },
      "shape_pt_sequence": {
        "type": "N",
        "decimal": "0"
      },
      "shape_dist_traveled": {
        "type": "N",
        "decimal": "4"
      }
    }
    
    self.values_spec = {
      "shape_id": str,
      "shape_pt_lat": float,
      "shape_pt_lon": float,
      "shape_pt_sequence": int,
      "shape_dist_traveled": float
    }
    
    self.filepath = filepath
    self.w = shp.Writer(filepath, shapeType=shapeType)
    self.w.autoBalance = 1
    self.proj = self.getWKT_PRJ(4326)
  
  def getWKT_PRJ(self, epsg_code):
    wkt = req.get("http://spatialreference.org/ref/epsg/{0}/prettywkt/".format(epsg_code))
    remove_spaces = wkt.text.replace(" ", "")
    output = remove_spaces.replace("\n", "")
    
    return output
  
  
  def setup_layer_fields(self, fields):
    self.headers = fields
    for field in fields:
      self.w.field(field, "C")
      #if self.fields_spec[field]["type"] == "C":
      #  self.w.field(field, self.fields_spec[field]["type"], size=self.fields_spec[field]["size"])
      #elif self.fields_spec[field]["type"] == "N":
      #   self.w.field(field, self.fields_spec[field]["type"], decimal=self.fields_spec[field]["decimal"])   
      
         
  def write_row(self, values):
    values = self.format_values(values)
    self.w.point(float(values[self.headers.index("shape_pt_lon")]),float(values[self.headers.index("shape_pt_lat")]))
    self.w.record(*tuple(values))

  def draw_shape(self, values, headers):
    lineCoords = []
    for d in values:
      lineCoords.append([
        float(d[headers.index("shape_pt_lon")]),
        float(d[headers.index("shape_pt_lat")])
      ])
      
    self.w.line([lineCoords])
    self.w.record(d[headers.index("shape_id")])
    
    
  def close( self ):
    # self.w.save(self.filepath)
    
    proj = open(self.filepath + '.prj', 'w')
    proj.write(self.proj)
    proj.close()
    print("generated: ", self.filepath + '.shp')
    
  
  def format_values( self, values ):
    dictValues = dict(enumerate(values))
    return list(map(lambda i: self.values_spec[self.headers[i]](dictValues[i]), dictValues))
    

def sort_data(data, headers):
  sortedata = dict()
  for d in data:
    if len(d):
      shape_id = d[headers.index("shape_id")]
      if not sortedata.get(shape_id):
        sortedata[shape_id] = list()
        
      
      sortedata[shape_id].append(d)
    
  # for k in sortedata.keys():
  #  sortedata[k] = sorted(sortedata[k], key=lambda d: d[headers.index("shape_pt_sequence")])

  return sortedata
  
  
cwd = os.getcwd()

# write as point layers by service
for folder in os.listdir(cwd):
  if 'gtfs' in folder:
    for file in os.listdir(os.path.join(cwd,folder)):
      if 'shape' in file:
        reader = csv.reader(open(os.path.join(cwd,folder,file), encoding="Latin1"), delimiter=',')
        writer = ShpGenerator(os.path.join(os.getcwd(), 'shp', folder), shapeType=1)
        headers = next(reader)
        writer.setup_layer_fields(headers)
        data = [d for d in reader]
        for row in data:
          if len(row):
            writer.write_row(row)
        
        writer.close()
          

# write as line layer by shape_id
for folder in os.listdir(cwd):
  if 'gtfs' in folder:
    for file in os.listdir(os.path.join(cwd,folder)):
      if 'shape' in file:
        reader = csv.reader( open( os.path.join(cwd, folder, file), encoding='Latin1'), delimiter=',')
        headers = next(reader)
        data = sort_data([d for d in reader], headers)
        writer = ShpGenerator(os.path.join(os.getcwd(), 'shp', folder + '-lines'), shapeType=3)
        writer.setup_layer_fields(["name"])
        for shape in data.keys():
          writer.draw_shape(data[shape], headers)

        writer.close()
