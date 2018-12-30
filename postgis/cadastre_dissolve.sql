DROP TABLE IF EXISTS width.dissolve_cad;
CREATE TABLE width.dissolve_cad AS (
	SELECT
    ST_Union(a.geom) as geom
  FROM (
    SELECT
      'cadastre' as dissolve_key,
      geom
    FROM
      cadastre
    ORDER BY ogc_fid
    OFFSET 0 ROWS
    FETCH NEXT 50000 ROWS ONLY
  ) a
  GROUP BY dissolve_key
);

INSERT INTO width.dissolve_cad
	SELECT
    ST_Union(a.geom) as geom
  FROM (
    SELECT
      'cadastre' as dissolve_key,
      geom
    FROM
      cadastre
    ORDER BY ogc_fid
    OFFSET 50001 ROWS
    FETCH NEXT 50000 ROWS ONLY
  ) a
  GROUP BY dissolve_key;

INSERT INTO width.dissolve_cad
	SELECT
    ST_Union(a.geom) as geom
  FROM (
    SELECT
      'cadastre' as dissolve_key,
      geom
    FROM
      cadastre
    ORDER BY ogc_fid
    OFFSET 100001 ROWS
    FETCH NEXT 50000 ROWS ONLY
  ) a
  GROUP BY dissolve_key;

INSERT INTO width.dissolve_cad
	SELECT
    ST_Union(a.geom) as geom
  FROM (
    SELECT
      'cadastre' as dissolve_key,
      geom
    FROM
      cadastre
    ORDER BY ogc_fid
    OFFSET 150001 ROWS
    FETCH NEXT 50000 ROWS ONLY
  ) a
  GROUP BY dissolve_key;

INSERT INTO width.dissolve_cad
	SELECT
    ST_Union(a.geom) as geom
  FROM (
    SELECT
      'cadastre' as dissolve_key,
      geom
    FROM
      cadastre
    ORDER BY ogc_fid
    OFFSET 200001 ROWS
    FETCH NEXT 50000 ROWS ONLY
  ) a
  GROUP BY dissolve_key;

  INSERT INTO width.dissolve_cad
	SELECT
    ST_Union(a.geom) as geom
  FROM (
    SELECT
      'cadastre' as dissolve_key,
      geom
    FROM
      cadastre
    ORDER BY ogc_fid
    OFFSET 250001 ROWS
    FETCH NEXT 50000 ROWS ONLY
  ) a
  GROUP BY dissolve_key;

INSERT INTO width.dissolve_cad
SELECT ST_Union(geom) as geom 
FROM width.dissolve_cad;