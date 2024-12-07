import a8

def test_four_slots_find_vip():
    example1_vips  = [[ True, False,  True,  True]] 
    assert a8.find_vip_slots(example1_vips, 4) == [0, 2, 3]


def test_three_slots_count_availability():
    example1_other = [[ True,  True, False, False],
                      [False,  True,  True, False]] 
    assert a8.count_availability(example1_other, 3)  == 0


def test_four_slots_best_meeting_time():
    example1_vips  = [[ True, False,  True,  True]]
    example1_other = [[ True,  True, False, False],
                      [False,  True,  True, False]] 
    assert a8.find_best_meeting_time(example1_vips, example1_other, 4) == (0, 2)