import tkinter as tk
from tkinter import messagebox

class PrediksiProdiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Prediksi Prodi Pilihan")
        self.root.geometry("520x680")
        self.root.config(bg="#f4f6f9")
        self.root.resizable(False, False)