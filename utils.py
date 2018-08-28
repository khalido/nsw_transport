import pickle
from configparser import ConfigParser
import boto3
import botocore


# API URLS
# Public Transport - Realtime Vehicle Positions API
# https://opendata.transport.nsw.gov.au/node/330/exploreapi
realtime_positions_api = "https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/"

# Public Transport - Realtime Trip Updates API
# https://opendata.transport.nsw.gov.au/node/328/exploreapi
realtime_trip_updates_api = "https://api.transport.nsw.gov.au/v1/gtfs/realtime/"

def save_to_disk(object, filename):
    "takes in a object and filename and pickles to disk"
    with open(filename, 'wb') as f:
        pickle.dump(object, f)
    print(f"saved {filename} to disk")

def read_from_disk(filename):
    "takes a pickle filename and returns the unpickled object"
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    print(f"loaded {filename}")
    return data

def get_keys():
    "load keys from ../keys.secret"
    keys = ConfigParser()
    keys.read('../keys.secret')
    print(f"loaded keys for: {keys.sections()}")
    return keys

