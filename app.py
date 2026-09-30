"""Open a CSV file and preview its first three data rows."""

import csv
from itertools import islice
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def main():
    window = tk.Tk()
    window.title("CSV Reader")
    window.geometry("760x440")

    ttk.Label(
        window,
        text="Choose a CSV file to preview its first three data rows.",
        padding=(12, 12),
    ).pack(anchor="w")

    file_label = ttk.Label(window, text="No file selected", padding=(12, 0, 12, 10))
    file_label.pack(anchor="w")

    table_frame = ttk.Frame(window, padding=(12, 0, 12, 12))
    table_frame.pack(fill="both", expand=True)

    table = ttk.Treeview(table_frame, show="headings", height=3)
    vertical_scrollbar = ttk.Scrollbar(
        table_frame, orient="vertical", command=table.yview
    )
    horizontal_scrollbar = ttk.Scrollbar(
        table_frame, orient="horizontal", command=table.xview
    )
    table.configure(
        yscrollcommand=vertical_scrollbar.set,
        xscrollcommand=horizontal_scrollbar.set,
    )
    table.grid(row=0, column=0, sticky="nsew")
    vertical_scrollbar.grid(row=0, column=1, sticky="ns")
    horizontal_scrollbar.grid(row=1, column=0, sticky="ew")
    table_frame.rowconfigure(0, weight=1)
    table_frame.columnconfigure(0, weight=1)

    def choose_file():
        filename = filedialog.askopenfilename(
            title="Choose a CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
        )
        if not filename:
            return

        try:
            with open(filename, "r", newline="", encoding="utf-8-sig") as csv_file:
                reader = csv.reader(csv_file)
                headers = next(reader, None)
                if headers is None:
                    raise ValueError("The selected file is empty.")
                rows = list(islice(reader, 3))
        except (OSError, UnicodeDecodeError, csv.Error, ValueError) as error:
            messagebox.showerror("CSV Reader", f"Could not read this file:\n{error}")
            return

        column_ids = [f"column_{index}" for index in range(len(headers))]
        table.configure(columns=column_ids)
        for index, (column_id, heading) in enumerate(zip(column_ids, headers)):
            table.heading(column_id, text=heading or f"Column {index + 1}")
            table.column(column_id, width=150, minwidth=80, stretch=True)

        for item in table.get_children():
            table.delete(item)
        for row in rows:
            padded_row = row[: len(headers)] + [""] * max(0, len(headers) - len(row))
            table.insert("", "end", values=padded_row)

        file_label.configure(text=filename)
        print(f"First {len(rows)} data rows from {filename}:")
        print(headers)
        for row in rows:
            print(row)

        if not rows:
            messagebox.showinfo("CSV Reader", "The CSV file has a header but no data rows.")

    ttk.Button(window, text="Choose CSV file", command=choose_file).pack(
        anchor="w", padx=12, pady=(0, 12)
    )
    window.mainloop()


if __name__ == "__main__":
    main()
