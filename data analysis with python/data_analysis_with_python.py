import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)
df.head()

df_anova= df[['make', 'price']]
grouped_anova= df_anova.groupby(['make'])
anova_results_1= stats.f_oneway(grouped_anova.get_grouped('honda')['price'], grouped_anova.get_group('subaru')['price'])


