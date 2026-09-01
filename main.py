from pathlib import Path

from src.loader import load_csv
from src.profiler import get_data_profile
from src.validator import validate_row
from src.cleaner import clean_order
from src.processor import process_orders
from src.transformer import transform_data
from src.reporter import (
    generate_summary_report,
    save_summary_report
)
from src.logger import setup_logger
from src.cleaner import (
    clean_order,
    save_clean_data
)
from src.config import (INPUT_FILE, CLEAN_OUTPUT, SUMMARY_OUTPUT,PROCESSED_DATA_DIR)


# --------------------------------------------------
# Configuration
# --------------------------------------------------

# INPUT_FILE = "data/raw/orders.csv"

# OUTPUT_DIR = Path("data/processed")

# CLEAN_OUTPUT = OUTPUT_DIR / "clean_orders.csv"

# SUMMARY_OUTPUT = OUTPUT_DIR / "summary_report.json"


# --------------------------------------------------
# Create Output Directory
# --------------------------------------------------

# OUTPUT_DIR.mkdir(
#     parents=True,
#     exist_ok=True
# )

PROCESSED_DATA_DIR.mkdir(parents=True,exist_ok=True)


# --------------------------------------------------
# Logger
# --------------------------------------------------

logger = setup_logger()


# --------------------------------------------------
# Main Pipeline
# --------------------------------------------------

def main():

    logger.info("Application started")

    # ----------------------------------------------
    # 1. Load Data
    # ----------------------------------------------

    logger.info("Loading CSV data")

    data = load_csv(INPUT_FILE)

    logger.info(
        f"{len(data)} records loaded"
    )

    # ----------------------------------------------
    # 2. Data Profiling
    # ----------------------------------------------

    logger.info("Starting data profiling")

    profile = get_data_profile(data)

    print(
        "Total Records:",
        profile["total_records"]
    )

    print(
        "Total Columns:",
        profile["total_columns"]
    )

    # ----------------------------------------------
    # 3. Validation
    # ----------------------------------------------

    logger.info("Starting validation")

    valid_data = []
    invalid_records = []

    for row in data:

        errors = validate_row(row)

        if errors:

            invalid_records.append({
                "Order ID": row.get("Order ID"),
                "errors": errors
            })

        else:

            valid_data.append(row)

    logger.info(
        f"Valid records: {len(valid_data)}"
    )

    logger.info(
        f"Invalid records: {len(invalid_records)}"
    )

    print(
        "Invalid Records:",
        len(invalid_records)
    )

    # ----------------------------------------------
    # 4. Cleaning
    # ----------------------------------------------

    logger.info("Starting data cleaning")

    cleaned_data = []

    for row in valid_data:

        cleaned_row = clean_order(row)

        cleaned_data.append(cleaned_row)

    logger.info("Data cleaning completed")

    # ----------------------------------------------
    # 5. Transformation
    # ----------------------------------------------

    logger.info("Starting data transformation")

    transformed_data = transform_data(
        cleaned_data
    )

    logger.info("Data transformation completed")

    save_clean_data(
    transformed_data,
    CLEAN_OUTPUT
    )

    logger.info("Clean data saved")
    # ----------------------------------------------
    # 6. Processing
    # ----------------------------------------------

    logger.info("Starting data processing")

    processing_summary = process_orders(
        transformed_data
    )

    logger.info("Data processing completed")

    # ----------------------------------------------
    # 7. Summary Report
    # ----------------------------------------------

    logger.info("Generating summary report")

    report = generate_summary_report(
        profile,
        processing_summary,
        len(invalid_records)
    )

    # ----------------------------------------------
    # 8. Save Summary
    # ----------------------------------------------

    save_summary_report(
        report,
        SUMMARY_OUTPUT
    )

    logger.info(
        "Summary report saved"
    )

    # ----------------------------------------------
    # 9. Print Summary
    # ----------------------------------------------

    print("\n========== SUMMARY ==========")

    print(
        "Total Orders:",
        processing_summary["total_orders"]
    )

    print(
        "Delivered:",
        processing_summary["delivered_orders"]
    )

    print(
        "Cancelled:",
        processing_summary["cancelled_orders"]
    )

    print(
        "Rejected:",
        processing_summary["rejected_orders"]
    )

    print(
        "Total Revenue:",
        processing_summary["total_revenue"]
    )

    print(
        "Average Order Value:",
        processing_summary["average_order_value"]
    )

    print(
        "Average Distance:",
        processing_summary["average_distance"]
    )

    print(
        "Average KPT:",
        processing_summary["average_kpt"]
    )

    print(
        "Average Rating:",
        processing_summary["average_rating"]
    )

    logger.info("Application completed")


if __name__ == "__main__":
    main()