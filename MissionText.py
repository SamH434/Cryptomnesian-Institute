import tkinter as tk


def MissionCommand():
    # Create the main window
    root = tk.Tk()
    root.title("Mission Summary")
    root.configure(bg='black')

    # Create the label and button widgets
    label_text0 = "Briefing"
    label0 = tk.Label(root, text=label_text0, fg='green', bg='black', font=('Helvetica', 20), justify='center', wraplength=400)
    label0.pack(pady=20)
    label_text = "You will be assigned 4 missions, each with their own respective ciphers and encoding systems. Each cipher is text-based or numeral-based, and some many require calculations by hand. Our forecasts have shown the first two ciphers to be encryption systems already documented by man, and the final two ciphers are something we have never encountered before; meaning you may have to figure out the encryption system on the fly. You will be provided the necessary techonological support by our agency during this operation (Systems located under [Cipher Tools]), and we will have personnel on standby in case the mission derails. We wish you luck on this journey"
    label = tk.Label(root, text=label_text, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label.pack(pady=20)
    label_text2 = "-Handler"
    label2 = tk.Label(root, text=label_text2, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label2.pack(pady=30)
    button = tk.Button(root, text="Understood", bg='black', fg='white', font=('Helvetica', 12), command=root.destroy)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
