from random import *
import tkinter as tk



root = tk.Tk()

root.geometry("500x400")

root['bg'] = 'yellow'

score = 0


instruction = tk.Label(root,text="Type in the color of the words, not the word text!")
instruction.pack()
i2 = tk.Label(root,text="Press space to start!")
i2.pack()

colors=["green","blue","red"]


root.title("Color Game")
label = tk.Label(root, fg="black", bg="yellow", font="Helvetica 30")
label.pack()


def spacepressed(event):
    global label
    counter_label(label)
    root.unbind("<space>")
    

counter=31
def counter_label(label):
    def count():
     global counter
     counter -= 1
     label.config(text=str(counter))
     if counter > 0:
          label.after(1000, count)
     if counter == 0:
          label.config(text="Time's Up!")
     if counter < 0:
          counter = 31
    count()

selected = choice(colors)

colorname = choice(colors)

nameofcolor = tk.Label(root, text=colorname, fg=selected, font="Helvetica 30")
nameofcolor.pack()

def reset():
    global nameofcolor
    global colorname
    global selected
    selected = choice(colors)
    colorname = choice(colors)
    if selected == colorname:
        reset()
    nameofcolor.config(text=colorname, fg=selected, font="Helvetica 30")
    nscore.config(text = "Score: " + str(score))
    cn.delete(0,100)

    
def enterpressed(event):
    global score
    cn.get()
    if cn.get() == selected:
        score = score+1
        cori.config(text = "Correct!")
        
    else:
        cori.config(text = "Incorrect")
    reset()



        
cori = tk.Label(root, bg="yellow")
cori.pack()

nscore= tk.Label(root, bg="yellow")
nscore.pack()


cn = tk.Entry(root)
cn.pack()



root.bind("<Return>",enterpressed)

root.bind("<space>",spacepressed)


root.mainloop()

