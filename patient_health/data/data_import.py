# Define a class for data import
class DataImporter:

  # Initialize the class with the necessary attributes
  def __init__(self, data_file, data_format):
    self.data_file = data_file  # The path to the data file
    self.data_format = data_format  # The format of the data file (CSV or JSON)

  # Define a method to import the data
  def import_data(self):
    # Check the data format and call the appropriate method
    if self.data_format == 'CSV':
      return self.import_csv()
    elif self.data_format == 'JSON':
      return self.import_json()
    else:
      raise ValueError('Invalid data format')

  # Define a method to import CSV data
  def import_csv(self):
    # Import the pandas library
    import pandas as pd

    # Read the CSV file and return a DataFrame
    return pd.read_csv(self.data_file)

  # Define a method to import JSON data
  def import_json(self):
    # Import the json library
    import json

    # Open the JSON file and load the content
    with open(self.data_file, 'r') as f:
      data = json.load(f)

    # Return the data as a dictionary
    return data


# Define the main function
def main():
  # Create an instance of the DataImporter class with the given parameters
  data_importer = DataImporter(
    data_file='./Raw_Data/data.json',
    data_format='JSON'
  )

  # Import the data and print it
  data = data_importer.import_data()
  print(data)


# Call the main function
if __name__ == '__main__':
  main()
