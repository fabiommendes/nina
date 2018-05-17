from nina  import *


# Settings
settings.TIME_ZONE = 'America/Sao_Paulo'


# Models
class Post(Model):
    author = ref('auth.User')
    title = field(str, max_length=200)
    text = field(str)
    created_date = field(datetime.now)
    published_date = field(datetime)

    def publish(self):
        self.published_date = now()
        self.save()


@route('', template='post-list.html')
def index():
    posts = Post.objects.filter(obj.published_date > now())
    posts.order_by(-obj.created_date)
    return {'posts': posts, 'title': 'My Blog'}


@route('{id}/')
def post_detail(id):
    post = Post.objects.get(id=id)
    return {'post': post, 'title': post.title}