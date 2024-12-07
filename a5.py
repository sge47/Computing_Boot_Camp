'''
1. Complete the function `compute_matching`, which takes two lists of equal
length and returns a list of the same length where the `i`th element is True if
the `i`th elements of the two lists are equal.
'''

def compute_matching(lst1, lst2):
    '''
    Given two lists of equal length, compute a list
    that where the ith element is True if the lists
    match at index i.

    Input: lst1, lst2 (lists)

    Returns: list of bools
    '''
    matching = []
    for i in range(len(lst1)):
        matching.append(lst1[i] == lst2[i])
    return matching

compute_matching(lst1, lst2)

'''
2. Complete the function `compute_matching_indices`, which takes two lists of
equal length and returns a list of the indices where the elements of the two
lists are equal.
'''

def compute_matching_indices(lst1, lst2):
    '''
    Given two lists of equal length, computed a list of
    the indices where the elements of the two lists
    are equal

    Input: lst1, lst2 (lists)

    Returns: list of ints
    '''
    matching = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            matching.append(i)
    return(matching)

compute_matching_indices(lst1, lst2)

'''
3. Write a python function `lowest_temperature(data, date)` that takes as an
argument a list of lists (of weather data -- as in the prompt on Canvas) and
returns the name of the city with the lowest temperature for the specified date.
'''

data = [["20081114", "Chicago", "50.1", "30.0", "35.7"],
        ["20081114", "Detroit", "45.2", "30.3", "33.4"]]
date_lst = 0
city = 1
low_temp = 3
date = "20081114"

def lowest_temperature(data, date):
    '''
	Computes which city reaches the lowest temperature on a specified day
	Input: date, city, lowest temperature (float)
	Returns: The name of the city with the lowest temperature for a specified day.
	'''
	lowest = 90.0
	lowest_city = None
	for x in data:
		if x[date_lst] == date:
			if float(x[low_temp]) < lowest:
				lowest = float(x[low_temp])
				lowest_city = x[city]
	return lowest_city

lowest_temperature(data, date)

'''
4. Generalize the coin flip prompt covered in class
'''

import random

def flip_coin(prob_heads):
    '''
    Simulates flipping a coin, returning "heads" if the random number is less than the probability of heads,
    otherwise returning "tails"
    Input: prob_heads (float)
    Returns: Heads or tails (str) depending on random outcome
    '''
    flip = random.random()
    if flip < prob_heads:
        return "heads"
    else: 
        return "tails"
    
def simulate_consecutive_heads(target, prob_heads):
    '''
    Simulates flipping a coin until a target number of consecutive heads is reached
    Input: target (int) and prob_heads (float)
    Returns: The total number of flips it took to reach the target number of consecutive heads (int)
    '''
    consecutive_heads = 0
    total_flips = 0
    while consecutive_heads < target:
        result = flip_coin(prob_heads)
        if result == "heads":
            consecutive_heads += 1
        else:
            consecutive_heads = 0
        total_flips += 1
    return total_flips

def run_simulation(target, prob_heads, num_trials):
    '''
	Runs the simulation for a specified number of trials and calculates the average number of flips required
    Input: target (int), prob_heads (float), and num_trials (int) 
    Returns: The average number of flips required to reach the target number of consecutive heads across all trials (float)
	'''
    total_flips_across_trials = 0
    for _ in range(num_trials):
        total_flips_across_trials += simulate_consecutive_heads(target, prob_heads)
    average_flips = total_flips_across_trials / num_trials
    return average_flips

def main():
    ''' 
    Main function that collects user input to run the simulation
    Input: User input
    Returns: The simulation runs
    '''
    
    random_seed = int(input("Enter the random seed: "))
    target = int(input("Enter the target number of consecutive heads: "))
    num_trials = int(input("Enter the number of trials to simulate: "))
    prob_heads = float(input("Enter the probability (between 0 and 1) of flipping heads: "))
    
    random.seed(random_seed)
    
    average_flips = run_simulation(target, prob_heads, num_trials)
    print(f"The average number of flips required to reach {target} consecutive heads over {num_trials} trials is: {average_flips}")
    
if __name__ == "__main__":
    main()
