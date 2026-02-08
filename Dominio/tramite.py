# Integrantes:
# - Collaguari Israel
# - Macias Brithany

from Dominio.cliente import Ciudadano

class Tramite:
    def __init__(self, codigo, descripcion, costo_base, ciudadano):
        """
        ciudadano: objeto de tipo Ciudadano (composición)
        """
        self.codigo = codigo
        self.descripcion = descripcion
        self.costo_base = costo_base
        self.ciudadano = ciudadano

    @property
    def codigo(self):
        return self._codigo
    @codigo.setter
    def codigo(self, valor):
        try:
            if not valor or not str(valor).strip():
                raise ValueError("El código no puede estar vacío.")
            self._codigo = str(valor).strip()
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el código: {str(e)}")

    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self, valor):
        try:
            if not valor or not valor.strip():
                raise ValueError("La descripción no puede estar vacía.")
            self._descripcion = valor.strip()
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar la descripción: {str(e)}")

    @property
    def costo_base(self):
        return self._costo_base
    @costo_base.setter
    def costo_base(self, valor):
        try:
            # Convertir a float sin importar si viene como string, int o float
            costo_convertido = float(valor)

            if costo_convertido < 0:
                raise ValueError("El costo base no puede ser negativo.")

            self._costo_base = costo_convertido

        except ValueError as ve:
            # Si el error ya es de validación, lo re-lanza
            if "negativo" in str(ve):
                raise
            # Si no pudo convertir a float
            raise ValueError("El costo base debe ser un número válido.")
        except Exception as e:
            raise ValueError(f"Error al procesar el costo base: {str(e)}")

    @property
    def ciudadano(self):
        return self._ciudadano
    @ciudadano.setter
    def ciudadano(self, valor):
        try:
            if not isinstance(valor, Ciudadano):
                raise ValueError("Debe ingresar un Ciudadano.")
            self._ciudadano = valor
        except ValueError:
            raise
        except Exception as e:
            raise ValueError(f"Error al procesar el ciudadano: {str(e)}")

    def calcular_costo(self):
        return self.costo_base

    def __str__(self):
        return (f"Trámite {self.codigo}: {self.descripcion}\n"
                f"Costo: ${self.costo_base:.2f}\n"
                f"Ciudadano: {self.ciudadano}")