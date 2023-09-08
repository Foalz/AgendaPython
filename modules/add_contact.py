import sqlite3
import tkinter as tk
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import DB

class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        label = ttk.Label(self, text ="Agregar contacto",)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        self.bind("<<ShowFrame>>", self.onShowFrame)

    def onShowFrame(self, event):
        self.form = {}
        form_labels = self.parse_xml()
        row = 0
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
        DB.add(data)

    def parse_xml(self):
        XMLTREE = xml.dom.minidom.parse("./views/contact.xml")
        nodeList = []

        if XMLTREE.childNodes:
            for node in XMLTREE.childNodes:
                for childNode in node.childNodes:
                    if childNode.nodeType == childNode.ELEMENT_NODE:
                        nodeList.append((childNode.attributes['name'].value, childNode.attributes['text'].value))
        return nodeList


