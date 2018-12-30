CREATE SCHEMA IF NOT EXISTS gtfs_merge;
CREATE TABLE gtfs_merge.stops_all AS (
	SELECT 'gtfs_amb' as source, stop_id,stop_lat,stop_lon FROM gtfs_amb.stops UNION
	SELECT 'gtfs_fgc' as source,stop_id,stop_lat,stop_lon FROM gtfs_fgc.stops UNION
	SELECT 'gtfs_renfe' as source, stop_id,stop_lat,stop_lon FROM gtfs_renfe.stops UNION
	SELECT 'gtfs_tmb' as source, stop_id,stop_lat,stop_lon FROM gtfs_tmb.stops UNION
	SELECT 'gtfs_tram_tbs' as source, stop_id, stop_lat, stop_lon FROM gtfs_tram_tbs.stops UNION
	SELECT 'gtfs_tram_tbx' as source,stop_id,stop_lat,stop_lon FROM gtfs_tram_tbx.stops
);

DROP TABLE IF EXISTS gtfs_merge.stops_all;



ALTER TABLE gtfs_tram_tbs.stops
RENAME COLUMN column_name TO new_column_name;

DROP TABLE IF EXISTS gtfs_tram_tbs.stops;
CREATE TABLE gtfs_tram_tbs.stops
(stop_id varchar, stop_name text,stop_desc text, stop_lat double precision, stop_lon double precision, stop_url text);

\copy gtfs_tram_tbs.stops(stop_id,stop_name,stop_desc,stop_lat,stop_lon,stop_url) FROM 'C:\Users\Cristina Ferrer\Documents\mobility\01_GTFS\00_GTFS_DEF_2018\TRAM_TBS_1801\stops.txt' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS gtfs_tram_tbx.stops;
CREATE TABLE gtfs_tram_tbx.stops
(stop_id varchar, stop_name text,stop_desc text, stop_lat double precision, stop_lon double precision, stop_url text);

\copy gtfs_tram_tbx.stops(stop_id,stop_name,stop_desc,stop_lat,stop_lon,stop_url) FROM 'C:\Users\Cristina Ferrer\Documents\mobility\01_GTFS\00_GTFS_DEF_2018\TRAM_TBX_1801\stops.txt' DELIMITER ',' CSV HEADER;
