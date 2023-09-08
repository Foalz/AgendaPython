import sqlite3
import tkinter as tk
from tkinter import ttk
import xml.dom.minidom

class Find(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Todos los contactos",)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        self.contact_table()

    def contact_table(self, contact_list=[]):
        self.columns = self.parse_xml()

        self.tree = ttk.Treeview(self, columns=self.columns, show='headings')
        self.tree.heading('name', text='Name')
        self.tree.heading('phone_number', text='Phone Number')
        self.tree.heading('email', text='Email Address')
        
        self.tree.insert('', 'end', values=[('nombre', 'hola', 'mundo')])
        self.tree.grid(row=0, column=0, sticky='nsew')

    def parse_xml(self):
        XMLTREE = xml.dom.minidom.parse("./views/contact.xml")
        nodeList = [] 
        if XMLTREE.childNodes:
            for node in XMLTREE.childNodes:
                for childNode in node.childNodes:
                    if childNode.nodeType == childNode.ELEMENT_NODE:
                        nodeList.append(childNode.attributes['name'].value)
        nodeList.append('action')
        return tuple(nodeList)

