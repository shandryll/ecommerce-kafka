from confluent_kafka import Producer
import json

producer = Producer({'bootstrap.servers': 'localhost:9092'})

pedido = {
    'id': '12345',
    'cliente': 'João Silva',
    'valor': 199.99,
    'itens': ['camiseta', 'boné']
}

def callback(err, msg):
    if err:
        print("Erro ao enviar:", err)
    else:
        print(f"Pedido enviado com sucesso para {msg.topic()}")

producer.produce('novo-pedido', value=json.dumps(pedido), callback=callback)
producer.flush()