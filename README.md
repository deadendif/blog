# blog
Blog system based on Django framework.

+ Based on Django framework, implemented the functions of editing, publishing, searching, filing, labeling, statistics, sending email, website crawler, etc.
+ Based on Thrift RPC framework, implemented the decoupling of email-sending function.
+ Used Redis to cache data and distributed task queue—Celery to deal with asynchronous email-sending tasks.

## Screenshot
#### [My Blog Site](https://deadend.me)
[![](https://deadend.me/media/images/2017/07/29/44e452f8-781e-4f4d-9e93-6199d57d9ed0.png)](https://deadend.me)

## Technology
#### Frontend
+ [Semantic UI Framework](https://semantic-ui.com/)
#### Backend
+ [Django Framework](https://www.djangoproject.com/)
+ [Redis](https://redis.io/)
+ [Celery](http://www.celeryproject.org/)
+ [Apache Thrift](https://thrift.apache.org/)
#### Deployment
+ uWSGI
+ Nginx

## TODO
+ Remove hardcode in navigation bar

## Related Project
+ [notifier](https://github.com/deadEnding/notifier)
