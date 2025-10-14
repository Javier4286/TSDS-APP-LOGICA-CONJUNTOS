from gestion_tareas import GestorTareas
from clear_console import clear_console
import sys


def mostrar_menu():

    print(f'\n{'='*46}\n{' '*8}Mi Agenda de Tareas Hogareñas\n{'='*46}\n\n1. Añadir nueva tarea a la lista\n\n2. Marcar tarea como realizada\n\n3. Ver mis tareas (Pendientes y Realizadas)\n\n4. Priorizar (Filtro Urgente y Pendiente)\n\n5. Salir de la Agenda\n\n{'-'*46}')


def ejecutar_app():

    gestor = GestorTareas()

    gestor.agregar_tarea('Lavar la ropa', False)
    gestor.agregar_tarea('Comprar pan', True)
    gestor.agregar_tarea('Estudiar Lógica Proposicional', False)

    while True:
        clear_console()
        mostrar_menu()

        eleccion = input(
            f'{' '*8}¿Que quieres hacer hoy? (1-5): \n{'-'*46}\n> ')

        if eleccion == '1':

            clear_console()
            desc = input(
                f'\n{'='*46}\n{' '*8}Añadir nueva tarea a la lista\n{'='*46}\n\nDescribe la tarea: ')
            urgente_input = input('\n¿Es urgente? (s/n): ').lower()
            es_urgente = urgente_input == 's'
            gestor.agregar_tarea(desc, es_urgente)

            input(
                f'\nTarea "{desc}" agregada a la lista.\n\nPresione ENTER para continuar ')
            clear_console()

        elif eleccion == '2':

            try:
                pendientes, _, _ = gestor.obtener_subconjuntos()
                if not pendientes:
                    clear_console()
                    input(
                        '\nSin tareas pendientes para marcar.\n\nPresione ENTER para continuar ')
                    continue

                clear_console()
                print(f'\n{'='*46}\n{' '*8}Tareas pendientes:')
                for t in pendientes:
                    print(t)

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
            pendientes, completadas, cardinalidad_u = gestor.obtener_subconjuntos()

            if not gestor.tareas:
                input(
                    '\nLa lista está vacía. ¡Añade algunas tareas!\n\nPresione ENTER para continuar ')
                continue

            print(f'TAREAS PENDIENTES {len(pendientes)}:')
            for t in pendientes:
                print(t)

            print(f'TAREAS HECHAS {len(completadas)}:')
            for t in completadas:
                print(t)

            input(
                f'\nTotal de tareas en tu lista (Cardinalidad): {cardinalidad_u}\n\nPresione ENTER para continuar ')

        elif eleccion == '4':

            clear_console()
            filtro = gestor.filtrar_tareas_logicas()
            print(
                '\n¡PRIORIDADES! Tareas urgentes Y que aún NO has completado (Q ^ ¬P): ')

            if filtro:
                for t in filtro:
                    print(t)
                input('\n\nPresione ENTER para continuar ')

            else:
                input('Sin tareas urgentes pendientes.')

        elif eleccion == '5':

            print(f'\n¡Gracias por haber corregido nuestro ABP!\n¡Felices Fiestas!')
            sys.exit(0)

        else:
            print('\nOpción no reconocida. Elige un número del 1 al 5.')


if __name__ == '__main__':
    ejecutar_app()
