## URL Shortener

PostMan Collection : [https://www.getpostman.com/collections/7050a69064738965d111](https://www.getpostman.com/collections/7050a69064738965d111)

# API Requests

Shorten URL :

```
curl --location --request POST 'BASE_URL' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name":"Any Random Name",
    "longurl":"Your Long URL"
}'
```
Access the Telegram bot at :
[t.me/ishanurl_bot](t.me/ishanurl_bot)