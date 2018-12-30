ALTER TABLE gtfs.pt_served_ways
ALTER COLUMN
    id
  TYPE 
    bigint
  USING 
    id::bigint;

DROP TABLE IF EXISTS gtfs.pt_served_ways_noded;
SELECT pgr_nodeNetwork(
  'gtfs.pt_served_ways',
  2,
  'id',
  'geom25831'
);

DROP TABLE IF EXISTS gtfs.pt_served_ways_noded_vertices_pgr;
SELECT pgr_createTopology(
  'gtfs.pt_served_ways_noded',
  2,
  'geom25831',
  'old_id',
  'source',
  'target'
);

SELECT pgr_analyzeGraph(
  'gtfs.pt_served_ways_noded',
  2,
  'geom25831',
  'old_id'
);