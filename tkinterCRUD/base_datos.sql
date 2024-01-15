-- Crear la base de datos si no existe y seleccionarla
CREATE DATABASE IF NOT EXISTS base_datos;
\c base_datos;

-- Crear la tabla 'productos' con las columnas respectivas
CREATE TABLE IF NOT EXISTS productos (
  ID serial PRIMARY KEY,
  CODIGO char(10) NOT NULL DEFAULT '0',
  NOMBRE char(20) NOT NULL DEFAULT '0',
  MODELO char(20) NOT NULL DEFAULT '0',
  PRECIO char(50) NOT NULL DEFAULT '0',
  CANTIDAD char(50) NOT NULL DEFAULT '0'
);

-- Insertar datos en la tabla 'productos'
TRUNCATE TABLE productos;
INSERT INTO productos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD) VALUES
  ('RES001', 'RESISTENCIA', 'RV', '2.00', '222'),
  ('TRAS-11', 'TRANSISTOR', 'PNP', '1.00', '554'),
  ('10101', 'CONDENSADOR', 'CERAMICO', '2.00', '100'),
  ('DB121', 'DIODO', 'ZENER', '1.50', '231'),
  ('IC002', 'IC', 'AND', '1.00', '200'),
  ('IC003', 'IC', 'XOR', '1.00', '300'),
  ('D0092', 'DIOD0', 'ZENER', '2.00', '232'),
  ('RE21', 'RELE', '221R', '2.50', '423'),
  ('2560', 'ARDUINO', 'MEGA', '30.0', '37'),
  ('2021DS', 'ARDUINO', 'UNO R3', '15.50', '73'),
  ('RES2021', 'RESISTENCIA', '4B', '0.10', '1000'),
  ('LED122', 'LED', 'GREENR3', '0.50', '144'),
  ('LDR43', 'LDR', 'LDRG', '2.00', '43'),
  ('FUSI232', 'FUSIBLE', '23FDEW', '2.00', '331'),
  ('MATRIZ32', 'MATRIZ', '32X8', '50.0', '56'),
  ('SENSORRE', 'ULTRASONIC', 'RGR0544', '5.00', '231'),
  ('555N', 'TIMER', '555', '1.50', '621'),
  ('ER43', 'PILAS', 'AAA', '2.00', '544'),
  ('1212', '12121', '12121', '22121', '12121');

