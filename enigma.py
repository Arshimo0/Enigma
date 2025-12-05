from tkinter import *
import tkinter.messagebox as messagebox

class EnigmaLogic:
    @staticmethod
    def process_text(text, key):
        if not key.isdigit():
            raise ValueError("Key must be a number")
        
        key_int = int(key)
        return ''.join(chr(ord(x) ^ key_int) for x in text)

if __name__ == "__main__":
    print("Logic module loaded. UI pending.")