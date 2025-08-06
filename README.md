# Ferreira's Park Shopping - Sistema de Pagamento de Estacionamento

Projeto desenvolvido durante as férias, por iniciativa própria, para praticar e aprofundar conhecimentos em desenvolvimento web e integração com banco de dados. Simula um sistema de pagamento de estacionamento, com front-end em HTML/CSS/JavaScript e back-ends em Node.js.

---

## 📁 Estrutura do Projeto

- `/frontend` – Código do front-end com HTML, CSS e JavaScript.  
- `/backend-node` – Servidor Node.js para receber dados e salvar no banco MySQL.

--
- `/backend-python` – Projeto separado em Python para lógica de pagamento, sem integração com o front-end ou banco de dados.
> Comecei desenvolvendo em python e depois reescrevi o projeto para rodar um página web.

---

## ⚠️ Observação

Para garantir o funcionamento correto da comunicação entre front-end e back-end (via `fetch`), recomenda-se rodar o front-end em um servidor local, como a extensão **Live Server** no VS Code, evitando problemas com bloqueios de requisições no navegador.

---

## 🧶 Instalação

Os pacotes e a pasta `node_modules` **não estão incluídos no repositório**, pois são gerados automaticamente ao instalar as dependências do projeto Node.js.

Para rodar o servidor Node.js, siga os passos abaixo no terminal:

```bash
cd backend-node
npm init -y
npm install express mysql2 cors
node server.js
