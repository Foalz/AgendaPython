import sqlite3
import logging
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import xml.dom.minidom
from .dbqueries import DB
import logging

logging.basicConfig(filename="logs.log", encoding='utf-8', level=logging.DEBUG)

class Add(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        logging.info("Rendering frame add_contact")

        self.controller = controller

        #Creating all components
        title = tk.Label(self, text="Agregar contacto", font=("Arial", 25))
        title.grid(row = 1, column = 1)
        go_back_btn = tk.Button(self, text="Volver al Menu", 
        command= lambda: self.controller.go_back())
        go_back_btn.grid(row=1, column=0)

        self.bind("<<ShowFrame>>", self.onShowFrame)
        logging.info("Rendered frame successfully")

    def onShowFrame(self, event):
        logging.info("Building view from ./views/contact.xml")
        self.form = {}
        form_labels = self.parse_xml()
        row = 2
        #Creating all components from parsed XML.
        for form_label in form_labels:
            ttk.Label(self, text=form_label[1]).grid(row = row, column = 1, padx = 10, pady = 10)
            self.form[form_label[0]] = ttk.Entry(self)
            self.form[form_label[0]].grid(row = row, column = 2, padx = 10, pady = 10)
            row+=1

        #Creating buttons
        submit_btn = ttk.Button(self, text="Crear contacto", 
        command = lambda: self.create_contact())
        submit_btn.grid(row = 10, column = 1, padx = 10, pady = 10)
        cancel_btn = ttk.Button(self, text="Cancelar", 
        command = lambda: self.controller.go_back())
        cancel_btn.grid(row = 11, column = 1, padx = 10, pady = 10)
        logging.info("View built successfully!")

    def create_contact(self):
        #The contact data has the following structure:
        #[name, phone_number, email]
        logging.info("Checking contact data")
        data = []
        for i in self.form:
           data.append(self.form[i].get())
        try:
            #Checks if name is empty
            if (data[0] == ""): raise Exception("El nombre del contacto no puede estar vacio.")
            #Checks if any contact data (phone_number or email are empty)
            elif (data[1] == "" and data[2] == ""): raise Exception("Debe colocar al menos el numero de telefono o email del contacto.")
            #Checks if email field is not null and is a valid email
            elif (data[2] != "" and "@" not in data[2]): raise Exception("Debe ingresar un correo electronico valido")

            #If data is correct, then proceed to add the contact
            DB.add(data)
            tk.messagebox.showinfo("Operacion exitosa", "El contacto ha sido agregado exitosamente.")
            self.controller.go_back()
        except Exception as e:
            logging.error(e)
            tk.messagebox.showerror("Error", e)

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


