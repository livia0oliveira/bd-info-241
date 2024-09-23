# Atividade 10

Crie um Banco de Dados envolvendo quatro tabelas. Uma tabela é um Cadastro (por exemplo TB_ALUNO), uma outra tabela é cadastro (por exemplo TB_DISCIPLINA) e uma outra também é cadastro (por TB_PROFESSOR). A quarta tabela Matricula se relaciona com as tabelas Aluno, Professor e Disciplina. Na tabela Matricula existirão chaves estrangeiras para Aluno, Professor e Disciplina. na tabela Matricula existirão atributos com as notas N1, N2 e Faltas. Criar instruções SQL com CRUD para as 4 tabelas. Implementar um código Python para ler a tabela Matricula e listar o status de aprovação dos alunos Matriculados.

# Resolução usando o Play With Docker

## Primeiros passos

Utilize o comando a seguir para logar no docker evitando limite de pulls

```
docker login

```

Instale o mysql connector

```

pip install mysql-connector-python

```

## Crie o arquivo .yml com o comando 'vi' para abrir as portas e utilizar o MyPHP Admin

```

vi docker-compose.yml

```

Coloque alterando os dados necessários:

``` yaml

version: '3.8'

services:
  mysql:
    image: mysql:8.0
    container_name: mysql_container
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: mydbjosemaia
      MYSQL_USER: myjosemaia
      MYSQL_PASSWORD: mypassword
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    container_name: phpmyadmin_container
    environment:
      PMA_HOST: mysql
      PMA_PORT: 3306
      PMA_USER: root
      PMA_PASSWORD: rootpassword
    ports:
      - "8080:80"
    depends_on:
      - mysql

volumes:
  mysql_data:


```


## Criação do arquivo em python

Utilize o comando 'vi' para criar

```

vi main.py

```

Coloque alterando os dados necessários:


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


cursor.close()
mydb.close()



```

## Rodando

Utilize o comando python {nome do arquivo}.py

```

python main.py

```