desc;

CREATE TABLE IF NOT EXISTS marts.gender_age as(
SELECT * FROM 
tittare.tabelldata_alder
CROSS JOIN
tittare.tabelldata_kon

);