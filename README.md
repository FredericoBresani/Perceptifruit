# Perceptifruit

## Como rodar o projeto
Primeiro, você precisa compilar as imagens docker utilizadas pelo projeto.
```bash
docker-compose build --no-cache
```
_Esse processo demora alguns minutos._

Agora, você apenas precisa iniciar a rede virtual:
```bash
docker-compose up
```

Para encerrar o projeto, interrompa o projeto com `Ctrl+C` e execute:
```bash
docker-compose down
```

## Utilizando o shell
Para utilizar o interpretador do projeto em uma sessão interativa, você precisa se conectar ao serviço na rede virtual:
```bash
docker-compose exec server /bin/bash
```

No lugar do intepretador pytho, recomendamos usar o shell do django:
```bash
python perceptifruti/manage.py shell
```

## Initial results
Checkout the videos
[![Video Title](https://img.youtube.com/vi/c6KKnYIxAlI/0.jpg)](https://www.youtube.com/watch?v=c6KKnYIxAlI)

[![Video Title](https://img.youtube.com/vi/0Hoh1w_Er9w/0.jpg)](https://www.youtube.com/watch?v=0Hoh1w_Er9w)
