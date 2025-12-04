from tkinter import *
import tkinter.messagebox 
import tkinter.messagebox as messagebox

# create the main window
root = Tk()
root.title("Enigma Machine Simulator")
root.geometry("1920x1000+0+0")

# create the functions
def reset():
    key_entry.delete(0, END)
    plaintext_text.delete(1.0, END)
    ciphertext_text.delete(1.0, END)
    decrypted_text.delete(1.0, END)

def iexit():
    iexit = tkinter.messagebox.askyesno("Enigma Machine Simulator", "Confirm if you want to exit")
    if iexit > 0:
        root.destroy()
        return

def xor_encrypt_decrypt(text,key):
    encrypted = ''.join(chr(ord(x) ^ key)for x in text)
    return encrypted

def encrypt():
    try:
        key = int(key_entry.get())
        plaintext = plaintext_text.get(1.0, END).strip()
        encrypted = xor_encrypt_decrypt(plaintext, key)
        ciphertext_text.delete(1.0, END)
        ciphertext_text.insert(END, encrypted)

    except Exception as e:
        messagebox.showerror('Error',str(e))

def decrypt():
    try:
        key = int(key_entry.get())
        ciphertext = ciphertext_text.get(1.0, END).strip()
        decrypted = xor_encrypt_decrypt(ciphertext, key)
        decrypted_text.delete(1.0, END)
        decrypted_text.insert(END, decrypted)

    except Exception as e:
        messagebox.showerror('Error',str(e))
        
# create widget
key_label = Label(root, font=('arial', 24, 'bold'), text="Enter Key:")
key_label.pack()

key_entry = Entry(root, font=('arial', 24, 'bold'), width = 50, justify = 'center')
key_entry.pack()
key_entry.focus()

# plaintext
plaintext_label = Label(root, font=('arial', 24, 'bold'), text="Enter Plaintext:")
plaintext_label.pack()

plaintext_text = Text(root, font=('arial', 24, 'bold'), height=5, width=80)
plaintext_text.pack()

# encrypt button
encrypt_button = Button(root, font=('arial', 24, 'bold'), width=10 , text="Encrypt",command=encrypt)
encrypt_button.pack()

# ciphertext
ciphertext_label = Label(root, font=('arial', 24, 'bold'), text="Enter Ciphertext:")
ciphertext_label.pack()


ciphertext_text = Text(root, font=('arial', 24, 'bold'), height=5, width=80)
ciphertext_text.pack()

# decrypt button
decrypt_button = Button(root, font=('arial', 24, 'bold'), width=10 , text="Decrypt",command=decrypt)
decrypt_button.pack()

# decrypted text
decrypted_label = Label(root, font=('arial', 24, 'bold'), text="Enter Decrypted Text:")
decrypted_label.pack()

decrypted_text = Text(root, font=('arial', 24, 'bold'), height=5, width=80)
decrypted_text.pack()

# frame for reset and exit buttons
button_frame = Frame(root)
button_frame.pack()
# reset button
reset_button = Button(button_frame, font=('arial', 24, 'bold'), width=10 , text="Reset",command=reset)
reset_button.pack(side=LEFT, padx=10)
# exit button   
exit_button = Button(button_frame, font=('arial', 24, 'bold'), width=10 , text="Exit", command=iexit)
exit_button.pack(side=RIGHT, padx=10)
root.mainloop()



