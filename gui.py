import string
import customtkinter as ctk

from alert import AlertApp
from password import PasswordGenerator

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Initialize instances
        self.alert = AlertApp()
        self.password = PasswordGenerator()

        # Configure window
        self.width = 1000
        self.height = 600

        self.title("Key Guardian")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # Generating a sidebar and its elements
        self.sidebar = ctk.CTkFrame(
            self,
            width=200,
            height=self.height,
            corner_radius=0,
        )
        self.sidebar.pack_propagate(False)
        self.sidebar.pack(side="left")

        self.greeting_text = ctk.CTkLabel(
            self.sidebar,
            text="Key Guardian",
            font=ctk.CTkFont(size=20, weight="bold"),
        )
        self.greeting_text.pack(pady=(15, 0))

        self.slogan_text = ctk.CTkLabel(
            self.sidebar,
            text="Let us guard you through the internet",
            font=ctk.CTkFont(size=10)
        )
        self.slogan_text.pack(pady=(0, 50))

        self.appearance_option = ctk.CTkOptionMenu(
            self.sidebar,
            values=["System", "Light", "Dark"],
            command=self.change_appearance
        )
        self.appearance_option.pack(side="bottom", pady=(0, 25))

        self.appearance_text = ctk.CTkLabel(
            self.sidebar,
            text="Change background color",
            font=ctk.CTkFont(size=12)
        )
        self.appearance_text.pack(side="bottom")

        # Generating the elements for configuring the password
        self.configure_text = ctk.CTkLabel(
            self,
            text="Let's configure your password!",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.configure_text.pack(pady=(50, 15))

        self.frame_button = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_button.columnconfigure(0, weight=1)
        self.frame_button.columnconfigure(1, weight=1)

        self.lowercase_button = ctk.CTkButton(
            self.frame_button,
            width=200,
            text="Toggle lowercase letters",
            font=ctk.CTkFont(size=12),
            command=lambda: self.change_characters("lowercase")
        )
        self.lowercase_button.grid(row=0, column=0, padx=10, pady=10)

        self.uppercase_button = ctk.CTkButton(
            self.frame_button,
            width=200,
            text="Toggle uppercase letters",
            font=ctk.CTkFont(size=12),
            command=lambda: self.change_characters("uppercase")
        )
        self.uppercase_button.grid(row=0, column=1, padx=10, pady=10)

        self.numbers_button = ctk.CTkButton(
            self.frame_button,
            width=200,
            text="Toggle numbers",
            font=ctk.CTkFont(size=12),
            command=lambda: self.change_characters("numbers")
        )
        self.numbers_button.grid(row=1, column=0, padx=10, pady=10)

        self.symbols_button = ctk.CTkButton(
            self.frame_button,
            width=200,
            text="Toggle symbols",
            font=ctk.CTkFont(size=12),
            command=lambda: self.change_characters("symbols")
        )
        self.symbols_button.grid(row=1, column=1, padx=10, pady=10)

        self.frame_button.pack()

        self.configuration_text = ctk.CTkLabel(
            self,
            text="This is your password configuration:",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.configuration_text.pack(pady=(25, 10))

        self.configuration_lowercase_text = ctk.CTkLabel(
            self,
            width=300,
            fg_color="green",
            corner_radius=10,
            text="Lowercase is ENABLED",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.configuration_lowercase_text.pack(pady=5)

        self.configuration_uppercase_text = ctk.CTkLabel(
            self,
            width=300,
            fg_color="green",
            corner_radius=10,
            text="Uppercase is ENABLED",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.configuration_uppercase_text.pack(pady=5)

        self.configuration_numbers_text = ctk.CTkLabel(
            self,
            width=300,
            fg_color="green",
            corner_radius=10,
            text="Numbers is ENABLED",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.configuration_numbers_text.pack(pady=5)

        self.configuration_symbols_text = ctk.CTkLabel(
            self,
            width=300,
            fg_color="green",
            corner_radius=10,
            text="Symbols is ENABLED",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.configuration_symbols_text.pack(pady=5)

        self.length_text = ctk.CTkLabel(
            self,
            text="Set your password length (15)",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.length_text.pack(pady=(25, 15))

        self.length_slider = ctk.CTkSlider(
            self,
            width=300,
            orientation="horizontal",
            from_=8,
            to=60,
            number_of_steps=52,
            command=self.set_password_length
        )
        self.length_slider.pack()

        # Generating elements for password actions
        self.password_frame = ctk.CTkFrame(
            self,
            width=650,
            height=40,
            corner_radius=10
        )
        self.password_frame.pack_propagate(False)
        self.password_frame.pack(side="bottom", padx=10, pady=10)

        self.check_password_button = ctk.CTkButton(
            self.password_frame,
            width=160,
            height=30,
            corner_radius=10,
            text="Check strength",
            command=self.get_password_strength
        )
        self.check_password_button.pack(side="left", padx=5, pady=5)

        self.password_entry = ctk.CTkEntry(
            self.password_frame,
            width=300,
            height=30,
            corner_radius=10,
            justify="center",
            placeholder_text="Your password will be displayed here!"
        )
        self.password_entry.pack(side="left", padx=5, pady=5)

        self.generate_password_button = ctk.CTkButton(
            self.password_frame,
            width=160,
            height=30,
            corner_radius=10,
            text="Generate password",
            command=self.get_password_value
        )
        self.generate_password_button.pack(side="left", padx=5, pady=5)

        self.mainloop()

    # Function for changing the appearance ~ light, dark or system
    @staticmethod
    def change_appearance(new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_characters(self, target):
        target_name = (
            string.ascii_lowercase if target == "lowercase" else
            string.ascii_uppercase if target == "uppercase" else
            string.digits if target == "numbers" else
            string.punctuation
        )

        self.password.check_character(target_name)
        self.change_characters_status(target)

    def change_characters_status(self, target):
        element_name = f"configuration_{target}_text"
        element = getattr(self, element_name, None)

        if element:
            current_color = element.cget("fg_color")
            new_color = "red" if current_color == "green" else "green"
            new_text = f"{target.capitalize()} is DISABLED" if current_color == "green" else f"{target.capitalize()} is ENABLED"
            element.configure(fg_color=new_color)
            element.configure(text=new_text)

    # Function for setting the length of the password
    def set_password_length(self, value):
        self.length_text.configure(text=f"Set your password length ({int(value):02d})")
        self.password.change_length(int(value))

    # Function for generating the password
    def get_password_value(self):
        self.password.generate_password()
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, self.password.password)

    # Function for checking the password strength and adding the toplevel window
    def get_password_strength(self):
        if self.password_entry.get():
            password = self.password_entry.get()
        else:
            password = ""

        self.password.check_password(password)
