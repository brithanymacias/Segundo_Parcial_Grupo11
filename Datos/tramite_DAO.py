# Integrantes:
# - Collaguari Israel
# - Macias Brithany

from Datos.conexion import Conexion
from Dominio.tramite import Tramite
from Dominio.cliente import Ciudadano
import pyodbc as bd


class TramiteDAO:
    # Consultas SQL
    _INSERT = ("INSERT INTO Tramite (CodTramite, Descripcion, Costo, IdCiudadano, Nombre, Apellido) "
               "VALUES (?, ?, ?, ?, ?, ?)")

    _UPDATE = ("UPDATE Tramite SET Descripcion=?, Costo=?, IdCiudadano=?, Nombre=?, Apellido=? "
               "WHERE CodTramite=?")

    _DELETE = "DELETE FROM Tramite WHERE CodTramite=?"

    _SELECT = "SELECT * FROM Tramite WHERE CodTramite=?"

    @classmethod
    def existe_codigo_tramite(cls, cod_tramite):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Tramite WHERE CodTramite = ?", (cod_tramite,))
                resultado = cursor.fetchone()
                return resultado[0] > 0

        except Exception as e:
            print(f"Error al validar existencia de código: {e}")
            return False

    @classmethod
    def insertar_tramite(cls, tramite):
        try:
            # Validación de código duplicado
            if cls.existe_codigo_tramite(tramite.codigo):
                return {'ejecuto': False, 'mensaje': 'El código de trámite ya existe.'}

            try:
                with Conexion.obtenerCursor() as cursor:
                    datos = (
                        tramite.codigo,
                        tramite.descripcion,
                        tramite.costo_base,
                        tramite.ciudadano.cedula,
                        tramite.ciudadano.nombre,
                        tramite.ciudadano.apellido
                    )
                    cursor.execute(cls._INSERT, datos)
                    Conexion.obtenerConexion().commit()

                    if cursor.rowcount == 1:
                        return {'ejecuto': True, 'mensaje': 'Trámite guardado con éxito.'}
                    else:
                        return {'ejecuto': False, 'mensaje': 'No se pudo guardar el trámite.'}

            except bd.IntegrityError as e_bd:
                print(f"Error de integridad en BD: {e_bd}")
                if 'CodTramite' in str(e_bd):
                    return {'ejecuto': False, 'mensaje': 'El código de trámite ya existe.'}
                elif 'IdCiudadano' in str(e_bd):
                    return {'ejecuto': False, 'mensaje': 'Error con la cédula del ciudadano.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'Error de integridad en la base de datos.'}

        except Exception as e:
            print(f"Error general al insertar: {e}")
            print(f"Tipo de error: {type(e)}")
            return {'ejecuto': False, 'mensaje': 'Error al guardar los datos. Contacte con Sistemas.'}

    @classmethod
    def actualizar_tramite(cls, tramite):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    tramite.descripcion,
                    tramite.costo_base,
                    tramite.ciudadano.cedula,
                    tramite.ciudadano.nombre,
                    tramite.ciudadano.apellido,
                    tramite.codigo
                )
                cursor.execute(cls._UPDATE, datos)
                Conexion.obtenerConexion().commit()

                if cursor.rowcount > 0:
                    return {'ejecuto': True, 'mensaje': 'Trámite actualizado con éxito.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'No se encontró el trámite para actualizar.'}

        except Exception as e:
            print(f"Error al actualizar: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al actualizar los datos.'}

    @classmethod
    def eliminar_tramite(cls, cod_tramite):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._DELETE, (cod_tramite,))
                Conexion.obtenerConexion().commit()

                if cursor.rowcount > 0:
                    return {'ejecuto': True, 'mensaje': 'Trámite eliminado correctamente.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'El código de trámite no existe.'}

        except Exception as e:
            print(f"Error al eliminar: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al intentar eliminar el trámite.'}

    @classmethod
    def seleccionar_tramite(cls, cod_tramite):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECT, (cod_tramite,))
                registro = cursor.fetchone()

                if registro:
                    # Crear objeto Ciudadano
                    ciudadano = Ciudadano(
                        cedula=registro[3],
                        nombre=registro[4],
                        apellido=registro[5]
                    )

                    # Crear objeto Tramite con el ciudadano
                    tramite = Tramite(
                        codigo=registro[0],
                        descripcion=registro[1],
                        costo_base=registro[2],
                        ciudadano=ciudadano
                    )
                    return tramite
                return None
        except Exception as e:
            print(f"Error al seleccionar: {e}")
            return None
