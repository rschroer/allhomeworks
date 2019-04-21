## Homework 7

#1a. Display the first and last names of all actors from the table actor.
SELECT first_name, last_name 
FROM actor;

#1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.
SELECT upper(cONcat(first_name , " " , last_name)) AS "Actor Name" 
FROM actor;

#2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is ONe query would you use to obtain this informatiON?
SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name="Joe";

#2b. Find all actors whose last name contain the letters GEN:
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE "%GEN%";

#2c. Find all actors whose last names contain the letters LI. This time, order the rows BY last name and first name, in that order:
SELECT actor_id, first_name, last_name
FROM actor
WHERE last_name LIKE "%LI%"
ORDER BY last_name, first_name;

#2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:
SELECT country_id, country
FROM country
WHERE country IN  ("Afghanistan", "Bangladesh",  "China" );

#3a. You want to keep a description of each actor. You dON't think you will be performing queries on a description, so create a column in the table actor named descriptiON and use the data type BLOB (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).
ALTER TABLE actor ADD COLUMN description BLOB;
#Added this to verify column add
DESC actor;
#3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.
ALTER TABLE actor DROP COLUMN description;
#Added this to verify column delete
DESC actor;
#4a. List the last names of actors, as well as how many actors have that last name.
SELECT COUNT(*), last_name
FROM actor
GROUP BY last_name;

#4b. List last names of actors and the number of actors who have that last name, but only for names that are shared BY at least two actors
SELECT COUNT(*), last_name
FROM actor
GROUP BY last_name
HAVING COUNT(*) > 1;

#4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.
UPDATE actor
SET first_name="HARPO"
WHERE first_name= "GROUCHO" AND last_name="WILLIAMS"
;

SELECT * FROM actor 
WHERE first_name= "HARPO" AND last_name="WILLIAMS";
#4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.
UPDATE actor
SET first_name="GROUCHO"
WHERE first_name= "HARPO" AND last_name="WILLIAMS"
;

SELECT * FROM actor 
WHERE first_name= "GROUCHO" AND last_name="WILLIAMS";

#5a. You cannot locate the schema of the address table. Which query would you use to re-create it?

#Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html

SHOW CREATE TABLE address;

#Results FROM show create table are below:
# CREATE TABLE `address` (
#  `address` varchar(50) NOT NULL,
#  `address2` varchar(50) DEFAULT NULL,
#  `district` varchar(20) NOT NULL,
#  `city_id` smallint(5) unsigned NOT NULL,
#  `postal_code` varchar(10) DEFAULT NULL,
#  `phONe` varchar(20) NOT NULL,
#  `locatiON` geometry NOT NULL,
#  `last_update` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
#  PRIMARY KEY (`address_id`),
#  KEY `idx_fk_city_id` (`city_id`),
#  SPATIAL KEY `idx_locatiON` (`locatiON`),
#  CONSTRAINT `fk_address_city` FOREIGN KEY (`city_id`) REFERENCES `city` (`city_id`) ON UPDATE CASCADE
#) ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8


#6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:
SELECT * FROM staff LIMIT 10; #looking at each table
SELECT * FROM address LIMIT 10; #looking at each table

SELECT s.first_name, s.last_name, a.address
FROM staff s
JOIN address a ON s.address_id=a.address_id;

#6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.
SELECT * FROM payment LIMIT 10; #Checking payment

SELECT SUM(p.amount), s.first_name, s.last_name
FROM payment p, staff s
WHERE p.staff_id=s.staff_id
GROUP BY s.first_name, s.last_name;


#6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.
SELECT * FROM film_actor LIMIT 10; # looking at the Film Actor table

SELECT COUNT(fa.actor_id) AS "Number of Copies", f.title
FROM film f, film_actor fa
WHERE f.film_id = fa.film_id
GROUP BY f.title;

#6d. How many copies of the film Hunchback Impossible exist in the inventory system?
SELECT * FROM inventory LIMIT 10; #looking at inventory table

SELECT COUNT(i.inventory_id) AS "Number of Copies"
FROM inventory i, film f
WHERE i.film_id=f.film_id
AND f.title="Hunchback Impossible";


#6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:
SELECT * FROM payment LIMIT 10;
SELECT * FROM customer LIMIT 10;

SELECT SUM(p.amount) AS "Total Paid" ,c.last_name, c.first_name
FROM payment p
JOIN customer c ON p.customer_id=c.customer_id
GROUP BY c.last_name, c.first_name
ORDER BY c.last_name, c.first_name;


#7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. As an unintended consequence, films starting with the letters K and Q have also soared in popularity. Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.
SELECT language_id 
FROM language l
WHERE l.name="english";

SELECT title 
FROM film
WHERE 
	language_id = ( SELECT language_id 
					FROM language l
					WHERE l.name="english" )
	AND (title LIKE "K%" OR title LIKE "Q%")
;

#7b. Use subqueries to display all actors who appear in the film Alone Trip.
SELECT first_name, last_name 
FROM actor
WHERE actor_id in 	(SELECT actor_id
					FROM film_actor
					WHERE film_id IN 	(SELECT film_id
										FROM film
										WHERE title="Alone Trip"))
;

#7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.
SELECT * 
FROM customer c
JOIN address a ON a.address_id=c.address_id
JOIN city ON a.city_id=city.city_id
JOIN country ctry ON city.country_id=ctry.country_id  
AND ctry.country="Canada"
;

#7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.
SELECT f.title, c.name
FROM film f
JOIN film_category fc ON f.film_id=fc.film_id
JOIN category c ON c.category_id = fc.category_id
WHERE c.name="Family"
;

#7e. Display the most frequently rented movies in descending order.
SELECT f.title, COUNT(rental_id) AS "Number of Rentals"
FROM rental r
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film f ON f.film_id = i.film_id
GROUP BY f.title
ORDER BY COUNT(rental_id) DESC
;

#7f. Write a query to display how much business, in dollars, each store brought in.
SELECT s.store_id, SUM(p.amount) AS "Store Total"
FROM payment p
JOIN staff s ON p.staff_id=s.staff_id
GROUP BY s.store_id;

#7g. Write a query to display for each store its store ID, city, and country.
SELECT s.store_id, c.city, cn.country 
FROM store s
JOIN address a ON s.address_id=a.address_id
JOIN city c ON a.city_id=c.city_id
JOIN country cn ON c.country_id=cn.country_id
;

#7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)

SELECT  c.name AS "Category Name", SUM(p.amount) AS "Category Total"
FROM payment p
JOIN rental r ON r.rental_id=p.rental_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film_category fc ON fc.film_id = i.film_id
JOIN category c ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY 2 DESC
LIMIT 5
;




#8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.
CREATE VIEW top_5 AS
SELECT  c.name AS "Category Name", SUM(p.amount) AS "Category Total"
FROM payment p
JOIN rental r ON r.rental_id=p.rental_id
JOIN inventory i ON i.inventory_id = r.inventory_id
JOIN film_category fc ON fc.film_id = i.film_id
JOIN category c ON c.category_id = fc.category_id
GROUP BY c.name
ORDER BY 2 DESC
LIMIT 5
;

#8b. How would you display the view that you created in 8a?
SELECT * FROM top_5;

#8c. You find that you no longer need the view top_five_genres. Write a query to delete it.
DROP VIEW top_5;


