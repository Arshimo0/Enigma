import customtkinter as ctk
from tkinter import messagebox
from logic import CipherLogic  # <--- IMPORTING YOUR OTHER FILE

# Appearance Settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class EnigmaApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Connect to the Logic file
        self.logic = CipherLogic()

        # Window Setup
        self.title("Enigma Project")
        self.geometry("600x500")

        self.create_ui()

    def create_ui(self):
        # 1. Title
        self.label = ctk.CTkLabel(self, text="Secret Message System", font=("Arial", 24, "bold"))
        self.label.pack(pady=20)

        # 2. Key Input
        self.key_entry = ctk.CTkEntry(self, placeholder_text="Enter Numeric Key (e.g. 123)")
        self.key_entry.pack(pady=10)

        # 3. Text Input Area
        self.input_label = ctk.CTkLabel(self, text="Enter Text:")
        self.input_label.pack()
        
        self.text_area = ctk.CTkTextbox(self, height=150)
        self.text_area.pack(padx=20, pady=5, fill="x")

        # 4. Button
        self.btn = ctk.CTkButton(self, text="Encrypt / Decrypt", command=self.run_cipher)
        self.btn.pack(pady=20)

        # 5. Result Area
        self.result_label = ctk.CTkLabel(self, text="Result:")
        self.result_label.pack()

        self.result_area = ctk.CTkTextbox(self, height=150)
        self.result_area.pack(padx=20, pady=5, fill="x")

        # 6. Bottom Buttons Frame (to keep them side-by-side)
        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.pack(pady=10)

        # Reset Button (Gray color)
        self.btn_reset = ctk.CTkButton(self.bottom_frame, text="Reset", command=self.reset_fields)
        self.btn_reset.pack(side="left", padx=10)

        # Exit Button (Red color)
        self.btn_exit = ctk.CTkButton(self.bottom_frame, text="Exit", command=self.exit_app) 
        self.btn_exit.pack(side="left", padx=10)

    def run_cipher(self):
        key = self.key_entry.get()
        text = self.text_area.get("1.0", "end-1c")

        result = self.logic.process_text(text, key)

        if result is None:
            messagebox.showerror("Error", "Key must be a number!")
        else:
            self.result_area.delete("1.0", "end") 
            self.result_area.insert("1.0", result)
             
    def reset_fields(self):
        # Clear the Key entry
        self.key_entry.delete(0, "end")
        # Clear the Text Input
        self.text_area.delete("1.0", "end")
        # Clear the Result Input
        self.result_area.delete("1.0", "end")

    def exit_app(self):
        # Ask for confirmation
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            self.destroy()
if __name__ == "__main__":
    app = EnigmaApp()
    app.mainloop()