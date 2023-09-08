import sqlite3
import tkinter as tk
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import Database

DB = Database("contactos")

class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Agregar contacto",)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        self.form = {}
        form_labels = self.parse_xml()
        distance = 0
        for form_label in form_labels:
            ttk.Label(self, text=form_label[1]).place(x=50, y=50 + distance)
            self.form[form_label[0]] = ttk.Entry(self)
            self.form[form_label[0]].place(x=200, y=50 + distance)
            distance+=50

        submit_btn = ttk.Button(self, text="Crear contacto", 
        command = lambda: self.create_contact())
        submit_btn.grid(row = 10, column = 4, padx = 10, pady = 10)
        cancel_btn = ttk.Button(self, text="Cancelar", 
        command = lambda: controller.go_back())
        cancel_btn.grid(row = 11, column = 4, padx = 10, pady = 10)

    def create_contact(self):
        data = []
        for i in self.form:
           data.append(self.form[i].get())
        
        print(DB.add(data))

    def parse_xml(self):
        XMLTREE = xml.dom.minidom.parse("./views/contact.xml")
        nodeList = []

        if XMLTREE.childNodes:
            for node in XMLTREE.childNodes:
                for childNode in node.childNodes:
                    if childNode.nodeType == childNode.ELEMENT_NODE:
                        nodeList.append((childNode.attributes['name'].value, childNode.attributes['text'].value))
        return nodeList


