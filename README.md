# Sweet Heart Backend API

Este es el backend de una aplicación para la gestión de productos y órdenes, diseñado para una pastelería. Proporciona endpoints RESTful para manejar productos y órdenes, permitiendo su creación, consulta, actualización y eliminación.

## Características
- Gestión de productos con información detallada como nombre, descripción, precio, stock y porciones.
- Gestión de órdenes con datos del cliente, productos incluidos y cálculo del precio total.

## Tecnologías
- **Framework**: Django + Django REST Framework (DRF)
- **Base de Datos**: POSTGRES
- **Documentación**: Swagger y ReDoc integrados

## Endpoints

### Productos
- **GET**    `/api/v1/products/`         - Lista de productos
- **POST**   `/api/v1/products/`         - Crear un producto
- **GET**    `/api/v1/products/{id}/`    - Detalles de un producto
- **PUT**    `/api/v1/products/{id}/`    - Actualizar un producto
- **DELETE** `/api/v1/products/{id}/`    - Eliminar un producto

### Órdenes
- **GET**    `/api/v1/orders/`           - Lista de órdenes
- **POST**   `/api/v1/orders/`           - Crear una orden
- **GET**    `/api/v1/orders/{id}/`      - Detalles de una orden
- **PUT**    `/api/v1/orders/{id}/`      - Actualizar una orden
- **DELETE** `/api/v1/orders/{id}/`      - Eliminar una orden

## Documentación API
Puedes acceder a la documentación interactiva de la API en las siguientes rutas:
- **Swagger UI**: `/docs/`
- **ReDoc**: `/redoc/`

## Cómo Ejecutar

1. Clona este repositorio:
   ```bash
   git clone <repo_url>
   cd sweetheart_backend

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt

3. Realiza las migraciones:
    ```bash
    python manage.py migrate

4. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver

5. Accede a la API en: http://127.0.0.1:8000/api/v1/