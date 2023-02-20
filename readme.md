# Sistema de Desafíos - Alternativa NoSQL

# Requerimientos
- Docker
- docker-compose
- Python >= 3.8
- [Mongo](https://www.mongodb.com/docs/manual/administration/install-community/)
- Sugerido - [MongoDB Compass](https://downloads.mongodb.com/compass/mongodb-compass-1.35.0-win32-x64.exe)

# Levantar la aplicación
```bash
docker-compose up
```
El comando va a ejecutar los tests y luego levantar la aplicación.
Para que funcione, es importante que mongo esté corriendo.

# Ingresar al contenedor
```bash
docker exec -it challenges bash
```
