# Welcome to Frontend world

---
## Intro

본 프로젝트는 한 개인의 욕심으로 프론트엔드 구현을 도와주는 여러 툴들이 구현되어있습니다. 더 나은 프론트엔드 개발을 돕고 디자이너도 UI개발에 참여 할 수 있는 환경이 되었으면 하는 바람을 담았으며 동시에 이 프론트엔드 환경을 꼭 배우고 따르지 않더라도 django 개발자들도 최대한 이전의 방식대로도 사용할 수 있게 하는 것이 본 프로젝트의 철학입니다.

## Getting Started

django 서버 세팅을 모두 마쳤다고 가정하며, js 패키지 매니저로 [npm][15705dba]을 사용하기떄문에 설치되어있지 않다면 설치하도록 합니다. 반드시 현재폴더가 frontend/ 에 있어야합니다. 모든 프론트엔드 작업은 frontend/에서 이루어 집니다.

본 프로젝트는 여러 frontend관련 task들을 [gulp][f18c84a1]를 통해 실행합니다. gulp를 사용하기 위해 npm의 global위치에 gulp-cli를 설치합니다.

  [15705dba]: http://npmjs.com/ "npmjs"
  [f18c84a1]: http://gulpjs.com/ "gulpjs"

> $ npm install -g gulp

또한 js dependency를 npm을 통해 설치합니다. 다시한번 말씀드리지만 현재 폴더는 frontend/ 입니다.

> npm install

준비가 모두 끝났습니다. UI dev 환경을 실행해 봅시다.

> gulp start

기본포트는 3000입니다. 변경하고 싶으시면 config.js파일에서 browserSync항목을 참고해주세요. localhost:3000에 접속하면 web폴더에 있는 index.html이 실행됩니다. 브라우저를 켜둔채 html, sass파일을 변경하고 저장해보세요.

## 새 페이지 만들기 Tutorial

[UI 튜토리얼](../docs/create-page-tutorial.md)은 sass, template, 심지어 django를 몰라도 js, css, html만 알고 있다면 바로 시작 가능합니다.

## 구성

### gulp

gulp는 직접 여러 task를 작성할 수 있는 라이브러리 입니다. 작성한 테스크는 tasks/에 있으며, 주로 사용할 테스크는 다음과 같습니다.

- start
  - UI Dev 환경을 실행합니다. (build가 포함되어있습니다.)
- build
  - 배포에 필요한 파일(sass, js등)을 build합니다.

그 밖의 테스크들은 파일을 참고해주세요. 꼭 필요한 사항은 아니지만 추가 테스크를 작성할 경우 파일 이름과 테스크 이름을 동일하게 작성하면 좋습니다.

### django render only server

UI Dev 환경의 경우는 디자인을 하면서 django를 만지지 않아도되게끔 서버로직을 완전히 분리했습니다. UI Dev환경 전용 django 설정은 apply_sparcs/ui_dev 에서 볼 수 있으며 templates를 단순히 render해주는 django setting을 사용합니다.

### [sass][6354966c]

  [6354966c]: http://sass-lang.com/ "sass"

sass, scss 버전중 scss를 사용하며 이는 css를 모듈별로 관리 할 수 있게 도와줍니다.

## 이하 작업중인 기타

### html template 규칙

- 폴더의 index.html은 최초 진입점을 의미한다 (ex. example.com/manage/ -> web/manage/index.html)
- 폴더구조는 url에서의 폴더와 일치한다. (ex. example.com/manage/ -> web/manage/)
- 언더바(\_)는 직접 view와 연결되지 않는 것들이다.
- 되도록 다른 app의 \_components 나 \_layouts를 참고하지 않도록한다. 찾기가 어려워진다. 같은 layout이더라도 해당 앱의 layouts에서 간단히 다른 앱의 layout을 extend하여 쓴다.

## 개발 시 유의사항
frontend 개발용 django의 html render 우선사항
- example.com/manage(/) 검색시
  1. web/manage.html
  2. web/manage/index.html
  3. 404

## 라이브러리 사용법
