# Import the Flask library
from flask import Flask

# Import the event handlers module
from event_handlers import EventHandlers


# Define a class for creating the user interface
class UserInterface:

  # Initialize the class with the necessary attributes
  def __init__(self, app):
    self.app = app  # The Flask app object
    self.event_handlers = EventHandlers (app)  # The event handlers object

    # Define the routes and their corresponding methods
    self.app.route ('/') (self.event_handlers.home)
    self.app.route ('/login', methods=['POST']) (self.event_handlers.login)
    self.app.route ('/logout') (self.event_handlers.logout)
