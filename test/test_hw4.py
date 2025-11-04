# Test for hw4.py
import pytest
from best_library.hw4 import count_simba, get_day_month_year, compute_distance, sum_general_int_list
import pandas as pd
import datetime

# Tests for exericise 1
def test_count_simba():
    strings = [
        "Simba and Nala are lions.",
        "I laugh in the face of danger.",
        "Hakuna matata",
        "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    ]
    assert count_simba(strings) == 3
    assert count_simba(["No lions here."]) == 0
    assert count_simba(["simba simba SIMBA"]) == 3

# Tests for exercise 2
def test_get_day_month_year():
    dates = [datetime.date(2020, 5, 17), datetime.date(1995, 12, 25)]
    df = get_day_month_year(dates)
    expected_df = pd.DataFrame({
        'day': [17, 25],
        'month': [5, 12],
        'year': [2020, 1995]
    })
    assert df.equals(expected_df)

# Tests for exercise 3
def test_compute_distance():
    coords = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
    distances = compute_distance(coords)
    assert len(distances) == 2
    assert all(isinstance(d, float) for d in distances)
    assert distances[0] == pytest.approx(31.4, rel=1e-1)


# Tests for exercise 4
def test_sum_general_int_list():
    assert sum_general_int_list([[2], 3, [[1,2],5]]) == 13
    assert sum_general_int_list([1, [2, [3, 4]], 5]) == 15
    assert sum_general_int_list([[[[10]]], 20, [30]]) == 60
    assert sum_general_int_list([]) == 0


def test_sum_general_int_list_invalid_type():
    with pytest.raises(ValueError):
        sum_general_int_list([1, "Simba"])    