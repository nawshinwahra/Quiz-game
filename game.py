from tkinter import *

q=[
    "Capital of Bangladesh",
    "Name the world's biggest island",
    "Coolest Teacher of Cse depertment",
    "Longest sea beach of the world ",
    "National Anthem of Bangladesh",



]

options =[
    ["Dhaka","Khunla","Barisal","Jossor"] ,
    ["Greenland","Aberdeen","Abu Musa","Cayo Arenas"],
    ["Hero alam","Shakib Khan","Atanu Shome","Tom Cruse"],
    ["Potenga Sea beach","Kuakata Sea beach","Coxs Bazar","Deegha"],
    ["Chol Chol Chol","Amar Shoner Bangla","Dhono Dhanne","Amer Vai er Rokte Ragano"],


]

bkcolor='#FFFF00'
"""
def bkclolorset(color):
    if color==None:
        bkcolor='#66CCFF'
    else:
        bkcolor=color
"""
a=[1,1,3,3,2]

class Window(Frame):
    def red(self):

        bkcolor="#FF0000"

        print('done')


       # root.geometry("400x200+400+200")
        root.configure(background=bkcolor)


    def yellow(self):
        bkcolor = "#FFFF00"
        root.configure(background=bkcolor)

       # app = Quiz(root)
        #root.title("Quiz")
        #app = Window(root)
       # root.mainloop()
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
       # self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        theme = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        theme.add_command(label="Red",command=self.red)
        theme.add_command(label="Yellow", command=self.yellow)
        #bkcolor="#66FFFF"

        #added "file" to our menu
        menu.add_cascade(label="Theme", menu=theme)

    
    def client_exit(self):
        exit()

        






class Quiz:
    def __init__(self,master=None):
        
        

        
        
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master,self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        #self.button = Button(master, text="Back", command=self.back_btn)
       #self.button.pack(side=BOTTOM)

        self.button=Button(master, text="Next",command=self.next_btn,bg="GREEN")
        self.button.pack(side=BOTTOM)



    def create_q(self,master,qn):
        w = Label(master, text=q[qn],bg=bkcolor)
        print("q bk=",bkcolor)
        w.pack(side=TOP)
        return w
    def create_options(self,master, n):
        b_val =0
        b=[]
        while b_val < n:
            btn = Radiobutton(master, text="foo" , variable=self.opt_selected,value=b_val+1,bg=bkcolor)
            b.append(btn)
            btn.pack(side=TOP , anchor="w")
            b_val = b_val+1
        return b
    def display_q(self,qn):
        b_val =0
        self.opt_selected.set(0)
        self .ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1
            #b_val=2
    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False
    def print_result(self):
        print("Score: ",self.correct,"/", len(q))
        w = Label(root, text=len(q), bg=bkcolor)
        w.pack(side=RIGHT, anchor="se")
        w = Label(root, text="/", bg=bkcolor)
        w.pack(side=RIGHT, anchor="se")
        w = Label(root, text=self.correct, bg=bkcolor)
        w.pack(side=RIGHT, anchor="se")
        w = Label(root, text="Score: ", bg=bkcolor)
        w.pack(side=RIGHT, anchor="se")

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.qn):
            print("correct")
            w = Label(root, text="Correct", bg=bkcolor)
            w.pack(side=RIGHT, anchor="w")
            #self.tag_confi("Correct")
            self.correct +=1
        else:
            print("Wrong")
            w = Label(root, text="Wrong", bg=bkcolor)
            w.pack(side=RIGHT,anchor="w")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.print_result()
        else:
            self.display_q(self.qn)

root =Tk()

root.geometry("400x200+400+200")
root.configure(background=bkcolor)
app = Quiz(root)
root.title("Quiz")
app = Window(root)
print(bkcolor)
root.mainloop()



