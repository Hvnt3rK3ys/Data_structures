from random import randint  # Se utiliza en la funcion QueueSQS
from fastapi import FastAPI, Query  # Se utiliza en la instanciacion de la aplicacion FastAPI
import multiprocessing  # Se utiliza en el endpoint desencolar
import boto3  # Se utiliza en la autenticacion con AWS y conexion con SQS
import uuid  # Se utiliza en la funcion QueueSQS
import uvicorn
from dotenv import load_dotenv
import os


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
'''
Seccion de autenticacion con AWS y conexion con SQS

aws_access_key_idSec = input("Por favor, ingrese su AWS Access Key ID: ")
aws_secret_access_keySec = input("Por favor, ingrese su AWS Secret Access Key: ")
queue_urlSec = input("Por favor, ingrese su AWS SQS Queue URL: ")
region_zoneSec = input("Por favor, ingrese su AWS Region: ")
'''

# Carga las variables de entorno del archivo .env
load_dotenv()

aws_access_key_idSec = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_keySec = os.getenv("AWS_SECRET_ACCESS_KEY")
queue_urlSec = os.getenv("AWS_SQS_QUEUE_URL")
region_zoneSec = os.getenv("AWS_REGION")


# Crear un cliente de AWS SQS
sqs = boto3.client(
    'sqs',
    region_name=region_zoneSec,
    aws_access_key_id=aws_access_key_idSec,
    aws_secret_access_key=aws_secret_access_keySec
)

'''
Funcion para extraer la totalidad de mensajes en la cola SQS
'''


def get_SQS_length():
    response = sqs.get_queue_attributes(
        QueueUrl=queue_urlSec,
        AttributeNames=['ApproximateNumberOfMessages']
    )
    return int(response['Attributes'].get('ApproximateNumberOfMessages', 0))


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
'''
Funcion para encolar mensajes en la cola SQS
'''


def QueueSQS(cantidad_mensajes: int):
    consumirCola = list()
    # Publicar un mensaje en la cola
    for i in range(0, cantidad_mensajes):
        response = sqs.send_message(
            QueueUrl=queue_urlSec,
            MessageBody=f'{randint(0, cantidad_mensajes)}',  # Expected 1m maximum free tier
            MessageGroupId='pagos',
            MessageDeduplicationId=str(uuid.uuid4())
        )
        consumirCola.append(response["MessageId"])
        print(f"Mensaje enviado: {response['MessageId']}")
    return consumirCola


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

'''
Funcion para desencolar mensajes de la cola SQS
'''


def DequeueSQS():
    # Recibir mensajes de la cola
    response = sqs.receive_message(
        QueueUrl=queue_urlSec,
        AttributeNames=[
            'All'
        ],
        MessageAttributeNames=[
            'All'
        ],
        MaxNumberOfMessages=1,
        VisibilityTimeout=30,
        WaitTimeSeconds=0
    )
    # print(response)
    if response.get('Messages'):
        message = response['Messages']
        print(f"Mensaje recibido: {message[0]['Body']}")
        sqs.delete_message(
            QueueUrl=queue_urlSec,
            ReceiptHandle=message[0]['ReceiptHandle']
        )
        return message[0]['Body']
    else:
        print("No se encontraron mensajes en la cola.")
    sqs.close()


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

'''
Función para generar el árbol binario con los datos recibidos de la cola

Clase TreeNode:
    Esta clase representa un nodo en un árbol binario.
    Atributos:
        value: El valor almacenado en el nodo.
        left (TreeNode): El hijo izquierdo del nodo.
        right (TreeNode): El hijo derecho del nodo.


Función create_binary_tree(linearConsumer: list):
    Crea un árbol binario a partir de una lista de valores.
    La función toma una lista de valores y crea un árbol binario completo de izquierda a derecha.
    Args:
        linearConsumer (list): La lista de valores para crear el árbol.
    Returns:
        TreeNode: La raíz del árbol binario creado.

Función tree_to_dict(node):
    Convierte un árbol binario en un diccionario.
    La función toma un nodo (que representa un árbol binario) y lo convierte en un diccionario. 
    Cada nodo se convierte en una clave en el diccionario, y los hijos izquierdo y derecho del nodo se convierten en sub-diccionarios.
    Args:
        node (TreeNode): El nodo raíz del árbol binario.
    Returns:
        dict: El diccionario que representa el árbol binario.

'''


class TreeNode:
    def __init__(self, value):
        self.value = value  # Crea un nodo con un valor
        self.left = None  # Inicializa el hijo izquierdo como None
        self.right = None  # Inicializa el hijo derecho como None


def create_binary_tree(linearConsumer: list):
    if not linearConsumer:  # Si la lista está vacía, devuelve None
        return None
    root = TreeNode(linearConsumer[0])  # Crea la raíz con el primer elemento
    queue = [root]  # Inicializa la cola con la raíz
    index = 1  # Índice para recorrer los elementos de la lista

    while index < len(linearConsumer):
        node = queue.pop(0)  # Saca el primer nodo de la cola
        if index < len(linearConsumer):
            node.left = TreeNode(linearConsumer[index])  # Crea el hijo izquierdo
            queue.append(node.left)  # Agrega el hijo izquierdo a la cola
            index += 1
        if index < len(linearConsumer):
            node.right = TreeNode(linearConsumer[index])  # Crea el hijo derecho
            queue.append(node.right)  # Agrega el hijo derecho a la cola
            index += 1

    return root  # Devuelve la raíz del árbol


def tree_to_dict(node):
    if not node:  # Si no hay nodo, devuelve None
        return None
    return {  # Crea un diccionario con la información del nodo
        'value': node.value,  # Valor del nodo
        'left': tree_to_dict(node.left),  # Recursivamente crea el hijo izquierdo
        'right': tree_to_dict(node.right)  # Recursivamente crea el hijo derecho
    }


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

'''
Instanciacion de la aplicacion FastAPI
'''
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the SQS api"}


@app.get("/check_credentials")
def check_credentials():
    try:
        # Intentar obtener los atributos de la cola
        response = sqs.get_queue_attributes(
            QueueUrl=queue_urlSec,
            AttributeNames=['All']
        )
        # Si la operación es exitosa, imprimir un mensaje y devolver un estado exitoso
        print("Las credenciales de AWS son correctas.")
        return {"status": "Las credenciales de AWS son correctas."}
    except Exception as e:
        # Si la operación falla, imprimir un mensaje y devolver un estado de error
        print(f"Las credenciales de AWS son incorrectas. Error: {e}")
        return {"status": f"Las credenciales de AWS son incorrectas. Error: {e}"}

# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

'''
Endpoint para enviar mensajes a SQS
'''


def process_batch(batch_size: int):
    return QueueSQS(batch_size)


@app.get("/encolar")
async def encolar(cantidad_mensajes: int = Query(..., description="Cantidad de mensajes a enviar")):
    # Obtener el número de workers máximos según el número de CPU cores
    max_workers = multiprocessing.cpu_count()
    # Número total de mensajes a enviar
    total_messages = cantidad_mensajes
    # Crear una lista de tamaños de lotes a procesar
    batch_sizes = [min(max_workers, total_messages - i) for i in range(0, total_messages, max_workers)]
    # Crear un pool de workers
    with multiprocessing.Pool(max_workers) as pool:
        # Procesar los mensajes en paralelo
        results = pool.map(process_batch, batch_sizes)
    # Aplanar la lista de resultados
    linear_consumer = [msg_id for batch in results for msg_id in batch]
    # Devolver la respuesta con la lista de consumidores y la cantidad de mensajes
    return {
        "queue_messages": linear_consumer,
        "queue_quantity": len(linear_consumer)
    }


# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


'''
Endpoint para recibir mensajes de SQS
'''


# Resolver llamado dinamico a SQS para preguntar la longitud maxima de la cola
@app.get("/desencolar")
async def desencolar(cantidad_mensajes: int = Query(..., description="Cantidad de mensajes a consumir (0 para todos)")):
    # Obtener el número de workers máximos según el número de CPU cores
    max_workers = multiprocessing.cpu_count()
    # Obtener la longitud de la cola de SQS
    maxlength = get_SQS_length()
    # Si la longitud de la cola es cero, detener el proceso y devolver un mensaje
    if maxlength == 0:
        return {"message": "La longitud de la cola es nula"}
    # Si el usuario selecciona 0, desencolar todos los mensajes disponibles
    if cantidad_mensajes == 0:
        cantidad_mensajes = maxlength
    else:
        cantidad_mensajes = min(cantidad_mensajes, maxlength)
    # Crear una lista de consumidores lineales
    linearConsumer = []
    # Procesar los mensajes por lotes
    batch_size = min(cantidad_mensajes, max_workers)
    total_dequeued = 0
    while total_dequeued < cantidad_mensajes:
        batch = []
        for _ in range(min(batch_size, cantidad_mensajes - total_dequeued)):
            message = DequeueSQS()
            if message:
                batch.append(message)
        if not batch:
            break  # Si no se obtienen mensajes, salir del bucle
        # Agregar el lote de mensajes a la lista de consumidores lineales
        linearConsumer.extend(batch)
        total_dequeued += len(batch)
    # Crear un árbol binario a partir de la lista de consumidores lineales
    binary_tree_root = create_binary_tree(linearConsumer)
    # Convertir el árbol binario a un diccionario
    binary_tree_dict = tree_to_dict(binary_tree_root)
    # Devolver la respuesta con la lista de consumidores, la cantidad de mensajes y el árbol binario
    return {
        "dequeue_messages": linearConsumer,
        "dequeue_quantity": len(linearConsumer),
        "generated_tree 🌲": binary_tree_dict
    }




# ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


# Punto de entrada para iniciar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
