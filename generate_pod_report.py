import sys
import pandas 
from openpyxl import Workbook
from openpyxl.drawing.image import Image
from openpyxl.utils.dataframe import dataframe_to_rows

# Get arguments from the shell script
data_file = sys.argv[1]
output_excel = sys.argv[2]
logo_path = sys.argv[3]

# Read data from the temporary file
site_info = {}
pod_data = []

with open(data_file, "r") as file:
    for line in file:
        parts = line.strip().split("|")
        if parts[0].startswith("Pod"):
            pod_data.append(parts)
        else:
            site_info[parts[0]] = parts[1]

# Create a DataFrame for pod data
columns = [
    "Pod Name",
    "Male Cleaned (Y/N)",
    "Female Cleaned (Y/N)",
    "Storage Usage (Y/N)",
    "Oil Levels (%)",
    "Diesel Levels (%)",
    "Power ON/OFF",
    "Comments"
]
pod_df = pd.DataFrame(pod_data, columns=columns)

# Create Excel workbook
wb = Workbook()
ws = wb.active
ws.title = "Shannon Onsite Update"

# Add site information
ws.append(["Site Information"])
ws.append(["Timestamp", site_info["Timestamp"]])
ws.append(["Site Access Location", site_info["Site Access Location"]])
ws.append(["Duty SAC Manager", site_info["Duty SAC Manager"]])
ws.append([])

# Add pod data to Excel
ws.append(["Pod Data"])
for row in dataframe_to_rows(pod_df, index=False, header=True):
    ws.append(row)

# Add logo to the top-left corner
img = Image(logo_path)
img.width = 150  # Adjust size as needed
img.height = 150
ws.add_image(img, "A1")

# Save the Excel file
wb.save(output_excel)
