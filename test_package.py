from a9 import module2

def test_simple():
    venues = {"Venue 1": 1,
              "Venue 2": 2}
    lectures = {"A": "Venue 1",
                "B": "Venue 2"}
    requests = [("P", ["A", "B"]),
                ("Q", ["B"]),
                ("R", ["A", "B"]),
                ("S", ["B", "A"])]
    assert module2.allocate_seats(venues, lectures, requests) == {'P': 'A',
                                                                  'Q': 'B',
                                                                  'R': 'B',
                                                                  'S': 'Wait Listed'}

def test_complicated():
    ccf_venue_capacity = {"Venue1": 3,
                          "Venue2": 2,
                          "Venue3": 1}
    test_venue_assignments = \
    {"Examining Nighthawks": "Venue1",
     "How Chicago got The Blues": "Venue1",
     "Anatomy of a Hubbard Street Dance": "Venue2",
     "The History of the Lyric Opera House": "Venue3"}
    sample_requests = \
    [("S. Seaborn", ["Examining Nighthawks",
                     "How Chicago got The Blues"]),
     ("J. Bartlet", ["How Chicago got The Blues",
                      "The History of the Lyric Opera House"]),
     ("J. Lyman", ["Examining Nighthawks",
                   "How Chicago got The Blues"]),
     ("D. Moss", ["Anatomy of a Hubbard Street Dance",
                  "How Chicago got The Blues",
          "Examining Nighthawks"]),
     ("C. Young", ["Examining Nighthawks",
                   "How Chicago got The Blues"]),
     ("T. Ziegler", ["How Chicago got The Blues",
                     "Examining Nighthawks"]),
     ("CJ. Cregg", ["Examining Nighthawks",
                    "How Chicago got The Blues"]),
     ("L. McGarry", ["Examining Nighthawks",
                     "How Chicago got The Blues"]),       
     ("A. Bartlet", ["Chicago's Skyline in Pictures",
                     "Anatomy of a Hubbard Street Dance",
             "How Chicago got The Blues"]),
     ("M. Hooper", ["Chicago's Skyline in Pictures",
                    "Anatomy of a Hubbard Street Dance"]),
     ("N. McNally", ["The History of the Lyric Opera House"])]
    assert module2.allocate_seats(ccf_venue_capacity, test_venue_assignments, sample_requests) == {'S. Seaborn': 'Examining Nighthawks',
                                                                                                   'J. Bartlet': 'How Chicago got The Blues',
                                                                                                   'J. Lyman': 'Examining Nighthawks',
                                                                                                   'D. Moss': 'Anatomy of a Hubbard Street Dance',
                                                                                                   'C. Young': 'Examining Nighthawks',
                                                                                                   'T. Ziegler': 'How Chicago got The Blues',
                                                                                                   'CJ. Cregg': 'How Chicago got The Blues',
                                                                                                   'L. McGarry': 'Wait Listed',
                                                                                                   'A. Bartlet': 'Anatomy of a Hubbard Street Dance',
                                                                                                   'M. Hooper': 'Wait Listed',
                                                                                                   'N. McNally': 'The History of the Lyric Opera House'}