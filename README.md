# Entrega Final
### alumno: francolorenzino27@gmail.com

git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Franco2798/CoderHouse-54130-Python.git
git push -u origin main
git status

# Clase 17:

1. Crear proyecto Django
    ```bash
    django-admin startproject nombre_del_proyecto
    ```
    ```bash
    # Otras variantes del comando si falla:
    python -m django startproject nombre_del_proyecto
    # Y si usan python3 como comando:
    python3 -m django startproject nombre_del_proyecto
    ```

2. Testear servidor
    ```bash
    python manage.py runserver
    ```

3. Crear una `application` dentro de mi proyecto:
    ```bash
    python manage.py startapp <nombre de su aplicación>
    ```

4. Creamos un archivo que se llame `urls.py` en     Entrega_Final\Plataforma\bookings\urls.py