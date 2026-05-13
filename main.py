def hisobla_bmi(koychilik, boylam):
    """
    BMI (tana massasi indeksi) hisoblash funksiyasi
    """
    return koychilik / (boylam ** 2)

def tanqidi_bmi(bmi):
    """
    BMI qiymatiga asosan tanqidi ma'lumot beruvchi funksiya
    """
    if bmi < 18.5:
        return "Kam og'irlik"
    elif bmi < 25:
        return "Norma"
    elif bmi < 30:
        return "Og'irlik"
    else:
        return "Keng og'irlik"

def main():
    # Foydalanuvchi ma'lumotlari
    koychilik = float(input("Koychilikni kiriting (kg): "))
    boylam = float(input("Boylamni kiriting (m): "))

    # BMI hisoblash
    bmi = hisobla_bmi(koychilik, boylam)

    # Tanqidi ma'lumot berish
    tanqidi = tanqidi_bmi(bmi)

    # Natija chiqarish
    print(f"BMI: {bmi:.2f}")
    print(f"Tanqidi: {tanqidi}")

if __name__ == "__main__":
    main()
