#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import *

db.connect()
db.create_tables([User, Plan])

User.create(gid="118255980204068482103", name="Sebastian Schulz", nick="schulz.siwy", avatar="https://lh4.googleusercontent.com/-jY-Zpp_vTw8/AAAAAAAAAAI/AAAAAAAAAHY/BipyDpdobRg/photo.jpg")
User.create(gid="118255980204068482104", name="Jan Kowalski", nick="jan.kowalski", avatar="https://lh4.googleusercontent.com/-jY-Zpp_vTw8/AAAAAAAAAAI/AAAAAAAAAHY/BipyDpdobRg/photo.jpg")
Plan.create(name="Malaysia", nick="schulz.siwy", start="03-06-2016", final="05-07-2016")
Plan.create(name="Morocco", nick="schulz.siwy", start="07-09-2014", final="18-09-2014")
Plan.create(name="Iran", nick="schulz.siwy", start="11-08-2015", final="01-09-2015")
Plan.create(name="Radom", nick="jan.kowalski", start="12-12-2015", final="21-12-2015")

