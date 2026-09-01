def add_distance_category(row):

    distance = row.get("Distance")

    if distance is None:
        row["Distance Category"] = "Unknown"

    elif distance <= 3:
        row["Distance Category"] = "Near"

    elif distance <= 7:
        row["Distance Category"] = "Medium"

    else:
        row["Distance Category"] = "Far"

    return row


def add_kpt_category(row):

    kpt = row.get("KPT duration (minutes)")

    if kpt is None:
        row["KPT Category"] = "Unknown"

    elif kpt <= 15:
        row["KPT Category"] = "Fast"

    elif kpt <= 30:
        row["KPT Category"] = "Normal"

    else:
        row["KPT Category"] = "Slow"

    return row


def transform_data(data):

    transformed_data = []

    for row in data:

        row = row.copy()

        row = add_distance_category(row)

        row = add_kpt_category(row)

        transformed_data.append(row)

    return transformed_data