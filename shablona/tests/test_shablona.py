import pytest
import numpy as np

import shablona

def test_midi_to_hz_float():
    expected = 440.0
    assert shablona.midi_to_hz(69) == expected

def test_midi_to_hz_array():
    expected = [261.6255653, 329.62755691, 440.0]
    assert np.allclose(shablona.midi_to_hz([60, 64, 69]),  expected)

def test_hz_to_midi_float():
    expected = 69
    assert shablona.hz_to_midi(440.0) == expected

def test_hz_to_midi_array():
    expected = [57, 69, 81]
    assert np.allclose(shablona.hz_to_midi([220.0, 440.0, 880.0]), expected)

# Hello!  You could add the missing test here, in Part 5!


def test_hz_to_period_float():
    expected = 0.1
    assert shablona.hz_to_period(10) == expected

def test_hz_to_period_array():
    expected = [0.1, 0.01, 0.001]
    assert np.allclose(shablona.hz_to_period([10, 100, 1000]), expected)

def test_hz_to_period_throws_if_zero_or_less():
    with pytest.raises(ValueError):
        shablona.hz_to_period(0)
