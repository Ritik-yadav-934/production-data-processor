def validate_required_fields(row, fields):

    errors = []

    for field in fields:

        value = row.get(field, "").strip()

        if value == "":
            errors.append(f"{field} is missing")

    return errors


def validate_order_status(row):

    valid_statuses = {
        "Delivered",
        "Cancelled",
        "Rejected"
    }

    status = row.get("Order Status", "").strip()

    if status not in valid_statuses:

        return [f"Invalid Order Status: {status}"]

    return []


def validate_numeric_field(row, field):

    value = row.get(field, "").strip()

    if value == "":
        return [f"{field} is missing"]

    try:

        float(value)

        return []

    except ValueError:

        return [f"{field} must be numeric"]


def validate_rating(row):

    value = row.get("Rating", "").strip()

    # Rating can legitimately be missing
    if value == "":
        return []

    try:

        rating = float(value)

        if rating < 1 or rating > 5:

            return ["Rating must be between 1 and 5"]

    except ValueError:

        return ["Rating must be numeric"]

    return []


def validate_non_negative(row, field):

    value = row.get(field, "").strip()

    if value == "":
        return []

    try:

        number = float(value)

        if number < 0:

            return [f"{field} cannot be negative"]

    except ValueError:

        return [f"{field} must be numeric"]

    return []


def validate_row(row):

    errors = []

    required_fields = [
        "Order ID",
        "Restaurant ID",
        "Customer ID"
    ]

    errors.extend(
        validate_required_fields(
            row,
            required_fields
        )
    )

    errors.extend(
        validate_order_status(row)
    )

    numeric_fields = [
        "Total",
        "Distance",
        "KPT duration (minutes)",
        "Rider wait time (minutes)"
    ]

    for field in numeric_fields:

        errors.extend(
            validate_numeric_field(row, field)
        )

    errors.extend(
        validate_rating(row)
    )

    non_negative_fields = [
        "Distance",
        "KPT duration (minutes)",
        "Rider wait time (minutes)"
    ]

    for field in non_negative_fields:

        errors.extend(
            validate_non_negative(row, field)
        )

    return errors