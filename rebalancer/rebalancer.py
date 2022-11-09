from typing import List
from rebalancer.portfolio import Investment, Portfolio


def rebalance(
    portfolio: Portfolio, evenly=False, distribution: List[float] = [], additional_amt=0
):
    investment_cnt = len(portfolio.get_investments())
    if investment_cnt == 0:
        raise ValueError("Portfolio empty")
    if not evenly and investment_cnt != len(distribution):
        raise ValueError("Investments size and distribution size are not equals")

    if evenly:
        distribution = [100 / investment_cnt] * investment_cnt

    names: list[str] = []
    total_amount = additional_amt
    total_price = 0
    max_num = 0
    for investment in portfolio.get_investments():
        total_amount = total_amount + investment.price * investment.quantity
        total_price = investment.price + total_price
        max_num = max(max_num, investment.price)
        names.append(investment.name)

    amount_per_investment = [percent * 0.01 * total_amount for percent in distribution]

    quantity_per_investment = []
    for idx, amt in enumerate(amount_per_investment):
        quantity_per_investment.append(amt / portfolio.get_investments()[idx].price)
    # exact
    exact_portfolio = prepare_portfolio(portfolio, quantity_per_investment)
    # TODO round
    # TODO floor
    # TODO ceil
    return {"exact": exact_portfolio, "round": None, "floor": None, "ceil": None}


def prepare_portfolio(ref_portfolio: Portfolio, new_quantities: List[float]):
    return Portfolio(
        investments=[
            Investment(old_investment.name, new_quantities[idx], old_investment.price)
            for idx, old_investment in enumerate(ref_portfolio.get_investments())
        ]
    )
