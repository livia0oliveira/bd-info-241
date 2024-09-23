# Avaliação Prática para a N2

## Logar na conta
```
docker login
```

## Baixar o conector python
```
pip install mysql-connector-python
```

## Criar servidor
```
vim docker-compose.yml
```
```yaml
```
```
docker-compose up -d
```

## Criar arquivo-python
```
vim arquivo-python.py
```
```python

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myjosemaia",  
    password="mypassword",  
    database="mydbjosemaia"
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

print("")
print("\nAlunos Reprovados:")
print("Nome | Matéria | Professor | Nota N1 | Nota N2 | Media Final | Faltas | Status")
cursor.execute("""
    SELECT 
        A.nome_aluno AS 'Nome do Aluno',
        D.nome_disciplina AS 'Nome da Disciplina',
        P.nome_professor AS 'Nome do Professor',
        M.nota_n1 AS 'N1',
        M.nota_n2 AS 'N2',
        M.media AS 'Média',
        M.faltas AS 'Faltas',
        CASE
            WHEN M.faltas > 20 THEN 'Reprovado por Falta'
            WHEN M.media < 6.0 THEN 'Reprovado por Média'
        END AS 'Status da Reprovação'
    FROM 
        TB_MATRICULA M
    JOIN 
        TB_ALUNO A ON M.id_aluno = A.id_aluno
    JOIN 
        TB_DISCIPLINA D ON M.id_disciplina = D.id_disciplina
    JOIN 
        TB_PROFESSOR P ON M.id_professor = P.id_professor
    WHERE 
        M.aprovado = FALSE;
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT 
        COUNT(*) AS 'Quantidade de Alunos Reprovados'
    FROM 
        TB_MATRICULA
    WHERE 
        aprovado = FALSE;
""")
print("-- Quantidade de Alunos Reprovados:", cursor.fetchone()[0])
print("")
print("Nome | Matéria | Professor | Nota N1 | Nota N2 | Media Final | Faltas | Status")
print("\nAlunos Aprovados:")
cursor.execute("""
    SELECT 
        A.nome_aluno AS 'Nome do Aluno',
        D.nome_disciplina AS 'Nome da Disciplina',
        P.nome_professor AS 'Nome do Professor',
        M.nota_n1 AS 'N1',
        M.nota_n2 AS 'N2',
        M.media AS 'Média',
        M.faltas AS 'Faltas',
        'Aprovado por Média' AS 'Status da Aprovação'
    FROM 
        TB_MATRICULA M
    JOIN 
        TB_ALUNO A ON M.id_aluno = A.id_aluno
    JOIN 
        TB_DISCIPLINA D ON M.id_disciplina = D.id_disciplina
    JOIN 
        TB_PROFESSOR P ON M.id_professor = P.id_professor
    WHERE 
        M.aprovado = TRUE;
""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""
    SELECT 
        COUNT(*) AS 'Quantidade de Alunos Aprovados'
    FROM 
        TB_MATRICULA
    WHERE 
        aprovado = TRUE;
""")
print("\n -- Quantidade de Alunos Aprovados:", cursor.fetchone()[0])



cursor.close()
mydb.close()
```

## Executar o arquivo python
```
python arquivo-python.py
```
