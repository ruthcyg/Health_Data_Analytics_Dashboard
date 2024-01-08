# Define a class for health visualization
class HealthVisualization:

  # Initialize the class with the necessary attributes
  def __init__(self, data, metrics, plotter):
    self.data = data  # The preprocessed patient data
    self.metrics = metrics  # The health metrics object
    self.plotter = plotter  # The data plotter object

  # Define a method to visualize the health trends over time
  def visualize_health_trends(self):
    # Get the dates and the health metrics values from the data
    dates = self.data['date']
    blood_pressure = self.data['blood_pressure']
    cholesterol = self.data['cholesterol']
    bmi = self.data['bmi']

    # Plot the line charts for each health metric
    self.plotter.plot_line_chart(dates, blood_pressure, 'Blood Pressure over Time', 'Date', 'Blood Pressure (mmHg)')
    self.plotter.plot_line_chart(dates, cholesterol, 'Cholesterol Level over Time', 'Date', 'Cholesterol Level (mg/dL)')
    self.plotter.plot_line_chart(dates, bmi, 'Body Mass Index over Time', 'Date', 'Body Mass Index (kg/m2)')

  # Define a method to visualize the health statistics by age group
  def visualize_health_statistics_by_age_group(self):
    # Define the age groups and their ranges
    age_groups = ['young', 'middle-aged', 'old']
    age_ranges = [(18, 35), (36, 55), (56, 100)]

    # Initialize empty lists for storing the health metrics averages by age group
    blood_pressure_averages = []
    cholesterol_averages = []
    bmi_averages = []

    # Loop through the age groups and their ranges
    for age_group, age_range in zip(age_groups, age_ranges):
      # Filter the data by the age range
      filtered_data = self.data[(self.data['age'] >= age_range[0]) & (self.data['age'] <= age_range[1])]

      # Calculate the average health metrics for the filtered data
      blood_pressure_average = self.metrics.average_blood_pressure(filtered_data)
      cholesterol_average = self.metrics.average_cholesterol_level(filtered_data)
      bmi_average = self.metrics.average_body_mass_index(filtered_data)

      # Add the averages to the lists
      blood_pressure_averages.append(blood_pressure_average)
      cholesterol_averages.append(cholesterol_average)
      bmi_averages.append(bmi_average)

    # Plot the bar charts for each health metric by age group
    self.plotter.plot_bar_chart(age_groups, blood_pressure_averages, 'Average Blood Pressure by Age Group', 'Age Group', 'Blood Pressure (mmHg)')
    self.plotter.plot_bar_chart(age_groups, cholesterol_averages, 'Average Cholesterol Level by Age Group', 'Age Group', 'Cholesterol Level (mg/dL)')
    self.plotter.plot_bar_chart(age_groups, bmi_averages, 'Average Body Mass Index by Age Group', 'Age Group', 'Body Mass Index (kg/m2)')

  # Define a method to visualize the health distribution by health condition
  def visualize_health_distribution_by_health_condition(self):
    # Define the health conditions and their labels
    health_conditions = ['diabetes', 'heart_disease', 'stroke']
    health_labels = ['No Diabetes', 'Diabetes', 'No Heart Disease', 'Heart Disease', 'No Stroke', 'Stroke']

    # Initialize empty lists for storing the health condition values and counts
    health_values = []
    health_counts = []

    # Loop through the health conditions
    for health_condition in health_conditions:
      # Get the value counts for each health condition
      value_counts = self.data[health_condition].value_counts()

      # Add the values and counts to the lists
      health_values.extend(value_counts.index)
      health_counts.extend(value_counts.values)

    # Plot the pie chart for the health distribution by health condition
    self.plotter.plot_pie_chart(health_labels, health_counts, 'Health Distribution by Health Condition')
