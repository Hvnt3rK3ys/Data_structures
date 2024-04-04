from fastapi import FastAPI
from starlette.responses import RedirectResponse

from searcher import minning_datos, get_keyword

app = FastAPI()

@app.get("/")
async def root():
    """
    Esta función redirige la URL raíz a la URL de búsqueda.

    Returns:
        RedirectResponse: Una respuesta de redirección a la URL de búsqueda.
    """
    return RedirectResponse(url="/api/v1/search")

@app.get("/api/v1/search")
async def search_tutelas():
    """
    Esta función obtiene todas las tutelas y las devuelve en un diccionario.

    Returns:
        dict: Un diccionario con las tutelas como valor de la clave 'tutelas'.
    """
    tutelas = minning_datos()  # Obtener todas las tutelas
    return {"tutelas": tutelas}  # Devolver las tutelas en un diccionario

@app.get("/api/v1/search/{tipo_tutela}")
async def search_tutelas(tipo_tutela: str):
    """
    Esta función busca tutelas relacionadas con la palabra clave proporcionada en la ruta URL.

    Args:
        tipo_tutela (str): La palabra clave para buscar en las tutelas.

    Returns:
        dict: Un diccionario con la palabra clave y las tutelas relacionadas.
    """
    index_keyword = get_keyword()  # Obtener el índice de palabras clave
    if tipo_tutela in index_keyword:  # Si la palabra clave está en el índice
        return {"keyword": tipo_tutela, "tutelas": index_keyword[tipo_tutela]}  # Devolver las tutelas relacionadas
    else:  # Si la palabra clave no está en el índice
        return {"keyword": tipo_tutela, "tutelas": []}  # Devolver un diccionario vacío