def street_type(doc, weight, mode_idx, criteria):
  type = doc['properties']['tags']['highway']
  return criteria[type][mode_idx]*weight if criteria[doc['properties']['tags']['highway']] else None


def slope(doc, weight, mode_idx, criteria):
  key = doc['properties']['slope'] <= 5 and '0-5' or doc['properties']['slope'] > 5 and doc['properties']['slope'] <= 8 and '5-8' or '>8'
  return criteria[key][mode_idx]*weight if criteria[key] is not None and criteria[key][mode_idx] is not None else None


def length(doc, weight, mode_idx, criteria):
  key = doc['properties']['length'] <= 130 and '0-130' or doc['properties']['length'] > 130 and doc['properties']['length'] <= 500 and '130-500' or '<500'
  return criteria[key][mode_idx] * weight if criteria[key] is not None and criteria[key][mode_idx] is not None else None


def maxspeed(doc, weight, mode_idx, criteria):
    if not doc['properties'].get("maxspeed"):
        return None

    key = doc['properties']['maxspeed'] <= 30 and '0-30' or doc['properties']['maxspeed'] > 30 \
        and doc['properties']['maxspeed'] <= 50 and '30-50' or doc['properties']['maxspeed'] >= 50 \
        and doc['properties']['maxspeed'] < 80 and '50-80' or '>80'

    return criteria[key][mode_idx] * weight if criteria[key] is not None and criteria[key][mode_idx] is not None else None


def bike_lane(doc, weight, mode_idx, criteria):
    return doc["properties"]["bike_lane"] and criteria[mode_idx] and criteria[mode_idx]*weight or None


def pt(doc, weight, mode_idx, criteria):
    return doc["properties"]["pt"] and criteria[mode_idx] and criteria[mode_idx] * weight or None


def bike_parking(doc, weight, mode_idx, criteria):
    return doc["properties"]["bike_parking"] and criteria[mode_idx] and criteria[mode_idx] * weight or None


def motor_parking(doc, weight, mode_idx, criteria):
    return doc["properties"]["motor_parking"] and criteria[mode_idx] and criteria[mode_idx] * weight or None


def land_use(doc, weight, mode_idx, criteria):
    return criteria[doc["properties"]["land_use"]][mode_idx] * weight if criteria[doc["properties"]["land_use"]] is not None \
                                                                         and criteria[doc["properties"]["land_use"]][mode_idx] is not None else None


def lanes(doc, weight, mode_idx, criteria):
    key = doc["properties"]["lanes"] > 4 and '>4' or str(doc["properties"]["lanes"])
    return criteria[key][mode_idx] * weight if criteria[key] is not None and criteria[key][mode_idx] is not None else None


def vegetation(doc, weight, mode_idx, criteria):
    return doc["properties"]["vegetation"] and criteria[mode_idx] and criteria[mode_idx] * weight or None


def local_facilities(doc, weight, mode_idx, criteria):
    return doc["properties"]["local_facilities"] and criteria[mode_idx] and criteria[mode_idx] * weight or None


def public_space(doc, weight, mode_idx, criteria):
    return doc["properties"]["public_space"] and criteria[mode_idx] and criteria[mode_idx] * weight or None


table = {
    "columns": [
        "pedestrian",
        "byclicle",
        "pt",
        "motor"
    ],
    "rows": [
        "street_type",
        "slope",
        "length",
        "maxspeed",
        "bike_lane",
        "pt",
        "bike_parking",
        "motor_parking",
        "land_use",
        "lanes",
        "vegetation",
        "local_facilities",
        "public_space"

    ],
    "data": [
        {
            "weight": [0.2, 0.1, None, 0.20],
            "fn": street_type
        },
        {
            "weight": [0.2, 0.2, None, None],
            "fn": slope
        },
        {
            "weight": [0.1, 0.05, None, 0.2],
            "fn": length
        },
        {
            "weight": [0.1, 0.15, None, 0.2],
            "fn": maxspeed
        },
        {
            "weight": [None, 0.15, None, None],
            "fn": bike_lane
        },
        {
            "weight": [None, None, 1, None],
            "fn": pt
        },
        {
            "weight": [None, 0.5, None, None],
            "fn": bike_parking
        },
        {
            "weight": [None, None, None, 0.20],
            "fn": motor_parking
        },
        {
            "weight": [0.05, None, None, None],
            "fn": land_use
        },
        {
            "weight": [0.1, 0.1, None, 0.2],
            "fn": lanes
        },
        {
            "weight": [0.1, 0.1, None, None],
            "fn": vegetation
        },
        {
            "weight": [0.05, 0.05, None, None],
            "fn": local_facilities
        },
        {
            "weight": [0.1, 0.05, None, None],
            "fn": public_space
        }
    ]
}