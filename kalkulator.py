import tkinter as tk

# Fungsi untuk memperbarui ekspresi di layar
def tekan_tombol(angka):
    ekspresi_saat_ini = layar_var.get()
    layar_var.set(ekspresi_saat_ini + str(angka))

# Fungsi untuk menghitung hasil
def hitung():
    try:
        hasil = eval(layar_var.get())
        layar_var.set(hasil)
    except ZeroDivisionError:
        layar_var.set("Error (Div/0)")
    except Exception:
        layar_var.set("Error")

# Fungsi untuk menghapus layar
def hapus():
    layar_var.set("")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator GUI")
root.geometry("300x400")

layar_var = tk.StringVar()

# Layar Tampilan
layar = tk.Entry(root, textvariable=layar_var, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=5, justify='right')
layar.grid(row=0, column=0, columnspan=4)

# Definisi Tombol
tombol = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Membuat dan menyusun tombol ke dalam grid
baris = 1
kolom = 0
for t in tombol:
    if t == '=':
        aksi = hitung
    elif t == 'C':
        aksi = hapus
    else:
        # Menggunakan lambda agar fungsi menerima argumen tombol yang ditekan
        aksi = lambda x=t: tekan_tombol(x)
        
    tk.Button(root, text=t, padx=20, pady=20, font=("Arial", 14), command=aksi).grid(row=baris, column=kolom, sticky="nsew")
    
    kolom += 1
    if kolom > 3:
        kolom = 0
        baris += 1

# Mengatur agar ukuran tombol fleksibel saat jendela di-resize
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
