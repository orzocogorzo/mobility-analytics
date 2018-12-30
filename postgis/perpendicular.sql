CREATE SCHEMA IF NOT EXISTS width;
DROP TABLE IF EXISTS width.rotate90;
CREATE TABLE width.rotate90 AS  
	SELECT id, ST_rotate(geom25831,pi()/2,ST_Centroid(geom25831))
	FROM highways
		WHERE ST_GeometryType(geom)='ST_LineString';
