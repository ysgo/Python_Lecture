# Today I Learned

## [D01] 191021 INTRO
- 해피해킹 소개
- 교육 일정 안내
- Python remind

## [D02] 191022

- python 자료형(list, dict) 실습
- python 함수
- python web scrapping
- python class

## [D03] 191023

- Web Bootstrap
- Flask 설치
- Flask variable routing, render_template
- Flask telegram request - response

## [D04] 191024

- 학습 목록
  - Flask Chatbot request - response
  - Flask Chatbot Webhook / ngrok
  - Flask (Lotto, Papago) 실습
  - Django Intro
  - Django startproject
  - Django DTL
  - Django TV type (lotto, artii) 실습

### 가상환경 설정

```bash
$ python -m venv venv # 가상환경 파일 만들기
$ source ./venv/Scripts/activate # 가상환경 실행
$ code . #코드 실행
$ python -m pip install --upgrade pip # (업그레이드)
```

### FLASK 실행

```bash
$ FLASK_APP=(파일이름) flask run
```

### webHook

```python
$./ngrok http 5000 # webhook url확인 방법 (터미널)

#1. webhook을 통해 telegram에 보낸 요청 안에 있는 메시지를 가져와서 그대로 전송 (소스)
url = f'{base}/bot{token}/setWebhook?url=https://0660d15b.ngrok.io/{token}'
```

## [장고(Django)]

1. django 의 성격

   - 다소 독선적(Opinionated)
   - django 실행

   ```bash
   $ python manage.py runserver
   ```

2. for문 활용법

   - {% for 변수 in 변수 %} -> 기본 for문 사용법 (끝에 {% endfor %} 써줘야함)

3. urls.py

   ```python
   path('match/', views.match) 
   #앞에는 url주소, 뒤에는 views의 값
   ```
   
4. requirements.txt 생성

   ```bash
   $ pip freeze > requirements.txt
   ```

5. requirements.txt로 pip 라이브러리 설치

   ```bash
   $ pip  install -r requirements.txt
   ```

## [D05] 191025 - 아이디어톤

## [D06] 191028

- Django review
  - 가상환경 재설정
  
  - Django startproject
  
    1. 프로젝트 만드는 법
  
       ```bash
       $ django-admin startproject '이름'
       ```
  
    2. app 만드는법
  
       ```bash
       $ django-admin startapp '이름'
       ```
  
  - Django render / variable-routing

## [D07] 191029

- Django GET / POST
- Django Template Namespace
  - static파일을 사용할려면 html소스에 {% load static %} 를 써줘야함
  - {{% extends 'utilities/base,html' %}} -> base.html을 가져와서 사용하겠다
- Django Template Inheritance
  - Django Papago 번역 실습

## [D08] 191030

- Database(RDBMS)

  - 데이터베이스는 체계화된 데이터의 집합이다.
  - RDBMS(관계혀데이터베이스 관리 시스템)
    - 관계형 기반으로하는 데이터베이스 관리시스템
      - 오라클
      - MySQL
      - SQLite
  - 스키마(scheme)
    - 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조
      - PK = ID : 각 행의 고유값으로 Primary Key로 불린다. 반드시 설정해야하며 데이터베이스 관리 및 관계 설정시 주요하게 활용
  - SQL
    - 관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위한 프로그래밍 언어

- ORM(Object-relational mapping)

- Django shell

- Django Admin

- Django CRUD

- 단계별 객체와 관계의 설정

  - 장점
    - 재사용 및 유지보수의 편리성이 증가한다
    - 객체 지향적인 코드로 인해 더 직관적이고 비즈니스 로직에 더 집중할 수 있게 도와준다
    - DBMS에 대한 종속성이 줄어든다
  - 단점
    - 완벽한 ORM 으로만 서비스를 구현하기가 어렵다
    - 프로시저가 많은 시스템에선 ORM의 객체 지향적인 장점을 활용하기 어렵다
    - 프로시저란? -> 특정 작업을 수행 하는, 이름이 있는 PL/SQL BLOCK 이다

- migrations

  - 관련 명령어

  ```bash
  $ python manage.py makemigrations # migration 파일 생성
  $ python manage.py migrate # migration 적용(DB에 반영하기)
  ```

- shell

  - shell로 모델 조작하기

    ```shell
    $ python manage.py shell # shell 실행
    >>> from articles(만든app이름).models import Article # shell과 연결 후 작성
    >>> Article.objects.all() # 모든 데이터를 확인(QuerySet으로 확인)
    ```

  - 데이터 import방법

    ```shell
    # 방법 1
    >>> article = Article()
    >>> article.title = 'first'
    >>> article.content = 'django'
    >>> article.save()
    
    # 방법 2
    >>> article = Article(title='second', content='edition')
    >>> article
    >>> article.save()
    
    # 방법 3 (save 할 필요가 없다.)
    >>> Article.objects.create(title='third', content='eye')
    
    # 세부내용 확인
    def __str__(self):
          return f'{self.id}번 글 - {self.title} : {self.content}' 작성해주고 
    >>> Article.objects.all()해주면 됨
    
    # 마지막 세이브한거에 대하여 값 확인
    >>> article.id # 마지막 저장한 id값이 나온다.
    >>> article.title # 마지막 저장한 title값
    ```

  - 데이터 특정값 확인하기

    ```shell
    # filter - title이 'first'인 데이터를 보여준다.
    >>> Article.objects.filter(title='first')
    # title이 'first'인 데이터중에서 첫번째 데이터를 보여준다.
    >>> Article.objects.filter(title='first').first()
    # get - pk가 1인 값을 보여준다.
    >>> Article.objects.get(pk=1)
    # get활용(특정값 수정)
    >>> article = Article.objects.get(pk=4)
    >>> article.title = '4th'
    >>> article.save() # 저장하면 pk가 4인 데이터의 title을 4th로 바꿔준다.
    ```

  - 유효성 검사

    ```bash
    $ 클래스변수명(article).full_clean()
    ```

  - 활용

    ```shell
    # 역순으로 뽑기
    >>> articles = Article.objects.order_by('-pk')
    >>> article
    
    # 2번째 3번째 뽑아내기
    >>> articles = Article.objects.all()[1:3]
    >>> articles
    
    # title에 'fir'이 들어가있는거 뽑아내기
    >>> articles = Article.objects.filter(title__contains='fir')
    >>> articles
    
    # title에 f가 들어가 있는거 뽑기
    >>> articles = Article.objects.filter(title__startswith='f')
    >>> articles
    ```

  - 지우기(delete)

    ```shell
    >>> article = Article.objects.get(pk=[선택 pk 번호])
    >>> article.delete()
    ```

- 관리자 지정하기

  ```bash
  $ python manage.py [createsuperuser] 
  > 아이디 설정(선택: default값 존재)
  > 이메일 설정(선택)
  > 비밀번호 설정
  > y(완료)
  ```

- 관리자 설정

  - admin.py 파일을 생성한다.

  - 사이트 구조를 바꿀려면 아래 클래스 선언한다

    ```python
    class ArticleAdmin(admin.ModelAdmin):
        list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    
    admin.site.register(Article, ArticleAdmin)
    ```

- django-extensions

```bash
# django shell을 실행하기 위해 install해준다.
$ pip install django-extensions 
# settings에서 'django_extensions'를 INSTALLED_APPS에 추가해준다
# shell_plus로 가동(from import를 안해줘도 자동으로 모두 import)
$ python manage.py shell_plus
```

## [D09] 191031

### HTTP

1. 기본 속성
   - Stateless : 상태정보가 저장되지 않음. 즉, 요청 사이에는 연결고리가 없음
   - Connectless : 서버에 요청을 하고 응답을 한 이후에 연결은 끊어짐
2. 응답 코드
   - 200 : 정상적으로 수행됨
   - 300 : 서버가 클라이언트를 다른 주소로 보냄
   - 400 : 서버가 요청을 받지 못하였음
   - 401 : 미승인(비인증)
   - 403 : 접근할 권리가 없음
3. Method
   - GET
   - POST
   - PUT/PATCH

## [D10] 191101

- Django CRUD 종합실습(Movie app)

## [D11] 191104

- Django 1:N Intro
  - comment_create
  - comment_delete

### 댓글 기능

1. models.py(Comment클래스 추가)

   ```python
   class Comment(models.Model):
       content = models.CharField(max_length=300) #댓글
       created_at = models.DateTimeField(auto_now_add=True) #댓글 생성 날짜
       article = models.ForeignKey(Article, on_delete=models.CASCADE)
       #article클래스 외래키 설정(연결시키는거)
   ```

2. admin.py

   ```python
   class CommentAdmin(admin.ModelAdmin):
       list_display = ('id','content','created_at','article_id')
   ```

3. shell

   ```python
   # article을 pk에 맞게 불러온다
   article = Article.objects.get(pk=2)
   
   # comment를 만들어준다
   comment=Comment()
   
   # comment의 값을 넣어준다
   comment.content='first comment' -> 방법1
   comment = Comment(article=article, content='second comment') -> 방법2
   
   # comment에 article을 연결
   comment.article=article
   
   # comment의 맞는 article글 찾는 방법
   comment.article
   
   # article의 comment불러오기(comment는 여러개이므로 전체를 불러와야함)
   article.comment_set.all()
   ```

## [D10] 191105

- Django Static Image Upload

  - 이미지 파일 넣기

    ```bash
    # 이미지처리
    $ pip install pillow
    
    파일을 보낼려고 할 때 form태그에 enctype을 해줘야한다.
    Ex) enctype="multipart/form-data"
    
    # PIL, Pillow를 좀 더 쓰기 쉽도록 도와주는 라이브러리
    $ pip install pilkit
    
    # django를 안써주면 일반imagekit랑 2개가 install되서 충돌난다
    $ pip install django-imagekit
    ```

- Django Media Image Upload
  
  - Resize Image Upload (Win7 OSError > Win10 or Mac recommend)

## [D13] 191106

- Django 1:N 실습(Genre/Movie/Score)
- Favicon
- Django Form
  - get_object_or_404

## [D14] 191107

- 2차 아이디어톤 준비

## [D15] 191108 - 2차 아이디어톤

- GoldenHour (실시간 응급실 가용병상 조회 서비스) - 최영선, 전지나, 오현경
- 사자매 (의약품 주의사항 정보 제공 서비스) - 이영걸, 윤현수, 경현, 호유송
- Our Kitchen (공유주방 플랫폼) - 이민우, 김소미, 강다영
- 5인용 (집 밖은 위험해) - 설동재, 고예성, 박건호, 박찬우, 홍성재

## [D16] 191111

- Django 1:N 실습 풀이
- Django form class review
- Django ModelForm
  - request.resolver_match.url_name
  - bootstrap_form

## [D17] 191112

- Django ModelForm review
- Django Authentication
  - Signup / Login / Logout / Quit

## [D18] 191113

- Webpage Designing(Bootstrap)
- Django Authentication
  - Edit / Password
  - template: auth_form
  - Model: article.user

## [D19] 191114

- Django Authentication
  - comment.user
- Django Model Relation
  - 1:N (Article:Comment / User:Article / User:Comment)
  - M:N (User:Article[Like] / User:User[Following/Follower]) Logic

## [D20] 191115

- Django ModelForm, 1:N, Auth 종합실습(Movie / Rating)