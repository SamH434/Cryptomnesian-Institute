import tkinter as tk


def Level2Command():
    # Create the main window
    root = tk.Tk()
    root.title("Mission 2 Briefing")
    root.configure(bg='black')

    # Create the label and button widgets   
    label_text0 = "Congratulations!"
    label0 = tk.Label(root, text=label_text0, fg='green', bg='black', font=('Helvetica', 20), justify='center', wraplength=400)
    label0.pack(pady=30)

    label_text = '''Congratulations on your outstanding achievement! Your grade is above 90, showcasing your dedication and excellence. Revel in the success and let the soothing low-frequency experience create a positive and calming atmosphere. Your commitment to academic excellence is truly commendable, and PsyCommuVer1 is here to celebrate your achievements.'''
    label = tk.Label(root, text=label_text, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label.pack(pady=30)
    button = tk.Button(root, text="Understood", bg='black', fg='white', font=('Helvetica', 12), command=root.destroy)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
