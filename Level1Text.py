import tkinter as tk


def Level1Command():
    # Create the main window
    root = tk.Tk()
    root.title("Mission 1 Briefing")
    root.configure(bg='black')

    # Create the label and button widgets
    label_text0 = "Mission 1"
    label0 = tk.Label(root, text=label_text0, fg='green', bg='black', font=('Helvetica', 20), justify='center', wraplength=400)
    label0.pack(pady=30)

    label_text = "We are to inform you that our reconnaissance troops in the excavation site at Point B-7 have discovered a tomb and are in need of assistance in decrypting the code found within. Our analysts have suggested the possiblity of the cipher being a shift-based substitution cipher, although we do not know the shift value. The tomb has also been observed to have a weight-manipulated locking system, where if the code is entered incorrecly 4 times, the tomb will collapse in on itself and the subject of interest within will be destroyed. As our top priority is the successful retrieval and analysis of any potential intelligence, we urge you to provide us with your most skilled cryptography and decryption skills immediately. Any delay in this matter could result in the loss of crucial data."
    label = tk.Label(root, text=label_text, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label.pack(pady=30)
    button = tk.Button(root, text="Understood", bg='black', fg='white', font=('Helvetica', 12), command=root.destroy)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
