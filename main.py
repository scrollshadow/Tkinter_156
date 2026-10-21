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

        subjects = [
            "Matematika", "Bahasa Indonesia", "Bahasa Inggris", 
            "Fisika", "Kimia", "Biologi", 
            "Ekonomi", "Geografi", "Sosiologi", "Informatika"
        ]

        for i, subj in enumerate(subjects):
            row_frame = tk.Frame(input_frame, bg="#f4f6f9")
            row_frame.pack(fill=tk.X, pady=4)

            lbl = tk.Label(row_frame, text=f"{i+1}. {subj}:", font=("Arial", 10), bg="#f4f6f9", anchor="w", width=20)
            lbl.pack(side=tk.LEFT)

            var = tk.StringVar()
            self.entry_vars.append(var)

            entry = tk.Entry(row_frame, textvariable=var, font=("Arial", 10), width=15, justify="center")
            entry.pack(side=tk.RIGHT)

            btn_prediksi = tk.Button(
            main_frame, 
            text="Hasil Prediksi", 
            font=("Arial", 11, "bold"), 
            bg="#2980b9", 
            fg="white", 
            activebackground="#1abc9c", 
            activeforeground="white", 
            relief=tk.RAISED, 
            cursor="hand2", 
            command=self.hitung_prediksi
        )
        btn_prediksi.pack(fill=tk.X, pady=(5, 15), ipady=8)

        self.result_label = tk.Label(
            main_frame, 
            text="Hasil Prediksi Prodi akan muncul di sini", 
            font=("Arial", 12, "bold"), 
            bg="#eecf65", 
            fg="#2c3e50", 
            pady=12, 
            relief=tk.GROOVE
        )
        self.result_label.pack(fill=tk.X)


    def hitung_prediksi(self):
        for var in self.entry_vars:
            if not var.get().strip():
                messagebox.showwarning("Peringatan", "Mohon isi semua nilai mata pelajaran terlebih dahulu!")
            return
        prodi_hasil = "Teknologi Informasi"
    
        self.result_label.config(
            text=f"Prodi Pilihan Anda: {prodi_hasil}", 
            bg="#2ecc71", 
            fg="white"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = PrediksiProdiApp(root)
    root.mainloop()