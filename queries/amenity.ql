[timeout:100][bbox:41.2563,1.9304,41.5729,2.4397];
(
    node[amenity][amenity!~"^(fuel|parking|parking_entrance|parking_space|charging_station|null)$"];
    way[amenity][amenity!~"^(fuel|parking|parking_entrance|parking_space|charging_station|null)$"];
    relation[amenity][amenity!~"^(fuel|parking|parking_entrance|parking_space|charging_station|null)$"];
);
out body;
>;
out qt;