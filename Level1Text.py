import tkinter as tk


def Level1Command():
    # Create the main window
    root = tk.Tk()
    root.title("Mission 1 Briefing")
    root.configure(bg='black')

    # Create the label and button widgets
    label_text0 = "Don't Give Up!"
    label0 = tk.Label(root, text=label_text0, fg='green', bg='black', font=('Helvetica', 20), justify='center', wraplength=400)
    label0.pack(pady=30)

    label_text = """Your commitment to growth is commendable! While your recent performance falls below 60, we encourage you to view this as an opportunity for improvement. Remember, every challenge is a stepping stone toward success. Embrace the encouraging message below, and let the comforting frequency guide you towards a positive and supportive learning environment. You have the resilience to overcome obstacles and turn them into triumphs. Every stumble is a step towards success. Keep going, and remember, failure is just the beginning of your journey to success."""
    label = tk.Label(root, text=label_text, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label.pack(pady=30)
    button = tk.Button(root, text="Understood", bg='black', fg='white', font=('Helvetica', 12), command=root.destroy)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
