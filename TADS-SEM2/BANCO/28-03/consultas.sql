SELECT number, gender, givenname 
FROM fakenames 
LIMIT 10;

SELECT gender, givenname, number
FROM fakenames 
LIMIT 10;

SELECT number as ID, gender as genero, givenname as nome, surname as sobrenome, city as cidade, state as UF, statefull as estado
INTO Pessoa 
FROM fakenames
WHERE givenname = 'Paulo' 
LIMIT 10;

SELECT number as ID, gender as genero, givenname as nome, surname as sobrenome, city as cidade, state as UF, statefull as estado
INTO Pessoa 
FROM fakenames;

SELECT id, nome, sobrenome, cidade, UF
FROM Pessoa