[![Build Status](https://travis-ci.org/datosgobar/ckanext-andinotemplate.svg?branch=master)](https://travis-ci.org/datosgobar/ckanext-andinotemplate)

[![Docs Status](https://readthedocs.org/projects/ckanext-andinotemplate/badge/?version=master)](http://ckanext-andinotemplate.readthedocs.io/es/master/)

# ckanext-andinotemplate

Template de Plugin para Andino. Este repositorio es una muestra de cómo implementar un plugin base para una instancia 
de Andino y agregar funcionalidades extendiendo el plugin.


## Instalación de prueba

Antes de crear y comenzar a utilizar tu propio plugin basado en `ckanext-andinotemplate`, quizás quieras 
instalar el original a modo de prueba. Para lograrlo:

1. Activá el _virtualenv_ de tu instancia de CKAN:

     . /usr/lib/ckan/default/bin/activate

2. Instalá el paquete de Python `ckanext-andinotemplate` dentro del _virtualenv_:

     pip install -e git+https://github.com/datosgobar/ckanext-andinotemplate.git#egg=ckanext-andinotemplate

3. Agregá `andinotemplate` a la lista de `ckan.plugins` en tu archivo de configuración de CKAN
   (por defecto ubicada en `/etc/ckan/default/production.ini` dentro del contenedor `portal`).

4. Editar el archivo de configuración de Andino `/etc/ckan/default/production.ini` dentro del contenedor `portal` 
y agregar el setting `andino.base_page = andino_custom_base_page.html`, provisto por `ckanext-andinotemplate`.

5. Reiniciá Andino.

### Funcionalidades base

El plugin template default permite agregar a tu instancia de Andino dos puntos de menú en la navegación superior de Andino:

* Andino: Al hacer click redirige a la [documentación oficial de Portal Andino](http://portal-andino.readthedocs.io/).
* Nueva Sección: Es una demostración de cómo agregar una ṕágina de contenido estático en Andino.


## Soporte para plugin extensible

Para crear e instalar tu propia versión de `ckanext-andinotemplate` para agregar funcionalidades adicionales a tu 
Andino seguí los siguientes pasos:

1. Necesitás tener tu copia del proyecto `ckanext-andinotemplate`, lo cual podés lograr haciendo un fork 
del original o una copia del repositorio.

1. Renombrar el plugin acorde a la funcionalidad que agregarás. Por ejemplo `ckanext-miplugindeandino`.

2. Ingresá al contenedor `portal` de tu Andino y asegurate de que esté activado el _virtualenv_:

     . /usr/lib/ckan/default/bin/activate

3. Instalá el paquete de Python correspondiente a tu plugin en modo editable dentro del _virtualenv_:

     pip install -e <URL de tu plugin>

4. Agregá tu plugin a la lista de `ckan.plugins` en tu archivo de configuración de CKAN
   (por defecto ubicada en `/etc/ckan/default/production.ini` dentro del contenedor `portal`). Si tu plugin se llama 
   `ckanext-miplugindeandino` lo que debés agregar es `miplugindeandino`.

5. Editá el archivo de configuración de Andino `/etc/ckan/default/production.ini` dentro del contenedor `portal` y 
agregá el setting `andino.base_page = andino_custom_base_page.html`, provisto por tu copia de `ckanext-andinotemplate`. 
Este paso es opcional, y sólo debés hacerlo si deseás modificar los templates de Andino.

6. Reiniciá Andino.

### Utilizar un archivo nuevo como página base

El archivo `andino_custom_base_page.html` deberá contener lo que desees mostrar en vez del template default que 
utiliza Andino. Esto te permite, por ejemplo, agregar secciones nuevas en el header (las cuales te pueden servir 
para mostrar las nuevas funcionalidades) junto a las ya existentes.

Recomendamos basarse en el template utilizado por default en Andino y realizar modificaciones a partir del mismo.

### Agregar una página custom

Se requiere la utilización de un template nuevo para cada funcionalidad, el cual debe ser guardado en el mismo 
directorio que el archivo `template_nuevo.html`.

* Creá un nuevo template copiando el archivo template_nuevo.html, por ejemplo `mi_nuevo_template.html`.

* Agrega una nueva "acción" en la clase dentro de plugin_controller.py; éste debe ser un método que reciba cierto 
parámetro y devuelva render("mi_nuevo_template.html").

* En el archivo `plugin.py` de ckanext-andinotemplate, dentro de la función `after_map`, copiar y pegar un código 
parecido a éste _exactamente arriba de la línea "return m"_:

```
        m.connect('mi_pagina_custom', "/el_path_de_mi_pagina",
                  controller='ckanext.andinotemplate.plugin_controller:AndinoTemplateController',
                  action='nombre_de_mi_accion')
```

* En el archivo `plugin_controller.py` de ckanext-andinotemplate, pegar como función nueva este código:

```
    def nombre_de_mi_accion(self):
        return base.render('mi_nuevo_template.html')  # Especificamos el template
```

Es importante que el nombre de la función, en este ejemplo "nombre_de_mi_accion", sea _el mismo_ que se escribió para 
'action' en `plugin.py`.

### Documentación oficial de desarrollo de plugins para CKAN

Para más información acerca de cómo desarrollar un plugin para CKAN, podés ver la 
[documentación oficial](http://docs.ckan.org/en/ckan-2.7.3/extensions/tutorial.html).