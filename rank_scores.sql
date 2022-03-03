-- Data
create table Scores (id serial primary key, score decimal);

insert into Scores (score) values (3.50), (3.65), (4.0), (3.85), (4.0), (3.65);


-- Answer
select score, dense_rank () over (order by score desc) as rank from Scores;
