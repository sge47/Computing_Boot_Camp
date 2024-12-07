def count_availability(availability_lists, slot_num):
    '''
    Counts the number of participants who are available at a given slot.

    availability_lists: (list of lists of booleans) The availability
        lists of the meeting participants

    slot_num: (int) A slot number

    Returns: (int) The number of participants available at slot 'slot_num'
    '''
    count = 0

    for availability in availability_lists:
        if availability[slot_num]:
            count += 1
    return count


def find_vip_slots(vip_participants, num_slots):
    '''
    Finds the slots that work for all the VIPs.

    vip_participants, num_slots: Same as find_best_meeting_time

    Returns: (list of integers) A list with the slot numbers that work for all
        the VIPs
    '''
    vip_slots = []

    for slot in range(num_slots):
        all_available = True
        for vip in vip_participants:
            if not vip[slot]:
                all_available = False
                break
        if all_available:
            vip_slots.append(slot) 
            
    return vip_slots


def find_best_meeting_time(vip_participants, other_participants, num_slots):
    '''
    Finds the best meeting for some participants.

    vip_participants: (list of lists of booleans) The availability
       lists of the VIP participants
    other_participants: (list of lists of booleans) The availability
       lists of the non-VIP participants
    num_slots: (int) The number of slots

    Returns: ((int, int) tuple) The best meeting slot and the number of
        participants in that slot. (None, 0) if no meeting is possible.
    '''
    vip_slots = find_vip_slots(vip_participants, num_slots)
    best_slot = None
    max_participants = 0

    for slot in vip_slots:
        count = 0
        for participant in vip_participants + other_participants:
            if participant[slot]:
                count += 1
        if count > max_participants:
            best_slot = slot
            max_participants = count
    if best_slot is None:
        return (None, 0)
    return(best_slot, max_participants)
