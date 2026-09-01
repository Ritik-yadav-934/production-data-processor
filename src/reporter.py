import json


def generate_summary_report(
    profile,
    processing_summary,
    invalid_records
):

    report = {

        "data_profile": {
            "total_records": profile["total_records"],
            "total_columns": profile["total_columns"]
        },

        "missing_values": profile["missing_values"],

        "processing_summary": processing_summary,

        "validation": {
            "invalid_records": invalid_records
        }
    }

    return report


def save_summary_report(report, file_path):

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            report,
            file,
            indent=4
        )