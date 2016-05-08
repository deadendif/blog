#!/bin/bash

pip install django==1.8
pip install django-mptt
pip install django-tagging
pip install markdown
pip install Pillow

# 安装PIL
sudo apt-get install python-imaging

## 下面操作没有成功
pip uninstall PIL
# 前提:安装jpeg
sudo apt-get install libjpeg8-dev
pip install PIL
## 没有成功
