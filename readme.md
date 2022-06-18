## URL Shortener

PostMan Collection : [https://www.getpostman.com/collections/7050a69064738965d111](https://www.getpostman.com/collections/7050a69064738965d111)

# API Requests

Shorten URL :

```
curl --location --request POST 'http://127.0.0.1:8000/shorten/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"HappyJS",
    "longurl":"https://www.freecodecamp.org/news/javascript-skills-you-need-for-react-practical-examples/"
}'
```
Token : 5274104125:AAEiy26tisvtonW8eGQLN-7cpay6KBIkZlA
