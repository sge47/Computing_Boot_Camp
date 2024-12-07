# Question 2
lst1 = [10, 20, 30]
lst2 = [10, 30, 30]
def compute_matching(lst1, lst2):
    '''
    Given two lists of equal length, compute a list
    that where the ith element is True if the lists
    match at index i.

    Input: lst1, lst2 (lists)

    Returns: list of bools
    '''
    rv = []
    for i, val in enumerate(lst1):
        rv.append(val == lst2[i] and type(val) == type(lst2[i]))
    return rv

# Question 3
lst1 = [10, 20, 30]
lst2 = [10, 30, 30]

def compute_matching_indices(lst1, lst2):
    '''
    Given two lists of equal length, computed a list of
    the indices where the elements of the two lists
    are equal

    Input: lst1, lst2 (lists)

    Returns: list of ints
    '''
    return [i for i in range(len(lst1)) if lst1[i] == lst2[i]]

# Question 4
def lowest_temperature(data, date):
    '''
    Computes which city reaches the lowest temperature on a specified day.
    Input: city (str), low_temp (float)
    Returns: The name of the city with the lowest temperature for a specified day.
    '''
    DATE = 0
    CITY = 1
    LOW = 3
    
    minCity, minTemp = "", float('inf')
    for line in data:
        if line[DATE] == date and float(line[LOW]) < minTemp:
            minCity = line[CITY]
            minTemp = float(line[LOW])
    return minCity
# Example usage
data = [["20081114", "Chicago", "50.1", "30.0", "35.7"],
        ["20081114", "Detroit", "45.2", "30.3", "33.4"]]
date = "20081114"
print(lowest_temperature(data, date))  # Output: "Chicago"

def highest_temperature(data, date):
    '''
    Computes which city reaches the highest temperature on a specified day.
    Input: city (str), high_temp (float)
    Returns: The name of the city with the highest temperature for a specified day.
    '''
    DATE = 0
    CITY = 1
    HIGH = 2
    
    maxCity, maxTemp = "", float('-inf')
    for line in data:
        if line[DATE] == date and float(line[HIGH]) > maxTemp:
            maxCity = line[CITY]
            maxTemp = float(line[HIGH])
    return maxCity

# Example usage
data = [["20081114", "Chicago", "50.1", "30.0", "35.7"],
        ["20081114", "Detroit", "45.2", "30.3", "33.4"]]
date = "20081114"
print(highest_temperature(data, date))  # Output: "Chicago"

def average_temperature(data, date):
    '''
    Computes the average temperature of all cities on a specified day.
    Input: date (str)
    Returns: The average temperature (float) for the specified day.
    '''
    DATE = 0
    HIGH = 2
    LOW = 3
    
    total_temp = 0.0
    count = 0
    for line in data:
        if line[DATE] == date:
            high_temp = float(line[HIGH])
            low_temp = float(line[LOW])
            avg_temp = (high_temp + low_temp) / 2
            total_temp += avg_temp
            count += 1
    
    if count == 0:
        return None  # No data for the specified date
    
    return total_temp / count

# Example usage
data = [["20081114", "Chicago", "50.1", "30.0", "35.7"],
        ["20081114", "Detroit", "45.2", "30.3", "33.4"]]
date = "20081114"
print(average_temperature(data, date))  # Output: 38.9
