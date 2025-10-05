# Lógica central de aplicación (operaciones de conjuntos y lógica / lógica Matemática)

from tarea import Tarea


class GestorTareas:
    '''
    Clase que gestiona la colección de tareas, modelándolas como un Conjunto.
    '''

    def __init__(self):
        # La lista principal de tareas. Este es nuestro CONJUNTO UNIVERSAL (U)
        self.tareas = []

        # --- Operaciones de Conjuntos y Cardinalidad ---

    def agregar_tarea(self, descripcion, es_urgente):
        '''
        Añade un nuevo elemento al Conjunto Universal (U).
        '''
        nueva_tarea = Tarea(descripcion, es_urgente)
        self.tareas.append(nueva_tarea)
        # La nueva cardinalidad de U se actualiza automaticamente.

    def marcar_completada(self, tarea_id):
        '''
        Busca un elemento por su ID inyectivo y cambia el valor de su Proposición Lógica.
        '''

        # Buscamos en el Conjunto Universal (U)
        for tarea in self.tareas:
            if tarea.id == tarea_id:
                # Modificamos el valor de verdad de la proposición P: 'completada'
                tarea.completada = True
                return True  # Éxito
        return False  # Fracaso

    def obtener_subconjuntos(self):
        '''
        Calcula y devuelve los subconjuntos principales y su cardinalidad.
        '''

        # Subconjunto C: Tareas Completadas (P es VERDADERA)
        completadas = [t for t in self.tareas if t.completada]

        # Subconjunto P: Tareas Pendientes (P = U \ C, el complemento de C)
        pendientes = [t for t in self.tareas if not t.completada]

        # Cardinalidad del Conjunto Universal |U|
        cardinalidad_u = len(self.tareas)

        return pendientes, completadas, cardinalidad_u

    def filtrar_tareas_logicas(self):
        '''
        Realiza un filtrado basado en Lógica Proposicional.
        Usaremos la Conjunción (AND) y la Negación (NOT).

        Lógica aplicada: Q ^ ¬P
        (Tareas que son Urgentes AND que NO están Completadas)
        '''

        # Esta es la aplicación de la lógica Proposicional Q ^ ¬P

        filtro_logico = [
            t for t in self.tareas if t.es_urgente and not t.completada]

        # Aquí iteramos para obtener los elementos del conjunto resultante.

        return filtro_logico
