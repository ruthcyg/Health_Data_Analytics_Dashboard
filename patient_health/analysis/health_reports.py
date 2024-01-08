# Define a class for generating health reports
class HealthReports:

  # Initialize the class with the necessary attributes
  def __init__(self, data, metrics):
    self.data = data  # The preprocessed patient data
    self.metrics = metrics  # The health metrics object

  # Define a method to generate a report based on selected parameters
  def generate_report(self, age_group, health_condition):
    # Initialize an empty list for storing the report content
    report_content = []

    # Filter the patient data based on the age group and the health condition
    filtered_data = self.filter_data(age_group, health_condition)

    # Add the report title to the list
    report_title = f"Health Report for {age_group} Patients with {health_condition}"
    report_content.append(report_title)

    # Add the report summary to the list
    report_summary = f"This report summarizes the health status of {len(filtered_data)} patients who belong to the {age_group} age group and have {health_condition}."
    report_content.append(report_summary)

    # Add the report statistics to the list
    report_statistics = f"The average blood pressure of these patients is {self.metrics.average_blood_pressure(filtered_data)} mmHg. The average cholesterol level of these patients is {self.metrics.average_cholesterol_level(filtered_data)} mg/dL. The average body mass index of these patients is {self.metrics.average_body_mass_index(filtered_data)}."
    report_content.append(report_statistics)

    # Add the report recommendations to the list
    report_recommendations = f"These patients are advised to follow a healthy lifestyle, such as eating a balanced diet, exercising regularly, and avoiding smoking and alcohol. They should also consult their doctors regularly and monitor their health conditions."
    report_content.append(report_recommendations)

    # Join the report content with line breaks
    report = "\n".join(report_content)

    # Return the report
    return report

  # Define a helper method to filter the patient data based on the selected parameters
  def filter_data(self, age_group, health_condition):
    # Initialize an empty list for storing the filtered data
    filtered_data = []

    # Define the age range based on the age group
    if age_group == 'young':
      age_range = (18, 35)
    elif age_group == 'middle-aged':
      age_range = (36, 55)
    elif age_group == 'old':
      age_range = (56, 100)
    else:
      raise ValueError('Invalid age group')

    # Loop through the patient data
    for patient in self.data:
      # Get the age and the health condition value for each patient
      age = patient['age']
      condition = patient[health_condition]

      # Check if the patient meets the criteria
      if age_range[0] <= age <= age_range[1] and condition == 1:
        # Add the patient to the filtered data
        filtered_data.append(patient)

    # Return the filtered data
    return filtered_data
