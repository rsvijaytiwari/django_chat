
# django-chat 

These APIs included all the functionality which are related to Chat Functionality and Socket.

# Set up the environmental variables.

**DEFAULT_COMMAND**: It is default command to run the project if you need to run project in debug mode then set default value to **python manage.py runserver 0.0.0.0:9004** or if you are using the project in production mode then set default value **gunicorn django_chat.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:9004**.
```bash
export DEFAULT_COMMAND="python3 manage.py runserver 0.0.0.0:9004"
```
**CSRF_TRUSTED_ORIGINS**: It accepts list or array, but the value should be specified as string of url and seperated with comma without spaces. 
```bash
export CSRF_TRUSTED_ORIGINS='http://localhost'
```
**DEBUG**: It is string value of **"0"** or **"1"**, **"0"** means for production and **"1"** means for debug mode.
```bash
export DEBUG='1'
```
**ALLOWED_HOSTS**: It is string value of allowed hosts to use multiple hosts then use comma without without using spaces.
```bash
export ALLOWED_HOSTS='0.0.0.0,localhost,localhost:9004,127.0.0.1:9004'
```
**CORS_ALLOWED_ORIGINS**: It is string value of allowed cors origin (or cors configuration) to use multiple cors domain then use comma without without using spaces.
```bash
export CORS_ALLOWED_ORIGINS='http://localhost'
```
Database environmental variable are essential to setup in order to properly functioning of the project.
```bash
export DB_NAME=postgres
export DB_USER=postgres
export DB_PASSWORD=postgres
export DB_HOST=database
export DB_PORT=5432
``` 
**STATIC_URL**: It is string of url which is used for delivering the static files.

```bash
export STATIC_URL='http://0.0.0.0:9002/'
```
**MEDIA_URL**: It is string of url which is used for delivering the media files.

```bash
export MEDIA_URL='http://0.0.0.0:9003/'
```