
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import seaborn as sns

class TitanicEDAApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Titanic EDA Tool")
        self.data = None

        # Upload Button
        upload_btn = tk.Button(root, text="Upload CSV", command=self.upload_csv, width=20, bg="blue", fg="white")
        upload_btn.pack(pady=20)

        # Show Data Button
        show_data_btn = tk.Button(root, text="Show Data", command=self.show_data, width=20, bg="green", fg="white")
        show_data_btn.pack(pady=10)

        # EDA Button
        eda_btn = tk.Button(root, text="Perform EDA", command=self.perform_eda, width=20, bg="purple", fg="white")
        eda_btn.pack(pady=10)

    def upload_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            messagebox.showinfo("Success", "CSV loaded successfully!")
        else:
            messagebox.showwarning("Error", "No file selected!")

    def show_data(self):
        if self.data is not None:
            print(self.data.head())
            messagebox.showinfo("Data Head", "First 5 rows printed in console.")
        else:
            messagebox.showerror("Error", "No data loaded!")

    def perform_eda(self):
        if self.data is not None:
            # Show Missing Values
            print("\nMissing Values:")
            print(self.data.isnull().sum())

            # Correlation Heatmap
            correlation_matrix = self.data.corr(numeric_only=True)
            plt.figure(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
            plt.title("Correlation Heatmap")
            plt.show()
        else:
            messagebox.showerror("Error", "No data loaded!")

# Run the GUI
root = tk.Tk()
app = TitanicEDAApp(root)
root.mainloop()
