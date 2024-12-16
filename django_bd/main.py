import wx
from menu import MyMenuBar
from client_management import ClientManagementFrame

class aplicacion(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Gestión de clientes", size=(600, 400))
        frame.SetMenuBar(MyMenuBar(frame))
        frame.Show()
        return True

if __name__ == "__main__":
    app = aplicacion()
    app.MainLoop() 