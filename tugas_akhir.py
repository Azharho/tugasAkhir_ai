import numpy as np
import matplotlib.pyplot as plt

# Fungsi keanggotaan untuk Permintaan
def permintaan(x):
    if x < 2000:
        return (2000 - x) / 2000
    elif 2000 <= x <= 3000:
        return 1
    elif 3000 < x < 4000:
        return (4000 - x) / 1000
    return 0

# Fungsi keanggotaan untuk Persediaan
def persediaan(y):
    if y < 200:
        return (200 - y) / 200
    elif 200 <= y <= 400:
        return 1
    elif 400 < y < 600:
        return (600 - y) / 200
    return 0

# Fungsi untuk menghitung produksi berdasarkan fuzzy rules
def fuzzy_inference(permintaan_status, persediaan_status):
    if permintaan_status == "turun":
        return 1 if persediaan_status == "sedikit" else 0
    elif permintaan_status == "tetap":
        return 1 if persediaan_status == "sedikit" else 0
    elif permintaan_status == "naik":
        return 1 if persediaan_status in ["sedikit", "sedang"] else 0
    return 0

# Contoh Input
permintaan_input = "turun"
persediaan_input = "sedikit"

# Menghitung keanggotaan
keanggotaan_permintaan = permintaan(1500)
keanggotaan_persediaan = persediaan(100)

# Menghitung produksi
produksi = fuzzy_inference(permintaan_input, persediaan_input)

# Output
print("Keanggotaan Permintaan:", keanggotaan_permintaan)
print("Keanggotaan Persediaan:", keanggotaan_persediaan)
print("Produksi berdasarkan aturan:", produksi)

# Visualisasi
x = np.linspace(0, 6000, 100)
y_permintaan = np.vectorize(permintaan)(x)
y_persediaan = np.vectorize(persediaan)(x)

plt.figure(figsize=(12, 8))

# Plot Fungsi Keanggotaan Permintaan
plt.subplot(2, 1, 1)
plt.plot(x, y_permintaan, label='Permintaan', color='orange')
plt.title('Fungsi Keanggotaan Permintaan')
plt.xlabel('Jumlah Permintaan')
plt.ylabel('Keanggotaan')
plt.axhline(0, color='gray', lw=0.5, ls='--')
plt.axvline(2000, color='blue', lw=0.5, ls='--', label='Batas Permintaan')
plt.legend()
plt.grid()

# Plot Fungsi Keanggotaan Persediaan
plt.subplot(2, 1, 2)
plt.plot(x, y_persediaan, label='Persediaan', color='purple')
plt.title('Fungsi Keanggotaan Persediaan')
plt.xlabel('Jumlah Persediaan')
plt.ylabel('Keanggotaan')
plt.axhline(0, color='gray', lw=0.5, ls='--')
plt.axvline(200, color='green', lw=0.5, ls='--', label='Batas Persediaan')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()