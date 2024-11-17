import tkinter as tk
from tkinter import messagebox

# Struktur data tabel periodik
periodic_table = [
    {"name": "Hidrogen", "symbol": "H", "atomic_number": 1, "electron_config": "1s1", "atomic_radius": "53 pm"},
    {"name": "Helium", "symbol": "He", "atomic_number": 2, "electron_config": "1s2", "atomic_radius": "31 pm"},
    {"name": "Lithium", "symbol": "Li", "atomic_number": 3, "electron_config": "[He] 2s1", "atomic_radius": "167 pm"},
    {"name": "Beryllium", "symbol": "Be", "atomic_number": 4, "electron_config": "[He] 2s2", "atomic_radius": "112 pm"},
    {"name": "Boron", "symbol": "B", "atomic_number": 5, "electron_config": "[He] 2s2 2p1", "atomic_radius": "87 pm"},
    {"name": "Carbon", "symbol": "C", "atomic_number": 6, "electron_config": "[He] 2s2 2p2", "atomic_radius": "67 pm"},
    {"name": "Nitrogen", "symbol": "N", "atomic_number": 7, "electron_config": "[He] 2s2 2p3", "atomic_radius": "56 pm"},
    {"name": "Oxygen", "symbol": "O", "atomic_number": 8, "electron_config": "[He] 2s2 2p4", "atomic_radius": "48 pm"},
    {"name": "Fluorine", "symbol": "F", "atomic_number": 9, "electron_config": "[He] 2s2 2p5", "atomic_radius": "42 pm"},
    {"name": "Neon", "symbol": "Ne", "atomic_number": 10, "electron_config": "[He] 2s2 2p6", "atomic_radius": "38 pm"},
    {"name": "Sodium", "symbol": "Na", "atomic_number": 11, "electron_config": "[Ne] 3s1", "atomic_radius": "186 pm"},
    {"name": "Magnesium", "symbol": "Mg", "atomic_number": 12, "electron_config": "[Ne] 3s2", "atomic_radius": "160 pm"},
    {"name": "Aluminum", "symbol": "Al", "atomic_number": 13, "electron_config": "[Ne] 3s2 3p1", "atomic_radius": "143 pm"},
    {"name": "Silicon", "symbol": "Si", "atomic_number": 14, "electron_config": "[Ne] 3s2 3p2", "atomic_radius": "118 pm"},
    {"name": "Phosphorus", "symbol": "P", "atomic_number": 15, "electron_config": "[Ne] 3s2 3p3", "atomic_radius": "110 pm"},
    {"name": "Sulfur", "symbol": "S", "atomic_number": 16, "electron_config": "[Ne] 3s2 3p4", "atomic_radius": "104 pm"},
    {"name": "Chlorine", "symbol": "Cl", "atomic_number": 17, "electron_config": "[Ne] 3s2 3p5", "atomic_radius": "99 pm"},
    {"name": "Argon", "symbol": "Ar", "atomic_number": 18, "electron_config": "[Ne] 3s2 3p6", "atomic_radius": "71 pm"},
    {"name": "Potassium", "symbol": "K", "atomic_number": 19, "electron_config": "[Ar] 4s1", "atomic_radius": "303 pm"},
    {"name": "Calcium", "symbol": "Ca", "atomic_number": 20, "electron_config": "[Ar] 4s2", "atomic_radius": "231 pm"},
    {"name": "Scandium", "symbol": "Sc", "atomic_number": 21, "electron_config": "[Ar] 3d1 4s2", "atomic_radius": "160 pm"},
    {"name": "Titanium", "symbol": "Ti", "atomic_number": 22, "electron_config": "[Ar] 3d2 4s2", "atomic_radius": "147 pm"},
    {"name": "Vanadium", "symbol": "V", "atomic_number": 23, "electron_config": "[Ar] 3d3 4s2", "atomic_radius": "135 pm"},
    {"name": "Chromium", "symbol": "Cr", "atomic_number": 24, "electron_config": "[Ar] 3d5 4s1", "atomic_radius": "129 pm"},
    {"name": "Manganese", "symbol": "Mn", "atomic_number": 25, "electron_config": "[Ar] 3d5 4s2", "atomic_radius": "127 pm"},
    {"name": "Iron", "symbol": "Fe", "atomic_number": 26, "electron_config": "[Ar] 3d6 4s2", "atomic_radius": "126 pm"},
    {"name": "Cobalt", "symbol": "Co", "atomic_number": 27, "electron_config": "[Ar] 3d7 4s2", "atomic_radius": "125 pm"},
    {"name": "Nickel", "symbol": "Ni", "atomic_number": 28, "electron_config": "[Ar] 3d8 4s2", "atomic_radius": "124 pm"},
    {"name": "Copper", "symbol": "Cu", "atomic_number": 29, "electron_config": "[Ar] 3d10 4s1", "atomic_radius": "128 pm"},
    {"name": "Zinc", "symbol": "Zn", "atomic_number": 30, "electron_config": "[Ar] 3d10 4s2", "atomic_radius": "133 pm"},
    {"name": "Gallium", "symbol": "Ga", "atomic_number": 31, "electron_config": "[Ar] 3d10 4s2 4p1", "atomic_radius": "135 pm"},
    {"name": "Germanium", "symbol": "Ge", "atomic_number": 32, "electron_config": "[Ar] 3d10 4s2 4p2", "atomic_radius": "122 pm"},
    {"name": "Arsenic", "symbol": "As", "atomic_number": 33, "electron_config": "[Ar] 3d10 4s2 4p3", "atomic_radius": "119 pm"},
    {"name": "Selenium", "symbol": "Se", "atomic_number": 34, "electron_config": "[Ar] 3d10 4s2 4p4", "atomic_radius": "116 pm"},
    {"name": "Bromine", "symbol": "Br", "atomic_number": 35, "electron_config": "[Ar] 3d10 4s2 4p5", "atomic_radius": "114 pm"},
    {"name": "Krypton", "symbol": "Kr", "atomic_number": 36, "electron_config": "[Ar] 3d10 4s2 4p6", "atomic_radius": "112 pm"},
    {"name": "Rubidium", "symbol": "Rb", "atomic_number": 37, "electron_config": "[Kr] 5s1", "atomic_radius": "303 pm"},
    {"name": "Strontium", "symbol": "Sr", "atomic_number": 38, "electron_config": "[Kr] 5s2", "atomic_radius": "249 pm"},
    {"name": "Yttrium", "symbol": "Y", "atomic_number": 39, "electron_config": "[Kr] 4d1 5s2", "atomic_radius": "211 pm"},
    {"name": "Zirconium", "symbol": "Zr", "atomic_number": 40, "electron_config": "[Kr] 4d2 5s2", "atomic_radius": "180 pm"},
    {"name": "Niobium", "symbol": "Nb", "atomic_number": 41, "electron_config": "[Kr] 4d4 5s1", "atomic_radius": "147 pm"},
    {"name": "Molybdenum", "symbol": "Mo", "atomic_number": 42, "electron_config": "[Kr] 4d5 5s1", "atomic_radius": "139 pm"},
    {"name": "Technetium", "symbol": "Tc", "atomic_number": 43, "electron_config": "[Kr] 4d5 5s2", "atomic_radius": "137 pm"},
    {"name": "Ruthenium", "symbol": "Ru", "atomic_number": 44, "electron_config": "[Kr] 4d7 5s1", "atomic_radius": "138 pm"},
    {"name": "Rhodium", "symbol": "Rh", "atomic_number": 45, "electron_config": "[Kr] 4d8 5s1", "atomic_radius": "135 pm"},
    {"name": "Palladium", "symbol": "Pd", "atomic_number": 46, "electron_config": "[Kr] 4d10", "atomic_radius": "137 pm"},
    {"name": "Silver", "symbol": "Ag", "atomic_number": 47, "electron_config": "[Kr] 4d10 5s1", "atomic_radius": "144 pm"},
    {"name": "Cadmium", "symbol": "Cd", "atomic_number": 48, "electron_config": "[Kr] 4d10 5s2", "atomic_radius": "151 pm"},
    {"name": "Indium", "symbol": "In", "atomic_number": 49, "electron_config": "[Kr] 4d10 5s2 5p1", "atomic_radius": "162 pm"},
    {"name": "Tin", "symbol": "Sn", "atomic_number": 50, "electron_config": "[Kr] 4d10 5s2 5p2", "atomic_radius": "167 pm"},
    {"name": "Antimony", "symbol": "Sb", "atomic_number": 51, "electron_config": "[Kr] 4d10 5s2 5p3", "atomic_radius": "158 pm"},
    {"name": "Tellurium", "symbol": "Te", "atomic_number": 52, "electron_config": "[Kr] 4d10 5s2 5p4", "atomic_radius": "145 pm"},
    {"name": "Iodine", "symbol": "I", "atomic_number": 53, "electron_config": "[Kr] 4d10 5s2 5p5", "atomic_radius": "133 pm"},
    {"name": "Xenon", "symbol": "Xe", "atomic_number": 54, "electron_config": "[Kr] 4d10 5s2 5p6", "atomic_radius": "108 pm"},
    {"name": "Cesium", "symbol": "Cs", "atomic_number": 55, "electron_config": "[Xe] 6s1", "atomic_radius": "265 pm"},
    {"name": "Barium", "symbol": "Ba", "atomic_number": 56, "electron_config": "[Xe] 6s2", "atomic_radius": "253 pm"},
    {"name": "Lanthanum", "symbol": "La", "atomic_number": 57, "electron_config": "[Xe] 5d1 6s2", "atomic_radius": "195 pm"},
    {"name": "Cerium", "symbol": "Ce", "atomic_number": 58, "electron_config": "[Xe] 4f1 5d1 6s2", "atomic_radius": "182 pm"},
    {"name": "Praseodymium", "symbol": "Pr", "atomic_number": 59, "electron_config": "[Xe] 4f3 6s2", "atomic_radius": "180 pm"},
    {"name": "Neodymium", "symbol": "Nd", "atomic_number": 60, "electron_config": "[Xe] 4f4 6s2", "atomic_radius": "178 pm"},
    {"name": "Promethium", "symbol": "Pm", "atomic_number": 61, "electron_config": "[Xe] 4f5 6s2", "atomic_radius": "177 pm"},
    {"name": "Samarium", "symbol": "Sm", "atomic_number": 62, "electron_config": "[Xe] 4f6 6s2", "atomic_radius": "175 pm"},
    {"name": "Europium", "symbol": "Eu", "atomic_number": 63, "electron_config": "[Xe] 4f7 6s2", "atomic_radius": "173 pm"},
    {"name": "Gadolinium", "symbol": "Gd", "atomic_number": 64, "electron_config": "[Xe] 4f7 5d1 6s2", "atomic_radius": "171 pm"},
    {"name": "Terbium", "symbol": "Tb", "atomic_number": 65, "electron_config": "[Xe] 4f9 6s2", "atomic_radius": "169 pm"},
    {"name": "Dysprosium", "symbol": "Dy", "atomic_number": 66, "electron_config": "[Xe] 4f10 6s2", "atomic_radius": "167 pm"},
    {"name": "Holmium", "symbol": "Ho", "atomic_number": 67, "electron_config": "[Xe] 4f11 6s2", "atomic_radius": "166 pm"},
    {"name": "Erbium", "symbol": "Er", "atomic_number": 68, "electron_config": "[Xe] 4f12 6s2", "atomic_radius": "164 pm"},
    {"name": "Thulium", "symbol": "Tm", "atomic_number": 69, "electron_config": "[Xe] 4f13 6s2", "atomic_radius": "162 pm"},
    {"name": "Ytterbium", "symbol": "Yb", "atomic_number": 70, "electron_config": "[Xe] 4f14 6s2", "atomic_radius": "160 pm"},
    {"name": "Lutetium", "symbol": "Lu", "atomic_number": 71, "electron_config": "[Xe] 4f14 5d1 6s2", "atomic_radius": "159 pm"},
    {"name": "Hafnium", "symbol": "Hf", "atomic_number": 72, "electron_config": "[Xe] 4f14 5d2 6s2", "atomic_radius": "159 pm"},
    {"name": "Tantalum", "symbol": "Ta", "atomic_number": 73, "electron_config": "[Xe] 4f14 5d3 6s2", "atomic_radius": "147 pm"},
    {"name": "Tungsten", "symbol": "W", "atomic_number": 74, "electron_config": "[Xe] 4f14 5d4 6s2", "atomic_radius": "139 pm"},
    {"name": "Rhenium", "symbol": "Re", "atomic_number": 75, "electron_config": "[Xe] 4f14 5d5 6s2", "atomic_radius": "137 pm"},
    {"name": "Osmium", "symbol": "Os", "atomic_number": 76, "electron_config": "[Xe] 4f14 5d6 6s2", "atomic_radius": "137 pm"},
    {"name": "Iridium", "symbol": "Ir", "atomic_number": 77, "electron_config": "[Xe] 4f14 5d7 6s2", "atomic_radius": "136 pm"},
    {"name": "Platinum", "symbol": "Pt", "atomic_number": 78, "electron_config": "[Xe] 4f14 5d8 6s2", "atomic_radius": "139 pm"},
    {"name": "Gold", "symbol": "Au", "atomic_number": 79, "electron_config": "[Xe] 4f14 5d10 6s1", "atomic_radius": "144 pm"},
    {"name": "Mercury", "symbol": "Hg", "atomic_number": 80, "electron_config": "[Xe] 4f14 5d10 6s2", "atomic_radius": "150 pm"},
    {"name": "Thallium", "symbol": "Tl", "atomic_number": 81, "electron_config": "[Xe] 4f14 5d10 6s2 6p1", "atomic_radius": "157 pm"},
    {"name": "Lead", "symbol": "Pb", "atomic_number": 82, "electron_config": "[Xe] 4f14 5d10 6s2 6p2", "atomic_radius": "175 pm"},
    {"name": "Bismuth", "symbol": "Bi", "atomic_number": 83, "electron_config": "[Xe] 4f14 5d10 6s2 6p3", "atomic_radius": "160 pm"},
    {"name": "Polonium", "symbol": "Po", "atomic_number": 84, "electron_config": "[Xe] 4f14 5d10 6s2 6p4", "atomic_radius": "150 pm"},
    {"name": "Astatine", "symbol": "At", "atomic_number": 85, "electron_config": "[Xe] 4f14 5d10 6s2 6p5", "atomic_radius": "150 pm"},
    {"name": "Radon", "symbol": "Rn", "atomic_number": 86, "electron_config": "[Xe] 4f14 5d10 6s2 6p6", "atomic_radius": "150 pm"},
]

# Fungsi untuk menampilkan informasi unsur
def show_element_info(symbol):
    for element in periodic_table:
        if element['symbol'] == symbol:
            info = f"Nama: {element['name']}\n"
            info += f"Nomor Atom: {element['atomic_number']}\n"
            info += f"Konfigurasi Elektron: {element['electron_config']}\n"
            info += f"Ukuran Atom: {element['atomic_radius']}"
            messagebox.showinfo(f"Info Unsur {symbol}", info)
            return
    messagebox.showerror("Error", "Unsur tidak ditemukan.")

# Fungsi untuk membuat tombol tabel periodik
def create_periodic_table(root):
    row, col = 0, 0
    for element in periodic_table:
        button = tk.Button(root, text=element['symbol'], width=4, height=2, font=("Arial", 12),
                           command=lambda symbol=element['symbol']: show_element_info(symbol))
        button.grid(row=row, column=col, padx=9, pady=9)
        
        col += 1
        if col == 9:  # 9 kolom per baris
            col = 0
            row += 1

# Membuat jendela utama aplikasi
root = tk.Tk()
root.title("Tabel Periodik Unsur")

# Menambahkan tombol-tombol untuk tabel periodik
create_periodic_table(root)

# Menjalankan aplikasi
root.mainloop()
