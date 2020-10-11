# coding=utf-8

from sqlalchemy import Column, String
from datetime   import datetime
from .entity    import Entity, Base


class Activitie(Entity, Base):
    __tablename__ = 'activities'

    title       = Column(String)
    name_day    = Column(String)
    hours_sta   = Column(DateTime)
    hours_end   = Column(DateTime)
    detail      = Column(String)

    def __init__(self, title, name_day, hours_sta, hours_end, detail, created_by):
        Entity.__init__(self, created_by)
        self.title      = title
        self.name_day   = name_day
        self.hours_sta  = hours_sta
        self.hours_end  = hours_end
        self.detail     = detail
