# AntiCaptcha
A python library for anti-captcha.com

[Documentation for the API](https://anti-captcha.com/apidoc)

#### Requirements
- [git](https://git-scm.com/)

#### Install
```
$ pip install git+https://github.com/ShayBox/AntiCaptcha.git
```

#### Usage

```py
from anticaptcha import AntiCaptcha

captcha = AntiCaptcha("API KEY")
captcha.solve({"TASK": "OBJECT"})
```
