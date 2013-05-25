#Website

##Installation

###Clone the repository:
	git clone git@github.com:CSE-Club/Website.git

###Set webroot:
public/ should be your webservers root, other files should be one level up from it.

###Get Composer:
	curl -sS https://getcomposer.org/installer | php

###Install Laravel Dependencies:
	php composer.phar install

###Set up a database:
PostgreSQL, MySQL, SQLite, and SQL Server should all work

###Set up a cache driver (Optional):
Memcached or APC recommended

###Set up config:
	cp -r app/config.default app/config
Edit each config file appropriately.

###Run migrations:
	php artisan migrate

That's it!
