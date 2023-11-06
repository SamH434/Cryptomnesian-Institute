import tkinter as tk


def Level4Command():
    # Create the main window
    root = tk.Tk()
    root.title("Mission 4 Briefing")
    root.configure(bg='black')

    # Create the label and button widgets   
    label_text0 = "Mission 4"
    label0 = tk.Label(root, text=label_text0, fg='green', bg='black', font=('Helvetica', 20), justify='center', wraplength=400)
    label0.pack(pady=30)

    label_text = '''This will be you final mission. These are two data bits collected decoded from a certain radio frequency, and the only clues we have is this tapped message from the enemy's landline: "I think...uh...maybe check under the table...did you leave it at the...station?...I know you had to shift the letters around or something, like they did with that one search site...and then they took it back to the old System...used some sort of key to open it...anyways I'm heading back first...oh yeah one more thing, I think you're supposed to combine...the results before you leave...". The solution of this code shall be sent directly to headquarters, and as of 2200 hours today, you are dismissed. We grealy thank you for your cooperation. El Psy Congroo.'''
    label = tk.Label(root, text=label_text, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label.pack(pady=30)
    button = tk.Button(root, text="Understood", bg='black', fg='white', font=('Helvetica', 12), command=root.destroy)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
