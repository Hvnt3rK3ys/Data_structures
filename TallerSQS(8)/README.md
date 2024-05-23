# Uso de la API para hallar tutelas

Esta documentación describe cómo usar la API FastAPI para interactuar con un sistema de gestión de tutelas.

# API disponible en:
```markdown
http://146.190.154.215/api/v1/search
```



## Endpoints Disponibles

### 1. [GET] / (Root)

- **Descripción:** Este endpoint redirige la URL raíz a la URL de búsqueda.
- **Operación:** root__get
- **Respuesta Exitosa:**
  - Código: 200
  - Descripción: Respuesta exitosa
  - Formato: JSON

### 2. [GET] /api/v1/search (Search Tutelas)

- **Descripción:** Este endpoint obtiene todas las tutelas y las devuelve en un diccionario.
- **Operación:** search_tutelas_api_v1_search_get
- **Respuesta Exitosa:**
  - Código: 200
  - Descripción: Respuesta exitosa
  - Formato: JSON

### 3. [GET] /api/v1/search/{tipo_tutela} (Search Tutelas)

- **Descripción:** Este endpoint busca tutelas relacionadas con la palabra clave proporcionada en la ruta URL.
- **Operación:** search_tutelas_api_v1_search__tipo_tutela__get
- **Parámetros:**
  - `tipo_tutela` (str): La palabra clave para buscar en las tutelas.
- **Respuestas:**
  - Código: 200
    - Descripción: Respuesta exitosa
    - Formato: JSON
  - Código: 422
    - Descripción: Error de validación
    - Formato: JSON

## Modelos de Datos

### HTTPValidationError
- **Propiedades:**
  - `detail` (array): Detalles del error
- **Descripción:** Objeto que representa un error de validación HTTP.

### ValidationError
- **Propiedades:**
  - `loc` (array): Ubicación del error
  - `msg` (str): Mensaje de error
  - `type` (str): Tipo de error
- **Descripción:** Objeto que representa un error de validación.




