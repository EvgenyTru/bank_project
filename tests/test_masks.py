from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number_int(card_numbers_16_int: str) -> None:
    assert get_mask_card_number(card_numbers_16_int) == '7000 79** **** 6361'


def test_get_mask_card_number_19(card_numbers_19: str) -> None:
    assert get_mask_card_number(card_numbers_19) == 'Не корректный номер'


def test_get_mask_card_number_16(card_numbers_16: str) -> None:
    assert get_mask_card_number(card_numbers_16) == '7000 79** **** 6361'


def test_get_mask_card_numbers_with_spaces(card_numbers_16_space: str) -> None:
    assert get_mask_card_number(card_numbers_16_space) == 'Не корректный номер'


def test_get_mask_card_numbers_13(card_numbers_13: str) -> None:
    assert get_mask_card_number(card_numbers_13) == 'Не корректный номер'


def test_get_mask_card_numbers_alpha(card_numbers_alpha: str) -> None:
    assert get_mask_card_number(card_numbers_alpha) == 'Не корректный номер'


def test_get_mask_account_base(count_numbers_20: str) -> None:
    assert get_mask_account(count_numbers_20) == '**1234'


def test_get_mask_account_spaces(count_numbers_20_spaсes: str) -> None:
    assert get_mask_account(count_numbers_20_spaсes) == 'Не корректный номер'


def test_get_mask_account_alpha(count_numbers_alpha: str) -> None:
    assert get_mask_account(count_numbers_alpha) == 'Не корректный номер'
