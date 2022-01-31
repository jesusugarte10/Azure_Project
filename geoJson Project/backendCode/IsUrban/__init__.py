import json
import matplotlib.path as mplPath
import numpy as np

import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    geometry = req.params.get('geometry')

    if not geometry:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            geometry = req_body.get('geometry')

    if geometry:
        pointJson = req.get_json()

        Longitude = pointJson['geometry']['coordinates'][0]
        Latitude = pointJson['geometry']['coordinates'][1]
        point = (Longitude, Latitude)

        path = "/home/site/wwwroot/IsUrban/polygons.geojson"

        #Loading geoJSON File
        with open(path) as Data:
            data=json.load(Data)

        for features in data['features']:
            #Getting Coordinates of Polygon
            coordinates = features['geometry']['coordinates'][0]

            #Generating Path of Polygon 
            poly_path = mplPath.Path(np.array(coordinates))

            # If Point belongs to any of the locations return true
            if(poly_path.contains_point(point)):
                return func.HttpResponse("True",
                    status_code=200)
            else:
                continue

        # we return false assuming no point inside polygon is found
        return func.HttpResponse(
                "False",
                status_code=200
            )
        
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Please use geojson format",
            status_code=200
        )