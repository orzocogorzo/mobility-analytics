[bbox:41.2563,1.9304,41.5729,2.4397][timeout:800];
(
  node["amenity"="police"];
  way["amenity"="police"];
  relation["amenity"="police"];
)->.polices;
(
  node["amenity"="bank"];
  way["amenity"="bank"];
  rel["amenity"="bank"];
)->.banks;
(
  node.banks(around.polices:500);
  way.banks(around.polices:500);
  rel.banks(around.polices:500);
)->.banksNearPolices;
(
  .banks;
  - .banksNearPolices;
);
out body;
>;
out geom qt;

