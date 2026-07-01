
-- db_music
select composer, count(*) as Anzahl from track group by composer;


-- db_books
select customers.lastname , sum(amount) as Gesamtbestellwert
from orders 
join customers on customers.id = orders.customer_id
group by customer_id
having Gesamtbestellwert > 200;

-- db_littlemusic
select  al.id as `Album ID`,
		al.name as `Album Name`,
		ar.name as `Artist Name`
	from album al 
	join artist ar on ar.id = al.artist_id;  



