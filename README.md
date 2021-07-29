# Customized

## initial python3 enviroment
```gherkin=
pip3 install -r ./customized/module/requirements.txt
```

## run server
```gherkin=
python3 ./customized/module/server.py  
```

## run server with docker 
```gherkin=
./customized/docker/run.sh 1
```

## ACCESS_TOKEN
```
{"105566678410846":"EAAk4H5wUh88BAOpXY9vN56Sc11hFtNCZCVyWQkvijsDzcPaUZCuZCKYCrbfVZCUZCS4PfEZArJLhNHUrUf0ZCUulB5DnABqzBVdkVVGEosfNcV5lAlD6tmLdkZC273Ihd06qHQSO30vPV0AWdZCuyz8cqgqGrtiQSyrGhOEr8ytdCjmWbD6IjJFc5"}

# Emotibot
{"100903557951068":"EAAGJwZCK6hFUBANZCXTgn9pc6YnvBZBwKFGYHUjVEop2ZBT1CDBpg40G6WDyt8nIjiUe2nKZCr3fZBVAi29QoDL6SeZCDtOoGQXjb4hoTsf0sp1MZCZBOWjXVw420V7QSEUGFlF2ZCTFIvVD3aeapAkiSCmnz7HJGRHLuLMSwrIiTmS90RgCqSSi4V"}

{"108433087175265":"EAAFNM3mDiKcBALN4xxTQ9exRJnFc8SZB3aGg51b9kL6Pqbw5TY56Fv8i9ZBL6kEkk5xBikNRBtkZAq7YdRb5ZAheFWlf8ipB3ZByVyONx7D8N7uAmGdmkSAGrCGZBLx8zyy4hBzdV43xU1WjT9fvl0dZB3UZC1xZCyJtq7adCZAw4Ha4b79X8gQ1d4"}
```

## Manual setting greeting
``` 
curl -X POST -H "Content-Type: application/json" -d '{
  "greeting": [
    {
      "locale":"default",
      "text":"悠遊卡-EasyCard" 
    }
  ]
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=${token}"
```

## Manual setting get_started
```
curl -X POST -H "Content-Type: application/json" -d '{
  "get_started": {"payload": "GET_START"}
}' "https://graph.facebook.com/v2.6/me/messenger_profile?access_token=${token}"
```
  
> https://ithelp.ithome.com.tw/articles/10220214
