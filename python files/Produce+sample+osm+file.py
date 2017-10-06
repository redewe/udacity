
# coding: utf-8

# In[5]:


#Obtain sample to help with cleaning
import xml.etree.ElementTree as ET  # Use cElementTree or lxml if too slow
import base64

OSM_FILE = "../data_input_output/singapore.osm"  
SAMPLE_FILE = "../data_input_output/sample.osm"

k = 45 # Parameter: take every k-th top level element

def get_element(osm_file):
    context = iter(ET.iterparse(osm_file, events=('start', 'end')))
    _, root = next(context)
    for event, elem in context:
        if event == 'end':
            yield elem
            root.clear()


with open(SAMPLE_FILE, 'wb') as output:
    output_str='<?xml version="1.0" encoding="UTF-8"?>\n'
    output_str += '<osm>\n'
    
    output.write(output_str.encode('utf-8'))
    
    # Write every kth top level element
    for i, element in enumerate(get_element(OSM_FILE)):
        if i % k == 0:
            output.write(ET.tostring(element))#, encoding='utf-8'))
    
    output_str='</osm>'
    output.write(output_str.encode('utf-8'))

