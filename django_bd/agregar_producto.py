import wx
from facturacion.models import Producto

class AgregarProducto(wx.Frame):
    def __init__(self, title="Agregar Producto"):
        super().__init__(None, title=title, size=(400, 600))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Campo de entrada para el código
        self.codigo_label = wx.StaticText(self.panel, label="Código:")
        self.sizer.Add(self.codigo_label, 0, wx.ALL, 5)
        self.codigo_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.codigo_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el nombre
        self.nombre_label = wx.StaticText(self.panel, label="Nombre:")
        self.sizer.Add(self.nombre_label, 0, wx.ALL, 5)
        self.nombre_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.nombre_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para la descripción
        self.descripcion_label = wx.StaticText(self.panel, label="Descripción:")
        self.sizer.Add(self.descripcion_label, 0, wx.ALL, 5)
        self.descripcion_input = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.sizer.Add(self.descripcion_input, 1, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el precio
        self.precio_label = wx.StaticText(self.panel, label="Precio:")
        self.sizer.Add(self.precio_label, 0, wx.ALL, 5)
        self.precio_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.precio_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el stock
        self.stock_label = wx.StaticText(self.panel, label="Stock:")
        self.sizer.Add(self.stock_label, 0, wx.ALL, 5)
        self.stock_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.stock_input, 0, wx.EXPAND | wx.ALL, 5)

        # Botón para guardar
        self.save_button = wx.Button(self.panel, label="Guardar")
        self.sizer.Add(self.save_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save)

        # Botón para cancelar
        self.cancel_button = wx.Button(self.panel, label="Cancelar")
        self.sizer.Add(self.cancel_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)

        self.panel.SetSizer(self.sizer)
        self.Show()

    def on_cancel(self, event):
        self.Close()

    def on_save(self, event):
        # Obtener los valores ingresados
        codigo = self.codigo_input.GetValue().strip()
        nombre = self.nombre_input.GetValue().strip()
        descripcion = self.descripcion_input.GetValue().strip()
        precio = self.precio_input.GetValue().strip()
        stock = self.stock_input.GetValue().strip()

        # Validar campos requeridos
        if not codigo or not nombre or not precio or not stock:
            wx.MessageBox("Los campos Código, Nombre, Precio y Stock son obligatorios.", "Error", wx.ICON_ERROR)
            return

        # Guardar en la base de datos
        try:
            Producto.objects.create(
                codigo=codigo,
                nombre=nombre,
                descripcion=descripcion if descripcion else None,
                precio=precio,
                stock=stock
            )
            wx.MessageBox("Producto agregado con éxito.", "Éxito", wx.ICON_INFORMATION)
            self.Close()
        except Exception as e:
            wx.MessageBox(f"Error al guardar el producto: {e}", "Error", wx.ICON_ERROR)
