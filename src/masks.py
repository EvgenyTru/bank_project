from typing import Any


def get_mask_card_number(card_number: Any) -> str:
    """Заменяет звездочками часть номера карты"""
    card_number = str(card_number)
    if len(card_number) == 16:
        for i in card_number:
            if i.isdigit():
                return f'{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    return 'Не корректный номер'


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета и возвращает маску счета"""
    if len(account_number) == 20:
        for i in account_number:
            if i.isdigit():
                return f"**{account_number[-4:]}"
    return 'Не корректный номер'
