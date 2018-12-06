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
    ST_INTERSECTS(a.geom, b.buffer_geom)
) as temp
WHERE
  temp.id = highways.id;
  