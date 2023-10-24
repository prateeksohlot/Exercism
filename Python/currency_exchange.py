def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    money = budget/exchange_rate

    return money
    


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    change = budget - exchanging_value
    return change
    


def get_value_of_bills(exchanging_value, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - number of bills you received.
    :return: int - total value of bills you now have.
    """
    value = exchanging_value * number_of_bills
    return value
    


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    bills = budget// denomination

    return bills


def get_leftover_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    leftover = budget % denomination
    return leftover
    


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    spread_rate = ((spread/100) * exchange_rate) + exchange_rate
    money = budget/spread_rate
    value = money//denomination
    
    return value*denomination