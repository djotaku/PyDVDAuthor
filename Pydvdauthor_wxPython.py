import wx, os

from dvdauthor import dvdauthorxml

__program_name__ = "Pydvdauthor wxPython"
__author__ = "Eric Mesa"
__version__ = "v0.1.6"
__license__ = "GNU GPL v3"
__copyright__ = "(c)2008 Eric Mesa"
__email__ = "ericsbinaryworld at gmail dot com"

def cXML(event):
    ptdvd = pathtodvd.GetValue()
    ptvideo = pathtovideo.GetValue()
    chapters2 = chapters.GetValue().split(",")
    dvdauthorxml(ptdvd, ptvideo, chapters2)
    d = wx.MessageDialog( win, "Now look for the file named dvdauthor.xml.  It should be in this path, then type dvdauthor -x dvdauthor.xml","What to do next", wx.OK)
    d.ShowModal()
    d.Destroy()

ID_ABOUT = 101
ID_EXIT = 110

app = wx.App()
win = wx.Frame(None, title="Pydvdauthor", size=(500,500))

bkg = wx.Panel(win)

#the text boxes
pathtodvd = wx.TextCtrl(bkg)
pathtovideo = wx.TextCtrl(bkg)
chapters = wx.TextCtrl(bkg)

text1 = wx.StaticText(bkg, -1, "Please enter the path where you want the DVD files created.  This must be a full path (eg /home/user_name/spamalot)")
text2 = wx.StaticText(bkg, -1, "Please enter the path and filename where the video can be found.  At this time, this must be an MPEG-2 DVD compliant video (eg /home/user/spamspamspam.mpg)")
text3 = wx.StaticText(bkg, -1, "Please enter the times where you want a chapter to be created.  \n Enter this in the format of \n hour:minute:seconds.  \n If you don't want any chapters then at least enter 0. \n Separate all chapters with a comma. (eg 0, 14:30, 19:34)")

createXML = wx.Button(bkg, label="Create XML")
createXML.Bind(wx.EVT_BUTTON, cXML)

hbox1 = wx.BoxSizer()
hbox2 = wx.BoxSizer()
hbox3 = wx.BoxSizer()
hbox4 = wx.BoxSizer()
hbox5 = wx.BoxSizer()
hbox6 = wx.BoxSizer()
hbox7 = wx.BoxSizer()

hbox1.Add(text1, proportion=1, flag=wx.EXPAND)
hbox2.Add(pathtodvd, proportion=1, flag=wx.EXPAND)
hbox3.Add(text2, proportion=1, flag=wx.EXPAND)
hbox4.Add(pathtovideo, proportion=1, flag=wx.EXPAND)
hbox5.Add(text3, proportion=1, flag=wx.EXPAND)
hbox6.Add(chapters, proportion=1, flag=wx.EXPAND)
hbox7.Add(createXML, proportion=1, flag=wx.EXPAND)


vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox1, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox2, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox3, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox4, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox5, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox6, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(hbox7, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)

#menu and status bar
win.CreateStatusBar()
filemenu = wx.Menu()
filemenu.Append(ID_ABOUT, "&About", "Information About Pydvdauthor")
filemenu.AppendSeparator()
filemenu.Append(ID_EXIT, "&Exit", "Exit")
menuBar = wx.MenuBar()
menuBar.Append(filemenu, "&File")
win.SetMenuBar(menuBar)

def OnAbout(e):
    d = wx.MessageDialog( win, "A small utility to create dvdauthor xml file\n\n\n" + __program_name__ + "\nby\n" + __author__ + "\n" + __license__ + "\n"  + __copyright__, "About " + __program_name__ + __version__, wx.OK)
    d.ShowModal()
    d.Destroy()

def OnExit(e):
    win.Close(True)

#attach menu event to to method
wx.EVT_MENU(win, ID_ABOUT, OnAbout)
wx.EVT_MENU(win, ID_EXIT, OnExit)

bkg.SetSizer(vbox)

#show the window
win.Show()

#start the program
app.MainLoop()
