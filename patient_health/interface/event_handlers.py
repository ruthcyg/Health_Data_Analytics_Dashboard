# Import the Flask library
from flask import Flask

# Import the request and session objects
from flask import request, session

# Import the render_template and redirect functions
from flask import render_template, redirect

# Import the flash function
from flask import flash


# Define a class for handling events
class EventHandlers:

  # Initialize the class with the necessary attributes
  def __init__(self, app):
    self.app = app  # The Flask app object

  # Define a method to handle the home route
  def home(self):
    # Check if the user is logged in
    if not session.get ('logged_in'):
      # Render the login template
      return render_template ('login.html')
    else:
      # Render the home template
      return render_template ('home.html')

  # Define a method to handle the login route
  def login(self):
    # Check if the request method is POST
    if request.method == 'POST':
      # Get the username and password from the form
      username = request.form ['username']
      password = request.form ['password']

      # Validate the username and password
      if username == 'admin' and password == 'password':
        # Set the session variable to True
        session ['logged_in'] = True

        # Redirect to the home route
        return redirect ('/')
      else:
        # Flash an error message
        flash ('Invalid credentials!')

        # Redirect to the home route
        return redirect ('/')
    else:
      # Redirect to the home route
      return redirect ('/')

  # Define a method to handle the logout route
  def logout(self):
    # Clear the session variable
    session.clear ()

    # Flash a success message
    flash ('You have logged out!')

    # Redirect to the home route
    return redirect ('/')
