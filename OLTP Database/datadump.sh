#!/bin/bash

# Database credentials
DB_HOST="127.0.0.1"
DB_PORT="3306"
DB_USER="root"
DB_PASSWORD="MzIwMTMtdGhpc2lz"
DB_NAME="sales"  
TABLE_NAME="sales_data"

# Output file
OUTPUT_FILE="sales_data.sql"

# mysqldump command to export data
mysqldump --host="$DB_HOST" --port="$DB_PORT" --user="$DB_USER" --password="$DB_PASSWORD" "$DB_NAME" "$TABLE_NAME" > "$OUTPUT_FILE"

# Check if the mysqldump command was successful
if [ $? -eq 0 ]; then
  echo "Data exported successfully to $OUTPUT_FILE"
else
  echo "Error exporting data. Please check your credentials and database connection."
fi

