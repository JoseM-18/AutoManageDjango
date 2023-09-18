# Django Concesionario App

Este proyecto es una aplicación web para gestionar el inventario y los pedidos de un concesionario de automóviles. La aplicación está construida con Django en el backend y Django Template en el frontend, utilizando una base de datos PostgreSQL.

## Estructura del proyecto

El proyecto tiene la siguiente estructura de directorios:

```
django-app
├── backend
│   ├── concesionario
│   │   ├── templates
│   │   │   ├── base.html
│   │   │   ├── home.html
│   │   │   ├── inventario.html
│   │   │   ├── pedido.html
│   │   │   └── error.html
│   │   ├── static
│   │   │   ├── css
│   │   │   │   └── style.css
│   │   │   └── js
│   │   │       └── script.js
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── models.py
│   │   ├── forms.py
│   │   └── admin.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── requirements.txt
│   └── manage.py
├── frontend
│   ├── public
│   │   ├── index.html
│   │   ├── inventario.html
│   │   ├── pedido.html
│   │   └── error.html
│   ├── src
│   │   ├── App.js
│   │   ├── index.js
│   │   ├── components
│   │   │   ├── Home.js
│   │   │   ├── Inventario.js
│   │   │   ├── Pedido.js
│   │   │   └── Error.js
│   │   └── styles
│   │       └── App.css
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
├── db.sqlite3
└── README.md
```

La carpeta `backend` contiene el código del backend de la aplicación, mientras que la carpeta `frontend` contiene el código del frontend de la aplicación.

## Instalación

Para instalar la aplicación, siga los siguientes pasos:

1. Clone el repositorio:

```
git clone https://github.com/your-username/django-app.git
```

2. Cree un entorno virtual e instale las dependencias:

```
cd django-app
python -m venv env
source env/bin/activate
pip install -r backend/requirements.txt
cd frontend
npm install
```

3. Configure la base de datos:

La aplicación utiliza una base de datos PostgreSQL. Cree una base de datos y configure las credenciales en el archivo `backend/settings.py`.

4. Ejecute las migraciones:

```
python backend/manage.py migrate
```

5. Ejecute el servidor de desarrollo:

```
python backend/manage.py runserver
```

6. Abra la aplicación en su navegador:

```
http://localhost:8000/
```

## Uso

La aplicación tiene tres páginas principales:

- La página de inicio (`/`) muestra un mensaje de bienvenida y enlaces a las páginas de inventario y pedidos.
- La página de inventario (`/inventario/`) muestra una tabla con todos los coches en el inventario y permite agregar, editar o eliminar coches.
- La página de pedidos (`/pedido/`) muestra una tabla con todos los pedidos y permite agregar, editar o eliminar pedidos.

## Contribución

Si desea contribuir a la aplicación, siga los siguientes pasos:

1. Cree un fork del repositorio.
2. Cree una rama para su nueva función o corrección de errores (`git checkout -b my-new-feature`).
3. Haga sus cambios y pruebas.
4. Haga un commit de sus cambios (`git commit -am 'Add some feature'`).
5. Haga push a la rama (`git push origin my-new-feature`).
6. Cree un pull request en GitHub.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo LICENSE para obtener más detalles.