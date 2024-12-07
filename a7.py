def champions(ledger, threshold, num_champs):
	'''
    Computes the first num_champs houses to reach a score
    of at least threshold.

    Inputs:
        ledger: a list of scoring events, where each scoring
            event is a (string, integer) pair consisting of
            the name of the house and the number of points
            that is added to that house's score (which may
            be negative).
        threshold: (positive integer) a house has completed
            the house cup when they meet or exceed this score.
        num_champs: (positive integer) The maximum number
            of houses to include in the list of champions

    Returns: (list of strings) A list of the first num_champs
        houses to complete the house cup, in order.
    '''
	scores = {}
	champions = []
	house_cup = {}

	for house, points in ledger:
		scores[house] = scores.get(house, 0) + points

		if scores[house] >= threshold and house not in house_cup:
			champions.append(house)
			house_cup[house] = True
			
		if len(champions) == num_champs:
			break

	return champions

if __name__ == "__main__":
	ledger = [("Huff", 10),
          ("Griff", 50),
          ("RC", 40),
          ("Huff", 90),
          ("Sly", -10),
          ("Griff", 100),
          ("Griff", -60),
          ("RC", 80),
          ("Griff", 50)]
	threshold = 100
	num_champs = 6
	
	print(champions(ledger, threshold, num_champs))