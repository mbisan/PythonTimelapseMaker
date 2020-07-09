import cv2
import glob
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()

class MainWindow:
    def __init__(self, win):
        self.win = win
        self.n = 0
        self.rotation = 0

        self.images = self.load_images()
        self.cur_img = None
        self.size = None

        self.print_window()

    def print_window(self):
        for widget in self.win.winfo_children():
            widget.destroy()

        Button(self.win, text='<<', command=self.prev).grid(row=0, column=0) # self.back
        Button(self.win, text='>>', command=self.next).grid(row=0, column=1) # self.forw

        Button(self.win, text='Rotate_Left', command=self.rotate_left).grid(row=0, column=2) # self.rot_l
        Button(self.win, text='Rotate_Right', command=self.rotate_right).grid(row=0, column=3) # self.rot_r

        Button(self.win, text='Make Vid', command=self.make_video).grid(row=0, column=4) # self.rot_r

        img = Image.open(self.images[self.n])

        if self.rotation == 90:
            img = img.transpose(Image.ROTATE_90)
        elif self.rotation == 180:
            img = img.transpose(Image.ROTATE_180)
        elif self.rotation == 270:
            img = img.transpose(Image.ROTATE_270)

        self.size = img.size
        self.cur_img = ImageTk.PhotoImage(img.resize((self.size[0]//4, self.size[1]//4)))

        image = Label(self.win, image=self.cur_img)
        image.grid(row=1, column = 0, columnspan=20)

    def prev(self):
        if self.n>0:
            self.n -= 1
            self.print_window()

    def next(self):
        if self.n<len(self.images)-1:
            self.n += 1
            self.print_window()

    def rotate_left(self):
        self.rotation = (self.rotation+90)%360
        self.print_window()

    def rotate_right(self):
        self.rotation = (self.rotation-90)%360
        self.print_window()

    def make_video(self):
        self.win.destroy()

        l= len(self.images)
        ratio = l//50

        out = cv2.VideoWriter(self.dir+'/'+input('Video name: ')+'.avi', cv2.VideoWriter_fourcc(*'DIVX'),30,self.size)
        for i,img in enumerate(self.images):
            imbytes = cv2.imread(img)

            if self.rotation == 270:
                imbytes = cv2.rotate(imbytes,cv2.ROTATE_90_CLOCKWISE)
            elif self.rotation == 180:
                imbytes = cv2.rotate(imbytes,cv2.ROTATE_180)
            elif self.rotation == 90:
                imbytes = cv2.rotate(imbytes,cv2.ROTATE_90_COUNTERCLOCKWISE)

            out.write(imbytes)

            if i%ratio==0:
                print('#',end='', flush = True)

        print()
        out.release()
        input('Done, press any key to exit ... ')

    def load_images(self):
        self.dir = filedialog.askdirectory(initialdir = "./", title = "Select folder")
        print(self.dir)
        return glob.glob(self.dir + '/*.jpg')

app = MainWindow(root)
root.mainloop()
