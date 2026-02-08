# Integrantes:
# - Collaguari Israel
# - Macias Brithany

class Ciudadano:
    def __init__(self, cedula, nombre, apellido):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido

    @property
    def cedula(self):
        return self._cedula
    @cedula.setter
    def cedula(self, valor):
        try:
            if not valor or not str(valor).strip():
                raise ValueError("La cédula no puede estar vacía.")
            self._cedula = str(valor).strip()
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar la cédula: {str(e)}")

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, valor):
        try:
            if not valor or not valor.strip():
                raise ValueError("El nombre no puede estar vacío.")
            self._nombre = valor.strip()
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el nombre: {str(e)}")

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, valor):
        try:
            if not valor or not valor.strip():
                raise ValueError("El Apellido no puede estar Vacío")
            self._apellido = str(valor).strip()
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el apellido: {str(e)}")


    def __str__(self):
        return f"{self.nombre} (Cédula: {self.cedula})"