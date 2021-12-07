import pandas as pd

request = pd.read_csv("Holiday Schedule Ranking 2019.csv")

request.sort_index()

print(request)