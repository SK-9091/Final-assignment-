import tkinter as tk
from tkinter import messagebox
from models import User, Admin, SystemManager

class TicketApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Ticket System")
        self.manager = SystemManager()
        self.current_user = None

        if "admin" not in self.manager.users:
            self.manager.users["admin"] = Admin("A001", "admin", "admin123", "admin@example.com", "0000")
            self.manager.save_all()

        self.main_menu()

    def clear_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_frame()
        tk.Label(self.master, text="Ticket System").grid(row=0, column=0, pady=10)
        tk.Button(self.master, text="Create Account", command=self.register_screen).grid(row=1, column=0, pady=5)
        tk.Button(self.master, text="Exit", command=self.master.quit).grid(row=2, column=0, pady=5)

    def register_screen(self):
        self.clear_frame()
        fields = ["User ID", "Username", "Password", "Email", "Phone"]
        entries = {}
        for i, label in enumerate(fields):
            tk.Label(self.master, text=label).grid(row=i, column=0)
            entry = tk.Entry(self.master, show="*" if label == "Password" else "")
            entry.grid(row=i, column=1)
            entries[label] = entry

        def submit():
            uid = entries["User ID"].get()
            uname = entries["Username"].get()
            pw = entries["Password"].get()
            em = entries["Email"].get()
            ph = entries["Phone"].get()
            if uname in self.manager.users:
                messagebox.showerror("Error", "Username exists")
                return
            self.manager.users[uname] = User(uid, uname, pw, em, ph)
            self.manager.save_all()
            messagebox.showinfo("Success", "Registered!")
            self.main_menu()

        submit_btn = tk.Button(self.master, text="Submit", command=submit)
        submit_btn.grid(row=len(fields), column=0, columnspan=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketApp(root)
    root.mainloop()
