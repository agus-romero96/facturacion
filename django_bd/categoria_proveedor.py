import wx
from db_connection import ObtenerCategorias,Categoria

class GestionCategorias(wx.Frame):
    def __init__(self, title="Gestión de Categorías"):
        super().__init__(None, title=title, size=(400, 400))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        # Lista de Categorías
        self.listbox = wx.ListBox(self.panel)
        self.sizer.Add(self.listbox, 1, wx.EXPAND | wx.ALL, 5)

        # Botón de más acciones
        self.actions_button = wx.Button(self.panel, label="Más acciones")
        self.sizer.Add(self.actions_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        # botón para agregar una nueva categoría
        self.add_button = wx.Button(self.panel, label="Agregar categoría")
        self.sizer.Add(self.add_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.add_button.Bind(wx.EVT_BUTTON, self.AgregarNuevaCategoria)
        # Configuración final
        self.panel.SetSizer(self.sizer)
        self.MostrarCategorias()
        self.Show()

    def MostrarCategorias(self):
        self.listbox.Clear()
        categorias = ObtenerCategorias()
        for categoria in categorias:
            self.listbox.Append(categoria)
    
    def MasAcciones(self, event):
        """Muestra un menú con las acciones disponibles para el la categoría seleccionada."""
        selection = self.listbox.GetSelection()
        if selection == wx.NOT_FOUND:
            wx.MessageBox("Por favor, seleccione una categoría primero.", "Error", wx.ICON_ERROR)
            return
        selected_category = self.listbox.GetString(selection)
        # Crear el menú de opciones
        menu = wx.Menu()
        # Agregar acciones al menú
        delete_item = menu.Append(wx.ID_ANY, "Eliminar")
        update_item = menu.Append(wx.ID_ANY, "Actualizar")
        # Conectar las acciones
        self.Bind(wx.EVT_MENU, lambda evt: self.EliminarCategoria(selected_category), delete_item)
        self.Bind(wx.EVT_MENU, lambda evt: self.ActualizarCategoria(selected_category), update_item)
        # Mostrar el menú
        self.PopupMenu(menu)
        menu.Destroy()
    def EliminarCategoria(self, category):
        """Elimina una categoría de la base de datos."""
        try:
            if wx.MessageBox(
                "¿Está seguro de eliminar esta categoría?",
                "Confirmar eliminación",
                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION
            ) == wx.YES:
                categoria_obj = Categoria.objects.get(nombre=category)
                categoria_obj.delete()
                self.MostrarCategorias()  # Actualizar la lista
        except Exception as e:
            wx.MessageBox(f"Error al eliminar la categoría: {str(e)}", "Error", wx.ICON_ERROR)

    def AgregarCategorias(self):
