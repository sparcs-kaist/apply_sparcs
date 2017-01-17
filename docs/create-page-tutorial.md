## 새 페이지 만들기 튜토리얼

### 실행

본 튜토리얼은 현재 frontend/ 폴더에 있다고 가정합니다.

먼저 UI 개발 환경을 실행합니다.

``` bash
$ gulp start
  ...
  [BS] Access URLs:
  ...
```

위와같이 성공했다면 localhost:3000으로 접속합니다. 같은 인터넷 환경에 있다면 external 주소를 통해 모바일이나, 다른 컴퓨터에서 다양한 해상도를 동시에 테스트 할 수 있습니다.

### 간단한 페이지 만들기

http://example.com/welcome/hello 페이지를 만들어 보도록합시다. 먼저 localhost:3000/welcome/hello로 접속하여 404가 뜨는지 확인합니다. 혹시 IsADirectoryError 같은 것이 보인다면 virtualenv가 켜져있는지 확인합니다.

모든 html, css작업은 web폴더 안에서 이루어 집니다. web/ 폴더에 welcome/ 폴더를 만들고 그 안에 hello.html을 만들어 봅시다.

web/welcome/hello.html
``` html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Hello</title>
  </head>
  <body>
    <h1>Hello!</h1>
  </body>
</html>
```

localhost:3000/hello/world.html로 접속해 보면 이 페이지가 보이게 됩니다. 이처럼 UI 개발 모드에서 폴더의 구조가 곧 URL이 되도록 설정해 두었으며 더 나아가 html을 빼고 localhost:3000/welcome/hello 로도 접속 가능합니다.

그럼 이제 브라우저를 띄운 채로 hello.html을 수정하고 저장해봅시다.

``` html
  ...
  <h1>Hello Sparcs!</h1>
  ...
```

브라우저가 자동으로 새로고침 되는게 보이나요? 이제 모니터를 하나 더 쓸 이유가 생겼군요.

그 다음으로는 css를 적용해봅시다. 같은 welcome/ 폴더 안에 hello.css를 작성하고 html이 이를 추가하도록 수정합니다.

web/welcome/hello.css
``` css
h1 {
  color: tomato;
}
```

web/welcome/hello.html
``` html
...
<head>
  <meta charset="utf-8">
  <title>Hello</title>
  <link rel="stylesheet" href="/media/css/welcome/hello.css">
</head>
...
```

장고는 css같은 파일들을 보낼 때 /media 같은 특정 라우터를 추가로 사용하며 /media는 장고의 설정에 따라 다르게 바뀔 수 있습니다. /media/css/파일위치 의 형태로 href를 적어줍니다. 아마 바로 스타일이 적용된걸 확인 할 수 있을겁니다. 마찬가지로 css를 바꿔 색을 변경해봅시다.

web/welcome/hello.css
``` css
h1 {
  color: royalblue;
}
```

역시 자동으로 css가 바뀌어 적용됩니다.

/welcome/hello 는 있는데 /welcome 은 없는게 조금 이상합니다. 그러면 이제 welcome페이지를 만들어 봅시다. 마찬가지로 web/welcome.html을 만들어도 되지만 ... 좀더 우아한 방법을 써보도록하죠.

web/welcome/index.html
``` html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Welcome</title>
  </head>
  <body>
    <h1>Welcome!</h1>
  </body>
</html>
```

welcome과 welcome/hello 는 서로 관련되어있을 가능성이 크기 때문에 이렇게 같은 폴더에 넣어두는 것을 추천하지만, 필수는 아닙니다. 기획에 따라 자유롭게 선택하세요. index.html을 불러오는건 웹의 네추럴한 성질이기도 합니다. 이 html은 여러 url로 접근할 수 있습니다.

- localhost:3000/welcome/index.html
- localhost:3000/welcome/index
- localhost:3000/welcome/
- localhost:3000/welcome

마지막 방법이 좋겠죠? 또한 welcome/index.html 과 welcome.html이 둘다 있을 경우엔 전자를 먼저 확인한다는 것도 살짝 알아두세요.

### Todo
sass, template 사용법
