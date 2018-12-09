[timeout:100][bbox:41.2563,1.9304,41.5729,2.4397];
(
    node["highway"]["highway"~"(primary|secondary|trunk)"](if:(is_number(t["maxspeed"]) && t["maxspeed"] > 50) || !is_tag("maxspeed"));
    way["highway"]["highway"~"(primary|secondary|trunk)"](if:(is_number(t["maxspeed"]) && t["maxspeed"] > 50) || !is_tag("maxspeed"));
    relation["highway"]["highway"~"(primary|secondary|trunk)"](if:(is_number(t["maxspeed"]) && t["maxspeed"] > 50) || !is_tag("maxspeed"));
)->.interurbans;
(
  node["highway"]["highway"~"(primary|secondary|trunk)"]["sidewalk"](if:t["sidewalk"] != "no" && t["sidewalk"] != "none");
  way["highway"]["highway"~"(primary|secondary|trunk)"]["sidewalk"](if:t["sidewalk"] != "no" && t["sidewalk"] != "none");
  relation["highway"]["highway"~"(primary|secondary|trunk)"]["sidewalk"](if:t["sidewalk"] != "no" && t["sidewalk"] != "none");
)->.walkables;
(
  node["highway"]["highway"~"(primary|secondary|trunk)"]["foot"](if:t["foot"] != "no");
  way["highway"]["highway"~"(primary|secondary|trunk)"]["foot"](if:t["foot"] != "no");
  relation["highway"]["highway"~"(primary|secondary|trunk)"]["foot"](if:t["foot"] != "no");
)->.footables;
(
  .interurbans;
  - (
    .footables;
    .walkables;
  );
);
out body;
>;
out skel qt;