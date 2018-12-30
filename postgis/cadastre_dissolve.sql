DROP TABLE IF EXISTS width.dissolve_cad;
CREATE TABLE width.dissolve_cad AS (
	SELECT 'cadastre' as dissolve_key,ST_union(geom) as geom
	FROM cadastre
		GROUP BY dissolve_key
		ORDER BY dissolve_key
		OFFSET 0 ROWS
		FETCH NEXT 50000 ROWS ONLY
	);
INSERT INTO width.dissolve_cad (dissole_key,geom) VALUES (
	SELECT 'cadastre' as dissolve_key,ST_union(geom) as geom
	FROM cadastre
		GROUP BY dissolve_key
		ORDER BY dissolve_key
		OFFSET 50001 ROWS
		FETCH NEXT 50000 ROWS ONLY
	);