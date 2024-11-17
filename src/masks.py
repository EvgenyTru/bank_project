def get_mask_card_number(card_number: str) -> str:
    """Заменяет звездочками часть номера карты"""
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Принимает номер счета и возвращает маску счета"""

    return f"**{account_number[-4:]}"
