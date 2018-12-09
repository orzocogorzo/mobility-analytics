[timeout:180][bbox:41.2563,1.9304,41.5729,2.4397];
(
  node["highway"]["highway"~".*(primary|secondary|tertiary|residential|service|unclassified|living_street|trunk|road).*"];
  way["highway"]["highway"~".*(primary|secondary|tertiary|residential|service|unclassified|living_street|trunk|road).*"];
  relation["highway"]["highway"~".*(primary|secondary|tertiary|residential|service|unclassified|living_street|trunk|road).*"];
)->.roads;
(
    node["highway"]["maxspeed"](if:t["maxspeed"] > 50);
    way["highway"]["maxspeed"](if:t["maxspeed"] > 50);
    relation["highway"]["maxspeed"](if:t["maxspeed"] > 50);
)->.no_limited_speed;
(
  .roads;
  - .no_limited_speed;
);
out body;
>;
out qt;