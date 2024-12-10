#!/bin/bash

# File to store the data
DATA_FILE="pods_statistics.log"

# Get the current timestamp
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
REPORT_DATE=$(date +"%Y-%m-%d")
REPORT_TIME=$(date +"%H:%M")

# Collect general report details
echo "Enter Duty SAC Name:"
read DUTY_SAC_NAME

echo "Enter Site Location:"
read SITE_LOCATION

# Start capturing data
echo "--------------------------------------------------" >> "$DATA_FILE"
echo "Data Collection Timestamp: $TIMESTAMP" >> "$DATA_FILE"
echo "Duty SAC Name: $DUTY_SAC_NAME" >> "$DATA_FILE"
echo "Site Location: $SITE_LOCATION" >> "$DATA_FILE"
echo "Report Date: $REPORT_DATE" >> "$DATA_FILE"
echo "Report Time: $REPORT_TIME" >> "$DATA_FILE"
echo "--------------------------------------------------" >> "$DATA_FILE"

# Loop through PODs
NUM_PODS=5
for POD in $(seq 1 $NUM_PODS); do
    echo "Enter details for POD $POD"

    # Collect Welfare POD Number for this POD
    echo "Enter Welfare POD Number for POD $POD:"
    read WELFARE_POD_NUMBER

    # Collect input for each field
    echo "Was the Male toilet cleaned? (Y/N):"
    read MALE_TOILET_CLEANED

    echo "Was the Female toilet cleaned? (Y/N):"
    read FEMALE_TOILET_CLEANED

    echo "Is Storage Usage required? (Y/N):"
    read STORAGE_USAGE

    echo "Enter Oil levels gauge (%):"
    read OIL_LEVELS

    echo "Enter Diesel levels gauge (%):"
    read DIESEL_LEVELS

    echo "Is Power ON or OFF?"
    read POWER_STATUS

    echo "Comments on what POD $POD is used for:"
    read POD_COMMENTS

    # Save pod-specific data to file
    echo "POD $POD Statistics:" >> "$DATA_FILE"
    echo "Welfare POD Number: $WELFARE_POD_NUMBER" >> "$DATA_FILE"
    echo "Male Toilet Cleaned: $MALE_TOILET_CLEANED" >> "$DATA_FILE"
    echo "Female Toilet Cleaned: $FEMALE_TOILET_CLEANED" >> "$DATA_FILE"
    echo "Storage Usage: $STORAGE_USAGE" >> "$DATA_FILE"
    echo "Oil Levels Gauge (%): $OIL_LEVELS" >> "$DATA_FILE"
    echo "Diesel Levels Gauge (%): $DIESEL_LEVELS" >> "$DATA_FILE"
    echo "Power Status: $POWER_STATUS" >> "$DATA_FILE"
    echo "Comments: $POD_COMMENTS" >> "$DATA_FILE"
    echo "--------------------------------------------------" >> "$DATA_FILE"

    echo "Details for POD $POD have been recorded successfully!"
done

# Final confirmation message
echo "All data has been recorded successfully!"
