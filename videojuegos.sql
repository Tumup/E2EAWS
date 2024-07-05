CREATE EXTERNAL TABLE IF NOT EXISTS videojuegos (
  empresa_desarrolladora STRING,
  anio_publicacion INT,
  genero STRING,
  titulo STRING,
  id STRING,
  competicion STRING
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
)
LOCATION 's3://aws-project-videojuegos/';

-- SELECT * FROM libros;
