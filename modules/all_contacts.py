import sqlite3
import tkinter as tk
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import DB
from .edit_contact import Edit

class All(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.bind("<<ShowFrame>>", self.onShowFrame)

    def onShowFrame(self, contact_list=[]):
        self.columns = self.parse_xml()
        columns = tuple([i[0] for i in self.columns])
        self.label = ttk.Label(self, text ="Buscar por:",).grid(row = 0, column = 1, padx = 10, pady = 10)
        self.search = ttk.Entry(self)
        self.search.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.search_btn = ttk.Button(self, text="Buscar",
        command= lambda: self.find_contact(self.search.get())).grid(row = 1, column = 2, padx = 10, pady = 10)
        self.clear_filter_btn = ttk.Button(self, text="Limpiar filtro", 
        command= lambda: self.clear_filter()).grid(row = 1, column = 3, padx = 10, pady = 10)
        self.tree = ttk.Treeview(self, columns=columns, show='headings')


        for name, text in self.columns:
            self.tree.heading(name, text=text)
        self.tree.grid(row=2, column=1, sticky='nsew')
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        
        self.contacts = [i for i in DB.get_all()]
        
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=contact)
        

    def OnDoubleClick(self, event):
        item = self.tree.selection()
        self.user_data = item
        self.controller.show_frame(Edit)      

    def find_contact(self, data):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.contacts = [i for i in DB.find(data)]
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=contact)
    
    def clear_filter(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.search.delete(0, tk.END)
        self.contacts = [i for i in DB.get_all()]
        
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=contact)


    def parse_xml(self):
        XMLTREE = xml.dom.minidom.parse("./views/contact.xml")
        nodeList = []

        if XMLTREE.childNodes:
            for node in XMLTREE.childNodes:
                for childNode in node.childNodes:
                    if childNode.nodeType == childNode.ELEMENT_NODE:
                        nodeList.append((childNode.attributes['name'].value, childNode.attributes['text'].value))
        return nodeList

