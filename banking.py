#malik Stockton cis 131
#import tkinter to be used to create a banking sytstem
#import 
from tkinter import *
from tkinter import ttk   
import tkinter as tk
from tkinter import messagebox
import datetime
#classs that will give banking system labels 
#will also creat buttons
class BankSystemGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Bank System")
        self.create_account_window()
    #The first window that pops for user
    def create_account_window(self):
        frame = Frame(self.root)
        frame.pack()
        self.clear_window()

        self.account_label = tk.Label(self.root, text="Create an Account")
        self.account_label.pack()

        self.name_label = tk.Label(self.root, text=" First Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        
        self.lastname_label =tk.Label(self.root,text="Last Name")
        self.lastname_label.pack()
        self.lastname_entry=tk.Entry(self.root)
        self.lastname_entry.pack()

        self.dob_label = tk.Label(self.root,text ="Date Of Birth")
        self.dob_label.pack()
        self.dob_entry = tk.Entry(self.root)
        self.dob_entry.pack()
        
    #social security number entry
        self.ssn_label = tk.Label(self.root, text ="Enter Social Security Number:")
        self.ssn_label.pack()
        self.ssn_entry= tk.Entry(self.root)
        self.ssn_entry.insert(0,"000-00-0000")
        self.ssn_entry.pack()

# enter your address
        self.address_label = tk.Label(self.root,text="Address: ")
        self.address_label.pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack()
        self.address_entry.pack()
        
        self.balance_label = tk.Label(self.root, text="Initial Deposit:")
        self.balance_label.pack()
        self.balance_entry = tk.Entry(self.root)
        self.balance_entry.pack()

        self.create_button = tk.Button(self.root, text="Create Account", command=self.create_account)
        self.create_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()
    #will prompt user to create account
    def create_account(self):
        name = self.name_entry.get()
        balance = self.balance_entry.get()
        lastName = self.lastname_entry.get()
        dateofbirth = self.dob_entry.get()
        ssn = self.ssn_entry.get().replace("-","").strip()
        address = self.address_entry.get()
       
        #for invalid inputs
        if not name or not balance or not lastName or not dateofbirth or not ssn or not address:
            messagebox.showerror("Error", "Please fill out all fields")
            return

        try:
            balance = float(balance)
        except ValueError:
            messagebox.showerror("Error", "Invalid balance. Please enter a number.")
            return
        #checks for valid SSN
        if len(ssn) != 9 or not ssn.isdigit():
            messagebox.showwarning("Warning","Incorrect format of social security number.\nShould be in the form XXX-XX-XXXX")
            return
        #checks for valid dob format
        if dateofbirth != '%m%d%y':
            messagebox.showwarning("Warning","Incorrect Date Format.\nCorrect Format is YYYY-MM-DD")
        #to display all of the gathered information
        accnt =(name, balance, lastName, dateofbirth, ssn, address)
        print(accnt.__str__())
        messagebox.showinfo('Success', 'Account Created Successfully!')
        print(accnt.__str__())
        self.balance = balance
        self.show_balance_window()
    #will show balance
    def show_balance_window(self):
        self.clear_window()

        self.balance_label = tk.Label(self.root, text="Account Balance")
        self.balance_label.pack()

        self.balance_text = tk.Label(self.root, text="Your balance is: $%.2f" % self.balance)
        self.balance_text.pack()

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.show_deposit_window)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.show_withdraw_window)
        self.withdraw_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack()
    #will show where the use made a deposit
    def show_deposit_window(self):
        self.clear_window()

        self.deposit_label = tk.Label(self.root, text="Deposit Money")
        self.deposit_label.pack()

        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.pack()

        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit_money)
        self.deposit_button.pack()

        self.back_button = tk.Button(self.root, text="Back", command=self.show_balance_window)
        self.back_button.pack()

    def deposit_money(self):
        amount = self.deposit_entry.get()
        #for invalid inputs 
        if not amount:
            messagebox.showerror("Error", "Please enter an amount.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a number.")
            return
        
        self.balance += amount
        self.show_balance_window()

    def show_withdraw_window(self):
        self.clear_window()

        self.withdraw_label = tk.Label(self.root, text="Withdraw Money")
        self.withdraw_label.pack()

        self.withdraw_entry = tk.Entry(self.root)
        self.withdraw_entry.pack()

        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw_money)
        self.withdraw_button.pack()

        self.back_button = tk.Button(self.root, text="Back", command=self.show_balance_window)
        self.back_button.pack()

    def withdraw_money(self):
        amount = self.withdraw_entry.get()
        #for invlaid inputs
        if not amount:
            messagebox.showerror("Error", "Please enter an amount.")
            return
        
        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a number.")
            return

        if amount > self.balance:
            messagebox.showerror("Error", "Insufficient funds.")
            return

        self.balance -= amount
        self.show_balance_window()
        
    
    #for the clearing of the window or eciting 
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    bank_system = BankSystemGUI()
    bank_system.run()


