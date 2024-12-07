def allocate_seats(venue_capacity,
                   venue_assignments,
                   patron_requests):
    """
    Allocate seats to patrons on a first-come, first-served basis.
    Each patron gets at most one ticket.  Patrons who are not
    allocated a ticket should be marked as wait listed.

    Inputs:
      venue_capacity: dictionary that maps venue names (strings)
        to seating capacities (ints)
      venue_assignments: dictionary that maps lecture
        titles (strings) to venue names (strings)
      patron_requests: list of tuples, where each tuple has
        a patron's name (string) and a list of lecture
        titles (strings), in order of preference.

    Returns: dictionary that maps patron names to lecture titles
      or to the string "Wait Listed".
    """
    remaining_capacity = {}
    
    for lecture, venue in venue_assignments.items():
        remaining_capacity[lecture] = venue_capacity[venue]
    
    allocations = {}

    print("Initial Venue Capacities: {}".format(remaining_capacity))

    for patron, preferences in patron_requests:
        allocated = False
        print("Processing patron: {}, Preferences: {}".format(patron, preferences))
        for lecture in preferences:
            if lecture in remaining_capacity and remaining_capacity[lecture] > 0:
                allocations[patron] = lecture
                remaining_capacity[lecture] -= 1
                allocated = True
                print("Allocated {} to {} in {}. Remaining capacity: {}".format(
                    lecture, patron, venue, remaining_capacity[lecture]))
                break
        if not allocated:
            allocations[patron] = "Wait Listed"
            print("{} is Wait Listed.".format(patron))
            
    return allocations