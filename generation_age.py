"""
Written by Nahom Atnafu
Date: 12/16/ 2022
This program takes in your birth year and tells you which generation you belong to.
"""
birth_year = int(input("When were you born: "))

if birth_year <= 1928:
    print("You belong to the Greatest Generation.")
elif 1928 < birth_year <= 1946:
    print("You belong to the Traditionalists or the Silent Generation.")
elif 1946 < birth_year <= 1964:
    print("You belong to the Baby Boomers.")
elif 1965 <= birth_year <= 1976:
    print("You belong to the Gen X.")
elif 1977 <= birth_year <= 1995:
    print("You belong to the Gen Y or the Millennials.")
elif 1995 < birth_year <= 2010:
    print("You belong to the Gen Z, the iGen or the Centennials.")
elif 2010 < birth_year:
    print("You belong to the Generation Alpha.")
