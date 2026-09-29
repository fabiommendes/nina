from nina import *


app = App('blog')
app.settings.TIME_ZONE = 'America/Sao_Paulo'


# Models
class Post(app.Model):
    author = ref('auth.User')
    title = field(str, max_length=200)
    text = field(str)
    created_date = field(datetime.now)
    published_date = field(datetime)

    def publish(self):
        self.published_date = datetime.now()
        self.save()

@query(Post)
def posts(qs):
    posts = qs.filter(obj.published_date > datetime.now())
    return posts.order_by(-obj.created_date)
    


@route('', template='post-list.html')
def index(posts):
    return {'posts': posts, 'title': 'My Blog'}


@route('<model:post>/')
def post_detail(post):
    return {
        'post': post, 
        'title': post.title,
    }