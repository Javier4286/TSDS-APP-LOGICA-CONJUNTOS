# Modelado de datos (Elemento individual / Elemento Básico).

class Tarea:
    '''
    Clase que representa una tarea individual.

    Cada tarea es un 'elemento' en nuestro 'Conjunto Universal' de tareas.
    La asignación de IDs actúa como una función INYECTIVA:
    a cada tarea distinta le corresponde un ID distinto.
    '''
    # ID de clase para asegurar la unicidad (inyectividad)
    _siguiente_id = 1

    def __init__(self, descripcion, es_urgente=False):
        '''
        Constructor de la clase Tarea.
        :param descripcion: El contenido de la tarea.
        :param es_urgente: Proposición lógica simple para filtrar.
        '''

        # Asigna el ID único (garantizando inyectividad)
        self.id = Tarea._siguiente_id
        Tarea._siguiente_id += 1

        # El contenido de la tarea
        self.descripcion = descripcion

        # Estado de la tarea (Proposición Lógica P: 'La tarea está completada')
        self.completada = False

        # Urgencia de la tarea (Proposición Lógica Q: 'La tarea es urgente')
        self.es_urgente = es_urgente

    def __str__(self):
        '''
        Representación legible de la tarea para la interfaz de usuario.
        '''
        estado = '✅' if self.completada else '⏳'
        urgencia = '(🚨 ¡URGENTE!)' if self.es_urgente else ''
        return f'[{self.id}] {estado} {self.descripcion}{urgencia}'
