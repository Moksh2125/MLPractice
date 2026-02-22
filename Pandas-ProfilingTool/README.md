# Practicing analysing through Pandas - Profiling tool
- This is firstime using the pandas profiling tool to analysis a dataset. It help me understand the below things:

## What exactly is Pandas profile and how to implement it on a dataset:
- Pandas profile is a tool by which one can aquire the basic understanding of a dataset.
- It answers all the basic questions like do the dataset contains any null or duplicates? What is the size of the dataset? How many different features are on? etc..
- It also creates a very detailed content to be noticed about all features.
- Code to execute:
``` python
from ydata_profiling import ProfileReport

df = pd.read_csv("your_dataset") 
prof = ProfileReport(df)
prof.to_file(output_file = "GymDataAnalysis.html")
```
## Analysis of GymDataSet using pandas profile tool



Dataset link:
[Dataset](https://www.kaggle.com/datasets/zahranusratt/daily-gym-attendance-and-workout-activity-dataset)
