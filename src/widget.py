from masks import get_mask_card_number, get_mask_account

def mask_account_card(bank_info: str) -> str:
    """Маскировка номера карты либо счета"""
    if "Счет" in bank_info:
        return get_mask_account(bank_info)
    else:
        cards = get_mask_card_number(bank_info[-16:])
        masked_cards = bank_info.replace(bank_info[-16:], bank_info)
        return masked_cards


 def get_date(date: str) -> str | None:
     """Форматирование даты в нужный вид"""
     return f"{date[8:10]}.{date[5:7]}.{date[:4]}"

 print(get_date("2024-03-11T02:26:18.671407"))