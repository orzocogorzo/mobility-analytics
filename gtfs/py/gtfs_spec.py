gtfs_spec = {
  "agency": {
    "agency_id": "varchar",
    "agency_name": "text",
    "agency_url": "text",
    "agency_timezone": "text",
    "agency_lang": "text",
    "agency_phone": "text",
    "agency_fare_url": "text",
    "agency_email": "text"
  },
  "calendar": {
    "service_id": "varchar",
    "modnay": "smallint",
    "tuesday": "smallint",
    "wednesday": "smallint",
    "thurday": "smallint",
    "friday": "smallint",
    "staruday": "smallint",
    "sunday": "smallint",
    "start_date": "date",
    "end_date": "date"
  },
  "calendar_dates": {
    "service_id": "varchar",
    "date": "date",
    "exception_type": "smallint"
  },
  "fare_attributes": {
    "fare_id": "varchar",
    "price": "decimal",
    "currency_type": "text",
    "payment_method": "smallint",
    "transfers": "smallint",
    "agency_id": "varchar",
    "transfer_duration": "bigint"
  },
  "fare_rules": {
    "fare_id": "varchar",
    "route_id": "varchar",
    "origin_id": "varchar",
    "detination_id": "varchar",
    "contains_id": "varchar"
  },
  "feed_info": {
    "feed_publisher_name": "text",
    "feed_publisher_url": "text",
    "feed_lang": "text",
    "feed_start_date": "date",
    "feed_end_date": "date",
    "feed_version": "varchar"
  },
  "frequencies": {
    "trip_id": "varchar",
    "start_time": "time",
    "end_time": "time",
    "headway_secs": "bigint",
    "exact_times": "smallint"
  },
  "routes": {
    "route_id": "varchar",
    "agency_id": "varchar",
    "route_short_name": "text",
    "route_long_name": "text",
    "route_desc": "text",
    "route_type": "smallint",
    "route_url": "text",
    "route_color": "varchar",
    "route_text_color": "varchar",
    "route_sort_order": "integer"
  },
  "shapes": {
    "shape_id": "varchar",
    "shape_pt_lat": "double precision",
    "shape_pt_lon": "double precision",
    "shape_pt_sequence": "integer",
    "shape_dist_traveled": "decimal"
  },
  "stop_times": {
    "trip_id": "varchar",
    "arrival_time": "varchar",
    "departue_time": "varchar",
    "stop_id": "varchar",
    "stop_sequence": "integer",
    "stop_headsign": "text",
    "pickup_type": "smallint",
    "drop_off_type": "smallint",
    "shape_dist_traveled": "double precision",
    "timepoint": "smallint"
  },
  "stops": {
    "stop_id": "varchar",
    "stop_code": "varchar",
    "stop_name": "text",
    "stop_lat": "double precision",
    "stop_lon": "double precision",
    "zone_id": "varchar",
    "stop_url": "text",
    "location_type": "smallint",
    "parent_station": "varchar",
    "stop_timezone": "text",
    "wheelchair_boarding": "smallint"
  },
  "transfers": {
    "from_stop_id": "varchar",
    "to_stop_id": "varchar",
    "transfer_type": "smallint",
    "min_transfer_time": "bigint"
  },
  "trips": {
    "route_id": "varchar",
    "service_id": "varchar",
    "trip_id": "varchar",
    "trip_headsign": "text",
    "trip_short_name": "text",
    "direction_id": "smallint",
    "block_id": "varchar",
    "shape_id": "varchar",
    "wheelchair_accessible": "smallint",
    "bikes_allowed": "smallint"
  }
}
