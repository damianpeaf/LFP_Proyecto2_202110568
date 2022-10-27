from tkinter import *
from tkinter import ttk


class TokenTable():

    def __init__(self, window):
        self.window = window
        self.window.title("Tabla de tokens")
        self.table = ttk.Treeview(self.window, height=35)
        self.table['columns'] = ('No.', 'Fila', 'Columna', 'Lexema', 'Tipo')

        self.table.column('#0', width=0, stretch=NO)
        self.table.column("No.", anchor=CENTER, width=10)
        self.table.column("Fila", anchor=CENTER, width=10)
        self.table.column("Columna", anchor=CENTER, width=10)
        self.table.column("Lexema", anchor=CENTER, width=50)
        self.table.column("Tipo", anchor=CENTER, width=120)

        self.table.heading('#0', text="", anchor=CENTER)
        self.table.heading("No.", text="No.", anchor=CENTER)
        self.table.heading("Fila", text="Fila", anchor=CENTER)
        self.table.heading("Columna", text="Columna", anchor=CENTER)
        self.table.heading("Lexema", text="Lexema", anchor=CENTER)
        self.table.heading("Tipo", text="Tipo", anchor=CENTER)

    def loadData(self, data):

        # data = [ { number: 'Lexico', row: 1, column: 1, lexema: 'a', type: 'b']

        # Delete rows
        for row in self.table.get_children():
            self.table.delete(row)

        for row in data:
            self.table.insert('', 'end', values=(row['number'], row['row'], row['column'], row['lexema'], row['type']))
