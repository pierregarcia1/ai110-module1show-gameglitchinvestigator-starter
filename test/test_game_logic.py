import sys
from unittest.mock import MagicMock

# app.py runs Streamlit UI calls at import time; stub the module so importing
# it doesn't require a running Streamlit server.
sys.modules.setdefault("streamlit", MagicMock())

from app import check_guess


def test_too_high_hint_says_go_lower():
    # Regression for the inverted-hint bug: a guess above the secret must
    # tell the player to go LOWER.
    outcome, hint = check_guess(50, 30)
    assert outcome == "Too High"
    assert "LOWER" in hint


def test_too_low_hint_says_go_higher():
    outcome, hint = check_guess(10, 30)
    assert outcome == "Too Low"
    assert "HIGHER" in hint


def test_exact_guess_wins():
    outcome, _ = check_guess(30, 30)
    assert outcome == "Win"


def test_numeric_comparison_not_lexicographic():
    # FIX: stopped stringifying the secret on even attempts. With a str secret,
    # "9" > "100" is True lexicographically, so a guess of 9 wrongly reported
    # "Too High". With an int secret, 9 < 100 correctly reports "Too Low".
    outcome, hint = check_guess(9, 100)
    assert outcome == "Too Low"
    assert "HIGHER" in hint
