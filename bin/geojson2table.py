import sys
import simplejson as json

data = json.load(open(sys.argv[1]))
table = data["features"]
strTable = '\n'.join([json.dumps(d) for d in table])

open(sys.argv[2], 'w').write(strTable)