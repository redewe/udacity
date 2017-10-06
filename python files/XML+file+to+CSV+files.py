
# coding: utf-8

# # Convert Data from XML to CSV
# 
# 
# Here is the full length of code depicting how I've converted the files to CSV with help from the code in the Case Study
# https://classroom.udacity.com/nanodegrees/nd002/parts/860b269a-d0b0-4f0c-8f3d-ab08865d43bf/modules/316820862075461/lessons/5436095827/concepts/54908788190923
# 

# In[1]:


#Declare all libraries
import csv
import codecs
import re
import xml.etree.cElementTree as ET
import os
from operator import itemgetter
from collections import OrderedDict
from collections import defaultdict
import cerberus
import schema

#File path declaration and open
OSM_PATH = "../data_input_output/singapore.osm"

#Declare regex patterns
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]') #tags with problematic characters

SCHEMA = schema.schema

#Node Fields as per schema
NODE_FIELDS = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']

folder= "../data_input_output/"
NODES_PATH = folder + "nodes.csv"
NODE_TAGS_PATH = folder + "nodes_tags.csv"

#Way Fields as per schema
WAY_FIELDS = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']

WAYS_PATH = folder + "ways.csv"
WAY_NODES_PATH = folder + "ways_nodes.csv"
WAY_TAGS_PATH = folder + "ways_tags.csv"


# In[5]:


# ================================================== #
#               Helper Functions                     #  
# ================================================== #


def validate_k(k):
    if problemchars.match(k):
        return False

#Yield element if it is the right type of tag
def get_element(osm_file, tags=('node', 'way', 'relation')):
    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()

#Raise ValidationError if element does not match schema
def validate_element(element, validator, schema=SCHEMA):

    if validator.validate(element, schema) is not True:
        field, errors = next(validator.errors.iteritems())
        message_string = "\nElement of type '{0}' has the following errors:\n{1}"
        error_string = pprint.pformat(errors)
        
        raise Exception(message_string.format(field, error_string))

#Extend csv.DictWriter to handle Unicode input
class UnicodeDictWriter(csv.DictWriter, object):

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow(row)
            
            #{k: (v.encode('utf-8') if isinstance(v, str) else v) for k, v in row.items()}
    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


def list_tags(element, tags, default_tag_type):
    for t in element.iter("tag"):
        tags_sub = {}
        k = t.attrib['k']
        tags_sub['id'] = element.attrib['id']
        tags_sub['value'] = t.attrib['v']
          
        if validate_k(k) is not False:
            if lower_colon.match(k):
                k_colon = k.split(":")
                
                for index, item in enumerate(k_colon):
                    if index == 0:
                        tags_sub['type'] = item
                    elif index == 1:
                        tags_sub['key'] = item
                    else:
                        tags_sub['key'] += ":"+item
           
            else:
                tags_sub['type'] = default_tag_type
                tags_sub['key'] = t.attrib['k']
            tags.append(tags_sub)
        else:
            break
        
    return tags

#Clean and shape node or way XML element to Python dict
def shape_element(element, node_attr_fields=NODE_FIELDS, way_attr_fields=WAY_FIELDS,
                  problem_chars=problemchars, default_tag_type='regular'):
    
    node_attribs = {}
    way_attribs = {}
    way_nodes = []
    tags = []  # Handle secondary tags the same way for both node and way elements
  
    if element.tag == 'node':
        for n in node_attr_fields:
            node_attribs[n] = element.attrib[n]

        if len(element) > 0 and element.find("tag") is not None:
            tags = list_tags(element, tags, default_tag_type)
        return {'node': node_attribs, 'node_tags': tags}

    elif element.tag == 'way':
        for w in way_attr_fields:
            way_attribs[w] = element.attrib[w]
        if len(element) > 0:
            if element.find("tag") is not None:
                tags = list_tags(element, tags, default_tag_type)
            if element.find("nd") is not None:
                 for index, nd in enumerate(element.iter("nd")):
                     wn = {}
                     wn['id'] = way_attribs['id']
                     wn['node_id'] = nd.attrib['ref']
                     wn['position'] = index
                     way_nodes.append(wn)
        
        return {'way': way_attribs, 'way_nodes': way_nodes, 'way_tags': tags}


# In[6]:


# ================================================== #
#               MAIN code                            #  
# ================================================== #    
    
#Iteratively process each XML element and write to csv(s)

with codecs.open(NODES_PATH, 'w', encoding='utf-8') as nodes_file,      codecs.open(NODE_TAGS_PATH, 'w', encoding='utf-8') as nodes_tags_file,      codecs.open(WAYS_PATH, 'w', encoding='utf-8') as ways_file,      codecs.open(WAY_NODES_PATH, 'w', encoding='utf-8') as way_nodes_file,      codecs.open(WAY_TAGS_PATH, 'w', encoding='utf-8') as way_tags_file:

    nodes_writer = UnicodeDictWriter(nodes_file, NODE_FIELDS)
    node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
    ways_writer = UnicodeDictWriter(ways_file, WAY_FIELDS)
    way_nodes_writer = UnicodeDictWriter(way_nodes_file, WAY_NODES_FIELDS)
    way_tags_writer = UnicodeDictWriter(way_tags_file, WAY_TAGS_FIELDS)

    #nodes_writer.writeheader()
    #node_tags_writer.writeheader()
    #ways_writer.writeheader()
    #way_nodes_writer.writeheader()
    #way_tags_writer.writeheader()

    validator = cerberus.Validator()

    for element in get_element(OSM_PATH, tags=('node', 'way')):
        el = shape_element(element)

        if el:
            validate_element(el, validator)

            if element.tag == 'node':
                nodes_writer.writerow(el['node'])
                node_tags_writer.writerows(el['node_tags'])
            elif element.tag == 'way':
                ways_writer.writerow(el['way'])
                way_nodes_writer.writerows(el['way_nodes'])
                way_tags_writer.writerows(el['way_tags'])


