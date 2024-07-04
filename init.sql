-- Create the database
CREATE DATABASE inventario;

-- Use the created database
USE inventario;

-- Create the user and grant privileges
CREATE USER 'alfajor'@'%' IDENTIFIED BY 'alfajor';
GRANT ALL PRIVILEGES ON *.* TO 'alfajor'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

-- Creación de tablas

CREATE TABLE Datos (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    texto TEXT
);