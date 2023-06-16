## SPARQL CONSTRUCT queries for trasforming Getty ULAN

Requirements: python 3.11 and requests

Run convert.py

This is meant to read CONSTRUCT queries from the queries/ directory and execute them on the GETTY ULAN endpoint. Results are written on the ttl/ directory. Every query file shoul have the extension .SPARQL

## Build Fuseki container for publishing the data

`docker build -t ulan-fuseki .`

## Run

`docker run -d -p 3070:3030 --name ulan ulan-fuseki`

Get the Fuseki control panel password with `docker logs ulan`

## Upgrade

```
docker build -t ulan-fuseki .
docker stop ulan
docker rm ulan
docker run -d -p 3070:3030 --restart unless-stopped --name ulan ulan-fuseki
```