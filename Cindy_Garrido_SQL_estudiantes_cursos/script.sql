-- 1. Crear 3 cursos nuevos

INSERT INTO cursos (nombre, created_at, updated_at) 
VALUES 
('Matemáticas Avanzadas', NOW(), NOW()),
('Literatura Contemporánea', NOW(), NOW()),
('Programación en Python', NOW(), NOW());

--2. Eliminar los 3 cursos creados

DELETE FROM cursos WHERE nombre = 'Matemáticas Avanzadas' ;
DELETE FROM cursos WHERE nombre = 'Literatura Contemporánea' ;
DELETE FROM cursos WHERE nombre = 'Programación en Python';

-- 3. Crear otros 3 cursos nuevos

INSERT INTO cursos (nombre, created_at, updated_at) 
VALUES 
('Historia Universal', NOW(), NOW()),
('Biología Molecular', NOW(), NOW()),
('Diseño Gráfico', NOW(), NOW());

-- 4. Crear 3 estudiantes inscritos en el primer curso

-- Primero obtenemos el ID del primer curso
SET @primer_curso = (SELECT id FROM cursos ORDER BY id ASC LIMIT 1);

-- Insertamos estudiantes
INSERT INTO estudiantes (nombre, apellido, edad, created_at, updated_at, curso_id) 
VALUES 
('Juan', 'Pérez', 20, NOW(), NOW(), @primer_curso),
('María', 'Gómez', 21, NOW(), NOW(), @primer_curso),
('Carlos', 'López', 19, NOW(), NOW(), @primer_curso);

-- 5. Crear 3 estudiantes inscritos en el segundo curso

-- Obtenemos el ID del segundo curso
SET @segundo_curso = (SELECT id FROM cursos ORDER BY id ASC LIMIT 1 OFFSET 1);

INSERT INTO estudiantes (nombre, apellido, edad, created_at, updated_at, curso_id) 
VALUES 
('Ana', 'Martínez', 22, NOW(), NOW(), @segundo_curso),
('Luis', 'Rodríguez', 20, NOW(), NOW(), @segundo_curso),
('Sofía', 'Hernández', 21, NOW(), NOW(), @segundo_curso);

-- 6. Crear 3 estudiantes inscritos en el tercer curso

-- Obtenemos el ID del tercer curso
SET @tercer_curso = (SELECT id FROM cursos ORDER BY id ASC LIMIT 1 OFFSET 2);

INSERT INTO estudiantes (nombre, apellido, edad, created_at, updated_at, curso_id) 
VALUES 
('Pedro', 'Sánchez', 23, NOW(), NOW(), @tercer_curso),
('Laura', 'Díaz', 20, NOW(), NOW(), @tercer_curso),
('Jorge', 'Fernández', 19, NOW(), NOW(), @tercer_curso);

-- 7. Recuperar todos los estudiantes del primer curso

SELECT e.* 
FROM estudiantes e
JOIN cursos c ON e.curso_id = c.id
WHERE c.id = (SELECT id FROM cursos ORDER BY id ASC LIMIT 1);

-- 8. Recuperar todos los estudiantes del último curso

SELECT e.* 
FROM estudiantes e
JOIN cursos c ON e.curso_id = c.id
WHERE c.id = (SELECT id FROM cursos ORDER BY id DESC LIMIT 1);

-- 9. Recuperar el curso del último estudiante

SELECT c.* 
FROM cursos c
JOIN estudiantes e ON c.id = e.curso_id
WHERE e.id = (SELECT id FROM estudiantes ORDER BY id DESC LIMIT 1);