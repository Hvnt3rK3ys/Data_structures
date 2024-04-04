from myfaker import generar_tutela_es_ajustado
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')

def crear_datos_muestra():
    """
    Esta función genera 100 tutelas simuladas utilizando la función 'generar_tutela_es_ajustado'.

    Returns:
        list: Una lista de 100 tutelas simuladas.
    """
    # Generar 100 muestras de tutelas con los ajustes especificados
    listado_tutelas_es_ajustado = [generar_tutela_es_ajustado(i) for i in range(1, 101)]
    return listado_tutelas_es_ajustado

def preprocess_text(text):
    """
    Esta función procesa el texto eliminando la puntuación y las palabras de parada (stopwords).

    Args:
        text (str): El texto a procesar.

    Returns:
        str: El texto procesado.
    """
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar puntuación
    text = re.sub(r'[^\w\s]', '', text)
    # Combinar stopwords de ambos idiomas
    stop_words_es = set(stopwords.words('spanish'))
    stop_words_en = set(stopwords.words('english'))
    stop_words = stop_words_es.union(stop_words_en)
    # Eliminar stopwords
    words = text.split()
    filtered_text = [word for word in words if word not in stop_words]
    return ' '.join(filtered_text)

def minning_datos():
    """
    Esta función genera los datos de muestra y procesa el resumen de cada tutela.

    Returns:
        list: Una lista de tutelas con el resumen procesado.
    """
    tutelas = crear_datos_muestra()
    for tutela in tutelas:
        tutela['resumen'] = preprocess_text(tutela['resumen'])
    return tutelas

def get_index_tutelas():
    """
    Esta función indexa las tutelas por decreto.

    Returns:
        dict: Un diccionario donde las claves son los decretos y los valores son las tutelas correspondientes.
    """
    tutelas = minning_datos()
    index_tutelas = {}
    for tutela in tutelas:
        if tutela['decreto'] in index_tutelas:
            index_tutelas[tutela['decreto']].append(tutela)
        else:
            index_tutelas[tutela['decreto']] = [tutela]
    return index_tutelas

def get_keyword():
    """
    Esta función indexa las tutelas por palabra clave.

    Returns:
        dict: Un diccionario donde las claves son las palabras clave y los valores son las tutelas correspondientes.
    """
    tutelas = minning_datos()
    index_keyword = {} # Creación del hash table
    for tutela in tutelas:
        words = tutela['resumen'].split()
        for word in words:
            if word in index_keyword:
                index_keyword[word].append(tutela)  # Agregar tutela a la lista de una clave existente
            else:
                index_keyword[word] = [tutela] # Crear una nueva clave con la tutela como valor
    return index_keyword