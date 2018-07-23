# django-code-challenge


# Requirements
- Python > 3.6.0
- [Python requirements](requirements.txt)

# CREATE USER ACCOUNT

```
`post`
{
    "first_name":"",
    "last_name":"",
    "username":"",
    "email":"",
    "password":"",
}

to `/user`

```

# LOGIN TO OBTAIN TOKEN

```
`post`
{

    "username":"",
    "password":"",
}

to `/login`

```

# Use token to access other parts of the API 