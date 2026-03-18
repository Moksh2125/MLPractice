# Feature engineering: Scaling the Data
- This is a practice on dataset to understand different feature scaling methods and also, **Standardization vs Normalization** topic.

## Code and dataset showcase:
```Python
# importing dataset
dt = pd.read_csv("../dataset/ks-projects-201801.csv", usecols = [6,8,10,12,13,14])
dt.head(10)
```
| goal    | pledged | backers | usd pledged | usd_pledged_real | usd_goal_real |
|---------|--------:|--------:|------------:|-----------------:|--------------:|
| 1000.0  | 0.00    | 0       | 0.00        | 0.00             | 1533.95       |
| 30000.0 | 2421.00 | 15      | 100.00      | 2421.00          | 30000.00      |
| 45000.0 | 220.00  | 3       | 220.00      | 220.00           | 45000.00      |
| 5000.0  | 1.00    | 1       | 1.00        | 1.00             | 5000.00       |
| 19500.0 | 1283.00 | 14      | 1283.00     | 1283.00          | 19500.00      |
| 50000.0 | 52375.00| 224     | 52375.00    | 52375.00         | 50000.00      |
| 1000.0  | 1205.00 | 16      | 1205.00     | 1205.00          | 1000.00       |
| 25000.0 | 453.00  | 40      | 453.00      | 453.00           | 25000.00      |
| 125000.0| 8233.00 | 58      | 8233.00     | 8233.00          | 125000.00     |
| 65000.0 | 6240.57 | 43      | 6240.57     | 6240.57          | 65000.00      |

```python
# Fit the data and transfrom it

from sklearn.preprocessing import StandardScaler # MinMaxScaler, MaxAbsScaler or RobustScaler 
scaler = StandardScaler() # use accordingly

scaler.fit(dt)
dt_transfrom = scaler.transform(dt)
dt_transfrom = pd.DataFrame(dt_transfrom, columns = dt.columns) # numpy to dataframe
```

```python
# Visualization

fig, axes = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns

axes[0].scatter(dt["usd_pledged_real"], dt['usd_goal_real'], label="Before")
axes[0].legend()

axes[1].scatter(dt_transfrom["usd_pledged_real"], dt_transfrom['usd_goal_real'], label="After")
axes[1].legend()

plt.tight_layout()
fig.suptitle("StandardScaler")
plt.show()
```
## Output and understanding:

<img width="1462" height="568" alt="Screenshot 2026-03-18 145953" src="https://github.com/user-attachments/assets/735ee691-30eb-4967-ac85-55d94a69fee0" />
<img width="1411" height="519" alt="Screenshot 2026-03-18 150013" src="https://github.com/user-attachments/assets/350513de-1bc3-48fd-a1d8-3452a501f569" />
<img width="1435" height="551" alt="Screenshot 2026-03-18 150032" src="https://github.com/user-attachments/assets/12006d6c-bd6c-4f19-994d-dc1552055b9b" />
<img width="1344" height="536" alt="Screenshot 2026-03-18 150115" src="https://github.com/user-attachments/assets/be849c2d-bdb2-40f5-a7be-d54963e4d73c" />

- The initial data has outliers crossing million in values, which can cause **hallucination** during training. The data is scaled down differently in all methods.
- **StandardScaler** focus on keeping it near to zero.
-  **MinMax and MaxAbs** gives same output keeping them in 1 unit square.
-  **Robust** focuses on the “middle bulk” of data, ignoring extreme values, which perfectly fits this dataset condition.

## Dataset:
- [kickstarter-projects](https://www.kaggle.com/datasets/kemical/kickstarter-projects?)
