from flask import Flask, render_template, request, send_file
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'logFile' not in request.files or 'welfarePod' not in request.form:
        return render_template('index.html', message="Missing file or Welfare POD selection.")
    
    file = request.files['logFile']
    welfare_pod = request.form['welfarePod']  # Get selected Welfare POD Number

    if file.filename == '':
        return render_template('index.html', message="No selected file.")
    
    if file and file.filename.endswith('.log'):
        # Save the uploaded log file
        log_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(log_path)
        
        # Process the log and export to Excel
        excel_path = convert_log_to_excel(log_path, welfare_pod)
        return send_file(excel_path, as_attachment=True)
    else:
        return render_template('index.html', message="Invalid file type. Please upload a .log file.")

def convert_log_to_excel(log_file, welfare_pod):
    # Initialize variables to store extracted data
    report_details = {"Welfare POD Number": welfare_pod}  # Add Welfare POD Number directly
    pod_data = []

    # Parse the log file
    with open(log_file, 'r') as file:
        lines = file.readlines()
        current_pod = {}

        for line in lines:
            line = line.strip()

            # Extract report-level details
            if "Data Collection Timestamp" in line:
                report_details["Timestamp"] = line.split(": ", 1)[1]
            elif "Duty SAC Name" in line:
                report_details["Duty SAC Name"] = line.split(": ", 1)[1]
            elif "Site Location" in line:
                report_details["Site Location"] = line.split(": ", 1)[1]
            elif "Report Date" in line:
                report_details["Report Date"] = line.split(": ", 1)[1]
            elif "Report Time" in line:
                report_details["Report Time"] = line.split(": ", 1)[1]
            
            # Extract POD-specific details
            elif "POD" in line and "Statistics" in line:
                if current_pod:  # Save the previous POD data if any
                    pod_data.append(current_pod)
                current_pod = {"POD": line.split(" ")[1]}  # Start a new POD entry
            elif ": " in line and current_pod is not None:
                key, value = line.split(": ", 1)
                current_pod[key] = value

        if current_pod:  # Add the last POD data
            pod_data.append(current_pod)

    # Create a DataFrame for POD data
    pod_df = pd.DataFrame(pod_data)

    # Create a DataFrame for report details (single-row table)
    report_df = pd.DataFrame([report_details])

    # Define output Excel file path
    excel_file = os.path.join(OUTPUT_FOLDER, "pods_statistics.xlsx")

    # Write data to Excel
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        report_df.to_excel(writer, sheet_name="Report Details", index=False)
        pod_df.to_excel(writer, sheet_name="POD Statistics", index=False)

    return excel_file

if __name__ == '__main__':
    app.run(debug=True)
