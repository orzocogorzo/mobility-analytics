DROP TABLE IF EXISTS width.rotate90;
CREATE TABLE width.rotate90 AS
  SELECT
    id,
    ST_MakeLine(
      ST_Centroid(
        ST_OffsetCurve(
          geom25831,
          50
        )
      ),
      ST_Centroid(
        ST_OffsetCurve(
          geom25831,
          -50
        )
      )
    ) AS geom
  FROM
    highways_noded
  WHERE
    ST_GeometryType(geom25831) = 'ST_LineString';