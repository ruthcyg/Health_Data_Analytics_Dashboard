# Import the Flask library
from flask import Flask

# Import the user interface module
from user_interface import UserInterface

# Create an instance of the Flask class
app = Flask (__name__)

# Create an instance of the UserInterface class
ui = UserInterface (app)


# Define the main function
def main():
  # Run the Flask app
  app.run (host='0.0.0.0', port=4000)


# Call the main function
if __name__ == '__main__':
  main()
