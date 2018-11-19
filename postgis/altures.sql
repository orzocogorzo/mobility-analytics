ALTER TABLE 
  highways
DROP COLUMN IF EXISTS source,
DROP COLUMN IF EXISTS target,
DROP COLUMN IF EXISTS x1,
DROP COLUMN IF EXISTS x2,
DROP COLUMN IF EXISTS y1,
DROP COLUMN IF EXISTS y2,
DROP COLUMN IF EXISTS source_alt,
DROP COLUMN IF EXISTS target_alt;

ALTER TABLE 
  highways
ADD COLUMN source geometry(POINT, 4326),
ADD COLUMN target geometry(POINT, 4326),
ADD COLUMN x1 FLOAT,
ADD COLUMN x2 FLOAT,
ADD COLUMN y1 FLOAT,
ADD COLUMN y2 FLOAT,
ADD COLUMN source_alt FLOAT,
ADD COLUMN target_alt FLOAT;

UPDATE
  highways
SET
  source = ST_StartPoint(geom),
  target = ST_EndPoint(geom);

UPDATE
  highways
SET
  x1 = st_X(source),
  y1 = st_Y(source),
  x2 = st_X(target),
  y2 = st_Y(target);

UPDATE
  highways
SET
  source_alt = tmp.alt
FROM
  (
    SELECT
      g.id,
      ST_Value(r.rast, g.source) as alt
    FROM
      raster.mde as r,
      highways as g
    WHERE
      ST_Intersects(r.rast, g.source) = true
  ) as tmp
WHERE
  highways.id = tmp.id;

UPDATE
  highways
SET
  target_alt = tmp.alt
FROM
  (
    SELECT
      g.id,
      ST_Value(r.rast, g.target) as alt
    FROM
      raster.mde as r,
      highways as g
    WHERE
      ST_Intersects(r.rast, g.target) = true
  ) as tmp
WHERE
  highways.id = tmp.id;