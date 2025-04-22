from confluent_kafka import Consumer
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'estoque',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['novo-pedido'])
print("📦 Serviço de Estoque ouvindo...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Erro:", msg.error())
    else:
        pedido = json.loads(msg.value())
        print(f"[Estoque] Reservando itens {pedido['itens']} do pedido #{pedido['id']}")