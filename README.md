# Aseland

## Introduction
Asexuality, sometimes considered a lack of sexual orientation, is a low/absent desire for sexual activity and a lack of sexual attraction to anyone.

Aseland is a dating app to help the asextual population in China to look for romantic non-sexual partnership.

V1 includes the following functions

## Goal

#### This project: 

The API for

- Users
	- signup
	- login
	- reset password
- Search
	- filter by condition 
	- view user list
	- view user detail
- Friend
	- save someone
	- block someone
	- know who saved me
- Article
	- post new article
	- like other's article	 
	- make comments
	- like other's comment

####Future work:

- Friend system
- Chat

## Architecture
### Frontend
React (Out of the scope of this project)
### Backend
Django REST framework
(prefix = api/v1/)

#### Users/Search

- **[POST] /authentication/login** login
- **[GET] /users** get users, can have condition in params
- **[POST] /users** create new user
- **[GET] /users/{pk}** get UserDeatil
- **[PUT] /users/{pk}** update UserDetail
- ??how to reset password

#### Friend
- **[POST] /users/{pk}/favolist/{pk}** save a user
- **[GET] /users/{pk}/favolist** get the list of saved users
- **[POST] /users/{pk}/blacklist/{pk}** blacklist a user
- **[GET] /users/{pk}/blacklist** get the blacklist of a user
- **[GET] /users/{pk}/loves** get list of users who saved me

#### Articles
- **[GET] /articles** get article list
- **[GET] /articles/{user_pk}** get articles of a user
- **[POST] /articles** create new article
- **[GET] /articles/{pk}** get an article
- **[PUT] /article/{pk}** update an article

#### Comments
- **[GET] articles/{articleid}/comments/** get all comments for an article
- **[POST] articles/{articleid}/comments/** create new comment for an article
- **[GET] articles/{articleid}/comments/{commentid}** get all comments for an article
- **[PUT] articles/{articleid}/comments/{commentid}** update a comment for an article

### Database 
![Postgresql](https://github.com/Jianyi-Ren/Aseland/blob/master/doc/Aseland%20UML.png)


## Roadmap & Milestones

Deadline  | Keyword | Expected Deliverible | Results
--------- | ------  | ------- | ----
4.14  | set up | setup enviroment, establish design docs|
4.21  | User | **User** APIs - Can Signup, login, logout |
4.28  | Friend | **Friend** APIs|
5.12  | Search | **[GET] /users** with condition - User List View, User Detail View|
5.19  | Article | **Articles** APIs|
5.26  |  Comment |**Comments** APIs|
5.31  | Deployment | (load test?) demo|
