import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["reading_time"].tolist()

mean = statistics.mean(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    return statistics.mean(dataset)


mean_list = []
for i in range(100):
    mean_list.append(random_set_of_mean(30))

sample_mean = statistics.mean(mean_list)
std_deviation = statistics.stdev(mean_list)
z_score = (mean - sample_mean) / std_deviation


first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([mean_list], ["Reading Time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 0.17], mode="lines", name="Sample Mean"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


print("Population Mean: ", mean)
print("Sample Mean: ", sample_mean)
print("Standard Deviation of Sample: ", std_deviation)
print("The Z Score is: ", z_score)
