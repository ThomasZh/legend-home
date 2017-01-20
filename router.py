# _*_ coding: utf-8_*_
#
# genral application route config:
# simplify the router config by dinamic load class
# by lwz7512
# @2016/05/17

import tornado.web
from foo import comm
from foo.ui import ui_bootstrapmade


def map():

    config = [

        # GET: 根据 HTTP header 收集客户端相关信息：是否手机、操作系统、浏览器等信息。
        (r'/', getattr(ui_bootstrapmade, 'HomeHandler')),

        (r'/bootstrapmade/one-page', getattr(ui_bootstrapmade, 'BootstrapmadeOnePageHandler')),
        (r'/bootstrapmade/butterfly', getattr(ui_bootstrapmade, 'BootstrapmadeButterflyHandler')),
        (r'/bootstrapmade/coming-soon', getattr(ui_bootstrapmade, 'BootstrapmadeComingSoonHandler')),
        (r'/bootstrapmade/delicious', getattr(ui_bootstrapmade, 'BootstrapmadeDeliciousHandler')),
        (r'/bootstrapmade/knight', getattr(ui_bootstrapmade, 'BootstrapmadeKnightHandler')),
        (r'/bootstrapmade/laura', getattr(ui_bootstrapmade, 'BootstrapmadeLauraHandler')),
        (r'/bootstrapmade/medilab', getattr(ui_bootstrapmade, 'BootstrapmadeMedilabHandler')),
        (r'/bootstrapmade/mentor', getattr(ui_bootstrapmade, 'BootstrapmadeMentorHandler')),
        (r'/bootstrapmade/squad', getattr(ui_bootstrapmade, 'BootstrapmadeSquadHandler')),

        # comm
        ('.*', getattr(comm, 'PageNotFoundHandler'))

    ]

    return config
