INSERT INTO Usuario(Nickname, Senha, Identificacao) VALUES ('user1', 'user1',1);
INSERT INTO Usuario(Nickname, Senha, Identificacao) VALUES ('user2', 'user2',2);
INSERT INTO Usuario(Nickname, Senha, Identificacao) VALUES ('user3', 'user3',3);
INSERT INTO Usuario(Nickname, Senha, Identificacao) VALUES ('user4', 'user4',4);
INSERT INTO Usuario(Nickname, Senha, Identificacao) VALUES ('user5', 'user5',5);
INSERT INTO Usuario(Nickname, Senha, Identificacao) VALUES ('user6', 'user6',6);

INSERT INTO Administrador(Identificacao) VALUES (1);
INSERT INTO Administrador(Identificacao) VALUES (2);
INSERT INTO Administrador(Identificacao) VALUES (3);


INSERT INTO Colaborador(Identificacao) VALUES (4);
INSERT INTO Colaborador(Identificacao) VALUES (5);
INSERT INTO Colaborador(Identificacao) VALUES (6);


INSERT INTO Comunidade(Identificacao, Seguidores, Numero_de_leitores) VALUES (1, 1, 1);
INSERT INTO Comunidade(Identificacao, Seguidores, Numero_de_leitores) VALUES (2, 2, 2);
INSERT INTO Comunidade(Identificacao, Seguidores, Numero_de_leitores) VALUES (3, 3, 3);
INSERT INTO Comunidade(Identificacao, Seguidores, Numero_de_leitores) VALUES (4, 4, 4);
INSERT INTO Comunidade(Identificacao, Seguidores, Numero_de_leitores) VALUES (5, 5, 5);
INSERT INTO Comunidade(Identificacao, Seguidores, Numero_de_leitores) VALUES (6, 6, 6);
INSERT INTO Comunidade(Identificacao, Seguidores, Numero_de_leitores) VALUES (7, 7, 7);

INSERT INTO Curiosidade(Identificacao, Curiosidade) VALUES (1, 'Filme');
INSERT INTO Curiosidade(Identificacao, Curiosidade) VALUES (2, 'Filme');
INSERT INTO Curiosidade(Identificacao, Curiosidade) VALUES (3, 'Serie');
INSERT INTO Curiosidade(Identificacao, Curiosidade) VALUES (4, 'Serie');
INSERT INTO Curiosidade(Identificacao, Curiosidade) VALUES (5, 'Personagem');
INSERT INTO Curiosidade(Identificacao, Curiosidade) VALUES (6, 'Quadrinho');
INSERT INTO Curiosidade(Identificacao, Curiosidade) VALUES (7, 'Cenario');


INSERT INTO Interage(IdentificacaoColaborador, IdentificacaoComunidade) VALUES (4, 1);
INSERT INTO Interage(IdentificacaoColaborador, IdentificacaoComunidade) VALUES (4, 5);
INSERT INTO Interage(IdentificacaoColaborador, IdentificacaoComunidade) VALUES (5, 2);

INSERT INTO Postagem(IdentificacaoInterageColaborador, IdentificacaoInterageComunidade, IdentificacaoPostagem, DataComentario, Comentario) VALUES (4, 1, 1, '2021-12-11', 'legal');
INSERT INTO Postagem(IdentificacaoInterageColaborador, IdentificacaoInterageComunidade, IdentificacaoPostagem, DataComentario, Comentario) VALUES (5, 2, 2, '2021-12-10', 'nao gostei');


INSERT INTO Gerencia(IdentificacaoAdministrador, IdentificacaoComunidade, DataInicio, DataFim) VALUES (1, 1, '2021-12-11', NULL);
INSERT INTO Gerencia(IdentificacaoAdministrador, IdentificacaoComunidade, DataInicio, DataFim) VALUES (2, 1, '2021-11-11', NULL);

INSERT INTO Midia(Avaliacao, Sinopse, Nome, Identificacao) VALUES (99.2, 'Peter Morreu', 'Homem Aranha', 1);
INSERT INTO Midia(Avaliacao, Sinopse, Nome, Identificacao) VALUES (98.2, 'Peter Morreu Denovo', 'Homem Aranha2', 2);
INSERT INTO Midia(Avaliacao, Sinopse, Nome, Identificacao) VALUES (97.2, 'Jhon Shelby morre', 'Peaky Blinder', 3);
INSERT INTO Midia(Avaliacao, Sinopse, Nome, Identificacao) VALUES (96.2, 'Rick foi embora', 'Rick Morty', 4);


INSERT INTO Genero(Nome, Identificacao) VALUES ('Acao', 1);
INSERT INTO Genero(Nome, Identificacao) VALUES ('Ficcao', 2);


INSERT INTO Contem(IdentificacaoMidia, IdentificacaoGenero) VALUES (1, 2);
INSERT INTO Contem(IdentificacaoMidia, IdentificacaoGenero) VALUES (2, 2);
INSERT INTO Contem(IdentificacaoMidia, IdentificacaoGenero) VALUES (3, 1);
INSERT INTO Contem(IdentificacaoMidia, IdentificacaoGenero) VALUES (4, 2);

INSERT INTO Filme(Bilheteria, Duracao, Identificacao) VALUES (100, 7200,1);
INSERT INTO Filme(Bilheteria, Duracao, Identificacao) VALUES (500, 7600,2);

INSERT INTO Serie(Identificacao) VALUES (3);
INSERT INTO Serie(Identificacao) VALUES (4);

INSERT INTO Episodio(Nome, Numero, Duracao, IdentificacaoSerie) VALUES ('Ep1', 1, '00:50:23', 3);
INSERT INTO Episodio(Nome, Numero, Duracao, IdentificacaoSerie) VALUES ('Ep2', 2, '00:45:08', 3);
INSERT INTO Episodio(Nome, Numero, Duracao, IdentificacaoSerie) VALUES ('Ep1', 1, '00:22:23', 4);
INSERT INTO Episodio(Nome, Numero, Duracao, IdentificacaoSerie) VALUES ('Ep2', 2, '00:21:50', 4);

INSERT INTO Personagem(Historia, Nome, Habilidade, Idade, Identificacao) VALUES ('Stand mais poderoso', 'Jotaro', 'Star Platinum', 40, 5);

INSERT INTO Autor(Avaliacao, Nacionalidade, Identificacao, Nome) VALUES (99.9, 'Brasileiro', 1, 'Mauricio');
INSERT INTO Autor(Avaliacao, Nacionalidade, Identificacao, Nome) VALUES (95.9, 'Brasileiro', 2, 'Jhon');

INSERT INTO Quadrinho(Editora, Nome, Volume, Identificacao, IDAutor) VALUES ('Limitada', 'Turma da Monica', 2, 6,1);

INSERT INTO Cenario(Descricao, Origem, Nome, Identificacao) VALUES ('Onde Hashirama e Madara Lutou', 'Naruto', 'Vale do Fim', 7);













































































