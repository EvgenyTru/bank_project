from masks import get_mask_card_number, get_mask_account


def mask_account_card(bank_info: str) -> None:
    """Маскировка номера карты либо счета"""
    if "Счет" in bank_info:
        return "Счет" + " " + get_mask_account(bank_info[5:])
    else:
        return f"""{bank_info[:-16]} {get_mask_card_number(bank_info[-16:])}"""


def get_date(date: str) -> str | None:
    """Форматирование даты в нужный вид"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
