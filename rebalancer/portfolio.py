from typing import List


class Investment:
    def __init__(self, name: str, quantity: float, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price


class Portfolio:
    def __init__(self, investments: List[Investment] = []):
        self.investments = investments

    def get_investments(self) -> List[Investment]:
        return self.investments

    def add_investment(self, investment: Investment):
        self.investments.append(investment)
