# BACKEND


## Curl to test APIs

Accessing CRUD functionality via CURL for Users (and authentication) and Articles

**Note :**
* -d = --data `# for passing data`
* -H = --header `# for Auth Token`

## USERS

### USER.CREATE
```sh
curl -X POST "localhost:8000/auth/users/" -d "username=...&password=...&email=..."
>> {"email": ..., "username": ...}
```
exemple:
```sh
curl -X POST "localhost:8000/auth/users/" -d "username=Alice&password=Apples123&email=alice@gmail.com"
>> {"email": "alice@gmail.com", "username": "Alice"}
```

### USER Login
```sh
curl -X POST "localhost:8000/auth/token/login/" -d "username=...&password=..."
>> {"auth_token":"..."}
```
example
```sh
curl -X POST "localhost:8000/auth/token/login/" -d "username=Alice&password=Apples123"
>> {"auth_token":"60c8bda1146d5703aa835e3c976426acfe91b8cf"}
```

### USER.GET

Get the infos of the authenticated user
```sh
curl -X GET "localhost:8000/auth/users/" -H "Authorization: Token ..."
>> {"id": ..., "username": ..., "email": ...}
```
example
```sh
curl -X GET "localhost:8000/auth/users/" -H "Authorization: Token 60c8bda1146d5703aa835e3c976426acfe91b8cf"
>> {"id": 5, "username": ..., "email": ...}
```

## ARTICLES

### ARTICLE.CREATE
```sh
curl -X POST "localhost:8000/api/articles/" -H "Authorization: Token ..." -d "titre=...&description=...&full_text=...&author=..."
>> {"id": ..., "titre": ..., "description": ..., "full_text": ..., "author": ...}
```
**Note :**  "author" = author_id -> user's ID

example
```sh
curl -X POST "localhost:8000/api/articles/" -H "Authorization: Token 60c8bda1146d5703aa835e3c976426acfe91b8cf" -d "titre=Mon%20Titre&description=Some%20long%20text&full_text=full%20text&author=1"
>> {
  "id": ...,
  "titre": "Mon Titre",
  "description": "Some long text",
  "full_text": "full text",
  "author": 1
}
```

### ARTICLE.READ (ALL)
```sh
curl -X GET "localhost:8000/api/articles/" -H "Authorization: Token ..."
>> [
      {"id":1, "titre": ..., ...},
      {"id":2, "titre": ..., ...},
      ...
]
```
example
```sh
curl -X GET "localhost:8000/api/articles/" -H "Authorization: Token 60c8bda1146d5703aa835e3c976426acfe91b8cf"
>> [
      {"id":1, "titre": ..., ...},
      {"id":2, "titre": ..., ...},
      ...
]
```

### ARTICLE.READ (ONE)
```sh
curl -X GET "localhost:8000/api/articles/{id}/" -H "Authorization: Token ..."
>> {"id": ..., "titre": ..., ...}
```
example
```sh
curl -X GET "localhost:8000/api/articles/1/" -H "Authorization: Token 60c8bda1146d5703aa835e3c976426acfe91b8cf"
>> {"id": 1, "titre": ..., ...}
```


### ARTICLE.UPDATE : Quick Notes - Patch vs Put
`PATCH` provides a set of instructions to modify the original resource whereas `PUT` supplies a modified version of the original resource

So in short:
`PATCH` -> one or more values from `RESOURCE`
`PUT` -> Modifies all values from `RESOURCE`

i.e:

* PATCH
```sh
curl -X PATCH ".../api/articles/{id}/" -d "field=new_value"
>> {"id": id, ..., "field": new_value}
```

* PUT
```sh
# ERROR: as if it was a PATCH request
curl -X PUT ".../api/articles/{id}/" -d "titre=new_value"
>> {
    "description":["This field is required."],
    "full_text":["This field is required."],
    "author":["This field is required."],
}
# CORRECT: Supply ALL fields from the RESOURCE you want to update
curl -X PUT ".../api/articles/{id}/" -d "titre={new_titre}&description=...&full_text=...&author=..."
>> {"id": id, ..., "titre": new_titre, "full_text": ..., "author": ...}
```


### ARTICLE.UPDATE (PATCH)


To modify just the titre:
```sh
curl -X PATCH "localhost:8000/api/articles/{id}/" -H "Authorization: Token ..." -d "titre=..."
>> {"id": ..., "titre": ..., "description": ..., "full_text": ..., "author": ...}
```

example
```sh
curl -X PATCH "localhost:8000/api/articles/1/" -H "Authorization: Token 60c8bda1146d5703aa835e3c976426acfe91b8cf" -d "titre=Updated%20Title"
>> {
  "id": 1,
  "titre": "Updated Title",
  "description": "...",
  "full_text": "...",
  "author": ...,
}
```

### ARTICLE.UPDATE (PUT)


To modify just the titre:
```sh
curl -X PUT "localhost:8000/api/articles/{id}/" -H "Authorization: Token ..." -d "titre={new_titre}&description=...&full_text=...&author=..."
>> {"id": ..., "titre": new_titre, "description": ..., "full_text": ..., "author": ...}
```

example
```sh
curl -X PUT "localhost:8000/api/articles/1/" -H "Authorization: Token 60c8bda1146d5703aa835e3c976426acfe91b8cf" -d "titre=Updated%20Title"
>> {
  "id": 1,
  "titre": "Updated Title",
  "description": "...",
  "full_text": "...",
  "author": ...,
}
```

### ARTICLE.DELETE

Delete by ID
```sh
curl -X DELETE "localhost:8000/api/articles/{id}/" -H "Authorization: Token ..."
>>
# For testing purpose:
curl -X GET "localhost:8000/api/articles/{id}/" -H "Authorization: Token ..."
>> {"detail": "Not found."}
```

example
```sh
curl -X DELETE "localhost:8000/api/articles/1/" -H "Authorization: Token 60c8bda1146d5703aa835e3c976426acfe91b8cf"
>>
# For testing purpose:
curl -X GET "localhost:8000/api/articles/1/" -H "Authorization: Token 60c8bda1146d5703aa835e3c976426acfe91b8cf"
>> {"detail": "Not found."}
```
