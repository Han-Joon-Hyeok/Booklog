BOOKLOG
===

π Introduction
---

λ©μμ΄μ¬μμ²λΌ 9κΈ° ν΄μ»€ν€ : λΆλ‘κ·Έ

π μ€μΉ μλ΄
---

### 1. git clone

μνλ ν΄λμ λ ν¬μ§ν λ¦¬λ₯Ό ν΄λ‘ ν΄μ£ΌμΈμ.

```bash
$ git clone https://github.com/Han-Joon-Hyeok/Booklog.git
```

### 2. κ°μνκ²½ μμ±

Djangoλ₯Ό μ€ννκΈ° μν κ°μνκ²½μ μμ±ν΄μ£ΌμΈμ.

```bash
$ python -m venv venv
```

> κ°μνκ²½ μ΄λ¦μ "venv"λ‘ ν΅μΌν©λλ€.

### 3. κ°μνκ²½μ νμ±ν μμΌμ€λλ€.

```bash
$ source venv/scripts/activate # for windows
$ source venv/bin/activate # for mac or linux
```

### 4. νλ‘μ νΈμ νμν ν¨ν€μ§λ₯Ό λ€μ΄ λ°μ΅λλ€.

μλμ λͺλ Ήμ΄λ₯Ό ν°λ―Έλμ μλ ₯ν΄μ£ΌμΈμ. (νμ)

```bash
$ pip install -r requirements.txt # for Windows
$ pip3 install -r requirements.txt # for Mac/Linux
```

> νλ‘μ νΈμ νμν ν¨ν€μ§ νμΌμ μλ‘­κ² μΆκ°νκ³ μ νλ€λ©΄ μλμ λͺλ Ήμ΄λ₯Ό μλ ₯ν΄μ£ΌμΈμ. (μ νμ¬ν­)

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

> <branch_name>μλ 'main' λλ λ€λ₯Έ λΈλμΉ μ΄λ¦μ μλ ₯ν΄μ£ΌμΈμ.

π§ What's inside?
---
    .
    βββ base
    βββ config
    βββ follow
    βββ post
    βββ singup
    βββ user
    βββ .gitignore
    βββ manage.py
    βββ README.md
    βββ requirements.txt

1. `/base`: main νμ΄μ§ λ° κ³΅ν΅ μ»΄ν¬λνΈ(ν€λ, νΈν°)
2. `/config`: νλ‘μ νΈ μμ ν΄λ
3. `/follow`: νλ‘μ°/νλ‘μ κΈ°λ₯
4. `/post`: κ²μλ¬Ό κ΄λ¦¬
5. `/signup`: νμκ°μ κ΄λ¦¬
6. `/user`: μ μ  κ΄λ¦¬
7. `.gitignore`: git νμΌμ μ μ₯νμ§ μμ νμΌ λͺ©λ‘
8. `manage.py`: Django μ»€λ§¨λ μ νΈ
9. `requirement.txt`: pip μΈμ€ν¨ ν¨ν€μ§ λ¦¬μ€νΈ

π License
---
This project uses the [MIT License](LICENSE)