BOOKLOG
===

📖 Introduction
---

멋쟁이사자처럼 9기 해커톤 : 북로그

🏁 설치 안내
---

### 1. git clone

원하는 폴더에 레포지토리를 클론해주세요.

```bash
$ git clone https://github.com/Han-Joon-Hyeok/Booklog.git
```

### 2. 가상환경 생성

Django를 실행하기 위한 가상환경을 생성해주세요.

```bash
$ python -m venv venv
```

> 가상환경 이름은 "venv"로 통일합니다.

### 3. 가상환경을 활성화 시켜줍니다.

```bash
$ source venv/scripts/activate # for windows
$ source venv/bin/activate # for mac or linux
```

### 4. 프로젝트에 필요한 패키지를 다운 받습니다.

아래의 명령어를 터미널에 입력해주세요. (필수)

```bash
$ pip install -r requirements.txt # for Windows
$ pip3 install -r requirements.txt # for Mac/Linux
```

> 프로젝트에 필요한 패키지 파일을 새롭게 추가하고자 한다면 아래의 명령어를 입력해주세요. (선택사항)

```bash
$ pip freeze > requirements.txt
```

:octocat: Git command
---

```bash
$ git pull origin <branch_name>
$ git add .
$ git commit -m "messages"
$ git push origin <branch_name>
```

> <branch_name>에는 'main' 또는 다른 브랜치 이름을 입력해주세요.

🧐 What's inside?
---
    .
    ├── base
    ├── config
    ├── follow
    ├── post
    ├── singup
    ├── user
    ├── .gitignore
    ├── manage.py
    ├── README.md
    └── requirements.txt

1. `/base`: main 페이지 및 공통 컴포넌트(헤더, 푸터)
2. `/config`: 프로젝트 셋업 폴더
3. `/follow`: 팔로우/팔로워 기능
4. `/post`: 게시물 관리
5. `/signup`: 회원가입 관리
6. `/user`: 유저 관리
7. `.gitignore`: git 파일에 저장하지 않을 파일 목록
8. `manage.py`: Django 커맨드 유틸
9. `requirement.txt`: pip 인스톨 패키지 리스트

📝 License
---
This project uses the [MIT License](LICENSE)