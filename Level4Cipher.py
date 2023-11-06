import tkinter as tk


class SignalGUI:
    def __init__(self):
        self.counter = 0
        self.window = tk.Tk()
        self.window.title("Signal Unit")
        self.window.configure(bg='black')

        title_label = tk.Label(self.window, text="Frequency 160.2", font=("Arial", 20), bg='black', fg='white')
        title_label.pack(pady=20)

        title_label1 = tk.Label(self.window, text='''"XEQEIXL DVRXRF"''', font=("Arial", 12, "bold"), bg="black", fg="green")
        title_label1.pack(pady=10)

        passcode_label = tk.Label(self.window, text="Passcode:", font=("Arial", 16), bg='black', fg='white')
        passcode_label.pack(pady=10)

        self.passcode_entry = tk.Entry(self.window, font=("Arial", 16))
        self.passcode_entry.pack(pady=10)

        confirm_button = tk.Button(self.window, text="Confirm", font=("Arial", 16), command=self.check_passcode,bg='white', fg='black')
        confirm_button.pack(pady=20)

    def check_passcode(self):
        passcode = self.passcode_entry.get().lower().strip()
        if passcode == "trinity vertex":
            self.show_spike()
        else:
            self.counter += 1
            if self.counter >= 100:
                self.report()
            else:
                self.reject()

    def show_spike(self):
        new_window = tk.Toplevel(self.window)
        new_window.title("Entry Unit")
        new_window.geometry("200x100")
        label = tk.Label(new_window, text="[5142]", font=("Arial", 20))
        label.pack(pady=20)

    def reject(self):
        rejection_label = tk.Label(self.window, text="Rejected", font=("Arial", 16), bg='black', fg='red')
        rejection_label.pack(pady=10)

    def report(self):
        self.window.destroy()
        label = tk.Label(text="Access Denied User Reported", font=("Arial", 20), justify='center', wraplength=200)
        label.pack(pady=20)

def SignalCommand():
    SignalGUI().window.mainloop()


