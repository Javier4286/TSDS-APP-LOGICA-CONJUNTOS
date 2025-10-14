from tarea import Tarea


class GestorTareas:

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, es_urgente):

        nueva_tarea = Tarea(descripcion, es_urgente)
        self.tareas.append(nueva_tarea)

    def marcar_completada(self, tarea_id):

        for tarea in self.tareas:
            if tarea.id == tarea_id:
                tarea.completada = True
                return True
        return False

    def obtener_subconjuntos(self):

        completadas = [t for t in self.tareas if t.completada]

        pendientes = [t for t in self.tareas if not t.completada]

        cardinalidad_u = len(self.tareas)

        return pendientes, completadas, cardinalidad_u

    def filtrar_tareas_logicas(self):

        filtro_logico = [
            t for t in self.tareas if t.es_urgente and not t.completada]

        return filtro_logico
