import pytest
from rebalancer import rebalance
from rebalancer.portfolio import Portfolio, Investment


def test_rebalance_empty_portfolio_throws_value_error():
    p = Portfolio()
    with pytest.raises(ValueError):
        rebalance(p, evenly=True)


def test_rebalance_portfolio():
    p = Portfolio(
        investments=[
            Investment("a", 200, 10),
            Investment("b", 300, 5),
            Investment("c", 10, 100),
            Investment("d", 2, 40),
        ]
    )
    ports = rebalance(p, evenly=True)
    final_investments = ports["exact"].get_investments()
    assert len(final_investments) == 4
    assert final_investments[0].name == p.get_investments()[0].name
    assert final_investments[0].price == p.get_investments()[0].price
    assert final_investments[0].quantity == 114.5

    assert final_investments[1].name == p.get_investments()[1].name
    assert final_investments[1].price == p.get_investments()[1].price
    assert final_investments[1].quantity == 229

    assert final_investments[2].name == p.get_investments()[2].name
    assert final_investments[2].price == p.get_investments()[2].price
    assert final_investments[2].quantity == 11.45

    assert final_investments[3].name == p.get_investments()[3].name
    assert final_investments[3].price == p.get_investments()[3].price
    assert final_investments[3].quantity == 28.625


