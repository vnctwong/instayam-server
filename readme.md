# pipenv

# init django server and django REST framework
  - warnings about dir not on path on installation

# implement psql through django
  - dont worry about this for now, just stick with the sqlite3 db included

# setup users model w/ friend relation
- pie manage?
- REST frmwrk will generate REST routes
- south app for migrations?

## user_model_data
name - str
email - str
password - str
followers - models.ForeignKey
following - models.ForeignKey

## Other stuff
  - plaintext for password for now, will be changed to some hashing algorithm to obfusticate
  - create a POST /login route
    - on successful login pass user a token (encrypted key that identifies user for us)
      - token should be tracked locally as well, maybe in the db or something
      - token should expire after some time?
      - I think django has tokens built in so check documentation
    - on fail redirect or just return a fail response
  - make sure all secrets are not pushed to git
