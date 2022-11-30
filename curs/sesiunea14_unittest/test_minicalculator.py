from minicalculator import MiniCalculator

def test_adunare():
    mc = MiniCalculator(1, 2)
    assert mc.adunare() == 3


def test_scadere():
    mc = MiniCalculator(1, 2)
    assert mc.scadere() == -1


def test_inmultire():
    mc = MiniCalculator(1, 2)
    assert mc.inmultire() == 2


def test_impartire():
    mc = MiniCalculator(2, 3)
    epsilon = 10 ** -6
    assert abs(mc.impartire()-0.666666666666) <= epsilon
