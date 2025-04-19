from peewee import *
from datetime import  datetime



db = SqliteDatabase("blog.db")


class BaseModel(Model):
    class Meta:
        database = db
        
        
class Category(BaseModel):
    name = CharField(unique=True)
    date_added = DateField(formats="%Y-%m-%d", default=datetime.now)
        
class User(BaseModel):

    # Fields | Column | Champ
    username = CharField(unique=True)
    age = IntegerField()
    country = CharField()
    join_date = DateTimeField(formats="%Y-%m-%d %H:%M:%S", default=datetime.now)    
    
        
class Comment(BaseModel):
    content = CharField(max_length=255,null = False)
    created_at = DateField(formats="%Y-%m-%d", default=datetime.now)
    is_published = BooleanField(default=False)
    user = ForeignKeyField(model=User, backref="comments")

        

class Post(BaseModel):
    title = CharField()
    content = TextField()
    created_at = DateTimeField(formats="%Y-%m-%d %H:%M:%S", default=datetime.now)
    user = ForeignKeyField(model=User, backref='posts')
    category = ForeignKeyField(model=Category, backref="posts")



if __name__ == '__main__':
    #db.connect()
    #db.create_tables([User, Comment, Category, Post])
    
    # get the user
    ninja = User.get(User.username == "ninja4games")
    
    # get the category
    cat_ai = Category.get(Category.name == 'ai' )
    
    
    new_blog = Post.create(
        title = "How Python is Powering the Future of Artificial Intelligence",
        content = "Artificial Intelligence (AI) is one of the most exciting and fast-growing fields in technology today. From self-driving cars to virtual assistants like Siri and Alexa, AI is changing the way we live and work. At the heart of many of these innovations is a powerful and easy-to-learn programming language: Python.Python has become the go-to language for AI development, and it’s not hard to see why. First, Python is known for its simple and clean syntax. This makes it easy for beginners to learn and also allows experienced developers to write code faster. Unlike other programming languages that can be complex and hard to understand, Python reads more like English. This is especially helpful when working with complicated AI algorithms.",
        user = ninja,
        category = cat_ai,
    )
    
    