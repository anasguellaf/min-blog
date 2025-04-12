from peewee import *
from datetime import  datetime



db = SqliteDatabase("blog.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    # Fields | Column | Champ
    username = CharField(unique=True)

        

class Post(BaseModel):
    title = CharField()
    content = TextField()
    created_at = DateTimeField(formats="%Y-%m-%d %H:%M:%S", default=datetime.now)
    user = ForeignKeyField(model=User, backref='posts')



if __name__ == '__main__':
    # db.connect()
    # db.create_tables([User, Post])

    # Ajouter un nouvel utilisateur.
    # new_user = User.create(username='ilyas2025')
    # Ajouter un post lié à un utilisateur.
    #abdo = User.get(User.username=='abdo007')
    #new_post = Post.create(title='how to win friends in 20 minutes', content = 'a simple blog showing you how to get more friends in 20 minutes by Abdelali ', user=abdo)
    
    new_user = User.create(username='aydoune')
    new_game_post = Post.create(
        title = 'new  aydoune post blog',
        content = 'to be created later ...',
        user = new_user,
    )
    
    