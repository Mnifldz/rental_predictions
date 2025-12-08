from math import radians, sin, cos, sqrt, atan2
import re

def haversine_miles(lat1, lon1, lat2, lon2):
    R = 3958.8  # Earth radius in miles
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def multipolygon_centroid(wkt: str):
    """
    Converts MULTIPOLYGON WKT string to a centroid (lon, lat)
    """
    # Extract all coordinate pairs: [-74.14 40.54, ...]
    matches = re.findall(r'(-?\d+\.\d+) (-?\d+\.\d+)', wkt)
    if not matches:
        return (None, None)
    
    lons, lats = zip(*[(float(lon), float(lat)) for lon, lat in matches])
    centroid_lon = sum(lons) / len(lons)
    centroid_lat = sum(lats) / len(lats)
    
    return (centroid_lon, centroid_lat)