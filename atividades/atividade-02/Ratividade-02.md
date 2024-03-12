# Atividade Banco de Dados - Entidade Relacionamento (ER)

### Questões
Defina os seguintes conceitos centrais da abordagem ER:
1. Entidade;
2. Relacionamento;
3. Atributo;
4. Domínio de um Atributo;
5. Generalização/especialização;
6. Entidade Associativa;
7. Cardinalidade de um Atributo.

### Respostas
1. Uma entidade pode ser definida como uma pessoa, objeto ou conceito.
2. É uma associação entre uma ou mais entidades, descrevem como entidades interagem entre si. Podem ser de vários tipos, como 1 para 1 (1,1), 1 para muitos (1,n), muitos para muitos (n,n).
3. Atributos são características ou propriedades que descrevem uma entidade. A entidade “Cliente” pode, por exemplo, ter os atributos “nome”, “sobrenome”, “endereço” e etc.
4. O domínio refere-se ao conjunto de valores permitidos, como um limite/intervalo para um atributo. Ex.: o domínio do atributo “idade” pode variar entre 0-120; o domínio do atributo “sexo” pode ser feminino, masculino ou outro.
5. Generalização/especialização é um conceito no modelo de dados de Entidade-Relacionamento (ER) que permite organizar entidades em hierarquias. A generalização é o processo de agrupar entidades semelhantes em uma entidade mais genérica, enquanto a especialização é o processo oposto, onde uma entidade mais genérica é dividida em entidades mais específicas.
6. Uma entidade associativa é usada em um modelo de banco de dados para representar uma relação muitos-para-muitos entre outras entidades, quando uma relação direta entre elas não é suficiente. Ela atua como uma tabela intermediária para conectar as entidades envolvidas, permitindo uma representação precisa da associação.
7. A cardinalidade de um atributo indica quantos valores ele pode ter em uma relação específica, podendo ser de 1 (um valor por instância) ou de muitos (vários valores por instância). Por exemplo, um atributo "telefone" pode ter uma cardinalidade de muitos se uma entidade puder ter vários números de telefone associados a ela.
