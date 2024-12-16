import wx
from client_management import ClientManagementFrame,SearchClientFrame,AgregarCliente

class MyMenuBar(wx.MenuBar):
    def __init__(self, parent):
        super().__init__()
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, "Salir")
        self.Append(file_menu, "&Archivo")

        management_menu = wx.Menu()
        self.ID_ADD_CLIENT = wx.NewId()
        self.ID_SEARCH_CLIENT = wx.NewId()
        self.ID_SHOW_ALL_CLIENTS = wx.NewId()

        management_menu.Append(self.ID_ADD_CLIENT, "Agregar Clientes", "Agregar un nuevo cliente")
        management_menu.Append(self.ID_SEARCH_CLIENT, "Buscar Clientes", "Buscar un cliente existente")
        management_menu.Append(self.ID_SHOW_ALL_CLIENTS, "Mostrar Todos los Clientes", "Mostrar todos los clientes")
        self.Append(management_menu, "&Gestión de Clientes")

        parent.Bind(wx.EVT_MENU, self.on_exit, id=wx.ID_EXIT)
        parent.Bind(wx.EVT_MENU, self.on_add_client, id=self.ID_ADD_CLIENT)
        parent.Bind(wx.EVT_MENU, self.on_search_client, id=self.ID_SEARCH_CLIENT)
        parent.Bind(wx.EVT_MENU, self.on_show_all_clients, id=self.ID_SHOW_ALL_CLIENTS)

    def on_exit(self, event):
        wx.CallAfter(wx.GetApp().ExitMainLoop)

    def on_add_client(self, event):
        AgregarCliente("Agregar Cliente")

    def on_search_client(self, event):
        SearchClientFrame("Buscar Cliente")

    def on_show_all_clients(self, event):
        ClientManagementFrame("Mostrar Todos los Clientes")
