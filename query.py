import requests
import json

def get_liquefaction_at_point(x, y):
    url = "https://gis.ecan.govt.nz/arcgis/rest/services/Public/Canterbury_Liquefaction_Susceptibility/MapServer/7/query"
    geometry = {
        "x": x,
        "y": y,
        "spatialReference": {"wkid": 2193}
    }
    params = {
        "geometry": json.dumps(geometry),
        "geometryType": "esriGeometryPoint",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "Liquefaction_Susceptibility",
        "returnGeometry": "false",
        "f": "json"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    try:
        return data['features'][0]['attributes']['Liquefaction_Susceptibility']
    except (IndexError, KeyError):
        return "No susceptibility data found at that location."

# Example usage:

if __name__ == "__main__":
    print(get_liquefaction_at_point(1511300, 5266130))