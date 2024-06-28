-- Active: 1710419443849@@127.0.0.1@3306@emprendimiento
-- Creamos la base de datos

USE emprendimiento;

-- Creamos las tablas 
CREATE TABLE Tipo_Usuario (
    Usuario ENUM('Admin','estandar')DEFAULT 'estandar',
    idTipo_Usuario INT PRIMARY KEY
);



CREATE TABLE Administrador (
    codigo_Administrador INT PRIMARY KEY,
    nombre VARCHAR(45),
    apellidos VARCHAR(45),
    telefono VARCHAR(45),
    email VARCHAR(45),
    clave VARCHAR(60),
    Tipo_Usuario_idTipo_Usuario INT,
    FOREIGN KEY (Tipo_Usuario_idTipo_Usuario) REFERENCES Tipo_Usuario(idTipo_Usuario)
);

CREATE TABLE clientes (
    idclientes INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(45),
    apellidos VARCHAR(45),
    telefono VARCHAR(45),
    correo VARCHAR(50),
    clave VARCHAR(10),
    Tipo_Usuario_idTipo_Usuario INT,
    FOREIGN KEY (Tipo_Usuario_idTipo_Usuario) REFERENCES Tipo_Usuario(idTipo_Usuario)
); 

CREATE TABLE producto (
    id_productos INT PRIMARY KEY,
    codigo_productos VARCHAR(45),
    nombre_producto VARCHAR(100),
    precio DECIMAL(10,2),
    descripcion TEXT(100)
    imagen BLOB,
);

ALTER TABLE producto
ADD CONSTRAINT imagen_formato_check
CHECK (
   SUBSTRING(imagen, 1, 4) = 0x89504E47 /* PNG */
   OR SUBSTRING(imagen, 1, 3) IN (0xFFD8FF, 0xFFD8FFE0, 0xFFD8FFE1) /* JPG */
);



CREATE TABLE Reporte (
    id_Reporte INT AUTO_INCREMENT PRIMARY KEY,
    descripcion TEXT(150),
    fecha_reporte DATE,
    clientes_idclientes INT,
    Administrador_codigo_Administrador INT,
    FOREIGN KEY (clientes_idclientes) REFERENCES clientes(idclientes),
    FOREIGN KEY (Administrador_codigo_Administrador) REFERENCES Administrador(codigo_Administrador)
);

