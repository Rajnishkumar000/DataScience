import pandas as pd
import numpy as np

from io import StringIO
json_str = '{"Courses":{"r1":"Spark"},"Fee":{"r1":"25000"},"Duration":{"r1":"50 Days"}}'
json_str = StringIO(json_str)
df = pd.read_json(json_str)
print(df)
print(df.head())
# Outputs
#   Courses    Fee Duration
# r1   Spark  25000  50 Days

# Data123 = "{'employee_name': 'James', 'email': 'james@gmail.com', 'job_profile':[ 'title1 ':'team lead','title2':'bbj']} "
# json_buffer123 = StringIO(Data123)
# print(pd.read_json(json_buffer123))










# json_data = '{"column1": [1, 2, 3], "column2": ["A", "B", "C"]}'
# # Wrap the JSON string in a StringIO object
# json_buffer = StringIO(json_data)
#
# # Read JSON data from the StringIO object
# df = pd.read_json(json_buffer)
# print(df)

# Now, you can work with the DataFrame 'df'
