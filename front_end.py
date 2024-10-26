from tkinter import *
from back_end import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="#4B4B4B")
        self.master = master
        self.pack(expand=True, fill="both")
        self.is_space2_visible = False
        self.is_space1_visible = True
        self.create_layout()

    def create_layout(self):
        space0 = Frame(self, bg="#3E3E3E")
        space0.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        space0.grid_rowconfigure(0, weight=1)
        space0.grid_columnconfigure(0, weight=1)

        self.space1 = Frame(space0, bg="grey")
        self.space1.grid(row=0, column=0, padx=2, pady=2, sticky='nsew')
        self.space2 = Frame(space0, bg="grey")
        self.space2.grid(row=2, column=0, padx=2, pady=2, sticky='nsew')
        self.space2.grid_remove()
        space3 = Frame(space0, bg="lightgray")
        space3.grid(row=1, column=0, padx=2, pady=2, sticky='nsew')

        self.toggle_button1 = Button(space3, text="CONVERSOR ↓", command=self.toggle_space1, bg="silver")
        self.toggle_button1.pack(pady=5, side='left')

        self.toggle_button2 = Button(space3, text="LOGIC OPERATION ↓", command=self.toggle_space2, bg="silver")
        self.toggle_button2.pack(pady=5)

        self.configure_grid2(self.space2)
        self.configure_grid(self.space1)

        # Creating entry sections for number conversions
        self.create_entry_section(self.space1, row=0, label_text="HEX", var_name="hex_var", conversion_func=self.update_hex)
        self.create_entry_section(self.space1, row=1, label_text="DEC", var_name="dec_var", conversion_func=self.update_dec)
        self.create_entry_section(self.space1, row=2, label_text="OCT", var_name="oct_var", conversion_func=self.update_oct)
        self.create_entry_section(self.space1, row=3, label_text="BIN", var_name="bin_var", conversion_func=self.update_bin)

        operations = ["AND", "OR", "XOR", "NAND", "NOR", "NOT"]
        for idx, label in enumerate(operations):
            self.create_entry_section1(self.space2, row=idx, column=0, label_text=label, var_name=f"{label.lower()}_var")

    def toggle_space1(self):
        if self.is_space1_visible:
            self.space1.grid_remove()
            self.toggle_button1.config(text="CONVERSOR ↑")
        else:
            self.space1.grid()
            self.toggle_button1.config(text="CONVERSOR ↓")
        self.is_space1_visible = not self.is_space1_visible

    def toggle_space2(self):
        if self.is_space2_visible:
            self.space2.grid_remove()
            self.toggle_button2.config(text="LOGIC OPERATION ↑")
        else:
            self.space2.grid()
            self.toggle_button2.config(text="LOGIC OPERATION ↓")
        self.is_space2_visible = not self.is_space2_visible

    def configure_grid(self, frame):
        for i in range(4):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(2):
            frame.grid_columnconfigure(j, weight=1)

    def configure_grid2(self, frame):
        for i in range(6):
            frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            frame.grid_columnconfigure(j, weight=1)

    def create_entry_section(self, parent, row, label_text, var_name, conversion_func):
        button = Button(parent, width=8, text=label_text, bg="silver")
        button.grid(row=row, column=0, padx=2, pady=2, sticky='wnse')

        entry_var = StringVar()
        entry = Entry(parent, width=47, textvariable=entry_var, font=("Consolas", 9), fg="white", bg="#3E3E3E", insertbackground="white")
        entry.grid(row=row, column=1, padx=2, pady=2, sticky='wnse')

        setattr(self, var_name, entry_var)

        # Add a trace to update the result in real time
        entry_var.trace("w", lambda *args: conversion_func(entry_var))

    def create_entry_section1(self, parent, row, column, label_text, var_name):
        label = Label(parent, text=label_text, bg="silver")
        label.grid(row=row, column=column + 1, padx=2, pady=2, sticky='wnse')

        entry_var1 = StringVar()
        entry = Entry(parent, width=16, textvariable=entry_var1, font=("Consolas", 9), fg="white", bg="#3E3E3E", insertbackground="white")
        entry.grid(row=row, column=column, padx=2, pady=2, sticky='wnse')

        if label_text != "NOT":
            entry_var2 = StringVar()
            entry = Entry(parent, width=16, textvariable=entry_var2, font=("Consolas", 9), fg="white", bg="#3E3E3E", insertbackground="white")
            entry.grid(row=row, column=column + 2, padx=2, pady=2, sticky='wnse')

        entry_var3 = StringVar()
        entry = Entry(parent, width=16, textvariable=entry_var3, font=("Consolas", 9), fg="white", bg="#3E3E3E", insertbackground="white")
        entry.grid(row=row, column=column + 3, padx=2, pady=2, sticky='wnse')

        setattr(self, var_name, entry_var1)

    def update_hex(self, hex_var):
        NumberConverter.update_hex(hex_var, self.dec_var, self.oct_var, self.bin_var)

    def update_dec(self, dec_var):
        NumberConverter.update_dec(dec_var, self.hex_var, self.oct_var, self.bin_var)

    def update_oct(self, oct_var):
        NumberConverter.update_oct(oct_var, self.hex_var, self.dec_var, self.bin_var)

    def update_bin(self, bin_var):
        NumberConverter.update_bin(bin_var, self.hex_var, self.dec_var, self.oct_var)
