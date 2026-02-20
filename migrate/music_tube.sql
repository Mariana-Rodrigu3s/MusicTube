create database if not exists MusicTube;

use MusicTube;

create table if not exists genero (
nome varchar(30) not null primary key,
icone char(100),
cor char(10)
);


create table if not exists musica (
codigo int not null primary key auto_increment,
cantor varchar(50),
duracao time, 
nome varchar(50),
url_imagem varchar(255),
nome_genero varchar(30),
constraint fk_musica_genero foreign key (nome_genero) references genero(nome)
);