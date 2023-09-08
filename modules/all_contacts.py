import sqlite3
import tkinter as tk
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import DB
import logging

logging.basicConfig(filename="logs.log", encoding='utf-8', level=logging.DEBUG)

class All(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logging.info("Rendering frame all_contacts")

        self.controller = controller
        title = tk.Label(self, text="Lista de Contactos", font=("Arial", 25))
        title.grid(row = 1, column = 1)
        go_back_btn = tk.Button(self, text="Volver al Menu", 
        command= lambda: self.controller.go_back())
        go_back_btn.grid(row=1, column=0)
        
        logging.info("Rendered successfully")
        self.bind("<<ShowFrame>>", self.onShowFrame)

    def onShowFrame(self, contact_list=[]):
        logging.info("Building view from ./views/contact.xml")
        self.columns = self.parse_xml()
        columns = tuple([i[0] for i in self.columns])

        #Creating UI components
        self.label = ttk.Label(self, text ="Buscar por:",).grid(row = 2, column = 0, padx = 10, pady = 10)
        self.search = tk.Entry(self, width=40)
        self.search.grid(row = 2, column = 1,)
        self.search_btn = ttk.Button(self, text="Buscar",
        command= lambda: self.find_contact(self.search.get())).grid(row = 2, column = 2, padx = 10, pady = 10)
        self.clear_filter_btn = ttk.Button(self, text="Limpiar filtro", 
        command= lambda: self.clear_filter()).grid(row = 2, column = 3, padx = 10, pady = 10)
        self.tree = ttk.Treeview(self, columns=columns, show='headings', selectmode="browse")
        vsb= ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        vsb.place(x=730, y=95, height=220)
        self.tree.configure(yscrollcommand=vsb.set)

        #Displaying all structure that was previously parsed from parse_xml method.
        for name, text in self.columns:
            self.tree.heading(name, text=text)
        self.tree.grid(row=3, column=1, sticky='nsew')
        logging.info("View built successfully!")
        
        #Getting all contacts from database
        self.contacts = [i for i in DB.get_all()]
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=contact)

    def find_contact(self, data):
        #Finding a contact by name in the database
        for item in self.tree.get_children():
            #First, we have to delete all the information that is currently displayed on the table
            self.tree.delete(item)
        self.contacts = [i for i in DB.find(data)]

        #And then write the new info that user wants.
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=contact)
    
    def clear_filter(self):
        #First, we have to delete all the information that is currently displayed on the table
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.search.delete(0, tk.END)
        self.contacts = [i for i in DB.get_all()]
        
        #And then write again all users on the table.
        for contact in self.contacts:
            self.tree.insert('', tk.END, values=contact)


    def parse_xml(self):
        #This method parses all the content on the <contact/> tag, to be displayed on contacts table
        logging.info("Parsing XML...")
        XMLTREE = xml.dom.minidom.parse("./views/contact.xml")
        nodeList = []

        if XMLTREE.childNodes:
            for node in XMLTREE.childNodes:
                for childNode in node.childNodes:
                    if childNode.nodeType == childNode.ELEMENT_NODE:
                        nodeList.append((childNode.attributes['name'].value, childNode.attributes['text'].value))
        logging.info("XML successfully parsed")
        return nodeList

