from models.menu_option import MenuOption
from .functions import *
import sys


class Menu:
    def __init__(self, title, enable_go_back = True, enable_quit = True):
        self.title = title
        self.options = []
        self.final_options = []
        if enable_go_back:
            self.final_options.append(MenuOption("Go Back",keybindings= universal_go_back(), is_go_back = True))
        if enable_quit:
            self.final_options.append(MenuOption("Quit",keybindings= universal_quit(), is_quit = True))
        self.options_set = {}

    def run_option(self, option, selection):
        log('selection: ' + selection)
        log('running option')
        if option is not None:
            log('option is not None')
            if selection in universal_go_back() or option.is_go_back:
                log('selection in universal_go_back()')
                return True
            if selection in universal_quit() or option.is_quit:
                log('selection in universal_quit()')
                sys.exit()
            
            log('Running Option Function')
            option.run()
            return False

        else:
            log('invalid option')
            self.invalid_option()
            return False

    def add_option(self, option):
        self.options.append(option)

    def print_options(self):
        row = 1
        self.options_set = {}
        for option in self.options:
            print(f"{row.__str__()}. {option.__str__()}")
            option.option_id = row
            self.options_set[row] = option
            row += 1
        print()

    def get_option(self, key):
        for option in self.options:
            if option.match_key(key):
                return option
            if key.isdigit():
                if int(key) in self.options_set:
                    return self.options_set[int(key)]
        return None

    def invalid_option(self):
        print("You have made an invalid selection... Try Again")
        any_key()

    def show(self, auto_close = False):
        self.options += self.final_options
        while True:
            print_top(self.title)
            self.print_options()

            selection = input("Enter Selection: ")

            option = self.get_option(selection)

            if self.run_option(option, selection):
                return
            
            if auto_close:
                return

    def show_dynamic(self, menu_builder, inject = None, auto_close = False):
        
        while True:
            print_top(self.title)
            self.options = []
            menu_builder(self)
            self.options += self.final_options
            print_line()
            print()

            self.print_options()

            selection = input("Enter Selection: ")

            if selection in universal_go_back():
                return

            if selection in universal_quit():
                sys.exit()

            option = self.get_option(selection)

            
            if self.run_option(option, selection):
                return

    def show_only(self):
        self.options += self.final_options
        self.print_options()
        selection = input("Enter Selection: ")

        if selection in universal_go_back():
            return

        option = self.get_option(selection)

        if option is not None:
            option.run()
            return True
        else:
            self.invalid_option()
            return False
        
    def show_injected(self, injected, auto_close = False):
        self.options += self.final_options
        while True:
            print_top(self.title)
            
            injected()
            print_line()
            print()

            self.print_options()

            selection = input("Enter Selection: ")

            if selection in universal_go_back():
                return

            option = self.get_option(selection)

            if self.run_option(option, selection):
                return
            
            if auto_close:
                return
