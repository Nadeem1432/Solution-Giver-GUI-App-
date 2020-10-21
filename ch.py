from tkinter import *
from tkinter.ttk import Combobox
from howdoi import howdoi
from tkinter.font import Font
import wikipedia
from tkinter import ttk
from tkinter import messagebox  


def Listen():
    import pyttsx3
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    T=answer.get(1.0,END)
    if len(T)>1:
                    
            engine.say(T)
            engine.runAndWait()
    else:
           engine.say("Sorry ! There is no data to speak !!")
           engine.runAndWait()


def Copy(event=""):
    data = answer.get(1.0,END)
    if len(data)>1:
        root.clipboard_clear()
        root.clipboard_append(data)
        messagebox.showinfo("information","you have successfully copeid to paste.")
    else:
         messagebox.showerror("Error","Sorry ! there is no data to copy.")



def Clear():
        answer.delete(1.0,END)

def Exit():

    e=messagebox.askquestion("exit","Are you sure to confirm to exit.")
    if e=="yes":
        root.quit()
        



def theory():        
        entry_value=search_entry.get()
        answer.delete(1.0,END)
        try:
            answer_value=wikipedia.summary(entry_value)
            answer.insert(INSERT,answer_value)
        except:
            answer.insert(INSERT,"please check your input  Or  check your internet connection")




def code():
    answer.delete(1.0,END)
    try:
        entry_value=search_entry.get()
        parser = howdoi.get_parser()
        args = vars(parser.parse_args(entry_value.split(' ')))

        output = howdoi.howdoi(args)
        answer.insert(INSERT,output)
    except:
        answer.insert(INSERT,"Internet Connection Error!!!")


    
    





def main():
    
    if type_combobox.get() == 'CODE':
        if len(search_entry.get())>1:
            code()
        else:
            answer.delete(1.0,END)
            answer.insert(INSERT,"please enter something related code...")
        
    elif type_combobox.get() == 'THEORY':
        if len(search_entry.get())>1:
            theory()
        else:
            answer.delete(1.0,END)
            answer.insert(INSERT,"please enter something related theory...")
        

    else:
        answer.delete(1.0,END)     
        answer.insert(INSERT,"please select a type")
                

    
root=Tk()
root.title("Code Helper")
root.geometry("400x400")
root.config(bg='navy',bd=5,relief=GROOVE)
##root.iconbitmap(".img/icon.ico")
#====fonts=====#
f1=Font(size=20,family="Cambria",weight="bold")

f3=Font(size=10,family="arial",weight='bold')


#===title_Lable===#
name_label=Label(root,text="Code Helper",font=f1,height=1,fg="navy",bg="ghostwhite",bd=5,relief=GROOVE)
name_label.place(x=100,y=0)


frame1=Frame(root,bg='slateblue')
frame1.pack(side=TOP,pady=50)

search_entry=Entry(frame1,width=30,bd=5, relief = RIDGE,font=f3)
search_entry.grid(row=0,column=1)

search_button=Button(frame1,text="Search",fg="white",bg="blue",width=5,bd=5,command=main)
search_button.grid(row=0,column=3,padx=5)
types= ["CODE","THEORY"]
type_combobox=ttk.Combobox(frame1,values=types,width=8,font=f3)
type_combobox.grid(row=0,column=0)
type_combobox.set("    TYPE")






frame2=Frame(root,bg='slateblue')


scroll=ttk.Scrollbar(frame2)
scroll.pack(side=RIGHT,fill=Y)


answer=Text(frame2,width=50,height=12,wrap=WORD,bd=5,yscrollcommand=scroll.set,font=f3)
answer.pack()
scroll.config(command=answer.yview)

btn_listen = Button(frame2,text="Listen",command=Listen,width=5,font=f3,bd=2,fg='navy',activebackground="blue",activeforeground="white")
btn_listen.pack(side=LEFT,padx=17,pady=5)

btn_copy = Button(frame2,text="Copy",command=Copy,width=5,font=f3,bd=2,fg='navy',activebackground="blue",activeforeground="white")
btn_copy.pack(side=LEFT,padx=17,pady=5)


btn_clear = Button(frame2,text="Clear",command=Clear,width=5,font=f3,bd=2,fg='navy',activebackground="blue",activeforeground="white")
btn_clear.pack(side=LEFT,padx=17,pady=5)


btn_exit = Button(frame2,text="Exit",command=Exit,width=5,font=f3,bd=2,fg='navy',activebackground="blue",activeforeground="white")
btn_exit.pack(side=LEFT,padx=17,pady=5)


frame2.pack()








root.mainloop()
