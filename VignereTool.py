import tkinter as tk


# Vignere cipher function for encryption and decryption
def vignere_cipher(text, key, mode):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - 97
            if mode == "encrypt":
                result += chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char.lower()) - 97 - shift) % 26 + 97)
            key_index += 1
        else:
            result += char
    return result


# GUI for Vignere Cipher
def VignereCommand():
    def encrypt():
        input_text = input_box.get('1.0', 'end-1c')
        key_text = key_box.get('1.0', 'end-1c')
        output_box.delete('1.0', 'end')
        output_box.insert('1.0', vignere_cipher(input_text, key_text, 'encrypt'))
    
    def decrypt():
        input_text = input_box.get('1.0', 'end-1c')
        key_text = key_box.get('1.0', 'end-1c')
        output_box.delete('1.0', 'end')
        output_box.insert('1.0', vignere_cipher(input_text, key_text, 'decrypt'))
    
    root = tk.Tk()
    root.title('Vignere Cipher')

    root.configure(bg='white')

    input_label = tk.Label(root, text='Enter Text:', bg='white')
    input_label.grid(row=0, column=0, padx=5, pady=5)
    input_box = tk.Text(root, height=5, width=50, bg='white')
    input_box.grid(row=0, column=1, padx=5, pady=5)
    
    key_label = tk.Label(root, text='Enter Key:', bg='white')
    key_label.grid(row=1, column=0, padx=5, pady=5)
    key_box = tk.Text(root, height=1, width=25, bg='white')
    key_box.grid(row=1, column=1, padx=5, pady=5)

    encrypt_button = tk.Button(root, text='Encrypt', command=encrypt, bg='white')
    encrypt_button.grid(row=2, column=0, padx=5, pady=5)
    decrypt_button = tk.Button(root, text='Decrypt', command=decrypt, bg='white')
    decrypt_button.grid(row=2, column=1, padx=5, pady=5)
    
    output_label = tk.Label(root, text='Result:', bg='white')
    output_label.grid(row=3, column=0, padx=5, pady=5)
    output_box = tk.Text(root, height=5, width=50, bg='white')
    output_box.grid(row=3, column=1, padx=5, pady=5)
    
    root.mainloop()
