import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_numbers_16):
    assert get_mask_card_number(card_numbers_16) == "7000 79** **** 6361"


def test_get_mask_card_numbers_with_spaces(card_numbers_16_space):
    with pytest.raises(AssertionError) as exc_info:
        assert str(exc_info.value) == "Не верный формат"


def test_get_mask_card_numbers_alpha(card_numbers_alpha):
    with pytest.raises(AssertionError) as exc_info:
        assert str(exc_info.value) == "Не верный формат"


def test_get_mask_account_base(count_numbers_20):
    assert get_mask_account(count_numbers_20) == "**1234"


def test_get_mask_account_spaces(count_numbers_20_spaсes):
    assert get_mask_account(count_numbers_20_spaсes) == "**1234"


def test_get_mask_account_alpha(count_numbers_alpha):
    with pytest.raises(AssertionError) as exc_info:
        assert str(exc_info.value) == "Не верный формат"