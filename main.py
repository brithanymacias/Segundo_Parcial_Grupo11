# Integrantes:
# - Collaguari Israel
# - Macias Brithany

import sys

from PySide6.QtWidgets import QApplication

from Servicio.tramite import TramiteServicio


app = QApplication()
vtn_principal = TramiteServicio()
vtn_principal.show()
sys.exit(app.exec())
