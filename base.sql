-- Tabla para grupos de edad
CREATE TABLE grupo_edad (
    id INT AUTO_INCREMENT PRIMARY KEY,
    grupoedad VARCHAR(20) NOT NULL UNIQUE
);

-- Tabla para tipos de productos
CREATE TABLE tipo_producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(200)
);

-- Tabla para géneros
CREATE TABLE genero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    genero VARCHAR(20) NOT NULL UNIQUE
);

-- Tabla para marcas
CREATE TABLE marca (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla para categorías de productos
CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(50) NOT NULL
);

-- Tabla para presentaciones de productos
CREATE TABLE presentacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    color VARCHAR(20) NOT NULL,
    talla VARCHAR(15) NOT NULL
);

-- Tabla para departamentos
CREATE TABLE departamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    departamento VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla para provincias
CREATE TABLE provincia (
    id INT AUTO_INCREMENT PRIMARY KEY,
    provincia VARCHAR(50) NOT NULL UNIQUE,
    id_departamento INT NOT NULL,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id)
);

-- Tabla para distritos
CREATE TABLE distrito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    distrito VARCHAR(50) NOT NULL UNIQUE,
    id_provincia INT NOT NULL,
    FOREIGN KEY (id_provincia) REFERENCES provincia(id)
);

-- Tabla para tipos de usuarios
CREATE TABLE tipo_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL UNIQUE
);

-- Tabla para usuarios
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numdocumento CHAR(8) NOT NULL UNIQUE,
    ape_paterno VARCHAR(200) NOT NULL,
    ape_materno VARCHAR(200) NOT NULL,
    nombres VARCHAR(200) NOT NULL,
    telefono CHAR(9) NOT NULL,
    correo VARCHAR(200) NOT NULL,
    usuario VARCHAR(20) NOT NULL,
    contraseña VARCHAR(20) NOT NULL,
    estado CHAR(1) NOT NULL,
    id_tipo_usuario INT NOT NULL,
    FOREIGN KEY (id_tipo_usuario) REFERENCES tipo_usuario(id)
);

-- Tabla para productos
CREATE TABLE producto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    precio DECIMAL(7, 2) NOT NULL,
    estado CHAR(1) NOT NULL,
    stock INT NOT NULL,
    descripcion VARCHAR(200),
    descuento DECIMAL(9, 2),
    id_tipo_producto INT NOT NULL,
    id_genero INT NOT NULL,
    id_marca INT NOT NULL,
    id_categoria INT NOT NULL,
    id_grupo_edad INT NOT NULL,
    id_presentacion INT NOT NULL,
    FOREIGN KEY (id_tipo_producto) REFERENCES tipo_producto(id),
    FOREIGN KEY (id_genero) REFERENCES genero(id),
    FOREIGN KEY (id_marca) REFERENCES marca(id),
    FOREIGN KEY (id_categoria) REFERENCES categoria(id),
    FOREIGN KEY (id_grupo_edad) REFERENCES grupo_edad(id),
    FOREIGN KEY (id_presentacion) REFERENCES presentacion(id)
);

-- Tabla para direcciones de envío
CREATE TABLE direccion_envio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(200) NOT NULL,
    direccion VARCHAR(200) NOT NULL,
    montoenvio DECIMAL(7, 2) NOT NULL,
    referencia VARCHAR(300),
    tipo_envio CHAR(1) NOT NULL,
    id_distrito INT NOT NULL,
    FOREIGN KEY (id_distrito) REFERENCES distrito(id)
);

-- Tabla para pedidos
CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_pedido DATE NOT NULL,
    hora_pedido TIME NOT NULL,
    estado CHAR(1) NOT NULL,
    id_usuario INT NOT NULL,
    id_envio INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuario(id),
    FOREIGN KEY (id_envio) REFERENCES direccion_envio(id)
);

-- Tabla para detalles de pedidos
CREATE TABLE detalle_pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha_pedido DATE NOT NULL,
    hora_pedido TIME NOT NULL,
    precio DECIMAL(9, 2) NOT NULL,
    cantidad INT NOT NULL,
    subtotal DECIMAL(9, 2) NOT NULL,
    id_producto INT NOT NULL,
    id_pedido INT NOT NULL,
    FOREIGN KEY (id_producto) REFERENCES producto(id),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id)
);

-- Tabla para comprobantes
CREATE TABLE comprobante (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    monto_envio DECIMAL(7, 2) NOT NULL,
    subtotal DECIMAL(7, 2) NOT NULL,
    igv DECIMAL(9, 2) NOT NULL,
    total DECIMAL(9, 2) NOT NULL,
    tipo_comprobante CHAR(1) NOT NULL,
    forma_pago CHAR(1) NOT NULL,
    id_pedido INT NOT NULL,
    FOREIGN KEY (id_pedido) REFERENCES pedido(id)
);
