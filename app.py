from peewee import *
from datetime import  datetime



db = SqliteDatabase("blog.db")


class BaseModel(Model):
    class Meta:
        database = db
        
        
class Category(BaseModel):
    cat_list = [
        ('art', 'ART'),
        ('law', 'LAW'),
        ('beauty', 'BEAUTY'),
        ('ai', 'Artificial Intelegence'),
        ('coding', 'Coding'),
    ]
    
    name = CharField(unique=True, choices = cat_list)
    date_added = DateField(formats="%Y-%m-%d", default=datetime.now)
        
class User(BaseModel):
    
    # Country list
    countries = [
        ('ma', 'Maroc'),
        ('fr', 'France'),
        ('es', 'Espagne'),
    ]
    
    
    # Fields | Column | Champ
    username = CharField(unique=True)
    age = IntegerField()
    country = CharField(choices = countries)
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
    db.connect()
    db.create_tables([User, Comment, Category, Post])

    # Ajouter un nouvel utilisateur.
    # new_user = User.create(username='ilyas2025')
    # Ajouter un post lié à un utilisateur.
    #abdo = User.get(User.username=='abdo007')
    #new_post = Post.create(title='how to win friends in 20 minutes', content = 'a simple blog showing you how to get more friends in 20 minutes by Abdelali ', user=abdo)
    
