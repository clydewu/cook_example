# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from django.db import transaction

from .models import Member, Point

BULK_AMOUNT = 1000


DEFAULT_DATA = [
    ['user1', '3452198438', 10],
    ['clyde', '0987654321', 10],
    ['user2', '7478349022', 10],
]


@transaction.atomic
def import_point(request):
    data = json.loads(request.POST.get('data', json.dumps(DEFAULT_DATA)))
    new_members = []
    new_points = []
    for item in data:
        name, mobile, point = tuple(item)
        member = Member(mobile=mobile, name=name)
        new_members.append(member)
        new_points.append(Point(member=member, point=point))

    Member.objects.bulk_create(new_members, BULK_AMOUNT)
    Point.objects.bulk_create(new_points, BULK_AMOUNT)

    return HttpResponse('Import OK')
