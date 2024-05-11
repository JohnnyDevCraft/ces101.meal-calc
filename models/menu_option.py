from os import error

from .functions import *


class MenuOption:

    def __init__(self, text, option_id = 0, keybindings = [], function = None, fn_data = None, is_quit = False, is_go_back = False):
        valid_keys = True

        for key in keybindings:
            if key in reserved_keys():
                valid_keys = False

        if not callable(function) and function is not None:
            raise ValueError("You did not pass a valid function in for the Menu Option")

        self.text = text
        self.keybindings = keybindings
        self.function = function
        self.fn_data = fn_data
        self.is_quit = is_quit
        self.is_go_back = is_go_back

    def run(self):
        if self.function is not None:
            if self.fn_data is not None:
                self.function(self.fn_data)
            else:
                self.function()

    def match_key(self, key):
        if key.isdigit():
            if int(key) == self.option_id:
                return True
        return key in self.keybindings

    def __str__(self):
        if len(self.keybindings) > 0:
            keys = ", ".join(self.keybindings)
            return f"{self.text}: ({keys}) "
        
        return f"{self.text}"

    def print(self):
        print(self.__str__())
