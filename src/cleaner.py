import csv


def save_clean_data(data, file_path):

    if not data:
        return

    fieldnames = data[0].keys()

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(data)
        
def clean_text(value):

    if value is None:
        return None

    return value.strip()


def clean_number(value):

    if value is None:
        return None

    value = value.strip()

    if value == "":
        return None

    try:

        return float(value)

    except ValueError:

        return None


def clean_order(row):

    cleaned = row.copy()

    # -------------------------
    # Text Cleaning
    # -------------------------

    text_fields = [
        "Restaurant name",
        "Subzone",
        "City",
        "Order Status",
        "Delivery",
        "Instructions",
        "Review",
        "Cancellation / Rejection reason",
        "Customer complaint tag"
    ]

    for field in text_fields:

        cleaned[field] = clean_text(
            cleaned.get(field, "")
        )

    # -------------------------
    # Numeric Cleaning
    # -------------------------

    numeric_fields = [
        "Restaurant ID",
        "Distance",
        "Items in order",
        "Discount construct",
        "Bill subtotal",
        "Packaging charges",
        "Restaurant discount (Promo)",
        "Restaurant discount (Flat offs, Freebies & others)",
        "Gold discount",
        "Brand pack discount",
        "Total",
        "Rating",
        "Restaurant compensation (Cancellation)",
        "Restaurant penalty (Rejection)",
        "KPT duration (minutes)",
        "Rider wait time (minutes)",
        "Customer ID"
    ]

    for field in numeric_fields:

        cleaned[field] = clean_number(
            cleaned.get(field, "")
        )

    return cleaned