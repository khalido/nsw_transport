# nsw_transport

looking at NSW transports realtime data, inspired by https://github.com/katharosada/bus-shaming

## all the libraries

NSW Transit and it seems just about every other transit system in the world flings data around using Google's data standards.

> [GTFS-realtime](https://developers.google.com/transit/gtfs-realtime/) is a data format for communicating real-time information about public transit systems. GTFS-realtime data is encoded and decoded using [Protocol Buffers](https://developers.google.com/protocol-buffers/), a compact binary representation designed for fast and efficient processing. 

So there are two types of feeds we are looking at:

- [GTFS](https://developers.google.com/transit/gtfs/reference/) - this is a set of zipped csv files. For NSW transport the [details are here](https://opendata.transport.nsw.gov.au/node/332/exploreapi).
- [GTFS Realtime](https://developers.google.com/transit/gtfs-realtime/) - this is a protobuf which sort of looks like a json but isn't, and is parsed using the libary above.

### reading GTFS

GTFS is just a zip file, so using requests to download it and pandas to make sense of the many csv files it contains. The NSW timetable is ~100MB, download it like so. Each api has a base url, then a slug to choose b/w buses, train and so on data.

```python
headers = {'Authorization': 'apikey ' + "TOP_SECRET_KEY"}
r = requests.get(url + "buses", headers=headers, stream=True)
    
if r.status_code == 200:
    filename = "timetable_" + \
        f"{datetime.now(tz=timezone):%Y-%m-%d-%H-%M-%S-%Z}.zip"
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=256):
            fd.write(chunk)
```

### reading GTFS Realtime

First up we need the [python libray to parse Googles GTFS-realtime format](https://github.com/google/gtfs-realtime-bindings/blob/master/python/README.md) for transit data which the entire world is using to feed info to Google Maps.

Install: `pip install --upgrade gtfs-realtime-bindings`

Use like so:

```python
import requests
from google.transit import gtfs_realtime_pb2

feed = gtfs_realtime_pb2.FeedMessage()

# the auth header needed for NSW Transports api server
headers = {'Authorization': 'apikey ' + "TOP_SECERT_API_KEY"}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    feed.ParseFromString(response.content)
    return feed
```


