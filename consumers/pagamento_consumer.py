from confluent_kafka import Consumer
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'pagamento',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['novo-pedido'])
print("🪙 Serviço de Pagamento ouvindo...")

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Erro:", msg.error())
    else:
        pedido = json.loads(msg.value())
        print(f"[Pagamento] Processando pagamento do pedido #{pedido['id']} no valor de R${pedido['valor']}")