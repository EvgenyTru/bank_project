import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_default(test_transactions):
    generator = filter_by_currency(test_transactions)
    assert next(generator) == test_transactions[0]
    assert next(generator) == test_transactions[1]
    assert next(generator) == test_transactions[3]


def test_filter_by_currency_manual_currency(test_transactions):
    generator = filter_by_currency(test_transactions, "RUB")
    assert next(generator) == test_transactions[2]
    assert next(generator) == test_transactions[4]


def test_filter_by_currency_not_currency(test_transactions):
    generator = filter_by_currency(test_transactions, "EUR")
    with pytest.raises(StopIteration):
        next(generator)


def test_filter_by_currency_not_list():
    generator = filter_by_currency([])
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(test_transactions):
    generator = transaction_descriptions(test_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions():
    generator = filter_by_currency([])
    with pytest.raises(StopIteration):
        next(generator)


@pytest.mark.parametrize("x, y, expected", [(1, 5, ["0000 0000 0000 0001", "0000 0000 0000 0002",
                                                    "0000 0000 0000 0003", "0000 0000 0000 0004",
                                                    "0000 0000 0000 0005"])])
def test_card_number_generator(x, y, expected) -> None:
    """Тест генератора номеров карт"""
    list_card_number_generator = list(card_number_generator(start=x, finish=y))
    assert list_card_number_generator == expected
