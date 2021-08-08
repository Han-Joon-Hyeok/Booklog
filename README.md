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

> If additional packages are installed, the following commands should be executed.

:octocat: Git command
---

```bash
$ git pull origin <branch_name>
$ git add .
$ git commit -m "messages"
$ git push origin <branch_name>
```

> Insert 'backend' or 'frontend' instead of <branch_name>.

🧐 What's inside?
---
    .
    ├── .config
    ├── account
    ├── config
    ├── page
    ├── .gitignore
    ├── manage.py
    ├── README.md
    └── requirements.txt

1. `/.config`: setup files to deploy
2. `/account`: account app
3. `/config`: setup files in project
4. `/page`: page app
5. `.gitignore`: define what should be ignored in git
6. `manage.py`: django command-line util
7. `requirement.txt`: list of pip-packages to install

📝 License
---
This project uses the [MIT License](LICENSE)