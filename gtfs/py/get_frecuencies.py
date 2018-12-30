import csv
import os
import math

cwd = os.getcwd()

def str_to_time(str_time):
    try:
        [hh, mm, ss] = str_time.split(':')
        return float(int(hh)*60+int(mm)) + int(ss)/60
    except:
        return str_time


def remove_columns(table, column_names):
  col_indexs = dict()
  for col_name in column_names:
    if col_name in table[0]:
      col_indexs[col_name] = table[0].index(col_name)

  for row_index in range(len(table)):
    for col_idx in col_indexs.values():
      table[row_index] = table[:col_idx] + table[col_idx+1:]


for folder in os.listdir('.'):
    if 'gtfs' in folder:
        service_name = "_".join(folder.split('_')[1:])
        stop_times = [[d[0], str_to_time(d[1]), str_to_time(d[2])] + d[3:] for d in csv.reader(open(os.path.join(cwd, folder, 'stop_times.txt'))) if len(d)]
        stop_times[1:] = sorted(sorted(stop_times[1:], key=lambda d: d[1]), key=lambda d: d[3])
        trips = [d for d in csv.reader(open(os.path.join(cwd, folder, 'trips.txt'))) if len(d)]
        routes = [d for d in csv.reader(open(os.path.join(cwd, folder, 'routes.txt'))) if len(d)]

        trips_map = dict()
        route_types = dict()
        headers = routes[0]
        route_id_idx = headers.index('route_id') if 'route_id' in headers else None
        route_type_idx = headers.index('route_type') if 'route_type' in headers else None
        for route in routes[1:]:
          trips_map[route[route_id_idx]] = dict()
          route_types[route[route_id_idx]] = route[route_type_idx]

        headers = trips[0]
        route_id_idx = headers.index('route_id') if 'route_id' in headers else None
        trip_id_idx = headers.index('trip_id') if 'trip_id' in headers else None
        for trip in trips[1:]:
          if len(trip):
            trips_map[trip[route_id_idx]][trip[trip_id_idx]] = True

        new_headers = ['route_id', 'route_type', 'service_name']
        # for header in new_headers:
        # remove_columns(stop_times, new_headers)

        stop_times[0] += new_headers
        for stop in stop_times[1:]:
            stop_route_id, stop_route_type = None, None
            for route_id, route in trips_map.items():
                if route.get(stop[0]):
                    stop_route_id = route_id
                    stop_route_type = route_types[route_id]

            stop += [stop_route_id, stop_route_type, service_name]
            stop[1] = str_to_time(stop[1])

        open(os.path.join(cwd, folder, 'stop_times.txt'), 'w').write("\n".join([",".join([str(d) for d in row]) for row in stop_times]))
        
        stops = dict()
        for stop in stop_times[1:]:
            stops[stop[3]] = stops.get(stop[3], {})
            stops[stop[3]][stop[len(stop)-2]] = stops[stop[3]].get(stop[len(stop)-2], [])
            stops[stop[3]][stop[len(stop) - 2]].append(stop)

        intervals = dict()
        for stop in stops.keys():
            intervals[stop] = intervals.get(stop, dict())
            for line in stops[stop].keys():
                intervals[stop][line] = intervals[stop].get(line, None)
                acum = []
                for idx in range(len(stops[stop][line])):
                    if idx < len(stops[stop][line])-1:
                        alpha = abs(float(stops[stop][line][idx+1][1]) - float(stops[stop][line][idx][1]))
                        if alpha:
                            acum += [alpha]

                acum.sort()
                try:
                    intervals[stop][line] = acum[int(math.floor(len(acum)/2))]
                except Exception as e:
                    intervals[stop][line] = -999

        data = "\n".join([",".join(["stop_id", "route_id", "avg_time"])] + [
            ",".join([stop, line, str(intervals[stop][line])]) for stop in intervals.keys()
            for line in intervals[stop].keys()
        ])

        open(os.path.join(cwd, folder, 'frequencies.txt'), 'w').write(data)
        print(os.path.join(cwd, folder, 'frequencies.txt') + ' was created')