import pandas as pd
file_errors_location = 'C:\\Users\\Karolina\\Documents\\book1.xlsx'
df = pd.read_excel(file_errors_location)
print(df)

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Waga', y='Wzrost', data=df,)
sns.color_palette("Spectral", as_cmap=True)
