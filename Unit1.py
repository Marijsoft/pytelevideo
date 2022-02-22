import os
from delphifmx import *
import urllib.request
useragent=urllib.request.build_opener()
useragent.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55')]
urllib.request.install_opener(useragent)
nfile = 'televideo.png'
img_url="https://www.televideo.rai.it/televideo/pub/tt4web/Nazionale/16_9_page-"
ex=".png"
global i
i=100


class Form1(Form):

    def __init__(self, owner):
        self.Image1 = Image
        self.ToolBar1 = ToolBar
        self.Button1 = Button
        self.Edit1 = Edit
        self.ClearEditButton1 = None
        self.Button2 = Button
        self.Button3 = Button
        self.Button4 = Button
        self.LoadProps(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Unit1.pyfmx"))

    def FormCreate(self, Sender):
        pass

    def FormClose(self, Sender, Action):
        if os.path.isfile(nfile):
            os.remove(nfile)
        exit
        pass

    def FormShow(self, Sender):
        self.Button1Click(Sender)
        pass

    def Button1Click(self, Sender):
        urllib.request.urlretrieve(img_url+"100.3.png", nfile)
        self.Image1.Bitmap.LoadFromFile("televideo.png")
        self.Edit1.Text="100"
        pass

    def Button2Click(self, Sender):
        urllib.request.urlretrieve(img_url+self.Edit1.Text+ex, nfile)
        self.Image1.Bitmap.LoadFromFile("televideo.png")
        global i
        i=int(self.Edit1.Text)
        self.Edit1.Text=str(i)
        pass

    def Button3Click(self, Sender):
        global i
        self.Edit1.Text=str(int(i-1))
        urllib.request.urlretrieve(img_url+self.Edit1.Text+ex, nfile)
        self.Image1.Bitmap.LoadFromFile("televideo.png")
        i=int(self.Edit1.Text)
        pass

    def Button4Click(self, Sender):
        global i
        self.Edit1.Text=str(int(i+1))
        urllib.request.urlretrieve(img_url+self.Edit1.Text+ex, nfile)
        self.Image1.Bitmap.LoadFromFile("televideo.png")
        i=int(self.Edit1.Text)
        pass

