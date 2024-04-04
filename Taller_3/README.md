# Uso de la API para hallar tutelas

Esta documentación describe cómo usar la API FastAPI para interactuar con un sistema de gestión de tutelas.

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



```
{
  "openapi": "3.1.0",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/": {
      "get": {
        "summary": "Root",
        "description": "Esta función redirige la URL raíz a la URL de búsqueda.\n\nReturns:\n    RedirectResponse: Una respuesta de redirección a la URL de búsqueda.",
        "operationId": "root__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/api/v1/search": {
      "get": {
        "summary": "Search Tutelas",
        "description": "Esta función obtiene todas las tutelas y las devuelve en un diccionario.\n\nReturns:\n    dict: Un diccionario con las tutelas como valor de la clave 'tutelas'.",
        "operationId": "search_tutelas_api_v1_search_get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    },
    "/api/v1/search/{tipo_tutela}": {
      "get": {
        "summary": "Search Tutelas",
        "description": "Esta función busca tutelas relacionadas con la palabra clave proporcionada en la ruta URL.\n\nArgs:\n    tipo_tutela (str): La palabra clave para buscar en las tutelas.\n\nReturns:\n    dict: Un diccionario con la palabra clave y las tutelas relacionadas.",
        "operationId": "search_tutelas_api_v1_search__tipo_tutela__get",
        "parameters": [
          {
            "name": "tipo_tutela",
            "in": "path",
            "required": true,
            "schema": {
              "type": "string",
              "title": "Tipo Tutela"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          },
          "422": {
            "description": "Validation Error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/HTTPValidationError"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "HTTPValidationError": {
        "properties": {
          "detail": {
            "items": {
              "$ref": "#/components/schemas/ValidationError"
            },
            "type": "array",
            "title": "Detail"
          }
        },
        "type": "object",
        "title": "HTTPValidationError"
      },
      "ValidationError": {
        "properties": {
          "loc": {
            "items": {
              "anyOf": [
                {
                  "type": "string"
                },
                {
                  "type": "integer"
                }
              ]
            },
            "type": "array",
            "title": "Location"
          },
          "msg": {
            "type": "string",
            "title": "Message"
          },
          "type": {
            "type": "string",
            "title": "Error Type"
          }
        },
        "type": "object",
        "required": [
          "loc",
          "msg",
          "type"
        ],
        "title": "ValidationError"
      }
    }
  }
}
```
