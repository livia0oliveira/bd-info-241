import sqlite3

conex = sqlite3.connect("tasks.db")
cursor = conex.cursor()

def create_task(description):
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
    conex.commit()

def mark_completed(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conex.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

def list_tasks():
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Descrição: {task[1]}, Completo: {'Sim' if task[2] else 'Não'}")



while True:
    print("""
Opções
    1 : Criar Tarefa
    2 : Marcar como concluido
    3 : Deletar Tarefa
    4 : Ver Tarefas
    5 : Sair

""")
    
    escolha = int(input("O que deseja fazer? : "))

    print()

    match escolha:
        case 1:
            criar_tr = input("Descreva sua tarefa: ")
            create_task(criar_tr)

        case 2:
            completo = int(input("Qual o id da tarefa que deseja completar?: "))
            mark_completed(completo)
        
        case 3:
            deletar = int(input("Qual o id da tarefa que deseja deletar?: "))
            delete_task(deletar)

        case 4:
            list_tasks()
        
        case 5:
            break