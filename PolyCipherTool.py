import tkinter as tk


def polybius_cipher(text, mode):
    # Define the Polybius Square
    polybius_square = {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
        'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
        'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
        'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
    }
    # Remove spaces and convert to upper case
    text = ''.join(text.upper().split())
    # Encrypt or Decrypt the text
    result = ''
    for char in text:
        if char in polybius_square:
            if mode == 'encrypt':
                result += polybius_square[char]
            else:
                # Find the corresponding letter in the square
                for key, value in polybius_square.items():
                    if value == char:
                        result += key
        else:
            result += char
    return result

def PolyCipherCommand():
    def encrypt():
        input_text = input_box.get('1.0', 'end-1c')
        output_box.delete('1.0', 'end')
        output_box.insert('1.0', polybius_cipher(input_text, 'encrypt'))
    
    def decrypt():
        input_text = input_box.get('1.0', 'end-1c')
        output_box.delete('1.0', 'end')
        output_box.insert('1.0', polybius_cipher(input_text, 'decrypt'))
    
    root = tk.Tk()
    root.title('Polybius Square Cipher')
    root.configure(background='white')
    
    input_label = tk.Label(root, text='Enter Text:', bg='white')
    input_label.grid(row=0, column=0, padx=5, pady=5)
    input_box = tk.Text(root, height=5, width=50, bg='white')
    input_box.grid(row=0, column=1, padx=5, pady=5)
    
    encrypt_button = tk.Button(root, text='Encrypt', command=encrypt, bg='white')
    encrypt_button.grid(row=1, column=0, padx=5, pady=5)
    decrypt_button = tk.Button(root, text='Decrypt', command=decrypt, bg='white')
    decrypt_button.grid(row=1, column=1, padx=5, pady=5)
    
    output_label = tk.Label(root, text='Result:', bg='white')
    output_label.grid(row=2, column=0, padx=5, pady=5)
    output_box = tk.Text(root, height=5, width=50, bg='white')
    output_box.grid(row=2, column=1, padx=5, pady=5)
    
    root.mainloop()
