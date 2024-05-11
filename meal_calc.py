from models.settings import Settings
from models.system import System
from models.functions import *

settings = Settings()
system = System(settings)

# Initial Instructor Message
print_top("Welcome to the Meal Cost Calculator")
print("This program is designed to help you calculate the cost of a meal at a restaurant.")
print("You can also track the cost of multiple meals and calculate the total cost of a meal.")
print("This system is configured with Auto Gratuity for large groups and a Tax Rate.")
print("You can adjust these settings and the pricing of the meals in the settings menu.")
print()
print("You gave me freedom over creativity, and I took it.  Please Enjoy! - Johnathon D Smith")
any_key()
system.load_initial()
