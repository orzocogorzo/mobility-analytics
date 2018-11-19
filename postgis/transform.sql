ALTER TABLE
  highways
DROP COLUMN IF EXISTS point25831,
DROP COLUMN IF EXISTS line25831;

ALTER TABLE
  highways
ADD COLUMN point25831 geometry(Point, 25831),
ADD COLUMN line25831 geometry(LineString, 25831);

UPDATE
  highways
SET
  point25831 = ST_Transform(geom, 25831)
WHERE
  ST_GeometryType(geom) = 'ST_Point';

UPDATE
  highways
SET
  line25831 = ST_Transform(geom, 25831)
WHERE
  ST_GeometryType(geom) = 'ST_LineString';