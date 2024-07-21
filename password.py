import secrets
import string
import math

from alert import AlertApp


class PasswordGenerator:
    def __init__(self):

        # Initialize instances
        self.alert = AlertApp()

        # Initialize important variables
        self.length = 15
        self.characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        self.password = ""

        self.possibilities = 0
        self.hacker_makes_guesses = 1E9  # Standard computers can take billions of actions per second

    def check_character(self, target):
        if target in self.characters:
            self.remove_character(target)
        else:
            self.add_character(target)

    # Function for adding certain strings to the character variable
    def add_character(self, target):
        self.characters += target

    # Function for removing certain strings of the character variable
    def remove_character(self, target):
        for x in target:
            self.characters = self.characters.replace(x, "")

    # Function for overriding the length variable with our slider value
    def change_length(self, length):
        self.length = length

    # Function for generating a password based on the character variable
    def generate_password(self):
        self.password = "".join(secrets.choice(self.characters) for _ in
                                range(self.length)) if self.characters else "No characters selected."

    # Function for analysing the strength of the password
    def check_password(self, password):
        if password and self.password != "No characters selected.":
            password_estimation_string = self.check_password_hack_time(password)
            password_status_string = self.check_password_status()

            self.alert.update_label_status(password_status_string)
            self.alert.update_label_estimation(password_estimation_string)

        else:
            self.alert.update_label_status("No password found in input field.")
            self.alert.update_label_estimation("")

        self.alert.show_self()

    # Function for checking your password based on the password entropy bits
    def check_password_status(self):
        password_status = (
            "nearly unhackable" if self.possibilities > 125 else
            "very strong" if self.possibilities > 100 else
            "strong" if self.possibilities > 75 else
            "good" if self.possibilities > 50 else
            "weak" if self.possibilities < 30 else
            "very weak" if self.possibilities < 15 else
            "nearly not existent"
        )

        return f"Your password is {password_status}."

    # Function for calculating how long it will take for brute forcing the password
    def check_password_hack_time(self, password):
        lowercase = any(char in string.ascii_lowercase for char in password)
        uppercase = any(char in string.ascii_uppercase for char in password)
        numbers = any(char in string.digits for char in password)
        symbols = any(char in string.punctuation for char in password)

        exponent = (lowercase + uppercase) * 26 + numbers * 10 + symbols * 32

        # This function is the basic calculation of password entropy
        possibilities_in_bits = len(password) * math.log2(exponent)

        # A hacker normally needs so many guesses based on the bit amount
        hacker_needs_guesses = 2 ** (possibilities_in_bits - 1)

        # This is the formula for a hacker which makes one billion guesses per second
        time_to_hack_s = hacker_needs_guesses / self.hacker_makes_guesses

        time_to_hack_y = time_to_hack_s // (60 * 60 * 24 * 365)
        time_to_hack_d = time_to_hack_s // (60 * 60 * 24)
        time_to_hack_h = time_to_hack_s // (60 * 60)
        time_to_hack_m = time_to_hack_s // 60

        time_to_hack = (
            (time_to_hack_y, "year") if time_to_hack_y > 0 else
            (time_to_hack_d, "day") if time_to_hack_d > 0 else
            (time_to_hack_h, "hour") if time_to_hack_h > 0 else
            (time_to_hack_m, "minute") if time_to_hack_m > 0 else
            (time_to_hack_s, "second")
        )

        time_value = "{:.2e}".format(time_to_hack[0]) if time_to_hack[0] > 100000 else "{:.0f}".format(time_to_hack[0])
        time_unit = time_to_hack[1] if time_value == "1" else time_to_hack[1] + "s"

        # Making the possibilities variable global
        self.possibilities = possibilities_in_bits

        return f"It takes {time_value} {time_unit} for a hacker to crack your password."
