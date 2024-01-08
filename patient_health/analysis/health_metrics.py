# Define a class for calculating health metrics
class HealthMetrics:

  # Initialize the class with the necessary attributes
  def __init__(self, data):
    self.data = data  # The preprocessed patient data

  # Define a method to calculate the average blood pressure
  def average_blood_pressure(self):
    # Initialize a list for storing the blood pressure values
    blood_pressure_list = []

    # Loop through the patient data
    for patient in self.data:
      # Get the blood pressure value for each patient
      blood_pressure = patient['blood_pressure']

      # Add the blood pressure value to the list
      blood_pressure_list.append(blood_pressure)

    # Calculate the average blood pressure
    average_blood_pressure = sum(blood_pressure_list) / len(blood_pressure_list)

    # Return the average blood pressure
    return average_blood_pressure

  # Define a method to calculate the average cholesterol level
  def average_cholesterol_level(self):
    # Initialize a list for storing the cholesterol values
    cholesterol_list = []

    # Loop through the patient data
    for patient in self.data:
      # Get the cholesterol value for each patient
      cholesterol = patient['cholesterol']

      # Add the cholesterol value to the list
      cholesterol_list.append(cholesterol)

    # Calculate the average cholesterol level
    average_cholesterol_level = sum(cholesterol_list) / len(cholesterol_list)

    # Return the average cholesterol level
    return average_cholesterol_level

  # Define a method to calculate the average body mass index
  def average_body_mass_index(self):
    # Initialize a list for storing the body mass index values
    bmi_list = []

    # Loop through the patient data
    for patient in self.data:
      # Get the height and weight values for each patient
      height = patient['height']
      weight = patient['weight']

      # Calculate the body mass index for each patient
      bmi = weight / (height ** 2)

      # Add the body mass index value to the list
      bmi_list.append(bmi)

    # Calculate the average body mass index
    average_bmi = sum(bmi_list) / len(bmi_list)

    # Return the average body mass index
    return average_bmi
