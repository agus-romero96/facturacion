import wx
from client_management import ClientManagementFrame,SearchClientFrame,AgregarCliente
from gestor_de_productos import GestionProductos
from agregar_producto import AgregarProducto

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
        # Menú Gestión de Productos
        product_menu = wx.Menu()
        self.ID_ADD_PRODUCT = wx.NewId()
        self.ID_SHOW_ALL_PRODUCTS = wx.NewId()

        product_menu.Append(self.ID_ADD_PRODUCT, "Agregar Producto", "Agregar un nuevo producto")
        product_menu.Append(self.ID_SHOW_ALL_PRODUCTS, "Mostrar Todos los Productos", "Mostrar todos los productos")
        self.Append(product_menu, "&Gestión de Productos")

        parent.Bind(wx.EVT_MENU, self.on_salir, id=wx.ID_EXIT)
        parent.Bind(wx.EVT_MENU, self.on_add_client, id=self.ID_ADD_CLIENT)
        parent.Bind(wx.EVT_MENU, self.on_search_client, id=self.ID_SEARCH_CLIENT)
        parent.Bind(wx.EVT_MENU, self.on_show_all_clients, id=self.ID_SHOW_ALL_CLIENTS)
        parent.Bind(wx.EVT_MENU, self.on_add_product, id=self.ID_ADD_PRODUCT)
        parent.Bind(wx.EVT_MENU, self.on_show_all_products, id=self.ID_SHOW_ALL_PRODUCTS)

    def on_salir(self, event):
        wx.CallAfter(wx.GetApp().ExitMainLoop)

    def on_add_client(self, event):
        AgregarCliente("Agregar Cliente")

    def on_search_client(self, event):
        SearchClientFrame("Buscar Cliente")

    def on_show_all_clients(self, event):
        ClientManagementFrame("Mostrar Todos los Clientes")
    def on_add_product(self, event):
        AgregarProducto()

    def on_show_all_products(self, event):
        GestionProductos()