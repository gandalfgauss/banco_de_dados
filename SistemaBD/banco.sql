CREATE TABLE Usuario (
    Nickname        VARCHAR(10)     NOT NULL,
    Senha           VARCHAR(8)      NOT NULL,
    Identificacao   SERIAL,
    CONSTRAINT PK_Usuario PRIMARY KEY(Identificacao),
    CONSTRAINT UK_Nickname UNIQUE (Nickname)
);

CREATE TABLE Administrador (
    Identificacao   SERIAL,
    CONSTRAINT PK_Administrador PRIMARY KEY(Identificacao),
    CONSTRAINT FK_Usuario FOREIGN KEY(Identificacao)
        REFERENCES Usuario (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    
    CONSTRAINT UK_Adm UNIQUE (Identificacao)
);

CREATE TABLE Colaborador (
    Identificacao   SERIAL,
    CONSTRAINT PK_Colaborador PRIMARY KEY(Identificacao),
    CONSTRAINT FK_Usuario FOREIGN KEY(Identificacao)
        REFERENCES Usuario (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT UK_Col  UNIQUE(Identificacao)
);

CREATE TABLE Comunidade (
    Identificacao   SERIAL,
    Seguidores          INT             NOT NULL,
    Numero_de_leitores  INT             NOT NULL,
    CONSTRAINT PK_Comunidade PRIMARY KEY(Identificacao)
);

CREATE TABLE Curiosidade (
    Identificacao SERIAL,
    Curiosidade VARCHAR(240) NULL,
    CONSTRAINT FK_Comunidade FOREIGN KEY(Identificacao)
        REFERENCES Comunidade (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Curiosidade PRIMARY KEY(Curiosidade,Identificacao)
);

CREATE TABLE Interage (
    IdentificacaoColaborador SERIAL,
    IdentificacaoComunidade SERIAL,
    CONSTRAINT FK_Comunidade FOREIGN KEY(IdentificacaoComunidade)
        REFERENCES Comunidade (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT FK_Colaborador FOREIGN KEY(IdentificacaoColaborador)
        REFERENCES Colaborador (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Interage PRIMARY KEY(IdentificacaoComunidade,IdentificacaoColaborador)
);

CREATE TABLE Postagem (
    IdentificacaoInterageColaborador SERIAL,
    IdentificacaoInterageComunidade SERIAL,
    IdentificacaoPostagem SERIAL,
    DataComentario DATE NOT NULL,
    Comentario VARCHAR(500) NOT NULL,
    CONSTRAINT FK_Interage FOREIGN KEY(IdentificacaoInterageColaborador, IdentificacaoInterageComunidade)
        REFERENCES Interage (IdentificacaoColaborador, IdentificacaoComunidade)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Postagem PRIMARY KEY(IdentificacaoInterageComunidade,IdentificacaoInterageColaborador,IdentificacaoPostagem)
);

CREATE TABLE Gerencia (
    IdentificacaoAdministrador SERIAL,
    IdentificacaoComunidade SERIAL,
    DataInicio DATE NOT NULL,
    DataFim DATE NULL,
    CONSTRAINT FK_IdentificacaoAdminstrador FOREIGN KEY(IdentificacaoAdministrador)
        REFERENCES Administrador (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT FK_IdentificacaoComunidade FOREIGN KEY(IdentificacaoComunidade)
        REFERENCES Comunidade (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Gerencia PRIMARY KEY(IdentificacaoAdministrador,IdentificacaoComunidade)
);

CREATE TABLE Midia (
    Avaliacao       NUMERIC(3,1)    NOT NULL,
    Sinopse         VARCHAR(240)    NOT NULL,
    Nome            VARCHAR(50)     NOT NULL,
    Identificacao   SERIAL,
    CONSTRAINT FK_IdentificacaoMidia FOREIGN KEY(Identificacao)
        REFERENCES Comunidade (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Midia PRIMARY KEY(Identificacao)
);

CREATE TABLE Genero (
    Nome            VARCHAR(50)     NOT NULL,
    Identificacao   SERIAL,
    CONSTRAINT PK_Genero PRIMARY KEY(Identificacao)
);

CREATE TABLE Contem (
    IdentificacaoMidia  SERIAL,
    IdentificacaoGenero SERIAL,
    CONSTRAINT FK_IdentificacaoMidia FOREIGN KEY(IdentificacaoMidia)
        REFERENCES Midia (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT FK_IdentificacaoGenero FOREIGN KEY(IdentificacaoGenero)
        REFERENCES Genero (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Contem PRIMARY KEY(IdentificacaoMidia,IdentificacaoGenero)
);

CREATE TABLE Filme (
    Bilheteria  INT     NOT NULL,
    Duracao     INT     NOT NULL,
    Identificacao   SERIAL,
    CONSTRAINT FK_IdentificacaoFilme FOREIGN KEY(Identificacao)
        REFERENCES Midia (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Filme PRIMARY KEY(Identificacao)
);

CREATE TABLE Serie (
    Identificacao   SERIAL,
    CONSTRAINT FK_IdentificacaoSerie FOREIGN KEY(Identificacao)
        REFERENCES Midia (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Serie PRIMARY KEY(Identificacao)
);

CREATE TABLE Episodio (
    Nome        VARCHAR(240)    NOT NULL,
    Numero      INT             NOT NULL,
    Duracao     TIME            NOT NULL,
    IdentificacaoSerie  SERIAL,
    CONSTRAINT FK_IdentificacaoEpisodio FOREIGN KEY(IdentificacaoSerie)
        REFERENCES Serie (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Episodio PRIMARY KEY(IdentificacaoSerie,Numero)
);

CREATE TABLE Personagem (
    Historia        VARCHAR(500)    NOT NULL,
    Nome            VARCHAR(50)     NOT NULL,
    Habilidade      VARCHAR(100)    NOT NULL,
    Idade           INT             NOT NULL,
    Identificacao   SERIAL,
    CONSTRAINT FK_IdentificacaoPersonagem FOREIGN KEY(Identificacao)
        REFERENCES Comunidade (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Personagem PRIMARY KEY(Identificacao)
);

CREATE TABLE Autor (
    Avaliacao       NUMERIC(5,1)    NOT NULL,
    Nacionalidade   VARCHAR(50)     NOT NULL,
    Identificacao   SERIAL,
    Nome            VARCHAR(50)    NOT NULL,
    CONSTRAINT PK_Autor PRIMARY KEY(Identificacao)
);

CREATE TABLE Quadrinho (
    Editora         VARCHAR(50)     NOT NULL,
    Nome            VARCHAR(100)    NOT NULL,
    Volume          INT             NOT NULL,
    Identificacao   SERIAL,
    IDAutor SERIAL,
    CONSTRAINT FK_IdentificacaoQuadrinho FOREIGN KEY(Identificacao)
        REFERENCES Comunidade (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT FK_IDAutor FOREIGN KEY(IDAutor)
        REFERENCES Autor (Identificacao)
        ON UPDATE CASCADE,
    CONSTRAINT PK_Quadrinho PRIMARY KEY(Identificacao)
);

CREATE TABLE Cenario (
    Descricao       VARCHAR(240)    NOT NULL,
    Origem          VARCHAR(100)    NOT NULL,
    Nome            VARCHAR(50)     NOT NULL,
    Identificacao   SERIAL,
    CONSTRAINT FK_IdentificacaoCenario FOREIGN KEY(Identificacao)
        REFERENCES Comunidade (Identificacao)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT PK_Cenario PRIMARY KEY(Identificacao)
);
