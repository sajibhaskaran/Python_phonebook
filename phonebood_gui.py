

from tkinter import *
import tkinter as tk

#importing the modules
import phonebook_main
import phonebook_func




def load_gui(self):

    #Labels
    self.lbl_fname = tk.Label(self.master, text = "First Name:")
    self.lbl_fname.grid(row = 0, column = 0, padx = (27,0), pady(10,0), sticky = N+W)
    self.lbl_lname = tk.Label(self.master, text = "Last Name:")
    self.lbl_lname.grid(row = 2, column = 0, padx = (27,0), pady(10,0), sticky = N+W)
    self.lbl_phone = tk.Label(self.master, text = "Phone Number:")
    self.lbl_phone.grid(row = 4, column = 0, padx = (27,0), pady(10,0), sticky = N+W)
    self.lbl_email = tk.Label(self.master, text = "Email Address:")
    self.lbl_email.grid(row = 6, column = 0, padx = (27,0), pady(10,0), sticky = N+W)
    self.lbl_user = tk.Label(self.master, text = "User:")
    self.lbl_user.grid(row = 0, column = 2, padx = (0,0), pady(10,0), sticky = N+W)

    #Entry boxes
    self.txt_fname = tk.Entry(self.master, text = '')
    self.txt_fname.grid(row = 1, column = 0, columnspan = 2, padx = (30,40), stick = N+E+W)
    self.txt_lname = tk.Entry(self.master, text = '')
    self.txt_lname.grid(row = 3, column = 0, columnspan = 2, padx = (30,40), stick = N+E+W)
    self.txt_phone = tk.Entry(self.master, text = '')
    self.txt_phone.grid(row = 5, column = 0, columnspan = 2, padx = (30,40), stick = N+E+W)
    self.txt_email = tk.Entry(self.master, text = '')
    self.txt_email.grid(row = 7, column = 0, columnspan = 2, padx = (30,40), stick = N+E+W)


    #List box and scroll bar.
    self.scroll_bar = Scrollbar(self.master, orient = VERTICAL)
    self.lst_list = Listbox(self.master, exportselection = 0, yscrollcommand = self.scroll_bar.set)
    self.lst_list.bind('<<ListboxSelect>>', lambda event: phonebook_func.onSelect(self, event))
    self.scroll_bar.config(command = self.lst_list.yview)
    self.scrll_bar.grid(row = 1, column = 5, rowspan = 7, columnspan = 1, padx=(0,0),pady=(0,0), sticky = N+E+S)
    self.lst_list.grid(row = 1, column = 2, rowspan = 7, columnspan = 3, padx = (0,0), pady=(0,0), sticky = N+E+S+W)

    
    #Buttons
    self.btn_add = tk.Button(self.master, width = 12, height = 2, text = 'Add', command = lambda: phonebook_func.addToList(self))
    self.btn_add.grid(row = 8, column = 0, padx= (25,0), pady= (45,10), sticky= W)
    self.btn_update = tk.Button(self.master, width = 12, height = 2, text = 'Update', command = lambda: phonebook_func.onUpdate(self))
    self.btn_update.grid(row = 8, column = 1, padx= (15,0), pady= (45,10), sticky= W)
    self.btn_delete = tk.Button(self.master, width = 12, height = 2, text = 'Delete', command = lambda: phonebook_func.onDelete(self))
    self.btn_delete.grid(row = 8, column = 2, padx= (15,0), pady= (45,10), sticky= W)
    self.btn_close = tk.Button(self.master, width = 12, height = 2, text = 'Close', command = lambda: phonebook_func.askQuit(self))
    self.btn_close.grid(row = 8, column = 4, padx= (15,0), pady= (15,0), sticky= E)


    phonebook_func.create_db(self)
    phonebook_func.onRefresh(self)



if __name__ == "__main__":
    pass
                        














    
