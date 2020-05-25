from tkinter import *
import tkinter.ttk as ttk
import urllib.request
import xml.dom.minidom

response = urllib.request.urlopen(\
"http://www.cbr.ru/scripts/XML_daily.asp?date_req=20/05/2000")
print(response)
print('result code: ' + str(response.getcode()))
#read_page = response.read()
#print(read_page.decode('utf-8'))
#print(read_page)
doc = xml.dom.minidom.parse(response)

valute = doc.getElementsByTagName("Valute")
names = []
for val in valute:
   name = val.getElementsByTagName("Name")[0]
   names.append(name.firstChild.data)
   #childList=val.childNodes
   #for child in childList:
   #     print(child.nodeName)
   #     print(child.childNodes[0].nodeValue)

window = Tk()
window.title("Конвертер валют")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control) 
tab2 = ttk.Frame(tab_control) 
tab_control.add(tab1, text="Курс")
tab_control.add(tab2, text="График")


srcValute = ttk.Combobox(tab1)
srcValute["values"] = [i for i in names]
srcValute.grid(column=0, row=0)

convValute = ttk.Combobox(tab1)
convValute["values"] = [i for i in names]
convValute.grid(column=2, row=0)

txt = Entry(tab1)
#btn = Button(tab1, text="Действ.", command=click)
lbl = Label(tab1,text="")

tab_control.pack(expand=1,fill='both')
window.mainloop()
