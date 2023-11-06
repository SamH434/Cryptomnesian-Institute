import tkinter as tk


def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts text using the Caesar Cipher with a specified shift value
    """
    shifted_text = ""
    for char in text:
        if char.isalpha():
            if direction == 'encrypt':
                shifted_text += chr((ord(char) + shift - 65) % 26 + 65)
            elif direction == 'decrypt':
                shifted_text += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            shifted_text += char
    return shifted_text

def CaesarCommand():
    def submit():
        input_text = input_box.get('1.0', 'end-1c')
        shift = int(shift_box.get())
        direction = mode.get()
        output_box.delete('1.0', 'end')
        output_box.insert('1.0', caesar_cipher(input_text, shift, direction))
    
    root = tk.Tk()
    root.title('Caesar Cipher')
    root.configure(background='white')
    
    input_label = tk.Label(root, text='Enter Text:', bg='white')
    input_label.grid(row=0, column=0, padx=5, pady=5)
    input_box = tk.Text(root, height=5, width=50, bg='white')
    input_box.grid(row=0, column=1, padx=5, pady=5)
    
    shift_label = tk.Label(root, text='Shift Amount:')
    shift_label.grid(row=1, column=0, padx=5, pady=5)
    shift_box = tk.Entry(root, width=10)
    shift_box.grid(row=1, column=1, padx=5, pady=5)
    
    mode_label = tk.Label(root, text='Select Mode:')
    mode_label.grid(row=2, column=0, padx=5, pady=5)
    mode = tk.StringVar(value='encrypt')
    encrypt_radio = tk.Radiobutton(root, text='Encrypt', variable=mode, value='encrypt')
    encrypt_radio.grid(row=2, column=1, padx=5, pady=5)
    decrypt_radio = tk.Radiobutton(root, text='Decrypt', variable=mode, value='decrypt')
    decrypt_radio.grid(row=2, column=2, padx=5, pady=5)
    
    submit_button = tk.Button(root, text='Submit', command=submit)
    submit_button.grid(row=3, column=1, padx=5, pady=5)
    
    output_label = tk.Label(root, text='Result:')
    output_label.grid(row=4, column=0, padx=5, pady=5)
    output_box = tk.Text(root, height=5, width=50)
    output_box.grid(row=4, column=1, padx=5, pady=5)
    
    root.mainloop()
