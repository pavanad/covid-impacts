
# COVID-19 Impacts Bot

## MacOS

```bash
export PATH=$PATH:/usr/local/mysql-8.0.17-macos10.14-x86_64/bin
cp -r /usr/local/mysql/lib /usr/local/lib
pip install -r requirements.txt
```

## Docker

```bash
sudo docker build -t covid_bot .
sudo docker run --restart=always covid_bot
```
