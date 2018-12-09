#!/bin/bash

dumppath="$HOME/projects/mobility/gtfs/db/dumps"
pg_dump "mobility" > "$dumppath/mobility.dump.sql"
sed -i "s/orzo/xreojngi/g" "$dumppath/mobility.dump.sql"
psql "postgres://xreojngi:9DKmioeskkbaFDBAbeWxbe5be0LakMIg@horton.elephantsql.com:5432/xreojngi" -f "$dumppath/mobility.dump.sql"

