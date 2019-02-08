from geographiclib.geodesic import Geodesic
import math

import collections

from pprint import pprint

Point = collections.namedtuple('Point', [
    'latitude',
    'longitude'
])

geod = Geodesic.WGS84  # define the WGS84 ellipsoid

def get_waypoints(p1, p2, speed=10):
    results = []
    l = geod.InverseLine(p1.latitude, p1.longitude, p2.latitude, p2.longitude)
    n = int(l.s13 / speed)
    distance_per_second = min((l.s13 / n, l.s13))
    for i in range(n + 1):
        s = min(distance_per_second * i, l.s13)
        g = l.Position(s, Geodesic.STANDARD | Geodesic.LONG_UNROLL)
        results.append(g)
    return results



point1 = Point(latitude=39.03342, longitude=-77.571044)
point2 = Point(latitude=39.040823, longitude=-77.584518)

kph = 25 # kilometers per hour
speed = kph/3.6 # meters per second

points = get_waypoints(point1, point2, speed)

pprint(points)