# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:54:04 2017

@author: jafema

https://colorlib.com/wp/css3-table-templates/

https://codepen.io/lukepeters/pen/bfFur?editors=0100


"""
import os, sys
from jinja2 import Environment, FileSystemLoader
from collections import namedtuple

data = namedtuple('data','date id')

PATH = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


def create_index_html():
     
    items=[data('16-06-2017','85')]
    items.append(data('17-06-2017','95'))
    items.append(data('18-06-2017','105'))
    fname = "hex_file_generation_log_report.html"
    urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
    envars = os.environ
    context = {
        'urls': urls,
        'envars': envars,
        'items': items
    }
    #
    with open(fname, 'w') as f:
        html = render_template('mytemplate.html', context)
        f.write(html)


    

def main():
    create_index_html()
 
########################################
 
if __name__ == "__main__":
    main()

print "END..."