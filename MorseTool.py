import tkinter as tk

# Morse Code dictionary
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def morse_code_cipher(text, mode):
    if mode == 'encrypt':
        cipher_text = ''
        for letter in text:
            if letter != ' ':
                cipher_text += MORSE_CODE_DICT[letter.upper()] + ' '
            else:
                cipher_text += ' '
        return cipher_text
    
    elif mode == 'decrypt':
        text += ' '
        decipher_text = ''
        citext = ''
        for letter in text:
            if letter != ' ':
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher_text += ' '
                else:
                    decipher_text += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                    citext = ''
        return decipher_text


def MorseCommand():
    def encrypt():
        input_text = input_box.get('1.0', 'end-1c')
        output_box.delete('1.0', 'end')
        output_box.insert('1.0', morse_code_cipher(input_text, 'encrypt'))
    
    def decrypt():
        input_text = input_box.get('1.0', 'end-1c')
        output_box.delete('1.0', 'end')
        output_box.insert('1.0', morse_code_cipher(input_text, 'decrypt'))
    
    root = tk.Tk()
    root.title('Morse Code Cipher')
    
    input_label = tk.Label(root, text='Enter Text:', bg='white')
    input_label.grid(row=0, column=0, padx=5, pady=5)
    input_box = tk.Text(root, height=5, width=50, bg='white')
    input_box.grid(row=0, column=1, padx=5, pady=5)
    
    encrypt_button = tk.Button(root, text='Encrypt', command=encrypt)
    encrypt_button.grid(row=1, column=0, padx=5, pady=5)
    decrypt_button = tk.Button(root, text='Decrypt', command=decrypt)
    decrypt_button.grid(row=1, column=1, padx=5, pady=5)
    
    output_label = tk.Label(root, text='Result:', bg='white')
    output_label.grid(row=2, column=0, padx=5, pady=5)
    output_box = tk.Text(root, height=5, width=50, bg='white')
    output_box.grid(row=2, column=1, padx=5, pady=5)
    
    root.mainloop()