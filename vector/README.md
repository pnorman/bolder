This directory contains the definitions needed to generate the vector tiles

## Dependencies

Generating vector tiles depends on

- osm2pgsql 0.90.1 or later with Lua support, loaded with `-G --hstore` and the Lua transform script provided
- PostgreSQL 9.3 or later. 9.5 or later is recommended and better tested.
- PostGIS 2.0 or later. 2.3 or later is recommended as earlier versions are not adequately tested with the style.

## Installation

##

### OpenStreetMap Data

You need OpenStreetMap data loaded into a PostGIS database with [osm2pgsql](https://github.com/openstreetmap/osm2pgsql) using the [OpenStreetMap Carto schema](https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md#openstreetmap-data)

Start by setting up your database to have PostGIS and hstore with ``psql -d gis -c 'CREATE EXTENSION postgis; CREATE EXTENSION hstore;'``, then grab some OSM data. It's probably easiest to grab an PBF of OSM data from [Mapzen](https://mapzen.com/metro-extracts/) or [geofabrik](http://download.geofabrik.de/). Once you've done that, import with osm2pgsql:

```
osm2pgsql -G --hstore --style openstreetmap-carto.style --tag-transform-script openstreetmap-carto.lua -d gis ~/path/to/data.osm.pbf
```
