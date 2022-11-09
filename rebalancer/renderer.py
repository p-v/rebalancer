from rebalancer.portfolio import Portfolio
from tabulate import tabulate


def render(portfolio: Portfolio):
    data = []
    for investment in portfolio.get_investments():
        data.append([investment.name, investment.quantity, investment.price])

    print(tabulate(data, headers=["Investment", "Quantity", "Price"]))
