from models.menu import Menu
from models.menu_option import MenuOption
from .functions import *

class Settings:
    def __init__(self):
        self.auto_gratuity_limit = 8
        self.auto_gratuity_rate = 0.15
        self.tax_rate = 0.06725
        self.child_price = 6.99
        self.adult_price = 12.99
        self.next_ticket_id = 0

    def update_auto_gratuity(self):
        print_top("Update Auto Gratuity Settings")

        limit = get_int_input("Enter new Auto Gratuity Limit: ")
        rate = get_float_input("Enter new Auto Gratuity Rate: ")
        self.auto_gratuity_rate = rate / 100
        self.auto_gratuity_limit = limit

        print("Auto Gratuity Settings Updated")
        any_key()

    def show_menu(self):
        menu = Menu("Settings Menu")
        menu.add_option(MenuOption("Update Auto Gratuity", function = self.update_auto_gratuity))
        menu.add_option(MenuOption("Update Tax Rate", function = self.update_tax_rate))
        menu.add_option(MenuOption("Update Pricing", function = self.update_pricing))
        menu.add_option(MenuOption("Print Settings", function = self.print_out_settings))
        menu.show_injected(self.print_out_settings)


    def update_tax_rate(self):
        print_top("Update Tax Rate")
        rate = get_float_input("Enter new Tax Rate: ")
        self.tax_rate = rate / 100
        print("Tax Rate Updated")
        any_key()

    def update_pricing(self):
        print_top("Update Pricing")
        adult_price = get_float_input("Enter new Adult Price: ")
        child_price = get_float_input("Enter new Child Price: ")
        self.adult_price = adult_price
        self.child_price = child_price
        print("Pricing Updated")
        any_key()

    def print_out_settings(self):
        print(f"Auto Gratuity Limit: {self.auto_gratuity_limit}")
        print(f"Auto Gratuity Rate: {self.auto_gratuity_rate * 100:.4f}%")
        print(f"Tax Rate: {self.tax_rate * 100:.4f}%")
        print(f"Child Price: ${self.child_price: .2f}")
        print(f"Adult Price: ${self.adult_price: .2f}")
