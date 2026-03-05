create database if not exists LunaWave;

use LunaWave;

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
url_imagem varchar(800),
nome_genero varchar(30),
constraint fk_musica_genero foreign key (nome_genero) references genero(nome)
);

create table if not exists cadastro(
id int not null primary key auto_increment,
usuario varchar(50) unique, 
senha varchar(100) not null
);



alter table musica
add column ativo bool default 0;