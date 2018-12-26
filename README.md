# django-spectre
![https://picturepan2.github.io/spectre/img/spectre-logo.svg](https://picturepan2.github.io/spectre/img/spectre-logo.svg)

## Overview 

Spectre css Docs

https://picturepan2.github.io/spectre/index.html


## Install

```.bash
# install from github
git clone https://github.com/Bit03/django-spectre.git
cd django-spectre
python setup.py install
```


## Configuration
Add to INSTALL_APPS in your settings.py
```.python
INSTALLED_APPS = [
    ...
    'spectre',
]


# spectre config
#
# -------------------------------------------------
SPECTRE_DEFAULTS = {
    "css_url": {
        "url": "https://unpkg.com/spectre.css/dist/spectre.min.css"
    },
}

```


## Usage

1. spectre avatar

    add spectre tags in your django template  
    
    ```.html
        {% load spectre_tags %}
        
        {% spectre_avatar '<avatar_url>' '<size>' %}

    ``` 
