import sqlite3
import logging
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import DB

class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        title = tk.Label(self, text="Agregar contacto", font=("Arial", 25))
        title.grid(row = 1, column = 1)
        go_back_btn = tk.Button(self, text="Volver al Menu", 
        command= lambda: self.controller.go_back())
        go_back_btn.grid(row=1, column=0)
        self.bind("<<ShowFrame>>", self.onShowFrame)

    def onShowFrame(self, event):
        self.form = {}
        form_labels = self.parse_xml()
        row = 2
        for form_label in form_labels:
            ttk.Label(self, text=form_label[1]).grid(row = row, column = 1, padx = 10, pady = 10)
            self.form[form_label[0]] = ttk.Entry(self)
            self.form[form_label[0]].grid(row = row, column = 2, padx = 10, pady = 10)
            row+=1

        submit_btn = ttk.Button(self, text="Crear contacto", 
        command = lambda: self.create_contact())
        submit_btn.grid(row = 10, column = 1, padx = 10, pady = 10)
        cancel_btn = ttk.Button(self, text="Cancelar", 
        command = lambda: self.controller.go_back())
        cancel_btn.grid(row = 11, column = 1, padx = 10, pady = 10)

    def create_contact(self):
        data = []
        for i in self.form:
           data.append(self.form[i].get())
        try:
            if (data[0] == ""): raise Exception("El nombre del contacto no puede estar vacio.")
            elif (data[1] == "" and data[2] == ""): raise Exception("Debe colocar al menos el numero de telefono o email del contacto.")
            elif ("@" not in data[2]): raise Exception("Debe ingresar un correo electronico valido")
            DB.add(data)
            tk.messagebox.showinfo("Operacion exitosa", "El contacto ha sido agregado exitosamente.")
            self.controller.go_back()
        except Exception as e:
            tk.messagebox.showerror("Error", e)

    def parse_xml(self):
        XMLTREE = xml.dom.minidom.parse("./views/contact.xml")
        nodeList = []

        if XMLTREE.childNodes:
            for node in XMLTREE.childNodes:
                for childNode in node.childNodes:
                    if childNode.nodeType == childNode.ELEMENT_NODE:
                        nodeList.append((childNode.attributes['name'].value, childNode.attributes['text'].value))
        return nodeList


