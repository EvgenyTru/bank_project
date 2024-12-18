import pytest

from src.widget import mask_account_card, get_date

@pytest.mark.parametrize(
    'value, expected',
    [
        ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
        ('Счет 64686473678894779589', 'Счет ** 9589'),
        ('Union Pay 6010203040506070', 'Union Pay 6010 20** **** 6070'),
        ('Мир 2200123456789010', 'Мир 2200 12** **** 9010'),

    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected
