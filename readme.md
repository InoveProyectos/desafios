# Sistema de Desafíos

# Requerimientos
- Docker
- docker-compose
- Python >= 3.8
- [Mongo](https://www.mongodb.com/docs/manual/administration/install-community/)
- Sugerido - [MongoDB Compass](https://downloads.mongodb.com/compass/mongodb-compass-1.35.0-win32-x64.exe)
- [Redis](https://redis.io/download/) - Leer sugerencia en el apartado de levantar la app antes de instalarlo)
- Sugerido - [RedisInsight](https://redis.com/es/redis-enterprise/redisinsight/)

# Levantar la aplicación
```bash
docker-compose up
```
Para que funcione, es importante que mongo y redis estén funcionando.
### Opción: Levantar mongo y redis desde docker
```bash
docker run -p 6379:6379 redis/redis-stack-server:latest
docker run -p 27017:27017 mongo:latest
```

# Ingresar al contenedor
```bash
docker exec -it challenges bash
```

# Ejecutar los tests
Ingresar al contenedor y ejecutar
```bash
pytest -s
```
