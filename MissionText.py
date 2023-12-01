import tkinter as tk


def MissionCommand():
    # Create the main window
    root = tk.Tk()
    root.title("Mission Summary")
    root.configure(bg='black')

    # Create the label and button widgets
    label_text0 = "How To Use App"
    label0 = tk.Label(root, text=label_text0, fg='green', bg='black', font=('Helvetica', 20), justify='center', wraplength=400)
    label0.pack(pady=20)
    label_text = """Getting Started: Welcome to PsyCommuVer1, where we believe in the transformative power of positive reinforcement in your learning journey. To begin, follow these simple instructions: Grade Submission: After each assessment, click on the "Submit Grade" button to log your academic performance. You will see two options: "Below 60" and "Above 90." Choose the button that corresponds to your grade range. Positive Reinforcement: If your grade is above 90, you'll be rewarded with a soothing low-frequency experience, creating a positive and calming atmosphere. Positive Encouragement: If your grade is below 60, experience an encouraging message that reminds you that every challenge is a stepping stone toward success. You'll also enjoy a comforting frequency, fostering a supportive learning environment. Study Sessions: During study sessions, click on the "Study Mode" button to immerse yourself in a calming environment enhanced by the comforting relief frequencies. Let go of the fear of failure and embrace the joy of learning."""
    label = tk.Label(root, text=label_text, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label.pack(pady=20)
    label_text2 = "-Handler"
    label2 = tk.Label(root, text=label_text2, fg='green', bg='black', font=('Helvetica', 12), justify='center', wraplength=400)
    label2.pack(pady=30)
    button = tk.Button(root, text="Understood", bg='black', fg='white', font=('Helvetica', 12), command=root.destroy)
    button.pack(pady=20)

    # Run the main event loop
    root.mainloop()
