[![Build Status](https://travis-ci.org/poligarcia/ckanext-gcbaandinotheme.svg?branch=master)](https://travis-ci.org/poligarcia/ckanext-gcbaandinotheme)

[![Docs Status](https://readthedocs.org/projects/ckanext-gcbaandinotheme/badge/?version=master)](http://ckanext-gcbaandinotheme.readthedocs.io/es/master/)

# ckanext-gcbaandinotheme

Plugin visual del portal de Datos Abiertos de la Ciudad Autónoma de Buenos Aires para Andino. 

## Instrucciones de instalación

1. Ingresar al host donde se encuentra instalado Andino.
1. Ingresar al contenedor `portal` (`docker-compose exec bash`).
1. Dentro del contenedor `portal` activar el `virtualenv` de CKAN: `. /usr/lib/ckan/default/bin/activate`.
1. Instalar el plugin con `pip`: `pip install -e git@github.com:poligarcia/ckanext-gcbaandinotheme.git@119cdc9#egg=ckanext-gcbaandinotheme`.
1. Editar el archivo `/etc/ckan/default/production.ini` y modificar:
    1. Agregar `gcbaandinotheme` a la lista de plugins inmediatamente después de `gobar_theme`.
    1. Agregar `andino.base_page = gcba_base_page.html` dentro de la sección `[app:main]`.
1. Reiniciar Andino.
