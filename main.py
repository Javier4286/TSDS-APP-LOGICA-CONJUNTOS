import sys
from clear_console import clear_console
from gestion_tareas import GestorTareas

input('\nEsta aplicación modela la organización de tareas bajo la óptica de la Matemática Discreta,\naplicando conceptos de Teoría de Conjuntos y Lógica Proposicional.\n\nEl sistema gestiona el Conjunto Universal (U),\nparticionado en subconjuntos disjuntos (P y C) con Cardinalidad |U| = |P| + |C|.\n\nLa adición de tareas es una operación de Unión, y cada tarea se identifica por una Función Inyectiva (ID). \n\nAdemás, el filtro de prioridad implementa una expresión lógica compuesta\n(la Conjunción Q ^ ¬P donde Q = "urgente" y P = "completada") para la selección precisa de subconjuntos,\nutilizando los conectivos lógicos para definir los criterios de búsqueda.\n\nIntegrantes:\nGonzález Javier Alexis\nJiménez Mariel Emilse\nLazarte Mansicidor Alexis Saúl\n\nPresione ENTER para continuar ')

clear_console()

input('\nAquí consideramos el conjunto U = {todas las tareas actuales}.\n\nAl seleccionar acciones, trabajaremos con subconjuntos de U, por ejemplo:\n\nP = tareas pendientes.\n\nC = tareas completadas.\n\nUsaremos cardinalidad |U| para mostrar el total y lógica proposicional para filtrar.\n(Por ejemplo: "Urgente" ^ ¬"Completada").\n\nPresione ENTER para continuar ')

input(
    '\n\nLa elección que hagas corresponderá a una operación sobre el conjunto U.\n\nEjemplos: agregar un elemento (operación de conjunto U <- U UNION {t}),\nmarcar como completada (mover elemento de P a C), o aplicar un filtro lógico.\n\nPresione ENTER para continuar ')


def mostrar_menu():

    clear_console()
    print(f'\n{'='*46}\n{' '*8}Mi Agenda de Tareas Hogareñas\n{'='*46}\n\n1. Añadir nueva tarea a la lista\n\n2. Marcar tarea como realizada\n\n3. Ver mis tareas (Pendientes y Realizadas)\n\n4. Priorizar (Filtro Urgente y Pendiente)\n\n5. Salir de la Agenda\n\n{'-'*46}')


def ejecutar_app():

    gestor = GestorTareas()

    gestor.agregar_tarea('Lavar la ropa', False)
    gestor.agregar_tarea('Comprar pan', True)
    gestor.agregar_tarea('Estudiar Lógica Proposicional', False)

    while True:

        mostrar_menu()

        eleccion = input(
            f'{' '*8}¿Que quieres hacer hoy? (1-5): \n{'-'*46}\n> ')

        if eleccion == '1':

            clear_console()

            input(
                '\nOperación: añadir elemento al conjunto U.\n\nFormalmente: Si U es el conjunto de tareas, al agregar tarea t hacemos U := U UNION {t}.\n\nEsta operación modifica la cardinalidad |U| -> |U| + 1.\n\n\nPresione ENTER para continuar ')

            desc = input(
                f'\n{' '*8}Añadir nueva tarea a la lista\n{'='*46}\n\nDescribe la tarea: ')

            input('\n\nLa propiedad "es_urgente" es una proposición booleana asociada al elemento.\nPodremos usarla luego en expresiones lógicas: por ejemplo Q ^ ¬P,\ndonde Q = "es urgente" y P = "está completada".\n\n\nPresione ENTER para continuar ')

            urgente_input = input('\n¿Es urgente? (s/n): ').lower()
            es_urgente = urgente_input == 's'
            gestor.agregar_tarea(desc, es_urgente)

            input(
                f'\nTarea "{desc}" agregada a la lista.\n\nPresione ENTER para continuar ')
            clear_console()

        elif eleccion == '2':

            clear_console()

            input('\nVamos a considerar la partición de U en P (pendientes) y C (completadas).\n\nMarcar una tarea como realizada equivale a mover un elemento de P a C.\n\nComprobamos la existencia del elemento por su identificador (función inyectiva).\n\n\nPresione ENTER para continuar ')

            try:
                pendientes, _, _ = gestor.obtener_subconjuntos()
                if not pendientes:
                    input(
                        '\nSin tareas pendientes para marcar.\n\nPresione ENTER para continuar ')
                    continue

                print(f'\n\n{' '*8}Tareas pendientes:')
                for t in pendientes:
                    print(t)

                input('\n\nCada tarea tiene un ID único: f(tarea) = n, donde f es inyectiva.\nIntroduce el número de ID para identificar la tarea de forma unívoca.\n\n\nPresione ENTER para continuar ')

                tarea_id = int(
                    input('\nIntroduce el [ID] de la tarea que terminaste: '))

                if gestor.marcar_completada(tarea_id):
                    input(
                        f'\n¡Excelente trabajo! Tarea {tarea_id} marcada como HECHA.\n\nPresione ENTER para continuar ')
                else:
                    print(
                        f'Error: El ID {tarea_id} no existe o ya está completado')

            except ValueError:
                print(
                    '\nEntrada no válida. Por favor, introduce solo el número de ID.')

        elif eleccion == '3':

            clear_console()
            input(
                f'\nConceptos: Conjuntos, Subconjuntos, Partición y Cardinalidad.\n\nEstamos trabajando con una **partición** del conjunto universal de tareas U:\n\n1. Conjunto de Tareas Pendientes (P)\n\n2. Conjunto de Tareas Completadas (C)\n\nEstas cumplen con:\n\n- **Unión**: P UNION C = U (Cubre todas las tareas)\n\n- **Intersección**: P ∩ C = 0 (Son **disyuntos**, la intersección es el **conjunto vacío**)\n\n- **Cardinalidad**: El total de tareas es la suma: |U| = |P| + |C|.\n\nPresione ENTER para continuar ')

            pendientes, completadas, cardinalidad_u = gestor.obtener_subconjuntos()

            if not gestor.tareas:
                input(
                    '\nLa lista está vacía. ¡Añade algunas tareas!\n\nPresione ENTER para continuar ')
                continue

            print(f'\nTAREAS PENDIENTES: {len(pendientes)}')
            for t in pendientes:
                print(t)

            print(f'\nTAREAS HECHAS: {len(completadas)}')
            for t in completadas:
                print(t)

            input(
                f'\nTotal de tareas en tu lista (Cardinalidad): {cardinalidad_u}\n\nPresione ENTER para continuar ')

        elif eleccion == '4':

            clear_console()
            input(
                f'\nConceptos: Lógica Proposicional, Conectivos y Filtros.\n\nEste filtro utiliza la **Conjunción** (^, el conectivo "Y") y la **Negación** (¬, el conectivo "NO") para definir un criterio de prioridad.\n\nSean las proposiciones:\n\nQ = "La tarea es urgente"\n\nP = "La tarea está completada"\n\nBuscamos las tareas que satisfacen la expresión lógica (Filtro de Prioridad):\n\nQ ^ ¬P\n\nEsto significa: Tarea es Urgente **Y** (Tarea **NO** está Completada).\n\nPresione ENTER para continuar ')

            # clear_console()
            filtro = gestor.filtrar_tareas_logicas()
            print(
                '\n\n¡PRIORIDADES! Tareas urgentes Y que aún NO has completado (Q ^ ¬P):\n')

            if filtro:
                for t in filtro:
                    print(t)
                input('\n\nPresione ENTER para continuar ')

            else:
                input('Sin tareas urgentes pendientes.')

        elif eleccion == '5':

            clear_console()
            input(
                f'\n¡Gracias por haber corregido nuestro ABP!\n¡Felices Fiestas!\n\nPresione ENTER para salir ')
            sys.exit(0)

        else:
            input(
                '\n¡Opción no reconocida!\nElige un número del 1 al 5. Presione ENTER para continuar ')


if __name__ == '__main__':
    ejecutar_app()
