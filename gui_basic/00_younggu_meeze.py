from tkinter import *
root = Tk()

root.geometry("640x480")
root.title("Nado GUI")

photo = PhotoImage(file = "gui_basic/img.png")

label1 = Label(root, text = "안녕하세요", fg = "red")
label1.pack()
label2 = Label(root, image = photo)
label2.pack()
def change():
    global photo2
    photo2 = PhotoImage(file = "gui_basic/img2.png")
    label1.config(image=photo2)
    label2.config(text="또 만나요")## 글자->그림은 되는데 역은 안됨


btn = Button(root, text = "클릭", command = change)
btn.pack()

root.mainloop()