from googlesearch import search
import socket
from tkinter import *

def get_first_website(company_name):
    query = f"{company_name} official website"
    websites = [] 
    try:
        for url in search(query, num_results=5):
            websites.append(url)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return websites

def executer(company_name, sus):
    global res
    legitIp = []
    try:
        susIp = socket.gethostbyname(sus.split("//")[1].split("/")[0])
    except:
        res['text'] = "Error occured"
        res['fg'] = 'red'
    websites = get_first_website(company_name)
    if websites:
        for i in websites:
            j = (i.split("//")[1]).split("/")[0]
            print(j)
            legitIp.append(socket.gethostbyname(j))
        if(susIp in legitIp):
            res['text'] = ("It's legit..!")
            res['fg'] = "green"
        else:
            res['text'] = ("Sus!!")
            res['fg'] = "red"
    else:
        res['text'] = (f"No websites found for {company_name}")
        res['fg'] = "yellow"


root = Tk()
root.geometry('500x400')
root.title("IP Legitmecy Checker")

l = Label(root, text="Legit?", font=("Helvetica", 20))
frm1 = Frame(root)
bt = Button(root, text = "CHECK", font=("Helvetica", 10), 
            command=lambda: executer(compe.get(), suse.get()))
res = Label(root, text = '', font=("courier new", 16), fg='green')

compl = Label(frm1, text="Company Name", width=20, anchor="w")
compe = Entry(frm1, width=30)
compl.grid(row=0, column=0, pady=10, padx=5)
compe.grid(row=0, column=1)

susl = Label(frm1, text="Sus Link", width=20, anchor="w")
suse = Entry(frm1, width=30)
susl.grid(row=1, column=0, pady=10, padx=5)
suse.grid(row=1, column=1)

l.pack(pady=40)
frm1.pack()
bt.pack(pady=40)
res.pack()

root.mainloop()