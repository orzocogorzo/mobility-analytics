ALTER TABLE cycleways
DROP COLUMN geom25831;

ALTER TABLE cycleways
ADD COLUMN geom25831 geometry(LineString, 25831);

UPDATE cycleways
SET geom25831=ST_Transform(geom, 25831);

ALTER TABLE cycleways
DROP COLUMN buffer_geom;

ALTER TABLE cycleways
ADD COLUMN buffer_geom geometry(Polygon, 25831);

UPDATE cycleways
SET buffer_geom = ST_Buffer(geom25831, 150);

ALTER TABLE highways
DROP COLUMN in_bikelane;

ALTER TABLE highways
ADD COLUMN in_bikelane BOOL;

UPDATE highways
SET in_bikelane=temp.is_in
FROM (
  SELECT
    a.id as id,
    true as is_in
  FROM 
    highways as a,
    cycleways as b
  WHERE
    ST_INTERSECTS(a.line25831, b.buffer_geom)
) as temp
WHERE
  temp.id = highways.id;
  