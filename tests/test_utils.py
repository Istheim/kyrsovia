import pytest
from utils import reading_file, get_filtered_date, get_last_values, get_formatted_date


def test_get_data():
    data = reading_file()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert get_formatted_date(test_data[:2]) == [{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]
    assert get_filtered_date(test_data[:2], fiter_empty_from=True) == []


def teat_get_last_values(test_data):
    data = get_last_values(test_data, 3)
    assert [x["date"] for x in data] == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364", "2019-04-04T23:20:05.206878"]

