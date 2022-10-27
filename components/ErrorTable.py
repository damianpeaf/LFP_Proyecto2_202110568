from tkinter import *
from tkinter import ttk


class ErrorTable():

    def __init__(self, window):
        self.window = window
        self.table = ttk.Treeview(self.window, height=35)
        self.window.title("Tabla de errores")
        self.table['columns'] = ('Tipo', 'Fila', 'Columna', 'Lexema', 'Esperaba', 'Descripcion')

        self.table.column('#0', width=0, stretch=NO)
        self.table.column("Tipo", anchor=CENTER, width=10)
        self.table.column("Fila", anchor=CENTER, width=10)
        self.table.column("Columna", anchor=CENTER, width=10)
        self.table.column("Lexema", anchor=CENTER, width=50)
        self.table.column("Esperaba", anchor=CENTER, width=120)
        self.table.column("Descripcion", anchor=CENTER, width=80)

        self.table.heading('#0', text="", anchor=CENTER)
        self.table.heading("Tipo", text="Tipo", anchor=CENTER)
        self.table.heading("Fila", text="Fila", anchor=CENTER)
        self.table.heading("Columna", text="Columna", anchor=CENTER)
        self.table.heading("Lexema", text="Lexema", anchor=CENTER)
        self.table.heading("Esperaba", text="Esperaba", anchor=CENTER)
        self.table.heading("Descripcion", text="Descripcion", anchor=CENTER)

    def loadData(self, data):

        # data = [ { type: 'Lexico', row: 1, column: 1, lexema: 'a', expected: 'b', description: 'c' } ]

        # Delete rows
        for row in self.table.get_children():
            self.table.delete(row)

        for row in data:
            self.table.insert('', 'end', values=(row['type'], row['row'], row['column'], row['lexema'], row['expected'], row['description']))
