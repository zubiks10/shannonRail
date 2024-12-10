import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to handle submission
def submit_data():
    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    data = {
        "Timestamp": timestamp,
        "Site Access Location": site_access_entry.get(),
        "Duty SAC Manager": sac_manager_entry.get(),
        "Pod 1 Usage": pod1_entry.get(),
        "Pod 2 Usage": pod2_entry.get(),
        "Pod 3 Usage": pod3_entry.get(),
        "Pod 4 Usage": pod4_entry.get(),
        "Pod 5 Usage": pod5_entry.get(),
        "Male Toilet Usage": male_toilet_entry.get(),
        "Female Toilet Usage": female_toilet_entry.get(),
        "Storage Usage": storage_entry.get(),
        "Oil Gauge Status (%)": oil_gauge_entry.get(),
        "Fuel Gauge Status (%)": fuel_gauge_entry.get(),
        "Power Status": power_entry.get(),
        "Comments": comments_entry.get("1.0", tk.END).strip()
    }

    # Display confirmation
    messagebox.showinfo("Data Submitted", f"Statistics Submitted Successfully!\nTimestamp: {timestamp}")
    print("Collected Data:", data)  # Replace with saving logic if needed

# Create main window
root = tk.Tk()
root.title("Daily Statistics Collection")
root.geometry("500x700")

# Site Access Location
tk.Label(root, text="Site Access Location:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
site_access_entry = tk.Entry(root, width=30)
site_access_entry.grid(row=0, column=1, pady=5)

# Duty SAC Manager
tk.Label(root, text="Duty SAC Manager:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
sac_manager_entry = tk.Entry(root, width=30)
sac_manager_entry.grid(row=1, column=1, pady=5)

# Pod Usage
tk.Label(root, text="Pod 1 Usage:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
pod1_entry = tk.Entry(root, width=30)
pod1_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Pod 2 Usage:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
pod2_entry = tk.Entry(root, width=30)
pod2_entry.grid(row=3, column=1, pady=5)

tk.Label(root, text="Pod 3 Usage:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
pod3_entry = tk.Entry(root, width=30)
pod3_entry.grid(row=4, column=1, pady=5)

tk.Label(root, text="Pod 4 Usage:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
pod4_entry = tk.Entry(root, width=30)
pod4_entry.grid(row=5, column=1, pady=5)

tk.Label(root, text="Pod 5 Usage:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
pod5_entry = tk.Entry(root, width=30)
pod5_entry.grid(row=6, column=1, pady=5)

# Toilet Usage
tk.Label(root, text="Male Toilet Usage:").grid(row=7, column=0, padx=10, pady=5, sticky="w")
male_toilet_entry = tk.Entry(root, width=30)
male_toilet_entry.grid(row=7, column=1, pady=5)

tk.Label(root, text="Female Toilet Usage:").grid(row=8, column=0, padx=10, pady=5, sticky="w")
female_toilet_entry = tk.Entry(root, width=30)
female_toilet_entry.grid(row=8, column=1, pady=5)

# Storage Usage
tk.Label(root, text="Storage Usage:").grid(row=9, column=0, padx=10, pady=5, sticky="w")
storage_entry = tk.Entry(root, width=30)
storage_entry.grid(row=9, column=1, pady=5)

# Oil and Fuel Gauge
tk.Label(root, text="Oil Gauge Status (%):").grid(row=10, column=0, padx=10, pady=5, sticky="w")
oil_gauge_entry = tk.Entry(root, width=30)
oil_gauge_entry.grid(row=10, column=1, pady=5)

tk.Label(root, text="Fuel Gauge Status (%):").grid(row=11, column=0, padx=10, pady=5, sticky="w")
fuel_gauge_entry = tk.Entry(root, width=30)
fuel_gauge_entry.grid(row=11, column=1, pady=5)

# Power Status
tk.Label(root, text="Power Status:").grid(row=12, column=0, padx=10, pady=5, sticky="w")
power_entry = tk.Entry(root, width=30)
power_entry.grid(row=12, column=1, pady=5)

# Comments
tk.Label(root, text="Comments:").grid(row=13, column=0, padx=10, pady=5, sticky="nw")
comments_entry = tk.Text(root, width=30, height=5)
comments_entry.grid(row=13, column=1, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_data, bg="blue", fg="white")
submit_button.grid(row=14, column=0, columnspan=2, pady=20)

# Start the Tkinter main loop
root.mainloop()
