This directory contains the definitions needed to generate the vector tiles

## Dependencies

Generating vector tiles depends on

- osm2pgsql 0.90.1 or later with Lua support, loaded with `-G --hstore` and the Lua transform script provided
- PostgreSQL 9.3 or later. 9.5 or later is recommended and better tested.
- PostGIS 2.0 or later. 2.3 or later is recommended as earlier versions are not adequately tested with the style.
- Python 3.4 with PyYaml, PsycoPG2, and requests.

On Debian or Ubuntu, these can be installed with

```sh
sudo apt-get install postgresql postgis osm2pgsql \
    python3-yaml python3-psycopg2 python3-requests
```

## Installation

Installation consists of installing the dependencies above, loading OpenStreetMap data, loading other data sources, and installing the vector tile server.

### OpenStreetMap Data

You need OpenStreetMap data loaded into a PostGIS database with [osm2pgsql](https://github.com/openstreetmap/osm2pgsql) using the [OpenStreetMap Carto schema](https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md#openstreetmap-data)

Start by setting up your database to have PostGIS and hstore with ``psql -d gis -c 'CREATE EXTENSION postgis; CREATE EXTENSION hstore;'``, then grab some OSM data. It's probably easiest to grab an PBF of OSM data from [Mapzen](https://mapzen.com/metro-extracts/) or [Geofabrik](http://download.geofabrik.de/). Once you've done that, import with osm2pgsql:

```
osm2pgsql --style openstreetmap-carto.style --tag-transform-script openstreetmap-carto.lua \
    -G --hstore -d gis ~/path/to/data.osm.pbf
```

### External Data

Bolder relies on external data sources from OpenStreetMapData.com and Natural Earth. These are downloaded and loaded into the database with a script. This can be run with

```
./get-external-data.py
```

More options are available with the `--help` option.

## Functions

Bolder requires some stylesheet-independent functions

```sh
psql -Xq -d gis -f functions.sql
```

## Tegola

The vector definitions work with [Tegola](http://tegola.io/). Tegola can be downloaded from its [release page](https://github.com/terranodo/tegola/releases). The definitions are developed against v0.6.0.

The tiles can be served with `TEGOLA_OPTIONS=DontSimplifyGeo tegola serve` and accessed at http://localhost:8080/.
