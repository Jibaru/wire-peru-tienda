# Wire Perú S.A.C

## Comandos iniciales

```
django-admin startproject wireperu
cd wireperu
python manage.py startapp tienda
```

## Migrar modelos

```
python manage.py makemigrations
python manage.py migrate
```

## Crear superusuario

```
python manage.py createsupeuser
```

## BD Ejemplo

Crear una copia de `ejemplo.db.sqlite3` removiendo `ejemplo.`
El superusuario es:

```
Usuario: admin
Contraseña: 123456789
```

## Prueba

[Página Prueba](https://cryptic-beach-87901.herokuapp.com/)
[Admin](https://cryptic-beach-87901.herokuapp.com/admin)