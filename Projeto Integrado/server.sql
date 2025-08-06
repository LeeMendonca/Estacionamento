CREATE DATABASE Estacionamento;

USE Estacionamento;

CREATE TABLE pagamentos_estacionamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(7) NOT NULL,
    tempo_minutos INT NOT NULL,
    valor_pago DECIMAL(6,2) NOT NULL,
    forma_pagamento ENUM('dinheiro', 'cartao') NOT NULL,
    tipo_cartao ENUM('credito', 'debito') DEFAULT NULL,
    data_pagamento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM pagamentos_estacionamento;