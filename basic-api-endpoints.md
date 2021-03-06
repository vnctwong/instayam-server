# Basic API Endpoints

## Login endpoint

`POST /login`

Request body:

```javascript
{
  "email": "jerry@example.com",
  "password": "helloworld123"
}
```

Response body:

```javascript
{
  "token": "eyJhbGciOiJI..." // user id field encoded inside
}
```

## Sign up endpoint

`POST /sign-up`

Request body:

```javascript
{
  "email": "newman@example.com",
  "username": "newman123",
  "password": "helloworld123",
  "fullName": "Newman" // not required
}
```

Response body (same as `POST /login`):

```javascript
{
  "token": "eyJhbGciOiJI..." // user id field encoded inside
}
```

## User profile endpoint

`GET /users/kramer123`

Request headers:

```
Authorization: Bearer eyJhbGciOiJI...
```

Response body:

```javascript
{
  "username": "kramer",
  "fullName": "Cosmo Kramer",
  "followers": 3,
  "following": 5,
  "isPrivate": false
}
```

The server should respond to each circumstance:

1. There is no authorization token provided.
2. The authorized user doesn't have permission to view all information.
3. The authorized user has permission to view all information.
4. The authorization token is invalid.
