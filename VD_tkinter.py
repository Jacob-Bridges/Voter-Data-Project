# Create class to load tkinter window

import tkinter as tk
import voter_file


class Data_UI:
    def __init__(self):
        # Main Window
        self.main_window = tk.Tk()
        self.main_window.title('Voter Reg Lookup')
        self.main_window.geometry('275x125')

        # Sub Windows
        self.search_window = tk.Frame(self.main_window)
        self.show_window = tk.Frame(self.main_window)
        self.show_window.pack()
        self.search_window.pack()

        # Label1
        self.search_label = tk.Label(self.search_window, text='Search Reg_ID:')
        self.search_label.pack(side='left')

        # Entry
        self.search_entry = tk.Entry(self.search_window, width=10)
        self.search_entry.pack(side='left')
        self.reg_id = tk.StringVar()
        self.fields = tk.StringVar()
        self.show_fields = tk.Label(self.show_window, textvariable=self.fields)
        self.show_search = tk.Label(self.show_window, textvariable=self.reg_id)
        self.show_fields.pack(side='top')
        self.show_search.pack(side = 'top')

        # Buttons
        self.button_window = tk.Frame(self.main_window)
        self.quit = tk.Button(self.button_window, text='Quit', command=self.main_window.destroy)
        self.search = tk.Button(self.button_window, text='Search', command=self.get_reg_id)
        self.search.pack(side='left')
        self.quit.pack(side='left')
        self.button_window.pack(side='top')

        tk.mainloop()

    def get_reg_id(self):
        self.fields.set(voter_file.fields)
        get_id = self.search_entry.get()

        if get_id in voter_file.voter_dict:

            self.reg_id.set(voter_file.voter_dict.get(get_id))
        else:
            self.reg_id.set('No Record Found')



