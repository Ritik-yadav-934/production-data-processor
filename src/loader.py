import csv


def load_csv(file_path):
    """
    Load CSV file and return records as a list of dictionaries.
    """

    with open(file_path, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        data = list(reader)

    return data