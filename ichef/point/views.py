# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.db import transaction

from .models import Member, Point

BULK_AMOUNT = 1000


DEFAULT_DATA = [
    ['clyde', '0987654321', 10]
]


@transaction.atomic
def import_point(request):
    new_members = []
    new_points = []
    for item in DEFAULT_DATA:
        name, mobile, point = tuple(item)
        member = Member(mobile=mobile, name=name)
        new_members.append(member)
        new_points.append(Point(member=member, point=point))

    Member.objects.bulk_create(new_members, BULK_AMOUNT)
    Point.objects.bulk_create(new_points, BULK_AMOUNT)

    return HttpResponse('Import OK')
