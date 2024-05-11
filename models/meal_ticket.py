from .functions import *
from .menu import Menu
from .menu_option import MenuOption


class MealTicket:
    def __init__(self, settings):
        print_top("Create new Ticket")
        self.child_count = get_int_input("How many children are there? ")
        self.adult_count = get_int_input("How many adults are there? ")
        self.child_total = 0.00
        self.adult_total = 0.00
        self.gratuity = 0.00
        self.gratuity_override = 0.00
        self.settings = settings
        self.settings.next_ticket_id += 1
        self.id = self.settings.next_ticket_id
        self.payment_amount = 0.00
        self.change_due = 0.00
        self.paid = False

    def print_ticket(self):
        if self.paid:
            print_top(f"Ticket Detail: {self.id} :: Paid in Full :: Change Due: ${self.change_due:.2f} / Payment Amount: ${self.payment_amount:.2f}")
        else:
            print_top(f"Ticket Detail: {self.id} :: Unpaid")

        print(f"Child Count: {self.child_count}")
        print(f"Adult Count: {self.adult_count}")

        if self.should_charge_auto_gratuity():
            print(f"Gratuity is required for this ticket.")

        print()
        print()
        print_title(f"Receipt: {self.id}")
        print(f"Sub Total: ${self.calc_sub_total():.2f}")
        print(f"Tax Amount: ${self.calc_tax():.2f}")
        print(f"Gratuity: ${self.get_gratuity():.2f}")
        print(f"Total: ${self.calc_grand_total():.2f}")
        if self.paid:
            print_line()            
            print(f'Total Paid: ${self.payment_amount:.2f}')
            print(f'Change Due: ${self.change_due:.2f}')
            print_line()
            print()

    def show_menu(self):
        menu = Menu("Ticket Detail Menu")

        if not self.paid:
            menu.add_option(MenuOption("Pay Ticket", function = self.pay_ticket))
            menu.add_option(MenuOption("Add Children", function = self.add_children))
            menu.add_option(MenuOption("Add Adult", function = self.add_adults))
            menu.add_option(MenuOption("Add Gratuity", function = self.add_gratuity))
       
        menu.show_injected(self.print_ticket, True)

    def pay_ticket(self):
        print_top(f"Pay Ticket: {self.id}")
        print()
        print(f"Total: ${self.calc_grand_total():.2f}")
        print()

        # Ask to add gratuity
        if self.should_charge_auto_gratuity():
            print(f"Gratuity is required for this ticket.")
            print()
            print(f"Total with Gratuity: ${self.calc_grand_total(): .2f}")
            print()
        else:
            take_gratuity = get_bool_input("Would you like to add Gratuity? (Y/N): ")

            if take_gratuity:
                print('Adding Gratuity')
                any_key()
                self.add_gratuity()
                print(f'Total with Gratuity: ${self.calc_grand_total():.2f}')

        amount = get_float_input("Enter Payment Amount: $")

        if amount >= self.calc_grand_total():
            self.payment_amount = amount
            self.change_due = amount - self.calc_grand_total()
            self.paid = True
            self.print_ticket()
            print("Payment Accepted")
            any_key()
        else:
            print("Insufficient Funds")
            any_key()

    def calc_sub_total(self):
        self.child_total = self.child_count * self.settings.child_price
        self.adult_total = self.adult_count * self.settings.adult_price
        return self.child_total + self.adult_total

    def calc_tax(self):
        return self.calc_sub_total() * self.settings.tax_rate

    def add_gratuity(self):
        while True:
            type_of_grat = input(
                "Would you like to use Total Ticket (T), Percentage (P), or Exact Amount(E): "
            )
            if type_of_grat in {"t", "T"}:
                amount = float(
                    input(
                        f"Enter total amount for ticket: (Must be greater than ${self.calc_grand_total():.2f})"
                    )
                )
                if amount > self.calc_total_with_tax():
                    self.gratuity_override = amount - self.calc_total_with_tax()
                    return
            if type_of_grat in {"p", "P"}:
                amount = get_float_input("Enter Gratuity Percentage %: ") / 100
                self.gratuity_override = amount * self.calc_sub_total()
                return
            if type_of_grat in {"E", "e"}:
                self.gratuity_override = get_float_input("Enter Gratuity Amount: $")
                return
            print("You have entered an invalid value... Try Again")
            any_key()

        self.gratuity = gratuity

    def get_gratuity(self):
        if self.should_charge_auto_gratuity():
            auto_gratuity = self.get_auto_gratuity_amount()
            if auto_gratuity > self.gratuity_override:
                return auto_gratuity
            else:
                return self.gratuity_override
        else:
            return self.gratuity_override

    def get_auto_gratuity_amount(self):
        return self.calc_sub_total() * self.settings.auto_gratuity_rate

    def calc_grand_total(self):
        return self.calc_sub_total() + self.calc_tax() + self.get_gratuity()

    def calc_total_with_tax(self):
        return self.calc_sub_total() + self.calc_tax()

    def should_charge_auto_gratuity(self):
        return (
            self.adult_count + self.child_count
        ) >= self.settings.auto_gratuity_limit

    def add_children(self):
        print_top(f"Add Children to Ticket {self.id}")
        print()
        count = get_int_input("Enter whole number.  Negative Numbers will be subtracted: ")
        count += self.child_count

        if count > 0:
            self.child_count = count
        else:
            print("Invalid Value results in negative count.")
            any_key()

    def add_adults(self):
        print_top(f"Add adults to Ticket {self.id}")
        print()
        count = get_int_input("Enter whole number.  Negative Numbers will be subtracted: ")
        count += self.adult_count
        if count > 0:
            self.adult_count = count
        else:
            print("Invalid value results in negative count.")
            any_key()

    def simple_str(self):
        if self.paid:
            return f"(PAID) Ticket ID: {self.id}, Paid: ${self.payment_amount:.2f}, Change: ${self.change_due:.2f}"
        return f"(UNPAID) Ticket ID: {self.id}, Children: {self.child_count}, Adults: {self.adult_count}, Gratuity: ${self.get_gratuity(): .2f}, Total: ${self.calc_grand_total(): .2f}"
