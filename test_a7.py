import a7

def test_1():
    ledger = [("Huff", 10),
          ("Griff", 50),
          ("RC", 40),
          ("Huff", 90),
          ("Sly", -10),
          ("Griff", 100),
          ("Griff", -60),
          ("RC", 80),
          ("Griff", 50)]
    expected = ['Huff', 'Griff', 'RC']
    assert a7.champions(ledger, 100, 6) == expected, "Expected champions are 'Huff', 'Griff', 'RC'"

def test_2():
    ledger = []
    expected = []
    assert a7.champions(ledger, 100, 2) == expected, "Empty list returned empty list"