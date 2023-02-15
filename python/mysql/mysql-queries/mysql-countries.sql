SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.code = languages.country_code
WHERE languages.language = "Slovene";

SELECT countries.name, COUNT(cities.country_id)
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.country_id) DESC;

SELECT cities.name, cities.population, cities.country_id FROM countries
JOIN cities on countries.id = cities.country_id
WHERE countries.name = "Mexico"
ORDER BY cities.population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT * FROM countries
WHERE countries.surface_area < 501
AND countries.population > 100000;

SELECT * FROM countries
WHERE countries.government_form = "Constitutional Monarchy"
AND countries.capital > 200
AND countries.life_expectancy > 75;

SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Argentina"
AND cities.district = "Buenos Aires"
AND cities.population > 500000;

SELECT region, COUNT(id)
FROM countries
GROUP BY region
ORDER BY COUNT(id) DESC;