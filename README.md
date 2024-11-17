# Advanced_Cabel_Plugin

A NetBox plugin to enhance cable functionality with fiber types and modules


* Free software: MIT
* Documentation: https://summoner1904.github.io/AdvancedCable/


## Features

The features the plugin provides should be listed here.

## Compatibility

| NetBox Version | Plugin Version |
|----------------|----------------|
|     4.0        |      0.1.0     |

## Installing

For adding to a NetBox Docker setup see
[the general instructions for using netbox-docker with plugins](https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins).

While this is still in development and not yet on pypi you can install with pip:

```bash
pip install git+https://github.com/summoner1904/AdvancedCable
```

or by adding to your `local_requirements.txt` or `plugin_requirements.txt` (netbox-docker):

```bash
git+https://github.com/summoner1904/AdvancedCable
```

Enable the plugin in `/opt/netbox/netbox/netbox/configuration.py`,
 or if you use netbox-docker, your `/configuration/plugins.py` file :

```python
PLUGINS = [
    'AdvancedCable'
]

PLUGINS_CONFIG = {
    "AdvancedCable": {},
}
```
----------------------------------------------------------------------
# Описание работы
Изначально не знали, что такое NetBox, поэтому возникло много сложностей.

В процессе работы:
- Узнали что такое NetBox;
- Научились разворачивать NetBox на Ubuntu;
- Улучшили навыки работы с терминалом Linux;
- Создали схему разварки муфты;
- Создали карту с маршрутом различных кабелей;

В самом начале накатаили Ubuntu 22.04 на виртуальную машину.
После этого клонировали репозиторий NetBox.
Настроили конфигурационный файл и развернули платформу на локальном сервере.
![image](https://github.com/user-attachments/assets/616ef13d-42bb-4ab8-9b05-dea63ee8563d)

Развернули с помощью uWSGI вместо Gunicorn, т.к. были ошибки с Gunicorn.
![image](https://github.com/user-attachments/assets/28b4c7d7-c47c-4ce0-a9a2-6dcccc1954be)

Визуализировали некоторые задачи, например, создали машрут различных кабелей.
![image](https://github.com/user-attachments/assets/b33a5af1-6b42-4532-864e-7b60f9290e03)
![image](https://github.com/user-attachments/assets/0db2ea1f-7f48-4dbf-a91a-7c09324a8878)
![image](https://github.com/user-attachments/assets/fe82e4a3-31d5-4085-9e4f-12a16c06658c)
Несколько примеров созданных маршрутов.

![image](https://github.com/user-attachments/assets/e96bd6d8-51df-462f-af36-9251b25fe17e)

В планах было встроить в страницу информации о кабеле вкладку Map, где была бы карта с маршрутом.

Имеется также схема оптической сети. Для ее перевода из .dot в .png прописать в терминале:
`dot -Tpng example.dot -o example.png`
![image](https://github.com/user-attachments/assets/6b550c06-2976-497c-b011-7063839abc19)


Схема разварки волоконно-оптической муфты.
![image](https://github.com/user-attachments/assets/2fdc75c8-43b9-450b-b336-2389ab5bbfec)
Для ее перевода из .dot в .png прописать в терминале:
`dot -Tpng mufta.dot -o mufta.png`

# Проблемы
Плагин в репозитории получился пустым, не стали добавлять весь имеющийся код (графику) в плагин,
поскольку не получилось интегрировать плагин в приложение. Скорее всего, проблемы с пониманием логики
написания приложений на Django. 





