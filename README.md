# social.sess-back

## Technologies Used:

- Python
- Django
- bcrypt
- WhiteNoise
- cors
- Gunicorn
- PostgresSQL

## User Stories:

- User has ability to view question cards- User can create an account
- User has ability to edit, update, delete question cards after logging into their account
- User can add comments to questions


## Approach Taken:

We wanted to build a backend using PostgresSQL and Django. We started with our basic questions model which contains the question ID and the body of the question. Then we added a user account model and used bcrypt for authentication. Afterwards we wanted the ability to add comments to the questions, so we set up a comments model with a many-to-many relationship to the associated question.

## Current Issues:

- Figuring out the many to many models (SOLVED)

## Links to live site:

- Frontend: https://social-sess-front.herokuapp.com/
- Backend: https://social-sess-back.herokuapp.com/api/questions

## gitHub links:
- Jessica Im: https://github.com/jessica-im
- Yianni Catege: https://github.com/Darkmatter43
- Kevin Trang: https://github.com/ktrng
