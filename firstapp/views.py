import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page was visited')
    return render(request, 'firstapp/index.html', {'title': 'Index'})


def about(request):
    logger.info('About page was visited')
    html = '''
           <h1>многострочный текст с HTML-вёрсткой и данными обо мне</h1>
           '''
    return HttpResponse(html)
