DROP TABLE IF EXISTS gtfs.pt_served_ways;
CREATE TABLE gtfs.pt_served_ways AS
  SELECT 
    highways.ogc_fid,
    highways.id,
    highways.geom,
    highways.geom25831,
    highways.length,
    highways.pendent
  FROM  
    highways,
    (
      SELECT 
        'buffer-union' as id,
        ST_UNION(buffer) as geom 
      FROM 
        gtfs.stops
      GROUP BY 
        id
    ) as buffer
  WHERE
      ST_Intersects(highways.geom25831, buffer.geom)
    AND
      highways.line25831 IS NOT NULL;