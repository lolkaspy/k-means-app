from tkinter import *
from tkinter.filedialog import *
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle

def rampage():
    t=asksaveasfilename()
    plt.savefig(t)

def ownage():
        zt=askopenfilename()
        b=Toplevel(root)
        b.resizable(width=False, height=False)
        oh=Image.open(zt)
        lel=ImageTk.PhotoImage(oh)
        topimg=Label(b,image=lel)
        topimg.pack(side="bottom", fill="both", expand="yes")
        global lel, oh

def compute(event):
    if clusters()!='' or clusters()!=0:
        img = oh
        img = np.array(img, dtype=np.float64) / 255
        w, h, d = original_shape = tuple(img.shape)
        assert d == 3
        image_array = np.reshape(img, (w * h, d))
        image_array_sample = shuffle(image_array, random_state=0)[:1000]
        kmeans = KMeans(n_clusters=clusters(), random_state=0).fit(image_array_sample)
        labels = kmeans.predict(image_array)
        plt.figure(2)
        plt.clf()
        ax = plt.axes([0, 0, 1, 1])
        plt.axis('off')
        q=recreate_image(kmeans.cluster_centers_, labels, w, h)
        plt.imshow(q)
        a['text']='Сжатие произведено,\n сохраните, посмотрите!'
        
def recreate_image(codebook, labels, w, h):
    d = codebook.shape[1]
    image = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            image[i][j] = codebook[labels[label_idx]]
            label_idx += 1
    return image

def clusters():
    a=e.get('1.0', END+'-1c')
    return int(a)

root=Tk()

root.title('kmeans 2018')
root.iconbitmap(u'C:\Documents and Settings\Dima B\Мои документы\Downloads\\auto-repair.ico')
root.geometry('360x35')
m=Menu(root)
root.config(menu=m)
u=Menu(m)
m.add_cascade(label='Файл',menu=u)
u.add_command(label='Открыть...', command=ownage)
u.add_command(label='Выйти', command=root.destroy)
root.resizable(width=False, height=False)
a = Label(root, text='Укажите число кластеров:', bg='white', width=23, height=2)
b = Button(root, text='Сжать', bg='white', width=5, height=2)
c = Button(root, text='Выйти', bg='white', command=root.destroy, width=5, height=2)
e = Text(root, width=5, height=2)
ch = Button(root, text='Сохранить как...', width=15, height=2, command=rampage,bg='white')
b.bind("<ButtonRelease-1>",compute)
a.place(x=0,y=0)
b.place(x=180,y=0)
c.place(x=320,y=0)
ch.place(x=220,y=0)
e.place(x=140,y=0)

root.mainloop()




