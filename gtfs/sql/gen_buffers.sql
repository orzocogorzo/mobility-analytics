DROP TABLE IF EXISTS gtfs.stops;
CREATE TABLE gtfs.stops AS (
  SELECT
      stop_id, 
      stop_name,
      stop_lat,
      stop_lon,
      '2acor' as service_name
    FROM
      gtfs_2acor.stops
  UNION
    SELECT
      stop_id, 
      stop_name,
      stop_lat,
      stop_lon,
      'amb' as service_name
    FROM
      gtfs_amb.stops
  UNION
    SELECT
      stop_id, 
      stop_name,
      stop_lat,
      stop_lon,
      'tmb' as service_name
    FROM
      gtfs_tmb.stops
  UNION
    SELECT
      stop_id, 
      stop_name,
      stop_lat,
      stop_lon,
      'fgc' as service_name
    FROM
      gtfs_fgc.stops
  UNION
    SELECT
      stop_id, 
      stop_name,
      stop_lat,
      stop_lon,
      'tram_tbs' as service_name
    FROM
      gtfs_tram_tbs.stops
  UNION
    SELECT
      stop_id, 
      stop_name,
      stop_lat,
      stop_lon,
      'tram_tbx' as service_name
    FROM
      gtfs_tram_tbx.stops
  UNION
    SELECT
      stop_id, 
      stop_name,
      stop_lat,
      stop_lon,
      'renfe' as service_name
    FROM
      gtfs_renfe.stops
  UNION
    SELECT
      stop_id, 
      stop_name,
      stop_lat,
      stop_lon,
      'gencat' as service_name
    FROM
      gtfs_gencat.stops
  );

ALTER TABLE gtfs.stops
ADD COLUMN geom geometry(Point, 4326),
ADD COLUMN stop_type text,
ADD COLUMN buffer geometry(Polygon, 25831);

UPDATE gtfs.stops
SET geom = ST_SetSRID(ST_Point(stop_lon, stop_lat), 4326);

UPDATE gtfs.stops
SET stop_type = stop_times.route_type
FROM (
  SELECT
      stop_id,
      route_type
    FROM
      gtfs_2acor.stop_times
  UNION
    SELECT
      stop_id,
      route_type
    FROM
      gtfs_amb.stop_times
  UNION
    SELECT
      stop_id,
      route_type
    FROM
      gtfs_tmb.stop_times
  UNION
    SELECT
      stop_id,
      route_type
    FROM
      gtfs_fgc.stop_times
  UNION
    SELECT
      stop_id,
      route_type
    FROM
      gtfs_tram_tbs.stop_times
  UNION
    SELECT
      stop_id,
      route_type
    FROM
      gtfs_tram_tbx.stop_times
  UNION
    SELECT
      stop_id,
      route_type
    FROM
      gtfs_renfe.stop_times
  UNION
    SELECT
      stop_id,
      route_type
    FROM
      gtfs_gencat.stop_times
  ) as stop_times
WHERE
    stops.stop_id = stop_times.stop_id
  AND
    stops.service_name = stop_times.service_name;

UPDATE gtfs.stops
SET buffer = CASE
  WHEN ( 
      stop_type = '1'
    OR   
      stop_type = '2'
  ) THEN
    ST_Buffer(ST_Transform(geom, 25831), 960)
  ELSE
    ST_Buffer(ST_Transform(geom, 25831), 680)
  END;