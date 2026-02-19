USE MusicTube;

INSERT INTO `musictube`.`genero`
(`nome`,
`icone`,
`cor`)
VALUES
("Kpop", "","blue"),
("Metal Gótico", "","red"),
("Infantil", "","pink");


INSERT INTO `musictube`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)
VALUES
("AESPA",
"03:14",
"Supernova",
"https://conteudo.imguol.com.br/c/entretenimento/02/2024/05/27/aespa-em-foto-do-disco-armageddon-1716841315538_v2_4x3.jpg",
"Kpop"),
("Type O Negative",
"07:09",
"Love You to Death",
"https://i.etsystatic.com/43716471/c/2000/1588/0/338/il/496d7d/5027685283/il_340x270.5027685283_fyhv.jpg",
"Metal Gótico"),
("PinkiePie",
"03:23",
"The Smile Song",
"https://cdn.staticneo.com/w/mylittlepony/thumb/PinkiePie.png/300px-PinkiePie.png",
"Infantil");
