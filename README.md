# cycle-route-risk-assessor
Automating risk assessment of new cycling routes

## Description
Listens to WhatsApp messages within a user specified conversation, waiting for Strava route links to be shared. 

On sharing, cross-references the route against a Google My Maps custom map to find pins within 5 m of the route, and replies in the same WhatsApp group with a summary and an interactive HTML map.

The use case this has initially been developed for is automating risk assessment of new cycling routes, by comparing user abitrary user generated Strava routes against a master list of known risks. However the use cases are broader: for instance providing referencing to cafes on routes, or bike mechanics, etc.

The tool was initially developed for use by Royal Leamington Spa Cycling Club.

## Workflow

| Step | Role | Path | Status |
| ---- | ---  | ------ | ------ |
| Whatsapp (Twilio) Responder | Listen for WhastApp messages and respond | ```/main.py``` | In Progress |
| Fetch Route | Access the route from the Strava API. | ```/services/strava_client.py``` | In Progress |
| Fetch Pins | Access Google Map Pins. | ```/services/map_loader.py``` | Not Started |
| Route Pins | Find pins on the route (with 5m) |  ```/services/geoprocessor.py``` | Not Started |
| HTML Generator | Generate an HTML map of the route with the pins. |  ```/services/html_generator.py``` | Not Started |