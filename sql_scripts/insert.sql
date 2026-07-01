insert into colors (name, hex) values ('schwarz','#FFFFFF');
insert into colors (name) values ('xyz');
insert into colors (hex) values ('#123123');

insert into colors (name, hex,datum) values ('schwarz2','#FFFFFF','2026-05-05');
insert into colors (name, hex) values ('grau2','#777777');


-- UPDATE

update colors c set hex ='#888888' where  name='grau2';

-- DELETE

delete from colors where id=1
