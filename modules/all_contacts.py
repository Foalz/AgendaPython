import sqlite3
import tkinter as tk
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import DB

class All(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Todos los contactos",)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        self.contact_table()

    def contact_table(self, contact_list=[]):
        self.columns = self.parse_xml()
        columns = tuple([i[0] for i in self.columns])
        self.tree = ttk.Treeview(self, columns=columns, show='headings')

        for name, text in self.columns:
            self.tree.heading(name, text=text)
        self.tree.grid(row=0, column=0, sticky='nsew')
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        
        dbquery = DB.get_all()
        contacts = [i for i in dbquery]
        
        for contact in contacts:
            self.tree.insert('', tk.END, values=contact)

    def OnDoubleClick(self, event):
        item = self.tree.selection()
        print("you clicked on", self.tree.item(item,"values"))

    def parse_xml(self):
        XMLTREE = xml.dom.minidom.parse("./views/contact.xml")
        nodeList = []

        if XMLTREE.childNodes:
            for node in XMLTREE.childNodes:
                for childNode in node.childNodes:
                    if childNode.nodeType == childNode.ELEMENT_NODE:
                        nodeList.append((childNode.attributes['name'].value, childNode.attributes['text'].value))
        return nodeList

