import tkinter as tk


def TombCommand():
    # Define variables
    attempts = 0
    password = "the ships never came"
    
    # Define functions
    def check_password():
        nonlocal attempts
        if entry.get().lower() == password:
            result_label.config(text="System 00")
        else:
            attempts += 1
            if attempts == 1:
                counter_label.config(text="[]")
            elif attempts == 2:
                counter_label.config(text="[] []")
            elif attempts == 3:
                counter_label.config(text="[] [] []")
            elif attempts == 4:
                counter_label.config(text="[] [] [] []")
                root.after(1000, root.destroy)
            result_label.config(text="Rejected")
            entry.delete(0, tk.END)
    
    # Create GUI window
    root = tk.Tk()
    root.title("Site B-7")
    root.geometry("400x300")
    root.config(bg="tan")
    
    # Create widgets
    title_label = tk.Label(root, text="[ Tomb B-7 ]", font=("Arial", 24, "bold"), bg="tan")
    title_label.pack(pady=20)
    
    paragraph_label = tk.Label(root, text="Why Brutus? I have yet to see the thirteen thousand army.", font=("Arial", 12), bg="tan")
    paragraph_label.pack(pady=10)
    paragraph_label1 = tk.Label(root, text="GUR FUVCF ARIRE PNZR", font=("Arial", 9), bg="tan")
    paragraph_label1.pack(pady=10)
    
    
    entry = tk.Entry(root, width=20)
    entry.pack(pady=10)
    
    check_button = tk.Button(root, text="Check", command=check_password)
    check_button.pack(pady=10)
    
    result_label = tk.Label(root, text="", font=("Arial", 12), bg="tan")
    result_label.pack()
    
    counter_label = tk.Label(root, text="", font=("Arial", 12), bg="tan")
    counter_label.pack()
    
    # Start event loop
    root.mainloop()

