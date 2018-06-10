from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Art,Tag



def DetailHandler(request):

    article_id = request.GET.get('id', None)
    if article_id == None:
        return HttpResponseRedirect('/app/index.html')
    else:
        art = Art.objects.get(id = int(article_id))


        # import redis
        # r = redis.Redis()
        # visit = 'a'+str(article_id)
        # res = r.get(visit)
        # if res == None:
        #     r.set(visit,0)
        # r.incr(visit)
        # time_visit = r.get(visit)




        context = {'art':art,
                   # 'time_visit':time_visit
                   }
        return render(request, 'home/detail.html', context = context)

