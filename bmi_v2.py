import pandas as pd

dane = pd.read_excel('bmi_tabela.xlsx')
lista_bmi = []

for numer in dane.index:
    bmi = round(dane["Waga"][numer]/(dane["Wzrost"][numer]**2), 2)
    lista_bmi.append(bmi)
    
print(dane)    

dane["BMI"] = lista_bmi
del dane["Unnamed: 0"]

with pd.ExcelWriter('output.xlsx', mode = 'w' ) as writer:
    dane.to_excel(writer, sheet_name="wynik")
    