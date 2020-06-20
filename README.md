
# COVID-19 Impacts

Analyze the impacts of the COVID-19 pandemic on some Brazilian economic indicators.

## Telegram Bot

### Install requirements

**macOS settings for MySQL**

```bash
export PATH=$PATH:/usr/local/mysql-8.0.17-macos10.14-x86_64/bin
cp -r /usr/local/mysql/lib /usr/local/lib
pip install -r requirements.txt
```

**Python dependencies**

```bash
poetry install

# or with pip
pip install -r requirements.txt
```

### How to use

**Credentials**

Set your telegram token and data connection to MySQL database in the **bot/config/.env** file.

```
DATABASE_HOST=<HOST>
DATABASE_NAME=<NAME>
DATABASE_PORT=<PORT>
DATABASE_USERNAME=<USERNAME>
DATABASE_PASSWORD=<PASSWORD>

TELEGRAM_TOKEN=<TOKEN>
```

**Running with Docker**

```bash
sudo docker build -t covid_bot .
sudo docker run -d --name covid-impacts --restart=always covid_bot
```
