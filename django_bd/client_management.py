import wx
from db_connection import ObtenerClientes, Cliente

class ClientManagementFrame(wx.Frame):
    def __init__(self, title):
        super().__init__(None, title=title, size=(400, 400))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Lista de clientes
        self.listbox = wx.ListBox(self.panel)
        self.sizer.Add(self.listbox, 1, wx.EXPAND | wx.ALL, 5)

        # Botón de más acciones
        self.actions_button = wx.Button(self.panel, label="Más acciones")
        self.sizer.Add(self.actions_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.actions_button.Bind(wx.EVT_BUTTON, self.on_actions)

        # Configuración final
        self.panel.SetSizer(self.sizer)
        self.populate_clients()

        self.Show()

    def populate_clients(self):
        """Llena la lista con los clientes de la base de datos."""
        self.listbox.Clear()  # Limpia la lista antes de rellenarla
        clients = ObtenerClientes()  # Obtener clientes de la base de datos
        for client in clients:
            self.listbox.Append(client)  # Agregar clientes a la lista

    def on_actions(self, event):
        """Muestra un menú con las acciones disponibles para el cliente seleccionado."""
        selection = self.listbox.GetSelection()
        if selection == wx.NOT_FOUND:
            wx.MessageBox("Por favor, seleccione un cliente primero.", "Error", wx.ICON_ERROR)
            return

        selected_client = self.listbox.GetString(selection)

        # Crear el menú de opciones
        menu = wx.Menu()
        delete_item = menu.Append(wx.ID_ANY, "Borrar este cliente")
        update_item = menu.Append(wx.ID_ANY, "Actualizar/Modificar")

        # Conectar las acciones
        self.Bind(wx.EVT_MENU, lambda evt: self.delete_client(selected_client), delete_item)
        self.Bind(wx.EVT_MENU, lambda evt: self.update_client(selected_client), update_item)

        # Mostrar el menú
        self.PopupMenu(menu)
        menu.Destroy()

    def delete_client(self, client_str):
        """Elimina un cliente de la base de datos."""
        try:
            cedula = client_str.split(" ")[0]  # Extraer la cédula del cliente
            cliente = Cliente.objects.get(cedula=cedula)
            cliente.delete()
            wx.MessageBox("Cliente eliminado con éxito.", "Éxito", wx.ICON_INFORMATION)
            self.populate_clients()  # Actualizar la lista
        except Exception as e:
            wx.MessageBox(f"Error al eliminar el cliente: {e}", "Error", wx.ICON_ERROR)

    def update_client(self, client_str):
        """Abre una ventana para actualizar los datos del cliente seleccionado."""
        cedula = client_str.split(" ")[0]  # Extraer la cédula del cliente
        cliente = Cliente.objects.get(cedula=cedula)
        UpdateClientFrame(cliente)  # Pasar el cliente seleccionado a la ventana de actualización


class UpdateClientFrame(wx.Frame):
    def __init__(self, cliente):
        super().__init__(None, title="Actualizar Cliente", size=(400, 500))
        self.cliente = cliente
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Campo de entrada para el nombre
        self.name_label = wx.StaticText(self.panel, label="Nombre:")
        self.sizer.Add(self.name_label, 0, wx.ALL, 5)
        self.name_input = wx.TextCtrl(self.panel, value=cliente.nombre)
        self.sizer.Add(self.name_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el apellido
        self.surname_label = wx.StaticText(self.panel, label="Apellido:")
        self.sizer.Add(self.surname_label, 0, wx.ALL, 5)
        self.surname_input = wx.TextCtrl(self.panel, value=cliente.apellido)
        self.sizer.Add(self.surname_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el email
        self.email_label = wx.StaticText(self.panel, label="Email:")
        self.sizer.Add(self.email_label, 0, wx.ALL, 5)
        self.email_input = wx.TextCtrl(self.panel, value=cliente.email or "")
        self.sizer.Add(self.email_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el teléfono
        self.telefono_label = wx.StaticText(self.panel, label="Teléfono:")
        self.sizer.Add(self.telefono_label, 0, wx.ALL, 5)
        self.telefono_input = wx.TextCtrl(self.panel, value=cliente.telefono or "")
        self.sizer.Add(self.telefono_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para la dirección
        self.direccion_label = wx.StaticText(self.panel, label="Dirección:")
        self.sizer.Add(self.direccion_label, 0, wx.ALL, 5)
        self.direccion_input = wx.TextCtrl(self.panel, value=cliente.direccion or "", style=wx.TE_MULTILINE)
        self.sizer.Add(self.direccion_input, 1, wx.EXPAND | wx.ALL, 5)

        # Botón para guardar los cambios
        self.save_button = wx.Button(self.panel, label="Guardar cambios")
        self.sizer.Add(self.save_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save)

        # Configuración final
        self.panel.SetSizer(self.sizer)
        self.Show()

    def on_save(self, event):
        """Guarda los cambios realizados en el cliente."""
        try:
            self.cliente.nombre = self.name_input.GetValue()
            self.cliente.apellido = self.surname_input.GetValue()
            self.cliente.email = self.email_input.GetValue()
            self.cliente.telefono = self.telefono_input.GetValue()
            self.cliente.direccion = self.direccion_input.GetValue()
            self.cliente.save()
            wx.MessageBox("Cliente actualizado con éxito.", "Éxito", wx.ICON_INFORMATION)
            self.Close()
        except Exception as e:
            wx.MessageBox(f"Error al actualizar el cliente: {e}", "Error", wx.ICON_ERROR)





class SearchClientFrame(wx.Frame):
    def __init__(self, title):
        super().__init__(None, title=title, size=(400, 300))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Campo de entrada para buscar
        self.search_label = wx.StaticText(self.panel, label="Buscar por Nombre:")
        self.sizer.Add(self.search_label, 0, wx.ALL, 5)
        self.search_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.search_input, 0, wx.EXPAND | wx.ALL, 5)

        # Botón de búsqueda
        self.search_button = wx.Button(self.panel, label="Buscar")
        self.sizer.Add(self.search_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.search_button.Bind(wx.EVT_BUTTON, self.on_search)

        # Lista de resultados
        self.result_list = wx.ListBox(self.panel)
        self.sizer.Add(self.result_list, 1, wx.EXPAND | wx.ALL, 5)

        # Configuración final
        self.panel.SetSizer(self.sizer)
        self.Show()

    def on_search(self, event):
        search_query = self.search_input.GetValue()

        if not search_query:
            wx.MessageBox("Ingrese un nombre para buscar.", "Error", wx.ICON_ERROR)
            return

        # Buscar en la base de datos
        results = Cliente.objects.filter(nombre__icontains=search_query)
        
        self.result_list.Clear()

        if not results:
            wx.MessageBox("No se encontraron clientes.", "Resultado", wx.ICON_INFORMATION)
            return

        for cliente in results:
            self.result_list.Append(f"{cliente.nombre} {cliente.apellido}")




class AgregarCliente(wx.Frame):
    def __init__(self, title):
        super().__init__(None, title=title, size=(400, 500))
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)

        # Campo de entrada para la cédula
        self.cedula_label = wx.StaticText(self.panel, label="Cédula:")
        self.sizer.Add(self.cedula_label, 0, wx.ALL, 5)
        self.cedula_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.cedula_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el nombre
        self.name_label = wx.StaticText(self.panel, label="Nombre:")
        self.sizer.Add(self.name_label, 0, wx.ALL, 5)
        self.name_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.name_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el apellido
        self.surname_label = wx.StaticText(self.panel, label="Apellido:")
        self.sizer.Add(self.surname_label, 0, wx.ALL, 5)
        self.surname_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.surname_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el email
        self.email_label = wx.StaticText(self.panel, label="Email:")
        self.sizer.Add(self.email_label, 0, wx.ALL, 5)
        self.email_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.email_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para el teléfono
        self.telefono_label = wx.StaticText(self.panel, label="Teléfono:")
        self.sizer.Add(self.telefono_label, 0, wx.ALL, 5)
        self.telefono_input = wx.TextCtrl(self.panel)
        self.sizer.Add(self.telefono_input, 0, wx.EXPAND | wx.ALL, 5)

        # Campo de entrada para la dirección
        self.direccion_label = wx.StaticText(self.panel, label="Dirección:")
        self.sizer.Add(self.direccion_label, 0, wx.ALL, 5)
        self.direccion_input = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.sizer.Add(self.direccion_input, 1, wx.EXPAND | wx.ALL, 5)

        # Botón para guardar
        self.save_button = wx.Button(self.panel, label="Guardar")
        self.sizer.Add(self.save_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.save_button.Bind(wx.EVT_BUTTON, self.on_save)
        # botón para cancelar.
        self.cancel_button = wx.Button(self.panel, label="Cancelar")
        self.sizer.Add(self.cancel_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        self.cancel_button.Bind(wx.EVT_BUTTON, self.on_cancel)
        
        
        # Configuración final
        self.panel.SetSizer(self.sizer)
        self.Show()
    def on_cancel(self, event):
        self.Close()

    def on_save(self, event):
        # Obtener los valores ingresados
        cedula = self.cedula_input.GetValue().strip()
        nombre = self.name_input.GetValue().strip()
        apellido = self.surname_input.GetValue().strip()
        email = self.email_input.GetValue().strip()
        telefono = self.telefono_input.GetValue().strip()
        direccion = self.direccion_input.GetValue().strip()

        # Validar campos requeridos
        if not cedula or not nombre or not apellido:
            wx.MessageBox("Los campos Cédula, Nombre y Apellido son obligatorios.", "Error", wx.ICON_ERROR)
            return

        # Validar longitud de la cédula y el teléfono
        if len(cedula) != 10 or (telefono and len(telefono) != 10):
            wx.MessageBox("La cédula y el teléfono deben tener 10 dígitos.", "Error", wx.ICON_ERROR)
            return

        # Guardar en la base de datos
        try:
            Cliente.objects.create(
                cedula=cedula,
                nombre=nombre,
                apellido=apellido,
                email=email if email else None,
                telefono=telefono if telefono else None,
                direccion=direccion if direccion else None
            )
            wx.MessageBox("Cliente agregado con éxito.", "Éxito", wx.ICON_INFORMATION)
            self.Close()
        except Exception as e:
            wx.MessageBox(f"Error al guardar el cliente: {e}", "Error", wx.ICON_ERROR)
