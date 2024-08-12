# Desenvolver um Backend Python que usa FASTAPI 
**Como um programador Python, crie uma aplicação back-end que usa o framework FASTAPI seguindo os seguintes passos:**

1) Crie um banco de dados SQLITE3 com o nome dbalunos.db.

2) Crie uma entidade aluno que será persistida em uma tabela TB_ALUNO com os seguintes campos: <br>
- **id** chave primária do tipo inteiro com autoincremento; <br>
- **aluno_nome** do tipo string com tamanho 50; <br>
- **endereço** do tipo string com tamanho 100; <br>

3) Crie os seguintes endpoints FASTAPI abaixo descritos: <br>
a) criar_aluno grava dados de um objeto aluno na tabela TB_ALUNO; <br>
b) listar_alunos ler todos os registros da tabela TB_ALUNO; <br>
c) listar_um_aluno ler um registro da tabela TB_ALUNO a partir do campo id; <br>
d) atualizar_aluno atualiza um registro da tabela TB_ALUNO a partir de um campo id e dos dados de uma entidade aluno; <br>
e) excluir_aluno exclui um registro da tabela TB_ALUNO a partir de um campo id e dos dados de uma entidade aluno;
