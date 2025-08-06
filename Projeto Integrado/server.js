const express = require('express');
const mysql = require('mysql2');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const db = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: '@Lee.2110Ferreira',
  database: 'Estacionamento'
});

app.post('/pagar', (req, res) => {
  const { placa, tempo, valor, forma, tipo } = req.body;

  if (!placa || tempo == null || isNaN(tempo) || valor == null || !forma) {
    return res.status(400).json({ erro: 'Dados incompletos' });
  }

  const sql = `
    INSERT INTO pagamentos_estacionamento 
    (placa, tempo_minutos, valor_pago, forma_pagamento, tipo_cartao) 
    VALUES (?, ?, ?, ?, ?)
  `;

  db.query(sql, [placa, tempo, valor, forma, tipo], (err, results) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ erro: 'Erro ao inserir no banco' });
    }
    res.json({ sucesso: 'Pagamento registrado' });
  });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});
