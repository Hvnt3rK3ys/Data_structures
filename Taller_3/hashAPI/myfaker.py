import random
import faker

# Generar datos de muestra utilizando Faker
fake = faker.Faker()

# Lista de palabras clave para usar en las tutelas
palabras_clave = ["violencia", "estafa", "alimentos", "salud", "pensión", "medicinas"]

def generar_tutela_es_ajustado(id):
    """
    Esta función genera una tutela simulada con un id, título, resumen y número de decreto.
    El resumen incluirá una de las palabras clave seleccionadas al azar de la lista 'palabras_clave'.

    Args:
        id (int): El id de la tutela.

    Returns:
        dict: Un diccionario que representa la tutela con las claves 'id', 'titulo', 'resumen' y 'decreto'.
    """
    # Seleccionar una palabra clave aleatoriamente para incluir en el resumen
    palabra_clave = random.choice(palabras_clave)

    # Generar dos partes del resumen
    parte1 = fake.sentence(nb_words=6, ext_word_list=None)  # Primera parte del resumen
    parte2 = fake.text(max_nb_chars=180)  # Segunda parte del resumen

    # Combinar las partes incluyendo la palabra clave una sola vez
    resumen = f"{parte1} {palabra_clave} {parte2}"  # Resumen final con la palabra clave

    # Crear y devolver la tutela como un diccionario
    return {
        "id": f"tutela{id}",  # El id de la tutela
        "titulo": fake.sentence(nb_words=6),  # Título de la tutela
        "resumen": resumen,  # Resumen de la tutela
        "decreto": str(random.randint(1000, 9999))  # Número de decreto aleatorio para la tutela
    }


