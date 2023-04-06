#!/usr/bin/env python
# -*- coding: utf-8 -*-
import googletrans

trn = googletrans.Translator()
tr = [trn.translate(text="Привет!", dest='english', src='ru')]


print(tr)