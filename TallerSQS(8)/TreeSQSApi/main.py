from random import randint # Se utiliza en la funcion QueueSQS
from fastapi import FastAPI # Se utiliza en la instanciacion de la aplicacion FastAPI
import multiprocessing # Se utiliza en el endpoint desencolar
import boto3 # Se utiliza en la autenticacion con AWS y conexion con SQS
import uuid # Se utiliza en la funcion QueueSQS

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
'''
Seccion de autenticacion con AWS y conexion con SQS
'''

aws_access_key_idSec = input("Por favor, ingrese su AWS Access Key ID: ")
aws_secret_access_keySec = input("Por favor, ingrese su AWS Secret Access Key: ")
queue_urlSec = input("Por favor, ingrese su AWS SQS Queue URL: ")
region_zoneSec = input("Por favor, ingrese su AWS Region: ")


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




#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
'''
Funcion para encolar mensajes en la cola SQS
'''

def QueueSQS(cantidad_mensajes:int):
    consumirCola = list()
    # Publicar un mensaje en la cola
    for i in range(0, cantidad_mensajes):
        response = sqs.send_message(
            QueueUrl=queue_urlSec,
            MessageBody= f'{randint(0, cantidad_mensajes)}', #Expected 1m maximum free tier
            MessageGroupId='pagos',
            MessageDeduplicationId=str(uuid.uuid4())
        )
        consumirCola.append(response["MessageId"])
    return consumirCola


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

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
    #print(response)
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


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

'''
Función para generar el árbol binario con los datos recibidos de la cola

Clase TreeNode:
    Esta clase representa un nodo en un árbol binario. Cada nodo tiene un valor y dos hijos: izquierdo y derecho.

Función insert_in_binary_tree(root, value):
    Esta función inserta un nuevo valor en el árbol binario. La inserción se realiza en el nivel más bajo posible y hacia la izquierda. 
    Si la raíz es None, se crea un nuevo TreeNode con el valor proporcionado. 
    Si la raíz no es None, se utiliza una cola para recorrer el árbol y encontrar el lugar adecuado para la inserción.

Función create_binary_tree(linearConsumer: list):
    Esta función crea un árbol binario a partir de una lista de valores (linearConsumer). 
    El primer elemento de la lista se convierte en la raíz del árbol, y los elementos restantes se insertan en el árbol en el orden en que aparecen en la lista.

Función tree_to_dict(node):
    Esta función convierte un árbol binario en un diccionario para facilitar su visualización y manipulación. 
    Cada nodo del árbol se convierte en una clave en el diccionario, y los hijos izquierdo y derecho del nodo se convierten en sub-diccionarios.
'''

class TreeNode:
    def __init__(self, value):
        self.value = value  # Crea un nodo con un valor
        self.left = None  # Inicializa el hijo izquierdo como None
        self.right = None  # Inicializa el hijo derecho como None

def insert_in_binary_tree(root, value):
    if root is None:  # Si no hay raíz, crea un nuevo nodo con el valor
        return TreeNode(value)
    queue = [root]  # Crea una cola con la raíz
    while queue:  # Mientras haya nodos en la cola
        node = queue.pop(0)  # Saca el primer nodo de la cola
        if not node.left:  # Si no hay hijo izquierdo, crea uno con el valor
            node.left = TreeNode(value)
            return
        else:
            queue.append(node.left)  # Agrega el hijo izquierdo a la cola
        if not node.right:  # Si no hay hijo derecho, crea uno con el valor
            node.right = TreeNode(value)
            return
        else:
            queue.append(node.right)  # Agrega el hijo derecho a la cola

def create_binary_tree(linearConsumer: list):
    if not linearConsumer:  # Si la lista está vacía, devuelve None
        return None
    root = TreeNode(linearConsumer[0])  # Crea la raíz con el primer elemento
    for value in linearConsumer[1:]:  # Itera sobre el resto de la lista
        insert_in_binary_tree(root, value)  # Inserta cada valor en el árbol
    return root  # Devuelve la raíz del árbol

def tree_to_dict(node):
    if not node:  # Si no hay nodo, devuelve None
        return None
    return {  # Crea un diccionario con la información del nodo
        'value': node.value,  # Valor del nodo
        'left': tree_to_dict(node.left),  # Recursivamente crea el hijo izquierdo
        'right': tree_to_dict(node.right)  # Recursivamente crea el hijo derecho
    }

#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

'''
Instanciacion de la aplicacion FastAPI
'''
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the SQS api"}

'''
Endpoint para enviar mensajes a SQS
'''
@app.post("/encolar")
async def encolar(cantidad_enviada: dict):
    consumo = QueueSQS(cantidad_enviada["cantidad_mensajes"])
    return {
        "queue_messages": consumo,
        "queue_quantity": len(consumo)
    }

'''
Endpoint para recibir mensajes de SQS
'''

# Resolver llamado dinamico a SQS para preguntar la longitud maxima de la cola
@app.get("/desencolar")
async def desencolar(cantidad_enviada: dict):
    # Obtener el número de workers máximos según el número de CPU cores
    max_workers = multiprocessing.cpu_count()
    # Obtener la longitud de la cola de SQS
    maxlength = get_SQS_length()
    # Crear una lista de consumidores lineales
    linearConsumer = []
    # Procesar los mensajes por lotes
    batch_size = min(maxlength, max_workers)
    for _ in range(0, maxlength, batch_size):
        batch = []
        for _ in range(batch_size):
            batch.append(DequeueSQS())
        # Agregar el lote de mensajes a la lista de consumidores lineales
        linearConsumer.extend(batch)
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


#⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘


# Punto de entrada para iniciar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)