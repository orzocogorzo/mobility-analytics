[timeout:100][bbox:41.2563,1.9304,41.5729,2.4397];
(
    node[highway][highway!~"^(crossing|level_crossing)$"]["maxspeed"](if:t["maxspeed"] <= 30);
    way[highway][highway!~"^(crossing|level_crossing)$"]["maxspeed"](if:t["maxspeed"] <= 30);
    relation[highway][highway!~"^(crossing|level_crossing)$"]["maxspeed"](if:t["maxspeed"] <= 30);
);
out body;
>>;
out skel qt;