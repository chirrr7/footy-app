import pandas as pd

from futx.scoring import clamp_score, per90


def test_per90():
    values = pd.Series([10.0, 2.0])
    minutes = pd.Series([900.0, 180.0])
    result = per90(values, minutes)
    assert result.tolist() == [1.0, 1.0]


def test_clamp_score():
    values = pd.Series([-2.0, 50.0, 103.0])
    result = clamp_score(values)
    assert result.tolist() == [0.0, 50.0, 100.0]
