[timeout:100][bbox:41.2563,1.9304,41.5729,2.4397];
(
    node["cycleway"];
    way["cycleway"];
    relation["cycleway"];
)->.cyclway;
(
    node["highway"~"cycleway"];
    way["highway"~"cycleway"];
    relation["highway"~"cycleway"];
)->.highway;
(
  .cycleway;
  .highway;
);
out body;
>;
out skel qt;