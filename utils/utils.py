from credit_card_checker import CreditCardChecker


def luhn_check(card_number: str):
    return CreditCardChecker(card_number).valid()
