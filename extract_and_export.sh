#!/bin/bash

# Input and output files
LOG_FILE="pods_statistics.log"
TEMP_DATA_FILE="pods_statistics.csv"

# Remove the temporary data file if it exists
if [ -f "$TEMP_DATA_FILE" ]; then
    rm "$TEMP_DATA_FILE"
fi

# Parse the log file and convert it into CSV format
echo "Parsing log file and preparing data for export..."

{
    echo "Timestamp,Duty SAC Name,Site Location,Report Date,Report Time,POD Number,Welfare POD Number,Male Toilet Cleaned,Female Toilet Cleaned,Storage Usage,Oil Levels (%),Diesel Levels (%),Power Status,Comments"
    awk '
        BEGIN { FS=": "; OFS="," }
        /Data Collection Timestamp/ { timestamp=$2 }
        /Duty SAC Name/ { sac_name=$2 }
        /Site Location/ { site_location=$2 }
        /Report Date/ { report_date=$2 }
        /Report Time/ { report_time=$2 }
        /POD [0-9]+ Statistics/ { pod_number=substr($1, 5, 1) }
        /Welfare POD Number/ { welfare_pod=$2 }
        /Male Toilet Cleaned/ { male_cleaned=$2 }
        /Female Toilet Cleaned/ { female_cleaned=$2 }
        /Storage Usage/ { storage_usage=$2 }
        /Oil Levels Gauge/ { oil_levels=$2 }
        /Diesel Levels Gauge/ { diesel_levels=$2 }
        /Power Status/ { power_status=$2 }
        /Comments/ { comments=$2 }
        /--------------------------------------------------/ {
            if (pod_number != "") {
                print timestamp, sac_name, site_location, report_date, report_time, pod_number, welfare_pod, male_cleaned, female_cleaned, storage_usage, oil_levels, diesel_levels, power_status, comments
                pod_number=""
            }
        }
    ' "$LOG_FILE"
} > "$TEMP_DATA_FILE"

echo "Data prepared in $TEMP_DATA_FILE. Proceeding to Excel conversion..."

# Call the Python script to convert the CSV data to Excel
/usr/local/bin/pip3 generate_pod_report.py
python3 <<EOF
import pandas as pd

# Load the CSV file
csv_file = "$TEMP_DATA_FILE"
xls_file = "pods_statistics.xlsx"

# Convert CSV to Excel
df = pd.read_csv(csv_file)
df.to_excel(xls_file, index=False)

print(f"Data successfully exported to {xls_file}.")
EOF

# Clean up temporary CSV file
rm "$TEMP_DATA_FILE"
