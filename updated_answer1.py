# -*- coding:utf-8 -*-
# There are fake models, not real models in this project
import Member, Point

BULK_AMOUNT = 1000


def import_points(data):
    """
    !!!NOTE!!!, this function only demonstrate a conception
    """
    member_names = [d[0] for d in data]
    if Member.objects.filter(name__in=member_names).exists():
        raise Exception('Input data has duplicated username')

    new_members = [Member(name=d[0], mobile=d[1]) for d in data]
    new_points = [Point(name=d[0], point=d[2]) for d in data]

    Member.objects.bulk_create(new_members, BULK_AMOUNT)
    Point.objects.bulk_create(new_points, BULK_AMOUNT)
