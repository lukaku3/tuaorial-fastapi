# tuaorial-fastapi

```
docker compose run --entrypoint "poetry init \
 --name app \
 --dependency fastapi \
 --dependency uvicorn[standard]" \
 demo-app
```

```
docker compose run --entrypoint "poetry init \
 --name backend \
 --dependency fastapi \
 --dependency uvicorn[standard]" \
 demo-app
```

# poetry install

```
docker compose run --entrypoint "poetry install --no-root" demo-app
```
