
def calculate_salary():
    try:
        # Meminta input jumlah jam kerja dan tarif per jam
        hours_worked = float(input("Masukkan jumlah jam kerja dalam seminggu: "))
        hourly_rate = float(input("Masukkan tarif per jam: "))

        # Hitung gaji normal
        if hours_worked <= 40:
            total_salary = hours_worked * hourly_rate
        else:
            # Hitung gaji normal dan lembur jika lebih dari 40 jam
            overtime_hours = hours_worked - 40
            overtime_rate = hourly_rate * 1.5
            total_salary = (40 * hourly_rate) + (overtime_hours * overtime_rate)

        # Menampilkan hasil
        print(f"\nGaji total karyawan: Rp {total_salary:,.2f}")

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar.")

# Menjalankan fungsi
if __name__ == "__main__":
    calculate_salary()
