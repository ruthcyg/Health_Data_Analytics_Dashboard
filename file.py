# import os

# # Define the structure of directories and files for the project
# project_structure = {
#     "Patient-Health-Data-Analytics-Dashboard": {
#         "data": ["patient_data.csv", "patient_data.json"],
#         "src": ["__init__.py", "data_import.py", "data_preprocessing.py", "data_analysis.py",
#                 "data_visualization.py", "user_interface.py", "health_reports.py", "performance_optimization.py"],
#         "tests": ["__init__.py", "test_data_import.py", "test_data_preprocessing.py", "test_data_analysis.py",
#                   "test_data_visualization.py", "test_user_interface.py", "test_health_reports.py", "test_performance_optimization.py"],
#         "docs": ["index.md", "data_import.md", "data_preprocessing.md", "data_analysis.md",
#                  "data_visualization.md", "user_interface.md", "health_reports.md", "performance_optimization.md"],
#         "root_files": [".gitignore", "README.md", "requirements.txt", "setup.py"]
#     }
# }

# base_path = "/data/"


# # Function to create directories and files based on the project structure
# def create_project_structure(base_path, structure):
#     for directory, content in structure.items():
#         dir_path = os.path.join(base_path, directory)
#         os.makedirs(dir_path, exist_ok=True)

#         for key, files in content.items():
#             if key != "root_files":
#                 subdir_path = os.path.join(dir_path, key)
#                 os.makedirs(subdir_path, exist_ok=True)
#                 for file in files:
#                     open(os.path.join(subdir_path, file), 'a').close()
#             else:
#                 for file in files:
#                     open(os.path.join(dir_path, file), 'a').close()


# # Create the project structure
# create_project_structure(base_path, project_structure)
# import pandas as pd

# # Create a DataFrame 'df' with 'category' and 'value' columns.
# df = pd.DataFrame({
#     'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C'],
#     'value': [10, 20, 10, 30, 20, 30, 40]
# })

# # Group by 'category' and compute the average 'value'.
# grouped = df.groupby('category').agg(average_value=('value', 'mean'))

# # Define a custom scaling function.
# scale = lambda x: (x - x.min()) / (x.max() - x.min())

# # Apply the scaling function to the 'average_value' column.
# grouped['scaled_avg_value'] = scale(grouped['average_value'])

# print(grouped)

# Import pandas library
# import pandas as pd

# # Create a DataFrame 'df' with 'Product_Category' and 'Sales' columns.
# df = pd.DataFrame({
#     'Product_Category': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture'],
#     'Sales': [1000, 2000, 1500, 3000, 2500, 3500, 4000]
# })

# # Group by 'Product_Category' and compute the average 'Sales'.
# grouped = df.groupby('Product_Category').agg(average_sales=('Sales', 'mean'))

# # Define a custom scaling function.
# scale = lambda x: (x - x.min()) / (x.max() - x.min())

# # Apply the scaling function to the 'average_sales' column.
# grouped['scaled_avg_sales'] = scale(grouped['average_sales'])

# print(grouped)

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Create a DataFrame 'df' with 'Diagnosis', 'Medication', 'Cost', 'Visits', 'Nutrition', 'BMI' and 'Parent_Education' columns.
# df = pd.DataFrame({
#     'Diagnosis': ['Disease1', 'Disease1', 'Disease1', 'Disease2', 'Disease2', 'Disease3', 'Disease3'],
#     'Medication': ['Med1', 'Med1', 'Med1', 'Med2', 'Med2', 'Med3', 'Med3'],
#     'Cost': [100, 150, 200, 250, 300, 350, 400],
#     'Visits': [5, 3, 4, 6, 2, 3, 5],
#     'Nutrition': ['Poor', 'Average', 'Poor', 'Good', 'Average', 'Poor', 'Good'],
#     'BMI': [15, 18, 16, 20, 19, 15, 21],
#     'Parent_Education': ['Low', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High']
# })

# # Convert categorical variables into numerical variables for correlation analysis
# df['Nutrition'] = df['Nutrition'].map({'Poor': 0, 'Average': 1, 'Good': 2})
# df['Parent_Education'] = df['Parent_Education'].map({'Low': 0, 'Medium': 1, 'High': 2})

# # Compute the correlation matrix
# corr = df.corr()

# # Generate a heatmap in seaborn
# sns.heatmap(corr, annot=True)

# # Show the plot
# plt.show()

# Importing Required Library
# import pandas as pd

# # Creating DataFrame 'df' with 'Product_Category' and 'Sales' columns.
# df = pd.DataFrame({
#     'Product_Category': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Clothing', 'Electronics', 'Furniture'],
#     'Sales': [1000, 2000, 1500, 3000, 2500, 3500, 4000]
# })

# # Grouping by 'Product_Category' and Computing the Average 'Sales'.
# grouped = df.groupby('Product_Category').agg(average_sales=('Sales', 'mean'))

# # Defining Custom Scaling Function.
# scale = lambda x: (x - x.min()) / (x.max() - x.min())

# # Applying the Scaling Function to the 'average_sales' Column.
# grouped['scaled_avg_sales'] = scale(grouped['average_sales'])

# # Printing the Result
# print(grouped)

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Create a DataFrame 'df' with 'Diagnosis', 'Medication', 'Cost', 'Visits', 'Nutrition', 'BMI' and 'Parent_Education' columns.
# df = pd.DataFrame({
#     'Diagnosis': ['Disease1', 'Disease1', 'Disease1', 'Disease2', 'Disease2', 'Disease3', 'Disease3'],
#     'Medication': ['Med1', 'Med1', 'Med1', 'Med2', 'Med2', 'Med3', 'Med3'],
#     'Cost': [100, 150, 200, 250, 300, 350, 400],
#     'Visits': [5, 3, 4, 6, 2, 3, 5],
#     'Nutrition': ['Poor', 'Average', 'Poor', 'Good', 'Average', 'Poor', 'Good'],
#     'BMI': [15, 18, 16, 20, 19, 15, 21],
#     'Parent_Education': ['Low', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High']
# })

# # Convert categorical variables into numerical variables for correlation analysis
# df['Nutrition'] = df['Nutrition'].map({'Poor': 0, 'Average': 1, 'Good': 2})
# df['Parent_Education'] = df['Parent_Education'].map({'Low': 0, 'Medium': 1, 'High': 2})

# # Normalize the 'Cost' column using a lambda function
# df['Cost'] = df['Cost'].apply(lambda x: (x - df['Cost'].min()) / (df['Cost'].max() - df['Cost'].min()))

# # Select only numeric columns for the correlation matrix
# numeric_df = df.select_dtypes(include=[np.number])

# # Compute the correlation matrix on numeric data only
# corr = numeric_df.corr()

# # Generate a heatmap in seaborn
# sns.heatmap(corr, annot=True)

# # Show the plot
# plt.show()

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np  # Importing NumPy

# # Create a DataFrame 'df' with 'Diagnosis', 'Medication', 'Cost', 'Visits', 'Nutrition', 'BMI' and 'Parent_Education' columns.
# df = pd.DataFrame({
#     'Diagnosis': ['Disease1', 'Disease1', 'Disease1', 'Disease2', 'Disease2', 'Disease3', 'Disease3'],
#     'Medication': ['Med1', 'Med1', 'Med1', 'Med2', 'Med2', 'Med3', 'Med3'],
#     'Cost': [100, 150, 200, 250, 300, 350, 400],
#     'Visits': [5, 3, 4, 6, 2, 3, 5],
#     'Nutrition': ['Poor', 'Average', 'Poor', 'Good', 'Average', 'Poor', 'Good'],
#     'BMI': [15, 18, 16, 20, 19, 15, 21],
#     'Parent_Education': ['Low', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High']
# })

# # Convert categorical variables into numerical variables for correlation analysis
# df['Nutrition'] = df['Nutrition'].map({'Poor': 0, 'Average': 1, 'Good': 2})
# df['Parent_Education'] = df['Parent_Education'].map({'Low': 0, 'Medium': 1, 'High': 2})

# # Normalize the 'Cost' column using a lambda function
# df['Cost'] = df['Cost'].apply(lambda x: (x - df['Cost'].min()) / (df['Cost'].max() - df['Cost'].min()))

# # Select only numeric columns for the correlation matrix
# numeric_df = df.select_dtypes(include=[np.number])

# # Compute the correlation matrix on numeric data only
# corr = numeric_df.corr()

# # Generate a heatmap in seaborn
# sns.heatmap(corr, annot=True)

# # Show the plot
# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  # Importing NumPy

# Create a DataFrame 'df' with 'Diagnosis', 'Medication', 'Cost', 'Visits', 'Nutrition', 'BMI' and 'Parent_Education' columns.
df = pd.DataFrame({
    'Diagnosis': ['Disease1', 'Disease1', 'Disease1', 'Disease2', 'Disease2', 'Disease3', 'Disease3'],
    'Medication': ['Med1', 'Med1', 'Med1', 'Med2', 'Med2', 'Med3', 'Med3'],
    'Cost': [100, 150, 200, 250, 300, 350, 400],
    'Visits': [5, 3, 4, 6, 2, 3, 5],
    'Nutrition': ['Poor', 'Average', 'Poor', 'Good', 'Average', 'Poor', 'Good'],
    'BMI': [15, 18, 16, 20, 19, 15, 21],
    'Parent_Education': ['Low', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High']
})

# Convert categorical variables into numerical variables for correlation analysis
df['Nutrition'] = df['Nutrition'].map({'Poor': 0, 'Average': 1, 'Good': 2})
df['Parent_Education'] = df['Parent_Education'].map({'Low': 0, 'Medium': 1, 'High': 2})

# Normalize the 'Cost' column using a lambda function
df['Cost'] = df['Cost'].apply(lambda x: (x - df['Cost'].min()) / (df['Cost'].max() - df['Cost'].min()))

# Select only numeric columns for the correlation matrix
numeric_df = df.select_dtypes(include=[np.number])

# Compute the correlation matrix on numeric data only
corr = numeric_df.corr()

# Generate a heatmap in seaborn
sns.heatmap(corr, annot=True)

# Show the plot
plt.show()
