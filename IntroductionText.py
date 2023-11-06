import sys
import tkinter as tk

import TestingMain


def IntroductionTextCommand():
    # Create the main window
    root = tk.Tk()
    root.title("Welcome")
    root.configure(bg='black')

    # Create the label and button widgets
    label_text1 = "Dear Candidate"
    label1 = tk.Label(root, text=label_text1, fg='green', bg='black', font=('mono', 20), justify='center', wraplength=400)
    label1.pack(pady=30)

    label_text2 = "The Cryptomnesian Institute is pleased to inform you that you have been selected to join our esteemed organization. Your discerning abilities and intellectual prowess have caught our attention, and we invite you to participate in our esoteric pursuits. As a member of our fraternity, you will be granted access to knowledge beyond human comprehension. We await your response to this invitation."
    label2 = tk.Label(root, text=label_text2, fg='green', bg='black', font=('mono', 12), justify='center', wraplength=400)
    label2.pack(pady=20)

    label_text3 = "Sincerely, The Cryptomnesian Institute"
    label3 = tk.Label(root, text=label_text3, fg='green', bg='black', font=('mono', 12), justify='center', wraplength=400)
    label3.pack(pady=10)

    def destroy_window():
        root.destroy()

    def destroy_main():
        sys.exit()

    button_accept = tk.Button(root, text="Accept", bg='black', fg='white', font=('mono', 12), command=destroy_window)
    button_accept.pack(pady=20)

    button_decline = tk.Button(root, text="Decline", bg='black', fg='white', font=('mono', 12), command=destroy_main)
    button_decline.pack(pady=20)

    # Run the main event loop
    root.mainloop()
