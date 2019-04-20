## Homework 7

#1a. Display the first and last names of all actors from the table actor.
select first_name, last_name 
from actor;

#1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
select upper(concat(first_name , " " , last_name)) AS "Actor Name" 
from actor;

#2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?
select actor_id, first_name, last_name
from actor
where first_name="Joe";

#2b. Find all actors whose last name contain the letters GEN:
select actor_id, first_name, last_name
from actor
where last_name like "%GEN%";

#2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:
select actor_id, first_name, last_name
from actor
where last_name like "%LI%"
order by last_name, first_name;

#2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
select country_id, country
from country
where country in ("Afghanistan", "Bangladesh",  "China" );

#3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, so create a column in the table actor named description and use the data type BLOB (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).
ALTER TABLE actor ADD COLUMN description blob;
#Added this to verify column add
describe actor;
#3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
Alter Table actor DROP COLUMN description;
#Added this to verify column delete
describe actor;
#4a. List the last names of actors, as well as how many actors have that last name.
select count(*), last_name
from actor
group by last_name;

#4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors
select count(*), last_name
from actor
group by last_name
having count(*) > 1;

#4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
update actor
set first_name="HARPO"
where first_name= "GROUCHO" AND last_name="WILLIAMS"
;

select * from actor 
where first_name= "HARPO" AND last_name="WILLIAMS";
#4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
update actor
set first_name="GROUCHO"
where first_name= "HARPO" AND last_name="WILLIAMS"
;

select * from actor 
where first_name= "GROUCHO" AND last_name="WILLIAMS";

#5a. You cannot locate the schema of the address table. Which query would you use to re-create it?

#Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html

show create table address;

#Results from show create table are below:
# CREATE TABLE `address` (
#  `address` varchar(50) NOT NULL,
#  `address2` varchar(50) DEFAULT NULL,
#  `district` varchar(20) NOT NULL,
#  `city_id` smallint(5) unsigned NOT NULL,
#  `postal_code` varchar(10) DEFAULT NULL,
#  `phone` varchar(20) NOT NULL,
#  `location` geometry NOT NULL,
#  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#  PRIMARY KEY (`address_id`),
#  KEY `idx_fk_city_id` (`city_id`),
#  SPATIAL KEY `idx_location` (`location`),
#  CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
#) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8


#6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
select * from staff limit 10; #looking at each table
select * from address limit 10; #looking at each table

select s.first_name, s.last_name, a.address
from staff s
join address a on s.address_id=a.address_id;

#6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
select * from payment limit 10; #Checking payment
select sum(p.amount), s.first_name, s.last_name
from payment p, staff s
where p.staff_id=s.staff_id
group by s.first_name, s.last_name;


#6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
select * from film_actor limit 10; # looking at the Film Actor table

select count(fa.actor_id), f.title
from film f, film_actor fa
where f.film_id = fa.film_id
group by f.title;

#6d. How many copies of the film Hunchback Impossible exist in the inventory system?
select * from inventory limit 10; #looking at inventory table

select count(i.inventory_id)
from inventory i, film f
where i.film_id=f.film_id
AND f.title="Hunchback Impossible";


#6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
select * from payment limit 10;
select * from customer limit 10;

select sum(p.amount) ,c.last_name, c.first_name
from payment p, customer c
where p.customer_id=c.customer_id
group by c.last_name, c.first_name
order by c.last_name, c.first_name


#7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.


#7b. Use subqueries to display all actors who appear in the film Alone Trip.


#7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.


#7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.


#7e. Display the most frequently rented movies in descending order.


#7f. Write a query to display how much business, in dollars, each store brought in.


#7g. Write a query to display for each store its store ID, city, and country.


#7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)


#8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.


#8b. How would you display the view that you created in 8a?


#8c. You find that you no longer need the view top_five_genres. Write a query to delete it.



