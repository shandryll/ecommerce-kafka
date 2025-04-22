from confluent_kafka import Consumer
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'nota_fiscal',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['novo-pedido'])
print("🧾 Serviço de Nota Fiscal ouvindo...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Erro:", msg.error())
    else:
        pedido = json.loads(msg.value())
        print(f"[Nota Fiscal] Gerando NF para o pedido #{pedido['id']} do cliente {pedido['cliente']}")