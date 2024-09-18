# Codigo que ta certo mas ta dando erro :)
docker-python.py
```python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="myanalivia",
    password="mypassword",
    database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_Aluno (
    id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50),
    
    PRIMARY KEY (id)
);""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_Disciplina (
    id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50),
    
    PRIMARY KEY (id)
);""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_Professor (
    id INT AUTO_INCREMENT NOT NULL,
    nome VARCHAR(50),
    
    PRIMARY KEY (id)
);""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS TB_Matricula (
  id INT AUTO_INCREMENT,
  aluno_id INT,
  disciplina_id INT,
  professor_id INT,
  nota_n1 DECIMAL (4,2),
  nota_n2 DECIMAL (4,2),
  media DECIMAL (4,2),
  faltas INT,
  aprovado_sn BOOLEAN,
  
  PRIMARY KEY (id),
  FOREIGN KEY (aluno_id) REFERENCES TB_Aluno(id),
  FOREIGN KEY (disciplina_id) REFERENCES TB_Disciplina(id),
  FOREIGN KEY (professor_id) REFERENCES TB_Professor(id)
);""")


mycursor.executemany("INSERT INTO TB_Aluno (id, nome) VALUES (%s, %s) ON DUPLICATE KEY UPDATE nome = VALUES(nome);",[
    (1, "Ana Livia"), (4, "Jose Maia"), (7, "Marina")
])

mycursor.executemany("INSERT INTO TB_Professor (id, nome) VALUES (%s, %s);",[
    (2, "Ana Olivia"), (5, "Joseph Maia"), (8, "Marine")
])

mycursor.executemany("INSERT INTO TB_Disciplina (id, nome) VALUES (%s, %s);",[
    (3, "Artes visuais"), (6, "Introduçao a programaçao"), (9, "Portugues")
])

mycursor.executemany("INSERT INTO TB_Matricula (aluno_id, disciplina_id, professor_id, nota_n1, nota_n2, faltas) VALUES (%s,%s,%s,%s,%s,%s);",[
    (1, 3, 2, 10, 9, 0),
    (4, 6, 5, 6, 10, 40),
    (7, 9, 8, 9, 4, 4)
])

mydb.commit()

mycursor.execute("SELECT * FROM TB_Matricula")
resultado = mycursor.fetchall()

for item in resultado:
    id, aluno_id, disciplina_id, professor_id, nota_n1, nota_n2, faltas, media, aprovado_sn = item
    print(item)
    
    media = (2 * nota_n1 + 3 * nota_n2 )/ 5
    
    if media < 6 or faltas >= 20:
        aprovado_sn = False
    else:
        aprovado_sn = True
        
    mycursor.execute("UPDATE TB_Matricula SET aprovado_sn = %s, media = %s, WHERE id= %s;", (aprovado_sn, media, id))
    
mydb.commit()

mycursor.execute("SELECT * FROM TB_Matricula")
resultado = mycursor.fetchall()

for item in resultado:
    print(item)
    
mycursor.close()
mydb.close()
```
