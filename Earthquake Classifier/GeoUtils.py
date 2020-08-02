from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="test")

def is_located(name):
    print(geolocator.geocode(name))
    return geolocator.geocode(name) != None

def get_latlong_from_name(name):
    location = geolocator.geocode(name)
    if location != None: 
        return location.latitude, location.longitude
    else:
        return None