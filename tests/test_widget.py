import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    'value, expected',
    [
        ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
        ('Счет 64686473678894779589', 'Счет **9589'),
        ('Union Pay 6010203040506070', 'Union Pay 6010 20** **** 6070'),
        ('Мир 2200123456789010', 'Мир 2200 12** **** 9010'),

    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum ", "номер карты не указан"),
        ("Счет ", "номер счета не указан"),
        ("", ""),
        ("1", ""),
    ],
)
def test_mask_account_card_error(value, expected):
    with pytest.raises(AssertionError) as exc_info:
        assert mask_account_card(value) == ('Не достаточно данных')


@pytest.mark.parametrize(
    "value, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-08-06", "06.08.2024")]
)
def test_get_date(value, expected):
    assert get_date(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("20/12/2023", "некорректный формат даты"),
        ("06.05.2021", "некорректный формат даты"),
        ("двадцать второе июня сорок первого года", "некорректный формат даты"),
        ("aa-bb-cc", "некорректный формат даты"),
        ("", "некорректный формат даты"),
    ],
)
def test_get_date_error(value, expected):
    with pytest.raises(AssertionError) as exc_info:
        assert get_date(value) == expected