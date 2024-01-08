# Define a class for data preprocessing
class DataPreprocessor:
  # Initialize the class with the necessary attributes
  def __init__(self, data_file, output_file, subword_vocab, token_vocab):
    self.data_file = data_file # The path to the raw data file
    self.output_file = output_file # The path to the output file
    self.subword_vocab = subword_vocab # The subword vocabulary object
    self.token_vocab = token_vocab # The token vocabulary dictionary
    self.end_of_token_index = 1 # The index of the end-of-token symbol
    self.epsilon = 1e-5 # A small constant to avoid zero division

  # Define a method to import and preprocess the data
  def preprocess_data(self):
    # Open the data file and read the JSON content
    with open(self.data_file, 'r') as f:
      data = json.load(f)

    # Initialize an empty dictionary for the output data
    output_data = {}

    # Loop through the projects in the data
    for project in data:
      # Get the project index and the directories
      project_index = project['project_index']
      directories = project['directories']

      # Initialize an empty dictionary for the project data
      output_data[project_index] = {}

      # Loop through the directories in the project
      for directory in directories:
        # Get the directory index and the files
        directory_index = directory['directory_index']
        files = directory['files']

        # Initialize an empty dictionary for the directory data
        output_data[project_index][directory_index] = {}

        # Loop through the files in the directory
        for file in files:
          # Get the file index and the lines
          file_index = file['file_index']
          lines = file['lines']

          # Initialize an empty list for the file subword indices
          file_subword_indices = []

          # Initialize an empty dictionary for the file token information
          file_token_info = {}

          # Loop through the lines in the file
          for line in lines:
            # Get the tokens and the token types
            tokens = line['tokens'].strip().split()
            token_types = line['token_types'].strip().split()

            # Initialize an empty list for the subword id ranges
            subword_id_ranges = []

            # Loop through the tokens and the token types
            for token, token_type in zip(tokens, token_types):
              # Handle string literals as a single token
              if token_type == 'STRINGLITERAL':
                # Find the end of the string literal
                for i in range(tokens.index(token), len(tokens)):
                  if tokens[i].endswith('"') or tokens[i].endswith("'"):
                    # Concatenate the tokens that form the string literal
                    token = ' '.join(tokens[tokens.index(token):i+1])
                    break

              # Get the initial length of the file subword indices
              init_length = len(file_subword_indices)

              # Encode the token into subword tokens
              subword_tokens = self.subword_vocab.encode_without_tokenizing(token)

              # Skip the token if it has more than 20 subword tokens
              if len(subword_tokens) > 20:
                continue

              # Get the subword id range for the token
              subword_id_range = (init_length, init_length + len(subword_tokens) + 1)

              # Add the subword id range to the list
              subword_id_ranges.append(subword_id_range)

              # Initialize an empty list for the token information
              token_info = []

              # Add the token, the token type, and the token vocabulary count to the list
              token_info.append(token)
              token_info.append(token_type)
              token_info.append(self.token_vocab.get(token, 0.0))

              # Add the token information to the file token information dictionary
              file_token_info[subword_id_range] = token_info

              # Add the subword tokens and the end-of-token index to the file subword indices
              file_subword_indices.extend(subword_tokens)
              file_subword_indices.append(self.end_of_token_index)

            # Loop through the subword id ranges
            for subword_id_range in subword_id_ranges:
              # Add the current length of the file subword indices to the token information
              file_token_info[subword_id_range].append(len(file_subword_indices))

          # Add the file subword indices and the file token information to the directory data
          output_data[project_index][directory_index][file_index] = (file_subword_indices, file_token_info)

    # Return the output data
    return output_data

  # Define a method to save the output data to a file
  def save_data(self, data):
    # Open the output file and write the data as a pickle object
    with open(self.output_file, 'wb') as f:
      pickle.dump(data, f)

# Define the main function
def main():
  # Create an instance of the DataPreprocessor class with the given parameters
  data_preprocessor = DataPreprocessor(
    data_file = './Raw_Data/data.json',
    output_file = './Preprocessed_Data/data.pkl',
    subword_vocab = SubwordTextEncoder('./Preprocessed_Data/subword_vocab.txt'),
    token_vocab = pickle.load(open('./Preprocessed_Data/token_vocab.dict', 'rb'))
  )

  # Preprocess the data and save it to a file
  data = data_preprocessor.preprocess_data()
  data_preprocessor.save_data(data)

# Call the main function
if __name__ == '__main__':
  main()
