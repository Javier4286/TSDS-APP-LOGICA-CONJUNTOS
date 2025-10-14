class Tarea:

    _siguiente_id = 1

    def __init__(self, descripcion, es_urgente=False):

        self.id = Tarea._siguiente_id
        Tarea._siguiente_id += 1

        self.descripcion = descripcion

        self.completada = False

        self.es_urgente = es_urgente

    def __str__(self):

        estado = 'OK' if self.completada else 'PENDIENTE'
        urgencia = '¡URGENTE!' if self.es_urgente else ''
        return f'[{self.id}] {estado} {self.descripcion}{urgencia}'
