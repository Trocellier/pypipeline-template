# scripts/03_export_results.py -------------------------------------------- #
# Author: Louis Trocellier
# Description: Step 03 - Exporting results.

from src.functions.f03_export_results import (
    export_load_processed_data,
    export_generate_summary,
    export_results
)

if __name__ == "__main__":
    # 1. Load processed data
    processed_data = export_load_processed_data()

    # 2. Generate summary statistics
    summary = export_generate_summary(processed_data)

    # 3. Export final results
    export_results(summary)