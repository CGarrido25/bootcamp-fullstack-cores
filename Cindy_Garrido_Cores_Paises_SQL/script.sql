SELECT * FROM mundo.paises p INNER JOIN mundo.idiomas i ON  p.id = i.pais_id WHERE i.idioma = "Español";

SELECT 
    p.nombre AS nombre_pais,
    i.idioma,
    COUNT(c.id) AS total_ciudades
FROM 
    paises p
LEFT JOIN 
    ciudades c ON p.id = c.pais_id
LEFT JOIN 
    idiomas i ON p.id = i.pais_id AND i.es_oficial = 'T'
GROUP BY 
    p.id, p.nombre, i.idioma
ORDER BY 
    total_ciudades DESC;



SELECT c.nombre,c.poblacion  FROM mundo.ciudades c 
INNER JOIN 
	mundo.paises p ON  c.pais_id = p.id 
WHERE 
	p.nombre = "Chile"
AND  
	c.poblacion > 200000
ORDER BY 
	c.poblacion	DESC
		


SELECT p.nombre, i.idioma, i.porcentage 
FROM mundo.paises p 
INNER JOIN 
	mundo.idiomas i ON  p.id = i.pais_id 
WHERE i.porcentage > 89
ORDER BY 
	i.porcentage	DESC


SELECT p.nombre, p.area_superficie , p.poblacion
FROM mundo.paises p 
WHERE
	p.poblacion > 10000
AND 
	p.area_superficie < 501 ;

SELECT 
    nombre AS pais,
    tipo_gobierno,
    capital,
    esperanza_vida
FROM 
    paises
WHERE 
    tipo_gobierno LIKE '%República%'
    AND capital > 2000
    AND esperanza_vida > 78
ORDER BY 
    esperanza_vida DESC;
    
SELECT 
    p.nombre AS pais,
    c.nombre AS ciudad,
    c.distrito,
    c.poblacion
FROM 
    ciudades c
JOIN 
    paises p ON c.pais_id = p.id
WHERE 
    p.nombre = 'Colombia'
    AND c.distrito = 'Valle'
    AND c.poblacion > 200000
ORDER BY 
    c.poblacion DESC;
    
SELECT 
    region,
    COUNT(id) AS numero_paises
FROM 
    paises
GROUP BY 
    region
ORDER BY 
    numero_paises DESC;