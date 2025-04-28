## Структура:

```text
├── api/
│   ├── __init__.py
│   ├── clash.py
│   └── sheets.py
│
├── config/
│   ├── __init__.py
│   ├── bot.py
│   ├── logger.py
│   ├── sheets.json  # YOUR CREDENTIALS
│   └── sheets.py
│
├── handlers/
│   ├── __init__.py
│   ├── account.py
│   ├── poll.py
│   └── core/
│       ├── __init__.py
│       ├── account_processor.py
│       ├── base.py
│       ├── message_processor.py
│       ├── poll_processor.py
│       └── users.py
│
├── .env
├── .gitignore
├── commands.py
├── main.py
├── readme.md
└── requirements.txt
```

## Встановлення:

В проєкті застосовуються наступні інтеграції: Telegram, Google Cloud, Google Sheets, Clash of Clans API. Тому потрібно попередньо налаштувати усі сервіси.

### Google Cloud:

* Переходимо на сайт <b>[Google Cloud](https://console.cloud.google.com/)</b>.
* API & Services. 
* Створюємо проєкт (зліва зверху, біля Google Cloud). 
* Додаємо бібліотеки (Library): Google Sheets API, Google Drive API. 
* Повертаємось в API & Services, переходимо в Credentials і там: Create Credentials --> Service account --> Заповнюємо дані. 
* Переходимо у створений сервісний аккаунт (нижче у списку) --> Зберігаємо E-mail --> Keys -> Add key --> Create new key. Зберігаємо у JSON, в будь-яку папку (можна в папку проєкта). 
* Створюємо таблицю в Google Sheets --> Налаштування доступу --> Додаємо E-mail сервісного аккаунту.

### Clash of Clans API

* Переходимо на сайт <b>[Clash of Clans for developers](https://developer.clashofclans.com/)</b>.
* Створюємо аккаунт на офіційному сайті.
* Переходимо в особистий аккаунт.
* Створюємо новий ключ із поточною публічною адресою.

### Налаштування проєкту:

* Завантажуємо проєкт:
```bash
git clone https://github.com/sergiok21/ternopil_telegram_bot.git
```
* Створюємо віртуальне середовище в папці з проєктом:
```bash
python -m venv venv
```
* Застосування у Windows:
```bash
./venv/Scripts/activate
```
для Unix-подібних:
```bash
source ./venv/bin/activate
```
* Завантажуємо залежності:
```bash
pip install -r requirements.txt
```
* <i>Додатково, якщо використовується PyCharm IDE: Налаштування --> Проєкт --> Python Interpreter --> Add Interpreter (local)...</i>
* Створюємо `.env`-файл в корені проєкту, та підставляємо свої дані:
```
BOT_TOKEN=...
CLASH_TOKEN=...
GROUP_ID=...
ADMINS=...
SHEET_CREDENTIALS=...
SHEET_URL=...
```
**Пояснення деяких полів `.env`:**\
`GROUP_ID` - можна отримати через бота.\
`ADMINS` - може записуватись через `123, 456`, цим самим адміністратором може бути не один користувач.\
`SHEET_CREDENTIALS` - повний шлях `.json`-файлу з Google Cloud.
`SHEET_URL` - посилання на таблицю (https://docs.google.com/spreadsheets/d/1ZX....23F/).
