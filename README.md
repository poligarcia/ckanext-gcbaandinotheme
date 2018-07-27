.. image:: https://travis-ci.org/datosgobar/ckanext-andinotemplate.svg?branch=master
    :target: https://travis-ci.org/datosgobar/ckanext-andinotemplate

.. image:: https://coveralls.io/repos/datosgobar/ckanext-andinotemplate/badge.svg
  :target: https://coveralls.io/r/datosgobar/ckanext-andinotemplate

.. image:: https://pypip.in/download/ckanext-andinotemplate/badge.svg
    :target: https://pypi.python.org/pypi//ckanext-andinotemplate/
    :alt: Downloads

.. image:: https://pypip.in/version/ckanext-andinotemplate/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-andinotemplate/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/ckanext-andinotemplate/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-andinotemplate/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/ckanext-andinotemplate/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-andinotemplate/
    :alt: Development Status

.. image:: https://pypip.in/license/ckanext-andinotemplate/badge.svg
    :target: https://pypi.python.org/pypi/ckanext-andinotemplate/
    :alt: License

# ckanext-andinotemplate

Template de Plugin para Andino. Este repositorio es una muestra de cómo implementar un plugin base para una instancia de Andino y agregar funcionalidades extendiendo el plugin.


## Instalación

Para instalar `ckanext-andinotemplate`:

1. Activá el _virtualenv_ de tu instancia de CKAN:

     . /usr/lib/ckan/default/bin/activate

2. Instalá el paquete de Python `ckanext-andinotemplate` dentro del _virtualenv_:

     pip install -e git+https://github.com/datosgobar/ckanext-andinotemplate.git#egg=ckanext-andinotemplate

3. Agregá `andinotemplate` a la lista de `ckan.plugins` en tu archivo de configuración de CKAN
   (por defecto ubicada en `/etc/ckan/default/production.ini` dentro del contenedor `portal`).

4. Reiniciá Andino.
