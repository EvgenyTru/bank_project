from typing import Any


def filter_by_state(list_of_dicts: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Функция принимает список словарей и значение для ключа и возвращает новый
    список содержащий только те словари у которых ключ содержит переданное значение"""
    return [i for i in list_of_dicts if i.get("state") == state]


def sort_by_date(list_of_dicts: list[dict[str, Any]], reverse_list: bool = True) -> list[dict[str, Any]]:
    """Функция принимает список и сортирует его по убыванию"""

    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=reverse_list)

    return sorted_list
