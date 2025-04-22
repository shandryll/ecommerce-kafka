from confluent_kafka import Producer
import json
import uuid

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def enviar_pedido(cliente, valor, itens):
    pedido = {
        'id': str(uuid.uuid4()),
        'cliente': cliente,
        'valor': valor,
        'itens': itens
    }

    def callback(err, msg):
        if err:
            print("❌ Erro ao enviar:", err)
        else:
            print(f"✅ Pedido enviado com sucesso para {msg.topic()} - ID: {pedido['id']}")

    producer.produce('novo-pedido', value=json.dumps(pedido), callback=callback)
    producer.flush()

print("=== CLI - Simulador de Pedidos Kafka ===")
while True:
    cliente = input("Nome do cliente (ou 'sair'): ")
    if cliente.lower() == 'sair':
        break

    try:
        valor = float(input("Valor do pedido: "))
    except ValueError:
        print("❌ Valor inválido.")
        continue

    itens = input("Itens (separados por vírgula): ").split(',')
    itens = [item.strip() for item in itens if item.strip()]

    if not itens:
        print("❌ Nenhum item informado.")
        continue

    enviar_pedido(cliente, valor, itens)