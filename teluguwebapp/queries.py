from .models import Links
from datetime import datetime,timedelta



def get_links(paper=''):

    now = datetime.now()
    #one week earlier
    print(now)
    mytime = now + timedelta(days=-7)
    mytime = mytime.strftime('%Y-%m-%d %H:%M:%S')
    # print(mytime)

    if paper:
        links = Links.objects(engsource=paper, insertdatetime__gte=mytime).only('title', 'url', 'source', 'mindesc','imagepath').\
                order_by('-insertdate', 'itemid', '-insertdatetime')
    else:
        links = Links.objects(insertdatetime__gte=mytime).only('title', 'url', 'source', 'mindesc', 'imagepath').\
                order_by('-insertdate', 'itemid', '-insertdatetime')
    return links
