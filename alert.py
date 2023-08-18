import customtkinter as ctk


class AlertApp:
    def __init__(self):
        self.alert_window = ctk.CTkToplevel(
            width=400,
            height=200,
        )

        self.alert_window.title("Strength Meter")
        self.alert_window.pack_propagate(False)
        self.alert_window.resizable(False, False)
        self.alert_window.withdraw()

        self.label_status = ctk.CTkLabel(
            self.alert_window,
            text="",
            font=ctk.CTkFont(size=16)
        )
        self.label_status.pack(pady=(70, 0))

        self.label_estimation = ctk.CTkLabel(
            self.alert_window,
            text="",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.label_estimation.pack()

    def show_self(self):
        self.alert_window.deiconify()
        self.alert_window.protocol("WM_DELETE_WINDOW", self.hide_self)

    def hide_self(self):
        self.alert_window.withdraw()

    def update_label_status(self, updated_text):
        self.label_status.configure(text=updated_text)

    def update_label_estimation(self, updated_text):
        self.label_estimation.configure(text=updated_text)
