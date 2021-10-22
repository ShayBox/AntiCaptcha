# AntiCaptcha
A python library for anti-captcha.com

[Documentation for the API](https://anti-captcha.com/apidoc)

#### Requirements
- [git](https://git-scm.com/)

#### Install
```
git clone https://github.com/ShayBox/AntiCaptcha.git
cd AntiCaptcha
$ poetry build
$ pip install dist/AntiCaptcha-0.1.0.tar.gz --user
```

#### Usage

```py
from anticaptcha import AntiCaptcha

captcha = AntiCaptcha("API KEY")
captcha.solve({"TASK": "OBJECT"})
```