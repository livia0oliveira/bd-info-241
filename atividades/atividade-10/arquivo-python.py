
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myanalivia",  
    password="mypassword",  
    database="mydbanalivia"
)

cursor = mydb.cursor()



cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_ALUNO (
        id_aluno INT PRIMARY KEY AUTO_INCREMENT,
        nome_aluno VARCHAR(255) NOT NULL
        
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_PROFESSOR (
        id_professor INT PRIMARY KEY AUTO_INCREMENT,
        nome_professor VARCHAR(255) NOT NULL
        
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_DISCIPLINA (
        id_disciplina INT PRIMARY KEY AUTO_INCREMENT,
        nome_disciplina VARCHAR(255) NOT NULL
        
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_MATRICULA (
        id_matricula INT PRIMARY KEY AUTO_INCREMENT,
        id_aluno INT,
        id_professor INT,
        id_disciplina INT,
        nota_n1 DECIMAL(5, 2),
        nota_n2 DECIMAL(5, 2),
        faltas INT,
        media DECIMAL(5, 2),
        aprovado BOOLEAN,
        FOREIGN KEY (id_aluno) REFERENCES TB_ALUNO(id_aluno),
        FOREIGN KEY (id_professor) REFERENCES TB_PROFESSOR(id_professor),
        FOREIGN KEY (id_disciplina) REFERENCES TB_DISCIPLINA(id_disciplina)
    );
""")


cursor.execute("""
    INSERT INTO TB_ALUNO (nome_aluno) 
    VALUES ('José Maia'),
           ('Ana Lívia'),
           ('Harry Potter')
    ON DUPLICATE KEY UPDATE nome_aluno=VALUES(nome_aluno);
""")

cursor.execute("""
    INSERT INTO TB_PROFESSOR (nome_professor) 
    VALUES ('Prof. Ana Olivia'),
           ('Prof. Josemar'),
           ('Prof. Severo')
    ON DUPLICATE KEY UPDATE nome_professor=VALUES(nome_professor);
""")

cursor.execute("""
    INSERT INTO TB_DISCIPLINA (nome_disciplina) 
    VALUES ('Artes Visuais'),
           ('História'),
           ('Química')
    ON DUPLICATE KEY UPDATE nome_disciplina=VALUES(nome_disciplina);
""")

cursor.execute("""
    INSERT INTO TB_MATRICULA (id_aluno, id_professor, id_disciplina, nota_n1, nota_n2, faltas, media, aprovado) 
    VALUES (1, 1, 1, 7.5, 8.0, 2, 0, false),
           (2, 2, 2, 6.0, 4.5, 3, 0, false),
           (3, 3, 3, 8.0, 6.0, 32, 0, false)
    ON DUPLICATE KEY UPDATE nota_n1=VALUES(nota_n1), nota_n2=VALUES(nota_n2), faltas=VALUES(faltas);
""")

mydb.commit()


cursor.execute("""
    SELECT A.id_aluno, A.nome_aluno, M.nota_n1, M.nota_n2, M.faltas
    FROM TB_MATRICULA M
    JOIN TB_ALUNO A ON M.id_aluno = A.id_aluno;
""")



matriculas = cursor.fetchall()


for matricula in matriculas:
    id, nome_aluno, nota_n1, nota_n2, faltas = matricula
    media = ((2 * nota_n1) + (3 * nota_n2)) / 5
    if faltas > 20:
        aprovado = False
    elif media >= 6.0:
        aprovado = True
    else:
        aprovado = False
    cursor.execute('UPDATE TB_MATRICULA SET aprovado = %s, media = %s WHERE id_matricula = %s;', (aprovado, media, id))
    print(f"Aluno: {nome_aluno}, Média: {media}, Aprovado: {aprovado}")

mydb.commit()


cursor.close()
mydb.close()


