#!/usr/bin/python3

# Converted Jupyter markdowns
from os import listdir
from os import system

files = listdir().copy()

if 'lessons' not in files:
    print('lessons folder not found ... creating lessons folder')
    cmd = 'mkdir lessons'
    system(cmd)
    print('lessons folder made.\n--')
else:
    print('lessons folder found.\n--')


notes = list(filter(lambda x : x.endswith('.md'), files))

frontMatter = '''---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

'''

for file in notes:
    print('Currently reading:', file)
    title = ''.join([x.lower() for x in file.split(' ')])
    data = None

    with open(file, 'r') as current_file:
        data = current_file.read()

    path = './lessons/' + title
    print('Writing to:', path)
    with open(path, 'w') as new_file:
        new_file.write(frontMatter)
        new_file.write(data)
