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
    
    new_categories = [
        'law',
        'economics',
        'coding',
        'web',
        'hacking',
        'touristics',
        'nature',
        'education',
        'marketing',
        'banking'
    ]
    
    for cat in new_categories: # loop
        Category.create(
        name = cat
    )
    
    
    