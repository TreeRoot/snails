import os


# default db set
SOURCE_DB = 'localhost'
SOURCE_PORT = 27089
SOURCE_DBNAME = 'main'


# templates
TEMPLATES = os.path.join(os.path.abspath("../"), "snails/templates")
STATICS = os.path.join(os.path.abspath("../"), "snails/statics")


# cookie
cookie_secret = "61oETzKXQAGaYdghdhgfhfhfg"

# login url
login_url = "/login"


if __name__ == "__main__":
    print(os.path.abspath(os.path.dirname("../__file__")))

