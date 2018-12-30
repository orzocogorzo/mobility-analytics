ALTER TABLE width.rotate90
DROP COLUMN difference;

ALTER TABLE width.rotate90
ADD COLUMN difference geometry(MultiLineString, 25831);

UPDATE width.rotate90
SET difference = ST_Multi(ST_Difference(lines.geom, intersections.geom))
  FROM
    width.rotate90 as lines
  LEFT JOIN (
    SELECT
      a.line_id,
      ST_UNION(a.poly) AS geom
    FROM (
      SELECT
        tmp_lines.id as line_id,
        cd.geom as poly
      FROM
        width.rotate90 as tmp_lines,
        cadastre as cd
      WHERE
        ST_Intersects(
          tmp_lines.geom::geometry,
          cd.geom::geometry
        ) = true
    ) as a
    GROUP BY
      a.line_id
  ) as intersections
  ON
    lines.id = intersections.line_id;