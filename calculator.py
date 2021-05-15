from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk
from PIL import Image,ImageTk

root = themed_tk.ThemedTk()
root.get_themes()
root.set_theme('black')#breeze
root.title('CALCULATOR')
root.geometry('500x380')
root['bg'] = 'grey'

def clearscreen():
  calculation_entry.delete(0, END)

def insertvalues(value):
  existing_in_entrybox = calculation_entry.get()
  position_to_insertnewvalue = len(existing_in_entrybox)
  calculation_entry.insert(position_to_insertnewvalue,value)

def calculate():
  expression = calculation_entry.get()
  if '/' in expression:
    expression = expression.replace('/','//')
  if '^' in expression:
    expression = expression.replace('^','**')
  if '^2' in expression:
    expression = expression.replace('^2','**2')
  value = eval(expression)
  calculation_entry.delete(0, END)
  calculation_entry.insert(0, value)

calculation_entry = ttk.Entry(root,width=50,font=('calibre',10, 'bold'))
calculation_entry.pack(side='top',ipady=10,padx=5,pady=10)
#basic_calci
#calculation_entry = ttk.Entry(root,width=45,font=('calibre',10, 'bold')).grid(row=3,column=10,padx=38,pady=15,ipady=10)

basic_calci = ttk.LabelFrame(root,height=230,width=400).place(x=50,y=100)

button1=ttk.Button(basic_calci,text=1,command=lambda: insertvalues('1')).place(x=50,y=100)
button2=ttk.Button(basic_calci,text=2,command=lambda: insertvalues('2')).place(x=150,y=100)
button3=ttk.Button(basic_calci,text=3,command=lambda: insertvalues('3')).place(x=250,y=100) 
button_add = ttk.Button(basic_calci,text='+',command=lambda: insertvalues('+')).place(x=350,y=100)

button4=ttk.Button(basic_calci,text=4,command=lambda: insertvalues('4')).place(x=50,y=137) 
button5=ttk.Button(basic_calci,text=5,command=lambda: insertvalues('5')).place(x=150,y=137)
button6=ttk.Button(basic_calci,text=6,command=lambda: insertvalues('6')).place(x=250,y=137)
button_subt = ttk.Button(basic_calci,text='-',command=lambda: insertvalues('-')).place(x=350,y=137)

button7=ttk.Button(basic_calci,text=7,command=lambda: insertvalues('7')).place(x=50,y=174)
button8=ttk.Button(basic_calci,text=8,command=lambda: insertvalues('8')).place(x=150,y=174)
button9=ttk.Button(basic_calci,text=9,command=lambda: insertvalues('9')).place(x=250,y=174)
button_mul = ttk.Button(basic_calci,text='*',command=lambda: insertvalues('*')).place(x=350,y=174)

button_zero=ttk.Button(basic_calci,text='0',command=lambda: insertvalues("0")).place(x=50,y=211)
button_open_brac=ttk.Button(basic_calci,text='(',command=lambda: insertvalues('(')).place(x=150,y=211)
button_close_brac=ttk.Button(basic_calci,text=')',command=lambda: insertvalues(')')).place(x=250,y=211)
button_div = ttk.Button(basic_calci,text='/',command=lambda: insertvalues('/')).place(x=350,y=211)

button_square=ttk.Button(basic_calci,text='x^2',command=lambda: insertvalues('^2')).place(x=50,y=245)
button_expo=ttk.Button(basic_calci,text='x^y',command=lambda: insertvalues('^')).place(x=150,y=245)
button_equal=ttk.Button(basic_calci,text='=',command=lambda: calculate()).place(x=250,y=245)#250,245
button_point = ttk.Button(basic_calci,text='.',command=lambda: insertvalues('.')).place(x=350,y=245)

button_clear = ttk.Button(basic_calci,text='Clear',command=clearscreen).pack(side='bottom',anchor='center',ipady=10,padx=5,pady=54)

root.mainloop()