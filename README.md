# InstaGrabberAPI

Esta é uma API desenvolvida em Python e Flask que permite extrair URLs de mídia (imagens e vídeos) de postagens públicas do Instagram, utilizando as bibliotecas Instaloader e Instagrapi, retornando as informações em JSON.

## Requisitos

- Python 3.7+
- Instalação das bibliotecas listadas em `requirements.txt`

## Uso
1. Inicie a aplicação:
`python3 app.py`


2. Acesse a API utilizando a seguinte URL: `http://localhost:5000/api/linkdopost`, substituindo "linkdopost" pelo link do post ou Reels do Instagram que deseja fazer download.

Por exemplo: `http://localhost:5000/api/https://www.instagram.com/reels/CrdcCySoJSU/`

A resposta será um JSON contendo as URLs das mídias, o nome de usuário e informações sobre a requisição, similar ao exemplo abaixo:

```json
{
  "client": "instaloader",
  "success": true,
  "urls": [
    "https://instagram.fcwb3-1.fna.fbcdn.net/v/t66.30100-16/334677064_3459597640992653_6005328953483360270_n.mp4?_nc_ht=instagram.fcwb3-1.fna.fbcdn.net&_nc_cat=105&_nc_ohc=uKIxlQSwscQAX-HaYE9&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfCP__WbTeRZNLDlW0KJKgovO6ws9vtahasnUQfMwZQTdg&oe=64518A3F&_nc_sid=4f375e"
  ],
  "username": "dvfilmx"
}
```

## Bibliotecas
- Instaloader: https://github.com/instaloader/instaloader
- Instagrapi: https://github.com/adw0rd/instagrapi

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.