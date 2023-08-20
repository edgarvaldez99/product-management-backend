# Product Management

Proyecto backend para el Product Management desarrollado con [Django](https://www.djangoproject.com/)

## EJECUTAR LOCALMENTE

### Pre-requisitos

-   Python 3.11
-   Pip 3 `(sudo apt-get install python3-pip)`
-   Instalar Poetry. Seguir la [guía para la instalación](https://python-poetry.org/docs/)
-   Instalar virtualenv `(sudo apt-get install python3-virtualenv python3-venv)`
-   Crear entorno virtual:
    ```
    poetry shell
    ```
    o
    ```
    virtualenv -p `which python3` .venv
    ```
-   Activar el entorno virtual:
    ```
    poetry shell
    ```
    o
    ```
    source .venv/bin/activate
    ```
    **OBS:** Al usar `poetry` no hay necesidad de activar el entorno virtual, simplemente utilice los comandos a través de `poetry`, por ejemplo, para levantar el servidor:
    ```
    poetry run python manage.py runserver
    ```
-   Instalar las dependencias especificadas en [pyproject.toml]:
    ```
    poetry install --no-root
    ```
-   Cree una base de datos con postgres o mysql
-   Generar archivos de i18n (Internacionalización):

    Para generar archivos de i18n (Si no existe), por ejemplo, para español utilice el comando:

    ```
    poetry run python manage.py makemessages -l es
    ```

    Este comando genera un archivo llamado `django.po` ubicado en la ruta `locale/es/LC_MESSAGES/*`. Este comando solo debe ejecutarse si no existe el archivo django.po en la carpeta mencionada.

    Para compilar los archivos i18n ejecutar el comando:

    ```
    poetry run python manage.py compilemessages
    ```

-   Copie y renombre el archivo `.env-example` a `.env` (No reemplace directamente el archivo `.env-example`, cópielo)
-   En el archivo `.env` cambie los valores de las variables de la base de datos para que apunten a la base de datos a utilizar.

    Ejemplo:

    ```
    ENV=development
    PORT=8000
    DATABASE_HOST=localhost
    DATABASE_NAME=django-test
    DATABASE_PASS=django-test
    DATABASE_PORT=5432
    DATABASE_USER=django-test
    DATABASE_TYPE=postgresql
    EXTERNAL_DATABASE_PORT=5432
    INSTALL_DEV=true
    LANGUAGE_CODE=es
    SECRET_KEY=secret_key
    TIME_ZONE=America/Asuncion
    CSRF_TRUSTED_ORIGINS=https://yourdomain.com,http://localhost:8000,http://localhost:8888
    ```

### Ejecutar

-   Para levantar la aplicación utilice el comando:

    Sin activar el entorno virtual:

    ```
    poetry run python manage.py runserver
    ```

    Con entorno virtual:

    ```
    python manage.py runserver
    ```

    **Obs:** Asegúrese de haber activado el virtualenv `(source .venv/bin/activate)` o `(poetry shell)`

-   La aplicación estará disponible en `http://localhost:8000`

## LEVANTAR LA BASE DE DATOS CON DOCKER

-   Copie y renombre el archivo `.env-example` a `.env` (No reemplace directamente el archivo `.env-example`, cópielo)
-   En el archivo `.env` cambie el valor del resto de las variables es opcional
-   Ejecutar
    ```
    docker-compose up
    ```

## EJECUTAR CON DOCKER

-   Copie y renombre el archivo `.env-example` a `.env` (No reemplace directamente el archivo `.env-example`, cópielo)
-   En el archivo `.env` cambie el valor de la variable `DATABASE_URL` a `db` (nombre del servicio de base datos en el docker-compose) y también quitar o vaciar el valor de `DATABASE_PORT`. Cambiar el valor del resto de las variables es opcional
-   Ejecutar
    ```
    docker-compose up --build
    ```
-   El backend estará disponible en `http://localhost:8000`

-   Para iniciar una sesión interactiva en el contenedor de backend ejecute:

    ```
    docker-compose exec app bash
    docker-compose exec nginx bash
    ```

-   Para ver el log utilice:
    ```
    docker-compose logs -f app
    docker-compose logs -f nginx
    ```

## TEST, LINT Y FORMATO DE CÓDIGO PYTHON

-   Para ejecutar test y verificar linteo utilice el comando [nox](https://nox.thea.codes/en/stable/):

    ```
    poetry run nox
    ```

    Para no instalar de vuelta las dependencias utilice:

    ```
    poetry run nox -r
    ```

### Test

-   Para ejecutar [test](https://docs.djangoproject.com/en/4.1/topics/testing) utilice:

    ```
    poetry run python manage.py test
    ```

-   Para obtener reporte de [coverage](https://docs.djangoproject.com/en/4.1/topics/testing/advanced/#integration-with-coverage-py) utilice:
    ```
    poetry run coverage run --source='.' manage.py test myapp
    poetry run coverage report
    ```

### Lint y Formato de código

-   Para ejecutar [flake8](https://flake8.pycqa.org/en/latest/) utilice:

    ```
    poetry run flake8
    ```

    En caso de error debe corregirse a mano. Para más información consulte el [glosario](https://flake8.pycqa.org/en/latest/glossary.html)

-   Para ejecutar [mypy](https://mypy.readthedocs.io/en/stable/) utilice:

    ```
    poetry run mypy .
    ```

    En caso de error debe corregirse a mano. Para más información consulte este [link](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

-   Para ejecutar [black](https://github.com/psf/black) utilice:

    ```
    poetry run black --check .
    ```

    En caso de error puede ejecutar el autocorrector:

    ```
    poetry run black .
    ```

-   Para ejecutar [isort](https://pycqa.github.io/isort/) utilice:
    ```
    poetry run isort --check-only .
    ```
    En caso de error puede ejecutar el autocorrector:
    ```
    poetry run isort .
    ```

### Pre-commit

-   [Pre-commit](https://pre-commit.com/) hook sirve para evitar que código no estándar se suba al repositorio.
    La configuración se basa en un archivo llamado .pre-commit-config.yaml.

        Para habilitar [pre-commit](https://pre-commit.com/) hooks utilice:
        ```
        poetry run pre-commit install
        ```
