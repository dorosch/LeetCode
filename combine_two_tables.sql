-- Data
create table person (
    personId BIGSERIAL PRIMARY KEY,
    lastName varchar(64),
    firstName varchar(64)
);

create table address (
    addressId BIGSERIAL PRIMARY KEY,
    personId BIGSERIAL REFERENCES person (personId),
    city varchar(64),
    state varchar(64)
);

insert into person (lastName, firstName) values ('Wang', 'Allen');
insert into person (lastName, firstName) values ('Alice', 'Bob');
insert into address (personId, city, state) values (1, 'Los Angeles', 'California');
insert into address (personId, city, state) values (2, 'New York City', 'New York');


-- Answer
select firstName, lastName, city, state from person left join address on person.personId = address.personId;
