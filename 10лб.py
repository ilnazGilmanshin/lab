import pandas as pd

df = pd.read_csv('rosstat_salary_ru10.csv', sep=None, engine='python')

to_remove = ['Рязанская область', 'Свердловская область', 'Чеченская Республика', 'Ростовская область']

df_filtered = df[~df['region_name'].isin(to_remove)].copy()

variation_series = df_filtered['salary'].dropna().sort_values()

mean_val = variation_series.mean()
median_val = variation_series.median()

print(f"Количество регионов в выборке: {len(variation_series)}")
print(f"Выборочное среднее: {mean_val:.2f}")
print(f"Выборочная медиана: {median_val:.2f}")