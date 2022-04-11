#создай тут фоторедактор Easy Editor!
from PyQt5.QtWidgets import *
from PIL import Image
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt 
import os
from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN,
   GaussianBlur, UnsharpMask
)

app =   QApplication([])
win = QWidget()
btn_dir = QPushButton('Папка')
win.resize(700,400)
img_list = QListWidget()
fid = QLabel('картинка')
btn1 = QPushButton('Лево')
btn2 = QPushButton('Право')
btn3 = QPushButton('Зеркало')
btn4 = QPushButton('Резкость')
btn5 = QPushButton('Ч/Б')

l1 = QVBoxLayout()
l3 = QHBoxLayout()
l2 = QVBoxLayout()
l4 = QHBoxLayout()

l1.addWidget(btn_dir)
l1.addWidget(img_list)
l3.addWidget(btn1)
l3.addWidget(btn2)
l3.addWidget(btn3)
l3.addWidget(btn4)
l3.addWidget(btn5)
l2.addWidget(fid)
l2.addLayout(l3)
l4.addLayout(l1)
l4.addLayout(l2)
win.setLayout(l4)
import os
workdir = ''

def filter(filenames, extentions):
    risalt = []
    for fn in filenames:
        for ex in extentions:
            if fn.endswith(ex):
                risalt.append(fn)
    print(risalt)
    return risalt


def showFilenamesList():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    filenames = os.listdir(workdir)
    filenames = filter(filenames, ['jpg', 'png', 'gif', 'tif'])
    img_list.clear()
    img_list.addItems(filenames)
class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None
    def load_image(self, dir, filename):
        self.image_path = os.path.join(dir, filename)
        self.dir = dir
        self.filename = filename
        self.image = Image.open(self.image_path)
    def show_image(self):
        pixmap = QPixmap(self.image_path)
        w = fid.width()
        h = fid.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        fid.setPixmap(pixmap)
    def black_white(self):
        self.image = self.image.convert('L')
        self.save_image()
        self.show_image()
    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        self.show_image()
    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        self.show_image()
    def miror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        self.show_image()
    def rezk(self):
        self.image = self.image.filter(DETAIL)
        self.save_image()
        self.show_image()

    
    def save_image(self):
        #path = os.path.join(self.dir, 'redacted/')
        self.image_path = self.dir + "/redacted/" + self.filename
        
        #self.image_path = os.path.join(path, self.filename)
        self.image.save(self.image_path)
IP = ImageProcessor()

btn1.clicked.connect(IP.left)
btn2.clicked.connect(IP.right)
btn3.clicked.connect(IP.miror)
btn4.clicked.connect(IP.rezk)
btn5.clicked.connect(IP.black_white)

btn_dir.clicked.connect(showFilenamesList)

def click_image():
    print('картинка выбрана')
    filename = img_list.currentItem().text()
    global workdir
    IP.load_image(workdir, filename)
    IP.show_image()
img_list.itemClicked.connect(click_image)







win.show()
app.exec_()








