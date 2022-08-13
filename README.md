# AlanMRamirez

## Portfolio 

<h6>Este portafolio es una aplicacion web hecha con Django </h6> 

![](https://designcodesolutions.com/wp-content/uploads/2019/08/plantilla-moderna-pagina-inicio-diseno-plano-ok.png)

## Librerias necesarias se encuentran en el archivo requirements

<p>Se recomienda utilizar un entorno virtual</p>

`pip install -r requirements.txt`

<p>Se recomienda utilizar la  base de datos PostgreSQL, para eso instalar psycopg2</p>

`pip install psycopg2-binary`

## Desarrollo

<p>Recordar que durante la fase de desarrollo se tiene colocar True en el DEBUG y si se requiere colocar localhost y 127.0.0.1 en ALLOWED_HOST</p>

    DEBUG = True
    
    ALLOWED_HOSTS = []

<h6>Para levantar el servidor local</h6>

`python manage.py runserver`
