# 📦 Projeto: Sistema de Pedidos com Apache Kafka

Este projeto simula um sistema de e-commerce distribuído usando Apache Kafka como intermediador de mensagens entre diferentes serviços.

## 📸 Visão Geral do Fluxo

![Fluxo de Kafka](assets\fluxo_ecommerce-kafka.png)

## 📂 Estrutura do Projeto

```
ecommerce-kafka/
├── cli_producer.py
├── requirements.txt
├── requirements.txt
├── assets/
│   └── fluxo_ecommerce-kafka.png
├── producers/
│   └── pedido_producer.py
└── consumers/
    ├── pagamento_consumer.py
    ├── estoque_consumer.py
    └── nota_fiscal_consumer.py
```

## 🚀 Como Executar

```bash
docker-compose up -d
python -m venv venv
source venv/bin/activate  # no Windows: venv\Scripts\activate
pip install -r requirements.txt

# Em três terminais separados
python consumers/pagamento_consumer.py
python consumers/estoque_consumer.py
python consumers/nota_fiscal_consumer.py

# Em outro terminal
python producers/pedido_producer.py
```