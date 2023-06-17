# Sistema de Desafíos

# Requerimientos
## Si se quiere levantar con docker
- Docker
- docker-compose

*NOTA: La descarga de la imagen de redis puede fallar, en ese caso ejecutar:
```bash
docker pull redis/redis-stack-server
```

## Si se quiere levantar a manopla
- Python >= 3.8
- [Mongo](https://www.mongodb.com/docs/manual/administration/install-community/)
- Sugerido
    - [MongoDB Compass Win](https://downloads.mongodb.com/compass/mongodb-compass-1.35.0-win32-x64.exe)
    - [MongoDB Compass Linux](https://downloads.mongodb.com/compass/mongodb-compass_1.37.0_amd64.deb)
- [Redis](https://redis.io/download/) - Leer sugerencia en el apartado de levantar la app antes de instalarlo)
- Sugerido - [RedisInsight](https://redis.com/es/redis-enterprise/redisinsight/)

# Levantar la aplicación
### Vía python (recomendado)
1. Instalar requerimientos
```bash
pip install -r requirements.txt
```
2. Levantar app
```bash
python -m uvicorn server.server:app --host 0.0.0.0 --port 9001 --reload
```

### Vía docker
```bash
docker-compose up
```
La app estará expuesta en el puerto 9001.
Al ejecutar este comando se va a levantar también la base de datos y la caché.
Mongo estará expuesto en el puerto 27018, y redis en 6380

### Opción: Levantar mongo y redis desde docker aparte
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

[Documentación](https://docs.google.com/document/d/11sYc6pS_zhEcRqV0SXSsP8Vvb0GIbeX62_426n1KPJI/edit#)