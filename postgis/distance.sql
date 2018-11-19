ALTER TABLE
  highways
DROP COLUMN IF EXISTS length;

ALTER TABLE
  highways
ADD COLUMN
  length float;

UPDATE
  highways
SET
  length = ST_Length(line25831)
WHERE
  line25831 IS NOT null;