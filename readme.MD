
# django-chat

These APIs include all the functionality related to chat functionality and WebSocket connections. 

## Features

- Supports real-time chat communication using WebSocket.
- To use the chat functionality, you need to register at least two users. You can do this via the Django Admin panel.

## Project Structure

```
django-chat/
├── authentication/
│   ├── admin.py
│   ├── apps.py
│   ├── backends.py
│   ├── __init__.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── chat/
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── connect/
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── django_chat/
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── nginx.conf
├── readme.MD
└── requirements.txt
```

### Key Files

- **`settings.py`**: Configuration for Django, DRF, and Channels.
- **`asgi.py`**: ASGI application used for running Django Channels.
- **`urls.py`**: Defines the routing configuration, including WebSocket routes, in the `chat` app.
- **`views.py`**: Contains the `ChatConsumer` that handles WebSocket connections and real-time communication in the `chat` app.
- **`docker-compose.yml`**: Docker Compose file for defining and running multi-container Docker applications.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/django-chat.git
   cd django-chat
   ```

2. **Build and start the Docker containers:**

   ```bash
   docker-compose up --build
   ```

3. **Apply the migrations:**

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Access the application:**

   - **Django REST Framework API**: Visit `http://127.0.0.1:8000/api/` to interact with the DRF-powered API.
   - **WebSocket Connections**: Connect to the WebSocket endpoint at `ws://127.0.0.1:9004/ws/chat/`.

## Environment Variables Setup

### Default Command

Set up the `DEFAULT_COMMAND` to specify how the project should run:

- **Development Mode**: 

   ```bash
   export DEFAULT_COMMAND="python3 manage.py runserver 0.0.0.0:9004"
   ```

- **Production Mode**: 

   ```bash
   export DEFAULT_COMMAND="gunicorn django_chat.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:9004"
   ```

### CSRF Trusted Origins

Set up `CSRF_TRUSTED_ORIGINS` to allow specific origins:

```bash
export CSRF_TRUSTED_ORIGINS='http://localhost'
```

### Debug Mode

Set `DEBUG` to "1" for development (debug mode) or "0" for production:

```bash
export DEBUG='1'
```

### Allowed Hosts

Specify the `ALLOWED_HOSTS` for your environment:

```bash
export ALLOWED_HOSTS='0.0.0.0,localhost,localhost:9004,127.0.0.1:9004'
```

### CORS Allowed Origins

Set up `CORS_ALLOWED_ORIGINS` for Cross-Origin Resource Sharing:

```bash
export CORS_ALLOWED_ORIGINS='http://localhost'
```

### Database Configuration

Set the following environment variables for database configuration:

```bash
export DB_NAME=postgres
export DB_USER=postgres
export DB_PASSWORD=postgres
export DB_HOST=database
export DB_PORT=5432
```

### Static and Media Files Configuration

- **Static Files**:

   ```bash
   export STATIC_URL='http://0.0.0.0:9002/'
   ```

- **Media Files**:

   ```bash
   export MEDIA_URL='http://0.0.0.0:9003/'
   ```

## Usage

- **Django REST Framework API**: Provides the backend API for your application.
- **WebSocket Connections**: Use WebSocket clients or front-end code to connect to the Channels-powered WebSocket endpoint at `ws://127.0.0.1:9004/ws/chat/`.

### Sending a Message

Once you've registered at least two users, you can send a message using the following WebSocket payload:

```json
{
   "message": "Hello World",
   "to_user_id": 1
}
```

## Postman Examples

For reference and testing, you can access the Postman workspace for this project [here](https://www.postman.com/rsvt-portfolio/workspace/django-chat/). Note that some APIs are still in development.

## Deployment

- **Docker Compose**: Use Docker Compose to manage your containers in development and production.
- **ASGI Server**: Use Daphne or Uvicorn for production deployment of ASGI applications.
- **Reverse Proxy**: Configure Nginx or Apache as a reverse proxy to manage connections to the Django application and WebSocket server.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions, feedback, or hiring inquiries, please reach out at [rsvijaytiwari@gmail.com](mailto:rsvijaytiwari@gmail.com). You can also hire me on a full-time basis.