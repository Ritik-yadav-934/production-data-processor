def get_data_profile(data):
    """
    Generate basic information about the dataset.
    """

    if not data:
        return {
            "total_records": 0,
            "total_columns": 0,
            "columns": [],
            "missing_values": {},
            "unique_values": {}
        }

    columns = list(data[0].keys())

    missing_values = {}

    for column in columns:

        count = 0

        for row in data:

            value = row.get(column, "")

            if value.strip() == "":
                count += 1

        missing_values[column] = count

    unique_values = {}

    for column in columns:

        values = set()

        for row in data:

            values.add(row.get(column, ""))

        unique_values[column] = values

    return {
        "total_records": len(data),
        "total_columns": len(columns),
        "columns": columns,
        "missing_values": missing_values,
        "unique_values": unique_values
    }