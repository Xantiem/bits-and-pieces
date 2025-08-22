import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json

class Main(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.widgets()

    def widgets(self):
        self.json = json.load(open('FSTW_prices.json'))
        self.options = list(self.json.keys())

        self.placeholder_have = tk.StringVar(self)
        self.placeholder_have.set('Please Select')

        self.placeholder_want = tk.StringVar(self)
        self.placeholder_want.set('Please Select')

        self.have_l = tk.Label(self)
        self.have_l['text'] = "Have:"
        
        self.have = ttk.Combobox(self)
        self.have['textvariable'] = self.placeholder_have
        self.have['state'] = "readonly"
        self.have['values'] = self.options

        self.want_l = tk.Label(self)
        self.want_l['text'] = "Want:"
        
        self.want = ttk.Combobox(self)
        self.want['textvariable'] = self.placeholder_want
        self.want['state'] = "readonly"
        self.want['values'] = self.options

        self.amount = tk.Label(self)
        self.amount['text'] = "Amount:"

        self.have_amount = tk.Entry(self)
        self.have_amount['width'] = 15
        
        self.have_confirm = tk.Button(self)
        self.have_confirm['text'] = "calculate"
        self.have_confirm['borderwidth'] = 1
        self.have_confirm['relief'] = "solid"

        self.have_confirm['command'] = self.confirmed

        self.quantity_l = tk.Label(self)
        self.quantity_l['text'] = "Quantity:"
        
        self.quantity = tk.Label(self)
        self.quantity['text'] = '0'
        

        self.have_l.grid(row='0', column='0')
        self.have.grid(row='0', column='1')
        self.amount.grid(row='0', column='2', padx=('5', '0'))
        self.have_amount.grid(row='0', column='3')

        self.have_confirm.grid(row='1', column='2', columnspan='2', rowspan='2', padx=('5', '0'), sticky=tk.N+tk.E+tk.S+tk.W)
        
        self.want_l.grid(row='1', column='0')
        self.want.grid(row='1', column='1')

        self.quantity_l.grid(row='2', column='0', padx=('22', '0'))

        self.quantity.grid(row='2', column='1')

    def confirmed(self):
        self.selected_have = self.have.get()
        self.selected_want = self.want.get()
        self.selected_have_amount = self.have_amount.get()

        if self.selected_have == 'Please Select':
            messagebox.showerror('Incorrect Value:', 'Please enter HAVE value')
        elif self.selected_want == 'Please Select':
            messagebox.showerror('Incorrect Value:', 'Please enter WANT value')
        elif self.selected_have_amount == '':
            messagebox.showerror('Incorrect Value:', 'Please enter an amount')
        else:

            try:
                self.number = float(self.selected_have_amount.replace(' ', ''))
            except ValueError:
                messagebox.showerror('Error:', 'Please enter only numbers')

            self.quantity_want = (self.json[self.selected_have]*self.number) / self.json[self.selected_want]
            
            self.quantity['text'] = round(self.quantity_want, 2)

root = tk.Tk()
root.title('STW Trading Calculator')
root.resizable(False, False)
root.geometry('500x80+0+0')
root.iconbitmap('icon.ico')
main = Main(master=root)
main.mainloop()
        
