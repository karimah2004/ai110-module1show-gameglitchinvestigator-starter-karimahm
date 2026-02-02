from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

#FIX HERE: Added tests for get_range_for_difficulty, parse_guess, and update_score (USING AI COPILOT)
def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
    # fallback
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_parse_guess_valid_and_decimal():
    ok, val, err = parse_guess("10")
    assert ok
    assert val == 10
    assert err is None

    ok, val, err = parse_guess("4.9")
    # current implementation casts float to int (truncates)
    assert ok
    assert val == 4


def test_parse_guess_invalid_and_empty():
    ok, val, err = parse_guess("")
    assert not ok
    assert val is None
    assert err == "Enter a guess."

    ok, val, err = parse_guess("abc")
    assert not ok
    assert val is None
    assert "not a number" in err


def test_update_score_behaviour():
    # Win scoring: first valid attempt (attempt_number=1) should award 100,
    # then decrease by 10 per additional attempt, with a floor of 10.
    assert update_score(0, "Win", 1) == 100
    assert update_score(0, "Win", 2) == 90
    # when computed points go below 10, floor applies
    assert update_score(0, "Win", 11) == 10

    # Too High: parity-based behavior in current impl.
    assert update_score(10, "Too High", 2) == 15
    assert update_score(10, "Too High", 3) == 5

    # Too Low always subtracts 5
    assert update_score(20, "Too Low", 1) == 15

    # Unknown outcome leaves score unchanged
    assert update_score(5, "Something", 1) == 5
