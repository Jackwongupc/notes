from tkinter import Tk
from time import sleep
from tkinter.messagebox import showwarning
import win32com.client as win32

warn=lambda app:showwarning(app,'Exit?')
Range=range(3,8)

def word():
    app='Word'
    word=win32.gencache.EnsureDispatch('%s.Application'%app)
    doc=word.Documents.Add()
    word.Visible=True
    sleep(1)

    rng=doc.Range(0,0)
    rng.InsertAfter('Python-to-%s Test \r\n\r\n'%app)
    sleep(1)
    for i in Range:
        rng.InsertAfter('line %d\r\n'%i)
        sleep(1)

    rng.InsertAfter("\r\n th-th-th-that")
    warn(app)
    doc.Close(False)
    word.Application.Quit()

if __name__=='__main__':
    Tk().withdraw()
    word()