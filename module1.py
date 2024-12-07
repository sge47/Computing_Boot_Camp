def find_vip_slots(vip_participants, num_slots):    
    '''
    Finds the slots that work for all the VIPs.

    vip_participants, num_slots: Same as find_best_meeting_time

    Returns: (list of integers) A list with the slot numbers that work for all
        the VIPs
    '''
    valid_slots = []
    for slot_num in range(num_slots):
        valid = True
        for vip in vip_participants:
            if not vip[slot_num]:
                valid = False
                break
        if valid:
            valid_slots.append(slot_num)

    return valid_slots


def count_availability(availability_lists, slot_num):
    '''
    Counts the number of participants who are available at a given slot.

    availability_lists: (list of lists of booleans) The availability
        lists of the meeting participants

    slot_num: (int) A slot number

    Returns: (int) The number of participants available at slot 'num_slot'
    '''
    num_attendees = 0
    for attendees in availability_lists:
        if attendees[slot_num]:
            num_attendees += 1
    
    return num_attendees


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
    assert all([len(row) == num_slots for row in vip_participants])
    assert all([len(row) == num_slots for row in other_participants])
    
    vip_slots = find_vip_slots(vip_participants, num_slots)
    # see if meeting is possible first
    if len(vip_slots) == 0:
        return(None, 0)
    
    best_slot = None
    best_attendance = 0
    for slot_num in vip_slots:
        attendance = count_availability(vip_participants + other_participants,
                                        slot_num)
        if attendance > best_attendance:
            best_slot = slot_num
            best_attendance = attendance
            
    return best_slot, best_attendance

find_best_meeting_time(example1_vips, example1_other, 4)