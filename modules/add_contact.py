import sqlite3
import tkinter as tk
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import Database

class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="Agregar contacto",)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        form = {}
        form_labels = self.parse_xml()
        i = 0
        for form_label in form_labels:
            ttk.Label(self, text=form_label[1]).place(x=50, y=50 + i)
            i+=50

    def parse_xml(self):
        XMLTREE = xml.dom.minidom.parse("./views/contact.xml")
        nodeList = []

        if XMLTREE.childNodes:
            for node in XMLTREE.childNodes:
                for childNode in node.childNodes:
                    if childNode.nodeType == childNode.ELEMENT_NODE:
                        nodeList.append((childNode.attributes['name'].value, childNode.attributes['text'].value))
        return nodeList


