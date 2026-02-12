create database IF NOT exists musictube;

use  musictube;


CREATE TABLE if not exists genero (
 nome_genero VARCHAR(30) NOT NULL primary key,
 icone VARCHAR(50),
 cor VARCHAR(10)
);




CREATE TABLE if not exists musica (
 código INT NOT NULL primary key auto_increment,
 cantor VARCHAR(50),
 duracao TIME,
 nome VARCHAR(50),
 url_imagem VARCHAR(200),
 nome_genero VARCHAR(30),
 constraint fk_musica_genero foreign key (nome_genero) references genero (nome_genero)
 );






