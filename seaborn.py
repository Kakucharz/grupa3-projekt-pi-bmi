import pandas as pd
file_errors_location = 'output.xlsx'
df = pd.read_excel(file_errors_location)
print(df)

from matplotlib import pyplot as plt
import seaborn as sns
sns.lmplot(x= 'Lp.', y='BMI', data=df,)
sns.color_palette("Spectral", as_cmap=True)
