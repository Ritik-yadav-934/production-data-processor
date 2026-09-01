from src.loader import load_csv


def test_load_csv():

    data = load_csv(
        "data/raw/orders.csv"
    )

    assert len(data) == 50
    assert len(data[0]) == 29