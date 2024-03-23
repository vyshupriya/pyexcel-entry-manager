import tkinter as tk
from openpyxl import Workbook
from datetime import datetime


def save_to_excel():
    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Write headers
    headers = [ 'Name', 'Age', 'Email' ]
    ws.append(headers)

    # Get data from entry fields
    data = [ name_entry.get(), age_entry.get(), email_entry.get() ]

    # Append data to worksheet
    ws.append(data)

    # Save the workbook with current timestamp as filename
    filename = f"data_entry_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    wb.save(filename)

    # Display success message
    status_label.config(text=f"Data saved to {filename}")


# Create main window
root = tk.Tk()
root.title("Data Entry")

# Create entry fields
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# Create Save button
save_button = tk.Button(root, text="Save", command=save_to_excel)
save_button.grid(row=3, column=0, columnspan=2)

# Display status
status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=2)

root.mainloop()