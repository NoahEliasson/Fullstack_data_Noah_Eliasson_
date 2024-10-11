desc;

SELECT * FROM operativsystem.diagramdata;

CREATE SCHEMA IF NOT EXISTS marts; 
-- DROP TABLE IF EXISTS marts.operationsystem_view;

CREATE TABLE IF NOT EXISTS marts.operationsystem_view AS
(
    SELECT 
        operativsystem, 
        SUM(visningar) AS total_visningar
    FROM 
        operativsystem.diagramdata
    GROUP BY 
        operativsystem
);