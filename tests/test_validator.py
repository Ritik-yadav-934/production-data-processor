from src.validator import validate_row


def test_valid_order():

    row = {
        "Order ID": "O0001",
        "Restaurant ID": "101",
        "Customer ID": "201",
        "Order Status": "Delivered",
        "Total": "500",
        "Distance": "2.5",
        "KPT duration (minutes)": "15",
        "Rider wait time (minutes)": "5",
        "Rating": "4.5"
    }

    errors = validate_row(row)

    assert errors == []


def test_invalid_status():

    row = {
        "Order ID": "O0001",
        "Restaurant ID": "101",
        "Customer ID": "201",
        "Order Status": "Pending",
        "Total": "500",
        "Distance": "2.5",
        "KPT duration (minutes)": "15",
        "Rider wait time (minutes)": "5",
        "Rating": "4.5"
    }

    errors = validate_row(row)

    assert len(errors) > 0