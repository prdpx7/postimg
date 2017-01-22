# postimg
:rocket: upload images on imgur & share instantly.(link will be copied to clipboard automatically)

<img src="http://i.imgur.com/aBoKRZe.png" alt="snap" height="200">

[![MITlicensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/zuck007/postimg/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/postimg.svg)](https://badge.fury.io/py/postimg)
## IMGUR API

  [Get](https://api.imgur.com/oauth2) IMGUR_CLIENT_ID and save it as an environment variable.(although default is hardcoded)
  ```
  export IMGUR_CLIENT_ID='xxxxxx'
  ```

## Installation
```
pip install postimg
```
## Usage
```
$ postimg --help
usage: postimg [-h] [--github] [--html] [--reddit] img_path

Post/upload image on imgur.com

positional arguments:
  img_path    image path of file

optional arguments:
  -h, --help  show this help message and exit
  --github    Github markdown code of imgur url
  --html      html <img> code of imgur url
  --reddit    reddit markdown code of imgur url

link will automatically copied to clipboard
```
