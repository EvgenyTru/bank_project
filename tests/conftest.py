import pytest


@pytest.fixture
def card_numbers_16():
    return "7000792289606361"


@pytest.fixture
def card_numbers_16_space():
    return "7000 7922 8960 6361"


@pytest.fixture
def card_numbers_alpha():
    return "anmdodfkgkgk"


@pytest.fixture
def count_numbers_20():
    return "70007922896063611234"


@pytest.fixture
def count_numbers_20_spaсes():
    return "70007 92289 60636 11234"

@pytest.fixture
def count_numbers_alpha():
    return "anmdodfkgkgk"