# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:54:04 2017

@author: jafema

https://colorlib.com/wp/css3-table-templates/

https://codepen.io/lukepeters/pen/bfFur?editors=0100

https://plot.ly/javascript/time-series/

"""
import os, sys
from jinja2 import Environment, FileSystemLoader
from collections import namedtuple
import csv
#import pandas as pd
#import numpy as np

csv_file = r"AirQualityUCI 2/dataset_min.csv"
l_time=[]
l_CO=[]
l_NMHC=[]

#df = pd.read_csv('/pyhtml/html/AirQualityUCI 2/AirQualityUCI.csv')

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
    dataPieMio = {'javi':33,
                  'eSTC': 15,
                  'casa':20}


    fname = "hex_file_generation_log_report.html"
    urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
    envars = os.environ
    context = {
        'urls': urls,
        'envars': envars,
        'items': items,
        'dataPieMio': dataPieMio,
        'l_time': l_time,
        'l_CO':l_CO,
        'l_NMHC':l_NMHC
    }
    #
    with open(fname, 'w') as f:
        html = render_template('mytemplate.html', context)
        f.write(html)

def get_data_from_csv():
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile,delimiter=';')

        for row in reader:
            l_time.append(row['Time'])
            l_CO.append(row['CO(GT)'])
            l_NMHC.append(row['NMHC(GT)'])
            #print (row['Time'],row['CO(GT)'])
            #print l_CO
   

def main():
    get_data_from_csv()
    create_index_html()


 
########################################
 
if __name__ == "__main__":
    main()

print "END..."