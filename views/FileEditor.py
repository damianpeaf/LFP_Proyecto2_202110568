from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from os.path import exists
from components.ErrorTable import ErrorTable
from core.Core import Core

from lexer.Lexer import Lexer
from parser2.Parser import Parser


class FileEditor():

    def __init__(self, parent):
        self.window = Toplevel(parent)
        self.window.geometry("1000x900")
        self.window.config(bg='#1B1F3B')
        self.window.title("Editor de archivo")
        self.filePath = ""
        self.initUI()

    def openFile(self):
        self.filePath = filedialog.askopenfilename(
            initialdir="./", title="Seleccionar archivo de entrada", filetypes=[("txt files", "*.gpw")])

        self.refreshEditor()

    def saveFile(self):
        try:
            file = open(self.filePath, 'w', encoding="utf-8", errors='ignore')
            file.write(self.editor.get("1.0", "end-1c"))
            file.close()
            messagebox.showinfo(title="Aviso", message="Archivo guardado")
            self.refreshEditor()
        except:
            messagebox.showwarning(
                title="Aviso", message="Error al guardar el archivo")

    def saveFileAs(self):
        try:
            self.filePath = filedialog.asksaveasfilename(
                filetypes=[("txt files", "*.gpw")], defaultextension=".gpw")

            # * File already exists
            if exists(self.filePath):
                self.saveFile()
            # * If not, create a new one
            else:
                file = open(self.filePath, 'x',
                            encoding="utf-8", errors='ignore')
                file.write(self.editor.get("1.0", "end-1c"))
                file.close()
                messagebox.showinfo(
                    title="Aviso", message="Archivo creado y guardado")
                self.refreshEditor()
        except:
            messagebox.showwarning(
                title="Aviso", message="Error al guardar el archivo")

    def refreshEditor(self):
        try:
            self.messageLabel.config(text=self.filePath)
            file = open(self.filePath, 'r', encoding="utf-8", errors='ignore')
            self.editor.delete('1.0', END)
            self.editor.insert(END, file.read())
            file.close()
        except Exception as e:
            print(e)
            messagebox.showwarning(
                title="Aviso", message="Error al leer el archivo")

    def analyze(self):
        try:
            file = open(self.filePath, 'r', encoding="utf-8", errors='ignore')
            text = file.read()
            file.close()

            lexer = Lexer(text)
            lexer.runLexicAnalysis()
            parser = Parser()
            parser.runSyntacticAnalysis()
            core = Core()
            errors = core.getErrors()

            print(errors)
            if len(errors) > 0:
                self.errorWindow = Toplevel(self.window)
                self.errorWindow.geometry("1000x900")
                self.errorTable = ErrorTable(self.errorWindow)
                self.errorTable.table.pack(expand=1, fill=BOTH)
                self.errorTable.loadData(errors)

            if len(Core.runTimeErrors) > 0:
                self.errorWindow = Toplevel(self.window)
                self.errorWindow.geometry("1000x900")
                self.errorTable = ErrorTable(self.errorWindow)
                self.errorTable.table.pack(expand=1, fill=BOTH)
                self.errorTable.loadData(Core.runTimeErrors)

        except Exception as e:
            print(e)
            messagebox.showwarning(
                title="Aviso", message="Error al leer el archivo")

    def cursorTrackerInfo(self, event=None):
        r, c = self.editor.index('insert').split('.')
        self.cursorLabel.config(text=f'Fila: {r} - Columna: {str(int(c)+1)}')

    def initUI(self):
        buttonFont = ("Helvetica", 10, "bold")
        messagesFont = ("Helvetica", 12)

        self.buttonsFrame = Frame(self.window)

        Button(self.buttonsFrame,
               text="Abrir",
               pady=5,
               padx=10,
               bg="#0D6EFD",
               fg="white",
               font=buttonFont,
               command=self.openFile).grid(row=0, column=0)

        Button(self.buttonsFrame,
               text="Guardar",
               pady=5,
               padx=10,
               bg="#108054",
               fg="white",
               font=buttonFont,
               command=self.saveFile).grid(row=0, column=1)

        Button(self.buttonsFrame,
               text="Guardar como",
               pady=5,
               padx=10,
               bg="#104554",
               fg="white",
               font=buttonFont,
               command=self.saveFileAs).grid(row=0, column=2)

        Button(self.buttonsFrame,
               text="Analizar",
               pady=5,
               padx=10,
               bg="#8502F7",
               fg="white",
               font=buttonFont,
               command=self.analyze).grid(row=0, column=3)

        # Button(self.buttonsFrame,
        #        text="Errores",
        #        pady=5,
        #        padx=10,
        #        bg="#E0C302",
        #        fg="white",
        #        font=buttonFont,
        #        command=self.errors).grid(row=0, column=4)

        Button(self.buttonsFrame,
               text="Salir",
               pady=5,
               padx=10,
               bg="#DC3545",
               fg="white",
               font=buttonFont,
               command=self.window.destroy).grid(row=0, column=5)

        self.buttonsFrame.pack()

        self.messageLabel = Label(
            self.window, text="archivo no seleccionado", bg='#1B1F3B', fg='white', font=messagesFont, pady=5)
        self.messageLabel.pack(fill="x")

        self.editor = Text(self.window, bg='#1B1F3B', fg='white')
        self.editor.config(insertbackground='red')
        self.editor.pack(expand=1, fill="both")

        self.cursorLabel = Label(self.window, text="", bg='#1B1F3B', fg='white', font=messagesFont, pady=5)
        self.cursorLabel.pack(fill="x")

        self.editor.event_add('<<REACT>>', *('<Motion>', '<ButtonRelease>', '<KeyPress>', '<KeyRelease>'))
        b = self.editor.bind('<<REACT>>', self.cursorTrackerInfo)
        self.cursorTrackerInfo()  # get the ball rolling
        self.editor.focus()
