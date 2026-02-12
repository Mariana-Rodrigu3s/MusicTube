CREATE TABLE genero (
 nome_genero VARCHAR(30) NOT NULL,
 icone VARCHAR(50),
 cor VARCHAR(10)
);

ALTER TABLE genero ADD CONSTRAINT PK_genero PRIMARY KEY (nome_genero);


CREATE TABLE musica (
 código INT NOT NULL,
 cantor VARCHAR(50),
 duracao TIME(10),
 nome VARCHAR(50),
 url_imagem VARCHAR(200),
 nome_genero VARCHAR(30)
);

ALTER TABLE musica ADD CONSTRAINT PK_musica PRIMARY KEY (código);


ALTER TABLE musica ADD CONSTRAINT FK_musica_0 FOREIGN KEY (nome_genero) REFERENCES genero (nome_genero);


