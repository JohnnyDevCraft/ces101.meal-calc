from .functions import *
from .meal_ticket import MealTicket
from .menu import Menu
from .menu_option import MenuOption


class System:
    def __init__(self, settings):
        self.settings = settings
        self.tickets = []
        self.closed_tickets = []
        self.running = True
        self.menus = {}
        self.setup_menus()

    def setup_menus(self):
        self.menus["main"] = Menu("Main Menu", enable_go_back= False)
        self.menus["settings"] = Menu("System Settings")

        self.menus["main"].add_option(
            MenuOption("System Settings", function= self.settings.show_menu)
        )
        self.menus["main"].add_option(
            MenuOption("Add New Ticket", function= self.add_ticket)
        )
        self.menus["main"].add_option(
            MenuOption("View Active Tickets", function= self.view_active_tickets)
        )
    

    def load_initial(self):
        while self.running:
            self.menus["main"].show()

    def add_ticket(self):
        ticket = MealTicket(self.settings)
        self.tickets.append(ticket)

    def view_active_tickets(self):
        menu = Menu("Active Tickets", enable_go_back= True, enable_quit= False)
        menu.show_dynamic(self.build_active_tickets_menu)

    def view_ticket(self, ticket):
        ticket.show_menu()

    def build_active_tickets_menu(self, menu):
        for ticket in self.tickets:
            menu.add_option(MenuOption(ticket.simple_str(), function= self.view_ticket, fn_data= ticket))
        menu.add_option(MenuOption("Add Ticket", function= self.add_ticket))

    def view_tickets(self):
        selection = self.printer.show_all_tickets(self.tickets)
        if selection not in ["E", "e"]:
            item = filter_array_by_id(self.tickets, int(selection))
            print("ticket selected: ")
            self.view_ticket(item)
