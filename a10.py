import math
import csv
from operator import itemgetter

class Location:
    """
    Represents a geographic location
    """

    def __init__(self, latitude, longitude):
        """
        Constructor
        Input: latitude, longitude: (float) The coordinates
            for this location.
        """
        self.latitude = latitude
        self.longitude = longitude


    def to_string(self):
        """
        Produces a string representation of the location.
        Input: None
        Returns: String representation of the location
        """
        if self.latitude < 0.0:
            lat = "S"
        else:
            lat = "N"

        if self.longitude < 0.0:
            lon = "W"
        else:
            lon = "E"

        return "({} {}, {} {})".format(abs(self.latitude),
                                       lat,
                                       abs(self.longitude),
                                       lon)


    def distance_to(self, other):
        """
        Computes the distance (m) to another location using the
        Haversine Formula
        Input: other: (Location object) Another location
        Returns: (float) the distance (m) to the other location
        """
        diffLatitude = math.radians(other.latitude - self.latitude)
        diffLongitude = math.radians(other.longitude - self.longitude)

        a = (math.sin(diffLatitude / 2))**2 \
            + math.cos(math.radians(self.latitude)) \
            * math.cos(math.radians(other.latitude)) \
            * (math.sin(diffLongitude / 2))**2
        d = 2 * math.asin(math.sqrt(a))

        return 6371000.0 * d


def read_csv(file='gps.csv'):
    data = []
    with open(file) as f:
         reader = csv.reader(f, delimiter='|')
         for row in reader:
             building_code, latitude, longitude = tuple(row)
             data.append((building_code, Location(float(latitude), float(longitude))))
    return data


def top_10_closest(file='gps.csv'):
    ''' 
    Finds the top 10 closest buildings to the MACSS building (building code "1155")
    Inputs: 
    file (str) is the path to the csv file containing building data
    buildings as tuples of building_code and location, 
    list of distances of buildings to MACSS
    Returns: 
    list of tuples: top 10 closest buildings to MACSS,
    each tuple containing a building code (str) and its distance (float) from the MACSS building,
    sorted by distance
    '''
    buildings = read_csv(file)
    macss_location = Location(41.7856443, -87.5970978)

    distances = []
    for building_code, location in buildings:
        if building_code != "1155":
            distance = macss_location.distance_to(location)
            distances.append((building_code, distance))
    
    sorted_distances = sorted(distances, key=itemgetter(1))

    top_10 = sorted_distances[:10]

    return top_10


def within_distance(max_distance, file='gps.csv'):
    ''' 
    Finds the number of building codes that are less than a user-defined number of meters away 
    from the MACSS building.
    Input:
    max_distance (float) is the maximum distance in meters that a user will set
    file (str) is the path to the csv file
    Returns:
    (int) The number of buildings within the specified distance
    '''
    buildings = read_csv(file)
    macss_location = Location(41.7856443, -87.5970978)

    count = 0
    for building_code, location in buildings:
            if building_code != "1155":
                 distance = macss_location.distance_to(location)
            if distance < max_distance:
                count += 1
    
    return count


class Student:
    def __init__(self, name, ss, cs, stat, ws, gpa, thesis):
        """
        Constructor to initialize a student's attributes
        Parameters:
        name (str): The student's name
        ss (int): Students need to complete at least four Social Science electives
        cs (int): Students need to complete at least four Computer Science courses
        stat (int): Students are allowed to substitute Computer Science courses with Statistics courses
        ws (int): Students need to complete two workshop classes
        gpa (float): GPA must be above 3.0 to graduate from the program under normal conditions
        thesis (bool): Thesis completion status if GPA is 3.0 or lower
        """
        self.name = name
        self.ss = ss
        self.cs = cs
        self.stat = stat
        self.ws = ws
        self.gpa = gpa
        self.thesis = thesis


    def graduation_eligible(self):
        ''' 
        Computes whether a student is eligible to graduate based on their attributes
        Returns:
        True if the student is eligible to graduate, False otherwise (bool)
        '''
        return ((self.cs + self.stat) >= 4
                and self.ss >= 4
                and self.ws == 2
                and (self.gpa > 3.0 or self.thesis))