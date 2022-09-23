"""
{% set name = "pyexcel-ezodf" %}
{% set version = "0.3.3" %}

- package:
  name: {{ name|lower }}
  version: {{ version }}

- name: loja
  path_driver: path
  browser: 
    path: path
    arguments:
      - remote-debugging-port=9226
      - profile-directory=nusp
      - user-data-dir="C:\Users\Franz\Downloads\nusp"

"""      
#!/usr/bin/env python

from rich import print
from jinja2 import Environment
from ruamel.yaml import YAML

with open("robo3n.yaml", "r") as stream:
    try:
        yaml = YAML(typ='safe')
        yaml_content = yaml.load(Environment().from_string(stream.read()).render())
        print(yaml_content)
    except yaml.YAMLError as exc:
        print(exc)
