# Mobile Hardware analysis

## Description:
  A basic analysis on the dataset, to understand the fundamentals and learn the perspective of dataset. This practice gave me the basic idea about how actually the data is observered for finding error/null if any, data visualization to breif out what data speaks rather then numbers, and played with some comman librs like **Seaborn, Matplotlib and pandas**.

## Analysis and conclusions:

### 1. Data analysing:

  - Using functions of pandas, like **.info(), .duplicated().sum()**  got an overview of do data has any null or duplicate values? 
  - Also using the same function got idea of columns that all of them are int64 except the clock_speed & m_dep they are float64.
  - Using **.corr()** got the correlation idea as follow

| Feature1       | Feature2       | CorrValue |
|----------------|----------------|-----------|
| battery_power  | px_width       | 0.053365  |
| blue           | ram            | 0.057570  |
| clock_speed    | px_width       | 0.070585  |
| dual_sim       | pc             | 0.073936  |
| fc             | pc             | 0.659338  |
| four_g         | three_g        | 0.553528  |
| int_memory     | sc_w           | 0.024521  |
| m_dep          | px_height      | 0.062559  |
| mobile_wt      | wifi           | 0.069762  |
| n_cores        | four_g         | 0.066716  |
| pc             | fc             | 0.659338  |
| px_height      | px_width       | 0.517650  |
| px_width       | px_height      | 0.517650  |
| ram            | blue           | 0.057570  |
| sc_h           | sc_w           | 0.497154  |
| sc_w           | sc_h           | 0.497154  |
| talk_time      | sc_w           | 0.063990  |
| three_g        | four_g         | 0.553528  |
| touch_screen   | clock_speed    | 0.061893  |
| wifi           | mobile_wt      | 0.069762  |

### 2. Graph Visualization:
1. Used columns like **four_g, three_g and dual_sim** for understanding **Categorical Data practice**.
  ```python
# BarGraph
import seaborn as sns
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(20, 8))

# 4G
sns.countplot(x=df['four_g'], ax=axes[0])
axes[0].set_title("Four_G")

# 3G
sns.countplot(x=df['three_g'], ax=axes[1])
axes[1].set_title("Three_G")

# Dual Sim
sns.countplot(x=df['dual_sim'], ax=axes[2])
axes[2].set_title("Dual_Sim")

plt.tight_layout()
plt.show()
```
<img width="1525" height="595" alt="Screenshot 2026-02-17 000743" src="https://github.com/user-attachments/assets/5d7a2714-4086-4ad0-b511-c16648e98e3c" />

**Conculsion: There are 487/1000 which are not using the 4g, 756/1000 uses 3g network. While 517/1000 uses dual sim card.** 

```python
# Pie Graph
fig, axes = plt.subplots(1, 3, figsize=(20, 8))

# 4G
df['four_g'].value_counts().plot(kind = 'pie', autopct = '%2f', ax=axes[0])
axes[0].set_title("Four_G")

# 3G
df['three_g'].value_counts().plot(kind = 'pie', autopct = '%2f',  ax=axes[1])
axes[1].set_title("Three_G")

# Dual Sim
df['dual_sim'].value_counts().plot(kind = 'pie', autopct = '%2f',  ax=axes[2])
axes[2].set_title("Dual_Sim")

plt.tight_layout()
plt.show()
```

<img width="1512" height="499" alt="Screenshot 2026-02-17 001307" src="https://github.com/user-attachments/assets/30d0531f-b1e4-46b8-a473-85323f4af21e" />

2. Used **battery_power and ram** columns to practice **Numerical Data Practice**

```python
# Hist Graph
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(20, 8))

# Histogram for battery_power
axes[0].hist(df['battery_power'], bins=20, color='skyblue', edgecolor='black')
axes[0].set_title("Battery Power")

# Histogram for ram
axes[1].hist(df['ram'], bins=20, color='salmon', edgecolor='black')
axes[1].set_title("RAM")

plt.tight_layout()
plt.show()
```

<img width="1506" height="608" alt="Screenshot 2026-02-17 014216" src="https://github.com/user-attachments/assets/71d0a142-1321-44ec-8da7-45fa77739b0f" />

## Dataset link: 
- [Mobile Price Prediction Dataset](https://www.kaggle.com/datasets/muhammadahmaddaar/mobile-price-classification)
