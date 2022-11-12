from django.db import models
# Create your models here.


class Notas:
    def __init__(self, titulo, descripcion, importante):
        self.titulo = titulo
        self.descripcion = descripcion
        self.importante = importante


class Listado:
    def __init__(self):
        """nota1 = Notas('Nota 1', 'Esta es la nota 1', False)
        nota2 = Notas('Nota 2', 'Esta es la nota 2', True)
        nota3 = Notas('Nota 3', 'Esta es la nota 3', True)
        nota4 = Notas('Nota 4', 'Esta es la nota 4', False)
        self.lista_notas = [nota1, nota2, nota3, nota4]"""
        self.lista_notas = []

    def agregar_nota(self, nota):
        if isinstance(nota, Notas):
            if nota.titulo == "" or nota.descripcion == "":
                return 'Nota no se guardo, ingrese los datos'
            for i in self.lista_notas:
                if i.titulo == nota.titulo:
                    return 'Nota ya existe'
        self.lista_notas.append(nota)
        return 'Nota agregada exitosamente'

    def ordenarNotas(self):
        return sorted(self.lista_notas, key=lambda x: x.importante, reverse=True)

    def eliminar_nota(self, titulo):
        for i in self.lista_notas:
            if i.titulo == titulo:
                self.lista_notas.remove(i)
                return 'Se elimino la nota'
        return 'Nota no encontrada'
