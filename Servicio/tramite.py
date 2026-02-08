# Integrantes:
# - Collaguari Israel
# - Macias Brithany

from PySide6.QtWidgets import QMainWindow, QMessageBox
from UI.vtnPrincipal import Ui_interfaz
from Dominio.tramite import Tramite
from Dominio.cliente import Ciudadano
from Datos.tramite_DAO import TramiteDAO


class TramiteServicio(QMainWindow, Ui_interfaz):
    '''
    Clase que genera la lógica de los objetos de tipo trámite
    '''
    def __init__(self):
        super(TramiteServicio, self).__init__()
        self.ui = Ui_interfaz()
        self.ui.setupUi(self)

        # Variable para guardar el código original al buscar
        self.codigo_original = None

        # Conectar señales con slots
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnCrear.clicked.connect(self.crear)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)

    def validaciones(self):
        codigo = self.ui.TxTCodigo.text().strip()
        if not codigo:
            return {'valido': False, 'mensaje': 'El código de trámite es obligatorio.'}
        if len(codigo) < 1 or len(codigo) > 3:
            return {'valido': False, 'mensaje': 'El código debe tener entre 1 y 3 caracteres.'}
        descripcion = self.ui.TxTDescripcion.text().strip()
        if not descripcion:
            return {'valido': False, 'mensaje': 'La descripción es obligatoria.'}
        if len(descripcion) < 3:
            return {'valido': False, 'mensaje': 'La descripción debe tener al menos 3 caracteres.'}
        costo_texto = self.ui.TxTCosto.text().strip()
        if not costo_texto:
            return {'valido': False, 'mensaje': 'El costo es obligatorio.'}
        try:
            costo = float(costo_texto)
            if costo <= 0:
                return {'valido': False, 'mensaje': 'El costo debe ser mayor a 0.'}
        except ValueError:
            return {'valido': False, 'mensaje': 'El costo debe ser un número válido.'}
        cedula = self.ui.TxTCedula.text().strip()
        if not cedula:
            return {'valido': False, 'mensaje': 'La cédula del ciudadano es obligatoria.'}
        if not cedula.isdigit():
            return {'valido': False, 'mensaje': 'La cédula debe contener solo números.'}
        if len(cedula) != 10:
            return {'valido': False, 'mensaje': 'La cédula debe tener exactamente 10 dígitos.'}
        nombre = self.ui.TxTNombre.text().strip()
        if not nombre:
            return {'valido': False, 'mensaje': 'El nombre del ciudadano es obligatorio.'}
        if len(nombre) < 2:
            return {'valido': False, 'mensaje': 'El nombre debe tener al menos 2 caracteres.'}
        if not nombre.replace(' ', '').isalpha():
            return {'valido': False, 'mensaje': 'El nombre solo debe contener letras.'}
        apellido = self.ui.TxTApellido.text().strip()
        if not apellido:
            return {'valido': False, 'mensaje': 'El apellido del ciudadano es obligatorio.'}
        if len(apellido) < 2:
            return {'valido': False, 'mensaje': 'El apellido debe tener al menos 2 caracteres.'}
        if not apellido.replace(' ', '').isalpha():
            return {'valido': False, 'mensaje': 'El apellido solo debe contener letras.'}
        return {'valido': True, 'mensaje': 'Validación exitosa'}

    def crear(self):
        self.limpiar()
        self.ui.TxTCodigo.setFocus()
        self.mostrar_mensaje("Información", "Ingrese los datos del nuevo trámite.", QMessageBox.Information)

    def guardar(self):
        validacion = self.validaciones()
        if not validacion['valido']:
            self.mostrar_mensaje("Error de Validación", validacion['mensaje'], QMessageBox.Warning)
            return

        try:
            codigo = self.ui.TxTCodigo.text().strip()
            descripcion = self.ui.TxTDescripcion.text().strip()
            costo = float(self.ui.TxTCosto.text().strip())
            cedula = self.ui.TxTCedula.text().strip()
            nombre = self.ui.TxTNombre.text().strip()
            apellido = self.ui.TxTApellido.text().strip()
            ciudadano = Ciudadano(cedula, nombre, apellido)
            tramite = Tramite(codigo, descripcion, costo, ciudadano)
            resultado = TramiteDAO.insertar_tramite(tramite)
            if resultado['ejecuto']:
                self.mostrar_mensaje("Éxito", resultado['mensaje'], QMessageBox.Information)
                self.limpiar()
            else:
                self.mostrar_mensaje("Error", resultado['mensaje'], QMessageBox.Critical)

        except ValueError as ve:
            self.mostrar_mensaje("Error de Validación", str(ve), QMessageBox.Warning)
        except Exception as e:
            self.mostrar_mensaje("Error", f"Error inesperado: {str(e)}", QMessageBox.Critical)

    def buscar(self):
        codigo = self.ui.TxTBuscarTramite.text().strip()
        if not codigo:
            self.mostrar_mensaje("Advertencia", "Ingrese un código de trámite para buscar.", QMessageBox.Warning)
            self.ui.TxTBuscarTramite.setFocus()
            return

        try:
            tramite = TramiteDAO.seleccionar_tramite(codigo)
            if tramite:
                self.codigo_original = codigo
                self.ui.TxTCodigo.setText(tramite.codigo)
                self.ui.TxTDescripcion.setText(tramite.descripcion)
                self.ui.TxTCosto.setText(str(tramite.costo_base))
                self.ui.TxTCedula.setText(tramite.ciudadano.cedula)
                self.ui.TxTNombre.setText(tramite.ciudadano.nombre)
                self.ui.TxTApellido.setText(tramite.ciudadano.apellido)
                self.mostrar_mensaje("Trámite Encontrado", "Trámite cargado correctamente.", QMessageBox.Information)
            else:
                self.mostrar_mensaje("No Encontrado", f"No existe un trámite con el código: {codigo}",
                                     QMessageBox.Warning)
                self.limpiar()

        except Exception as e:
            self.mostrar_mensaje("Error", f"Error al buscar el trámite: {str(e)}", QMessageBox.Critical)

    def actualizar(self):
        if self.codigo_original is None:
            self.mostrar_mensaje("Advertencia", "Primero debe buscar un trámite para actualizar.", QMessageBox.Warning)
            return
        validacion = self.validaciones()
        if not validacion['valido']:
            self.mostrar_mensaje("Error de Validación", validacion['mensaje'], QMessageBox.Warning)
            return
        # Confirmar actualización
        respuesta = QMessageBox.question(
            self,
            "Confirmar Actualización",
            "¿Está seguro de actualizar este trámite?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.No:
            return
        try:
            codigo_nuevo = self.ui.TxTCodigo.text().strip()
            descripcion = self.ui.TxTDescripcion.text().strip()
            costo = float(self.ui.TxTCosto.text().strip())
            cedula = self.ui.TxTCedula.text().strip()
            nombre = self.ui.TxTNombre.text().strip()
            apellido = self.ui.TxTApellido.text().strip()
            if codigo_nuevo != self.codigo_original:
                TramiteDAO.eliminar_tramite(self.codigo_original)
                ciudadano = Ciudadano(cedula, nombre, apellido)
                tramite = Tramite(codigo_nuevo, descripcion, costo, ciudadano)
                resultado = TramiteDAO.insertar_tramite(tramite)
            else:
                ciudadano = Ciudadano(cedula, nombre, apellido)
                tramite = Tramite(codigo_nuevo, descripcion, costo, ciudadano)
                resultado = TramiteDAO.actualizar_tramite(tramite)
            if resultado['ejecuto']:
                self.mostrar_mensaje("Éxito", resultado['mensaje'], QMessageBox.Information)
                self.codigo_original = None  # Resetear el código original
            else:
                self.mostrar_mensaje("Error", resultado['mensaje'], QMessageBox.Critical)
        except ValueError as ve:
            self.mostrar_mensaje("Error de Validación", str(ve), QMessageBox.Warning)
        except Exception as e:
            self.mostrar_mensaje("Error", f"Error inesperado: {str(e)}", QMessageBox.Critical)

    def eliminar(self):
        codigo = self.ui.TxTBuscarTramite.text().strip()
        if not codigo:
            self.mostrar_mensaje("Advertencia", "Ingrese un código de trámite para eliminar.", QMessageBox.Warning)
            return
        respuesta = QMessageBox.question(
            self,
            "Confirmar Eliminación",
            f"¿Está seguro de eliminar el trámite con código: {codigo}?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.No:
            return
        try:
            # Eliminar de la base de datos
            resultado = TramiteDAO.eliminar_tramite(codigo)
            if resultado['ejecuto']:
                self.mostrar_mensaje("Éxito", resultado['mensaje'], QMessageBox.Information)
                self.limpiar()
            else:
                self.mostrar_mensaje("Error", resultado['mensaje'], QMessageBox.Critical)
        except Exception as e:
            self.mostrar_mensaje("Error", f"Error al eliminar: {str(e)}", QMessageBox.Critical)

    def limpiar(self):
        self.ui.TxTBuscarTramite.clear()
        self.ui.TxTCodigo.clear()
        self.ui.TxTDescripcion.clear()
        self.ui.TxTCosto.clear()
        self.ui.TxTCedula.clear()
        self.ui.TxTNombre.clear()
        self.ui.TxTApellido.clear()
        self.codigo_original = None

    def mostrar_mensaje(self, titulo, mensaje, tipo):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(titulo)
        msg_box.setText(mensaje)
        msg_box.setIcon(tipo)
        msg_box.exec()