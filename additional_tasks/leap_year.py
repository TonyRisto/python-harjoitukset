year = int(input("Anna vuosiluku (esim. 2018): "))
original_year = year

fourths = year / 4
hundreds = year / 100
fourth_hundreds = year / 400

sum1 = fourths + hundreds + fourth_hundreds
isLeapYear = None

if sum1 == int(sum1):
    print(f"{year} on karkausvuosi.") ## Tsekkaa onko vuosisatojen mukaan karkausvuosi.
    isLeapYear = True
if (fourths == int(fourths)) and (hundreds != int(hundreds) and (fourth_hundreds != int)):
    print(f"{year} on karkausvuosi.")
    isLeapYear = True
if isLeapYear != True:
    print(f"{year} ei ole karkausvuosi.")