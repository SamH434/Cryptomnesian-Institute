import tkinter as tk


def Level3Command():
    # Create the main window
    root = tk.Tk()
    root.title("Mission 3 Briefing")
    root.configure(bg='black')

    # Create the label and button widgets
    label_text0 = "Mission 3"
    label0 = tk.Label(root, text=label_text0, fg='green', bg='black', font=('Helvetica', 20), justify='center', wraplength=400)
    label0.pack(pady=30)

    label_text = '''I am pleased to inform you that our infiltration efforts have been successful, and we have breached the second level of the enemy's database. While there is still a degree of error tolerance in the decryption process, it is significantly higher this time around (Limit: 16). Nonetheless, we urge you to proceed with the utmost care and urgency in decoding the passcode, as we do not wish to risk being discovered by the enemy. The information contained within this database is of critical importance to our mission, and we must do everything in our power to access it. Please keep us informed of any developments and report back to us immediately upon completion of the decryption process.'''
    label = tk.Label(root, text=label_text, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label.pack(pady=30)
    button = tk.Button(root, text="Understood", bg='black', fg='white', font=('Helvetica', 12), command=root.destroy)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
