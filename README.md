# Online Quiz App in Django

This is an online quiz organizing website project, developed using Python's web framework Django.<br>
For front-end designing we have used Twitter's front-end library Bootstrap4.

### Current Features

**Site access features:**


* Every quiz can be accessed only if the user is logged in.
* In the signing-up process the user is required to give the following information
	1. Full Name
	2. Email-id (unique for every user)
	3. Mobile Number (unique for every user)
	4. Roll No.
	5. Password
* For login the user will be required to enter *Email-id* and *Password* only

**Features of each quiz:**

* The logged in user either can create his own quiz or take an existing quiz.
* For creating the quiz, the user will be required to enter the *Title* of the quiz and questions and their corresponding options.
* Or the user can take the existing quiz.
* There will be timer of each quiz and the user is required to finish the quiz in time.
* When the timer stops, the corresponding record (i.e. number of correct answers) will be saved automatically.


**Dashboard features:**

* There are two type of dashboard
	1. Dashboard of corresponding user
	2. Global dashboard (i.e. Leaderboard)
* In the *Dashboard of corresponding user* the user can see his attempted quiz statistics <br>(i.e. *No. of Correct answers*, *Marks obtained* )
* In the *Global dashboard* there will be overall ranking of users who have attended the corresponding quiz.


### Getting started with development
Dependenciies:
- Python 3.6.x
- Django 1.11.x
- MySQL 5.7.x
- Ubuntu 17.04 or later

#### 1. Clone this repoistory
```bash
git clone git@github.com:neeraj1909/quiz.git
cd quiz
```

#### 2. Install the [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/)
Follow [instructions on official documentation page](https://virtualenvwrapper.readthedocs.io/en/latest/install.html).

#### 3. Create the virtualenv
```bash
## run following command from `quiz` directory
mkvirtualenv quiz -a "$(pwd)" -p python3.6
```

#### 4. Install python packages
```bash
## Activate the virtualenv which you created on the last step
workon quiz
pip install -r requirements.txt
```

#### 5. Setup the database
*TODO - Add instructions for this when we start using MySQL database.*

#### 6. Run database migrations
```bash
python manage.py migrate
```

#### 8. Run development server
```bash
python manage.py runserver
```

*TODO - Implementation of timer for the quiz still have to be done.*

### Contribute
----------
- Issue Tracker: [Issues](https://github.com/neeraj1909/quiz/issues)
- Source Code: [Here](https://github.com/neeraj1909/quiz/)

### Contributors
----------

* [Neeraj Singh](https://github.com/neeraj1909)


### Support
----------
* If you are having issues, please let us know.<gr>
We have a mailing list located at: bietquiz@gmail.com

### License
----------
MIT License

Copyright (c) 2018 Neeraj Kumar Singh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
