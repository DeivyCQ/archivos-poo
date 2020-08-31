class profesor():
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
        pass

class alumno():
    def __init__(self, nombre, documento, notas):
        self.nombre = nombre
        self.documento = documento
        self.notas = notas
        pass

class archivo_profesor():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        pass
    def mostrar_archivo(self):
        try:
            file = open(self.nombre_archivo, mode="r", encoding="utf-8")
            for linea in file.readline():
                print(linea)
                pass

        except Exception as e:
            print(f"{str(e)}")

        finally:
            if(file):
                file.close()
                print(file)

    def agregar_profesor(self, profesor):
        try:
            file = open(self.nombre_archivo, mode="a")
            profesor = f"\n{profesor.nombre} - {profesor.documento} \n"
            file.write(profesor)
            pass

        except Exception as e:
            print(f"{str(e)}")

        finally:
            if(file):
                file.close()
                print(file)
class archivo_alumno():
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        pass
    def mostrar_archivo(self):
        try:
            file = open(self.nombre_archivo, mode="r", encoding="utf-8")
            for linea in file.readline():
                print(linea)
                pass

        except Exception as e:
            print(f"{str(e)}")

        finally:
            if(file):
                file.close()
                print(file)

    def agregar_alumno(self, alumno):
        try:
            file = open(self.nombre_archivo, mode="a")
            alumno = f"{alumno.nombre} - {alumno.documento} - {alumno.notas} \n"
            file.write(alumno)
            pass

        except Exception as e:
            print(f"{str(e)}")

        finally:
            if(file):
                file.close()
                print(file)

profesor_1 = profesor("juan", 38976544)
archivo_profesor = archivo_profesor("profesor.txt")
archivo_profesor.agregar_profesor(profesor_1)
archivo_profesor.mostrar_archivo()

alumno_1 = alumno("deivy", 456789003, f"{12, 20, 14, 17, 15}")
archivo_alumno = archivo_alumno("alumno.txt")
archivo_alumno.agregar_alumno(alumno_1)
archivo_alumno.mostrar_archivo()