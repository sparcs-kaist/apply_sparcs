# Welcome to Frontend world

## 구성
templates를 단순히 render해주는 django setting을 사용한다. (frontend/settings.py)

## 사용법
```bash
python manage.py runserver --settings=apply_sparcs.frontend.settings
```

### html template 규칙

- 폴더의 index.html은 최초 진입점을 의미한다 (ex. example.com/manage/ -> web/manage/index.html)
- 폴더구조는 url에서의 폴더와 일치한다. (ex. example.com/manage/ -> web/manage/)
- 언더바(\_)는 직접 view와 연결되지 않는 것들이다.
- 되도록 다른 app의 \_components 나 \_layouts를 참고하지 않도록한다. 찾기가 어려워진다. 같은 layout이더라도 해당 앱의 layouts에서 간단히 다른 앱의 layout을 extend하여 쓴다.

## 개발 시 유의사항
frontend 개발용 django의 html render 우선사항
- example.com/manage(/)
  - web/manage.html
  - web/manage/index.html
