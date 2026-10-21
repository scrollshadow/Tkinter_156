import tkinter as tk
from tkinter import messagebox

class PrediksiProdiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Prediksi Prodi Pilihan")
        self.root.geometry("520x680")
        self.root.config(bg="#f4f6f9")
        self.root.resizable(False, False)

        self.entry_vars = []

        self.create_widgets()

    def create_widgets(self):
        main_frame = tk.Frame(self.root, bg="#f4f6f9", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(
            main_frame, 
            text="Aplikasi Prediksi Prodi Pilihan", 
            font=("Arial", 16, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50"
        )
        title_label.pack(pady=(0, 15))

        input_frame = tk.LabelFrame(
            main_frame, 
            text=" Input Nilai 10 Mata Pelajaran ", 
            font=("Arial", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#34495e", 
            padx=15, 
            pady=10
        )
        input_frame.pack(fill=tk.X, pady=(0, 15))