# OZ-Coding-School Main Team Project - Team 04

## Project Overview
- 주제: 자취생들을 위한 레시피 공유 커뮤니티
- 핵심기능: 게시판 및 채팅

## Assigned
- Recipe(=Board) CRUD <br>
**recipe App 생성하여 작성*
  
---
## Cautions
> * Virtual env: Poetry
> * Interpreter: Python 3.12.0
> * Git Branch: Gitflow

`User`, `Food` app은 임의로 생성하여 진행함.

### Models

RichTextField 를 ckeditor.fields에서 직접 가져오기 위해 아래 설치 진행
```
$ poetry add django-ckeditor
```

*실행하면 ckeditor WARNING이 뜨고 보안상의 이슈로 4가 아닌 5를 이용하라고 권장하는데, <br> 
ckeditor5는 유료..?인 것 같고 백엔드에서 다룰 일이 따로 없어 변경하진 않았음.*

#### config/settings.py
recipe 앱 및 ckeditor 기재
```
INSTALLED_APPS = [
  'recipe',
  'ckeditor',
]

CKEDITOR_BASEPATH = "/my_static/ckeditor/ckeditor/"
```

### Permissions
IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly 권한 클래스 활용
1. IsAuthenticatedOrReadOnly
  - 로그인 여부 상관 없이 읽기 권한 모두 허용
  - 데이터 변경 요청 시 로그인 여부 검사 후 응답 반환
2. IsOwnerOrReadOnly
  - 읽기 권한은 모두에게 항상 허용
  - Recipe 게시글 작성자만 수정, 삭제 가능


### Views
> - generics `ListCreateAPIView` `RetrieveUpdateDestroyAPIView` 활용하여 overriding
> - permissions에서 권한 클래스 불러옴
> - 권한 상관없이 CRUD 테스트 시, AllowAny로 진행

1. RecipeListCreateAPIView
   "POST" 요청 유저를 게시물 작성자로 지정하도록 `perform_create` 오버라이드

2. RecipeDetailAPIView
   `get_object` 요청 객체 존재하지 않으면 404 반환하도록 오버라이드

### Tests
- python shell 혹은 admin 통해 데이터 임의 추가하여 진행
API Test를 위하여 두 테스트 유저를 생성해 아래 5개 항목 테스트 
1. 레시피 리스트 조회
2. 레시피 생성 : 500 Server Error 조치 필요.
3. 레시피 상세 조회 및 수정(비인증)
4. 레시피 삭제(소유자)
5. 레시피 수정(비소유자)
