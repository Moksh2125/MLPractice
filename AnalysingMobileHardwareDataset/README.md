# Mobile Hardware analysis

## Description:
  A basic analysis on the dataset, to understand the fundamentals and learn the perspective of dataset. This practice gave me the basic idea about how actually the data is observered for finding error/null if any, data visualization to breif out what data speaks rather then numbers, and played with some comman librs like **Seaborn, Matplotlib and pandas**.

## Analysis and conclusions:

### 1. Data analysing:

    - Using functions of pandas, like **.info(), .duplicated().sum()**  got an overview of do data has any null or duplicate values? 
    - Also using the same function got idea of columns that all of them are int64 except the clock_speed & m_dep they are float64.
    - Using .corr() got the correlation idea as follow: 

    | Feature1 | Feature2 | CorrValue |
    |----------------|----------------|-----------|
    | battery_power | px_width | 0.053365 | 
    | blue | ram | 0.057570 | 
    | clock_speed | px_width | 0.070585 |
    | dual_sim | pc | 0.073936 |
    | fc | pc | 0.659338 | | four_g | three_g | 0.553528 | | int_memory | sc_w | 0.024521 | | m_dep | px_height | 0.062559 | | mobile_wt | wifi | 0.069762 | | n_cores | four_g | 0.066716 | | pc | fc | 0.659338 | | px_height | px_width | 0.517650 | | px_width | px_height | 0.517650 | | ram | blue | 0.057570 | | sc_h | sc_w | 0.497154 | | sc_w | sc_h | 0.497154 | | talk_time | sc_w | 0.063990 | | three_g | four_g | 0.553528 | | touch_screen | clock_speed | 0.061893 | | wifi | mobile_wt | 0.069762 |
