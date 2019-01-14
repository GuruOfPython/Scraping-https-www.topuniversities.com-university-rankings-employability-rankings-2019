#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from lxml import html
import requests
import csv

page_source = open("QS Graduate Employability Rankings 2019 _ Top Universities.html", "r", encoding="utf-8").read()
tree = html.fromstring(page_source)
csv_writer = csv.writer(open("result.csv", "w", encoding="utf-8", newline=""))
header = ["Rank", "Name", "Location", "About", "Link"]
csv_writer.writerow(header)

rows = tree.xpath('//table[@id="qs-rankings"]/tbody/tr')
for i, row in enumerate(rows):
    try:
        rank = row.xpath('.//span[@class="rank "]/text()')[0].strip()
    except:
        rank = ""
    try:
        name = row.xpath('td[@class=" uni"]//a[@class="title"]/text()')[0].strip()
    except:
        name = ""
    try:
        location = row.xpath('td[@class=" country"]/div/text()')[0].strip()
    except:
        location = ""
    try:
        link = row.xpath('td[@class=" uni"]//a[@class="title"]/@href')[0]
    except:
        link = ""

    try:
        r = requests.get(link)
        tree = html.fromstring(r.text)
        about = "\n".join([elm.strip() for elm in tree.xpath('//div[contains(@class,"field-profile")]//text()') if elm.strip()]).strip()
    except:
        about = ""

    result_row = [rank, name, location, about, link]
    csv_writer.writerow(result_row)
    print("[Details] {}".format(result_row))
