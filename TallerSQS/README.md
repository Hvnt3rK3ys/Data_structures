# Uso de la API SQS, bank service

Esta documentación describe cómo usar la API FastAPI para interactuar con un sistema de gestión de colas.

# Endpoint para enviar mensajes:
```markdown
ipDirection/8000/encolar?cantidad_mensajes=[coloque la cantidad de mensajes como entero]
```

# Endpoint para consumir mensajes:
```markdown
ipDirection/8000/desencolar?cantidad_mensajes=[coloque la cantidad de mensajes como entero]
```

## API Demo
[![API usage example](https://img.youtube.com/vi/ID_DEL_VIDEO/0.jpg)](https://www.youtube.com/watch?v=ID_DEL_VIDEO)


# API Documentation

## Overview
This API allows you to enqueue and dequeue messages. The main endpoints are:
- `/`: Root endpoint
- `/encolar`: Enqueue messages
- `/desencolar`: Dequeue messages

## Endpoints

### Root Endpoint

#### `GET /`
**Summary:** Read Root

**Responses:**
- `200`: Successful Response
  - Content: `application/json`

### Enqueue Messages

#### `GET /encolar`
**Summary:** Enqueue messages

**Parameters:**
- `cantidad_mensajes` (query, integer, required): The number of messages to send.
  - Description: The number of messages to send

**Responses:**
- `200`: Successful Response
  - Content: `application/json`
- `422`: Validation Error
  - Content: `application/json`
  - Schema: `HTTPValidationError`

### Dequeue Messages

#### `GET /desencolar`
**Summary:** Dequeue messages

**Parameters:**
- `cantidad_mensajes` (query, integer, required): The number of messages to consume (0 for all).
  - Description: The number of messages to consume (0 for all)

**Responses:**
- `200`: Successful Response
  - Content: `application/json`
- `422`: Validation Error
  - Content: `application/json`
  - Schema: `HTTPValidationError`

## Components

### Schemas

#### HTTPValidationError
- **Properties:**
  - `detail` (array of `ValidationError`): Detail
- **Type:** object
- **Title:** HTTPValidationError

#### ValidationError
- **Properties:**
  - `loc` (array of `string` or `integer`): Location
  - `msg` (string): Message
  - `type` (string): Error Type
- **Type:** object
- **Required:**
  - `loc`
  - `msg`
  - `type`
- **Title:** ValidationError

## Usage Examples

### Enqueue Messages

**Request:**
```
GET /encolar?cantidad_mensajes=20
```

**Response:**
```json
{
  "queue_messages": [
    "1450d28c-5736-4c31-a57c-f9232b62d2a5",
    "7134d548-60bc-48ca-9f4c-cb60e4e0de9a",
    ...
  ],
  "queue_quantity": 20
}
```

### Dequeue Messages

**Request:**
```
GET /desencolar?cantidad_mensajes=10
```

**Response:**
```json
{
  "dequeue_messages": [
    "8092a7cd-ec18-4180-b402-0f7e317153e0",
    "f540a0a2-6a03-4875-82b8-535d2c17ad40",
    ...
  ],
  "dequeue_quantity": 10,
  "generated_tree 🌲": {
    "value": "8092a7cd-ec18-4180-b402-0f7e317153e0",
    "left": {
      ...
    },
    "right": {
      ...
    }
  }
}
```

**Request for all messages:**
```
GET /desencolar?cantidad_mensajes=0
```

**Response:**
```json
{
  "dequeue_messages": [
    "8092a7cd-ec18-4180-b402-0f7e317153e0",
    "f540a0a2-6a03-4875-82b8-535d2c17ad40",
    ...
  ],
  "dequeue_quantity": 50,
  "generated_tree 🌲": {
    "value": "8092a7cd-ec18-4180-b402-0f7e317153e0",
    "left": {
      ...
    },
    "right": {
      ...
    }
  }
}
```

## Error Responses

### Validation Error (`422`)

**Response:**
```json
{
  "detail": [
    {
      "loc": ["query", "cantidad_mensajes"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

This documentation provides an overview of the API endpoints, their parameters, responses, and examples of usage.
