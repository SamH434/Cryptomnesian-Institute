import tkinter as tk


def Level2Command():
    # Create the main window
    root = tk.Tk()
    root.title("Mission 2 Briefing")
    root.configure(bg='black')

    # Create the label and button widgets   
    label_text0 = "Mission 2"
    label0 = tk.Label(root, text=label_text0, fg='green', bg='black', font=('Helvetica', 20), justify='center', wraplength=400)
    label0.pack(pady=30)

    label_text = ''' to inform you that our Cybersecurity Branch has successfully infiltrated an enemy intelligence agency's database and obtained a cipher that requires decryption. However, we must proceed with caution as there is a security protocol in place that can detect multiple entries (Limit: 3); if the limit is reached, the program will terminate and may risk expsoing our agency. As such, we urge you to exercise the utmost care and precision in your decryption efforts.'''
    label = tk.Label(root, text=label_text, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label.pack(pady=30)
    button = tk.Button(root, text="Understood", bg='black', fg='white', font=('Helvetica', 12), command=root.destroy)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
