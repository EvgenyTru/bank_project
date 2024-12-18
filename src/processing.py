from typing import Any
from datetime import datetime


def filter_by_state(list_of_dicts: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Функция принимает список словарей и значение для ключа и возвращает новый
    список содержащий только те словари у которых ключ содержит переданное значение"""
    return [i for i in list_of_dicts if i.get("state") == state]


def sort_by_date(dict_list: list, sort_by_date_descending: bool = True) -> list:
    """Принимает список словарей. Возвращает новый список, отсортированный по дате от новых к старым. Если надо
    изменить порядок сортировки, то при вызове функции вторым параметром передай False"""
    sorted_list = sorted(
        dict_list, key=lambda strindate: datetime.fromisoformat(strindate["date"]), reverse=sort_by_date_descending
    )
    return sorted_list
