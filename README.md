# Suggestic Code Challenge
# Teravision

------------
Create a web service using any framework that flattens a nested sequence into a single list of values.

## Input:
    {
        "items": [1, 2, [3, 4, [5, 6], 7], 8]
    }

## Output:
    {
        "result": [1, 2, 3, 4, 5, 6, 7, 8]
    }

------------
##### API
Se crea un API usando el microframework FLASK, el cual expone el metodo '/nested' el cual es consumido por 'GET' y recibe una lista de elementos.

##### Despliegue
La imagen de la aplicacion se encuentra en DockerHUB y se puede descargar con el siguiente comando:
```
docker pull giovanni299/teravision:latest
```

Para ejecutarla el comando seria:
```
docker run -it -p 5000:5000 -d IMAGE_ID
```

Para realizar pruebas y ver el funcionamiento de la API, esta fue desplegada en AWS en la URL http://3.134.93.234:5000/
Para probarla la APi por CURL:
```
    curl -L -X GET 'http://3.134.93.234:5000/nested' -H 'Content-Type: application/json' --data-raw '{
        "items": [1,2,[3,4,[5,6],7],8]
    }'
```