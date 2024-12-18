import pytest

@pytest.fixture
def numbers_16_int():
    return 7000792289606361


@pytest.fixture
def card_numbers_16():
    return "7000792289606361"

@pytest.fixture
def numbers_19():
    return "7000792289606361123"

@pytest.fixture
def numbers_13():
    return "7000792289606"


@pytest.fixture()
def card_numbers_15():
    return "700079228906361"


@pytest.fixture
def card_numbers_16_space():
    return "7000 7922 8960 6361"


@pytest.fixture
def card_numbers_alpha():
    return "anmdodfkgkgkasdf"


@pytest.fixture
def count_numbers_20():
    return "70007922896063611234"


@pytest.fixture
def count_numbers_20_spaсes():
    return "70007 92289 60636 11234"

@pytest.fixture
def count_numbers_alpha():
    return "sdfghtjranmdodfkgkgk"


@pytest.fixture
def list_of_dicts_base():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

@pytest.fixture
def list_of_dicts_bad_date():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
        {"id": 594226727, "state": "CANCELED", "date": "дата"},
        {"id": 615064591, "state": "CANCELED", "date": "2018"},
    ]

