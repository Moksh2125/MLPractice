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
1. The data do not contain any null and duplicate values.

2. It has a total of 10 features.

3. Starting with the **Visiting Date**
 <img width="1516" height="747" alt="image" src="https://github.com/user-attachments/assets/1a669f29-f9c7-47d5-96bd-c3fae466b28c" />
 
 - It can be notice that, the gym's average footfall is maintained annually excuding some point of the years.

4. Other then that it shows individual bar graphs for categorical features like **Gender, work_type, attendence_status and membership_type**

5. For the **workout_duration_minutes**:
<img width="1487" height="716" alt="image" src="https://github.com/user-attachments/assets/b16c1987-bdd0-460d-8639-eff0c33a0c3f" />

- From the spikes of the histogram, we can conclude that more people like to spead 2 hours at gym.

6. For the **calories_burned**:
<img width="1301" height="603" alt="image" src="https://github.com/user-attachments/assets/14a0ea22-29fc-474b-94f8-649ef6809f9f" />

- The graph shows that there is an avg building of calories in range of 200 to 650.

7. The correlation part:
<img width="845" height="615" alt="image" src="https://github.com/user-attachments/assets/e8bf1057-025f-4ed0-9829-aa58fde82c57" />

- There is a strong and obvious correlation between the calories bured and the duration a person workouts.
- Also the frequency of less calories burned is more compair to that of more calories burned.

## Dataset link:
[daily-gym-attendance-and-workout-activity-dataset](https://www.kaggle.com/datasets/zahranusratt/daily-gym-attendance-and-workout-activity-dataset)
