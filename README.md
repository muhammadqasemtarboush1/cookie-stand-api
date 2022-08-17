# cookie-stand-api

Author: Muhammad Qasem Tarboush

Links and Resources

back-end server url : [API Link](https://cookie-api-1.herokuapp.com/)

Setup
.env requirements (where applicable)

DB PORT: 5432

DATABASE_URL: postgres://username:password@tyke.db.elephantsql.com/db_name

> API:
> https://cookie-api-1.herokuapp.com/
>
>> admin/ : to enter the admin page (superuser is required)
>
>> api/v1/cookie_stand/ : to view the list of cookie stands (authentication required)
>
>> api/v1/cookie_stand/id : to view stand details (if user owner: Will be able to update and delete it)
>
>> api/token/ : to obtain token and refresh token this available for registered users

---

## API visual testing:

> ### No authentication

1. **api/v1/cookie_stand/**
   ![main no auth](imgs/main_no_auth.png)
2. **api/v1/cookie_stand/2**
   ![details](imgs/details_no_auth.png)

> ### With authentication

1. **api/v1/cookie_stand/**
   ![main auth](imgs/main_auth.png)
2. **api/v1/cookie_stand/**
   ![post](imgs/post.png)
3. **api/v1/cookie_stand/2**
   ![details](imgs/details_update.png)
> ### Database
![db](imgs/db_cookies.png)


---
Tests

How do you run tests?
>
> Python manage.py test

Expected results:
![test](imgs/testing.png)
