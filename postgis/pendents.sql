ALTER TABLE
  highways
DROP COLUMN IF EXISTS pendent;

ALTER TABLE
  highways
ADD COLUMN pendent float;

UPDATE
  highways
SET
  pendent = ABS(source_alt - target_alt)/length
WHERE
  length != 0 AND line25831 IS NOT null;