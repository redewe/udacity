
# coding: utf-8

# # Cleaning the Data
# 
# 

# In[5]:


#Declare all libraries
import csv
import codecs
import pprint
import re
import xml.etree.cElementTree as ET
from collections import defaultdict

#File path declaration and open
OSM_PATH = "../data_input_output/singapore.osm"

#Declare regex patterns
lower = re.compile(r'^([a-z]|_)*$') #tags that contain only lowercase letters 
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_|[0-9])*$') #tags that are with lower case and has one colon
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]') #tags with problematic characters

#Custom regex patterns
custom_regex = [
    re.compile(r'^([a-z]|_)*:([a-z]|_)*:([a-z]|_)*$'),#tags that are lower case with two colons
    re.compile(r'^([a-z]|_)*:([a-z]|_)*:([a-z]|_|[0-9])*:([a-z]|_)*$'),  #tags that are lower case with three colons
    re.compile(r'^(W|T)[0-9].*([A-Z]|[0-9])$'), #tags that locate buildings within Singapore's Polytechnic building
    re.compile(r'^ISO[0-9]'), #ISO tags
    re.compile(r'^(currency:|Update_Sta|3dr:|catmp|name:|Max_HDOP|Max_PDOP|GPS_|GNSS_|Easting|Northing|Latitude|Longitude|Feat_Name|Filt_Pos|Unfilt_Pos|Corr_Type|Rcvr_Type|Vert_Prec|Std_Dev|Point_ID|Comment|Horz_Prec|OBJECTID)')
    #roadID tags unique for this particular OSM / tags that capture different names of singapore / GPS/GNSS Tags, UTM and other Geo values
]

#helper function to loop through custom regex
def regex_check(k_attr, keys):
    for index, item in enumerate(custom_regex):
        if item.match(k_attr):
            keys["custom_regex"] = key_value("custom_regex", keys)
            return True


# ###  Analysis on structure
# 
# This part of the code attempts to do a simple analysis on some of the data errors before exporting to SQL. 

# In[2]:


osm_file = open(OSM_PATH, "r", encoding="utf-8")

#function to match key type
def key_type(element, keys):
    if element.tag == "tag":
        if element.findall('[@k]'):
            for tag in element.findall('[@k]'):
                if tag.attrib['k']:
                    if problemchars.match(tag.attrib['k']):
                        keys["problemchars"] = key_value("problemchars", keys)
                    elif lower_colon.match(tag.attrib['k']):
                        keys["lower_colon"] = key_value("lower_colon", keys)
                    elif lower.match(tag.attrib['k']):
                        keys["lower"] = key_value("lower", keys)
                    else:
                        if regex_check(tag.attrib['k'], keys) is not True:
                            keys["other"] = key_value("other", keys) #other tags that do not fall into the other three categories
                            #add value to other_keys list 
                            try:
                                other_keys[tag.attrib['k']] += 1
                            except:
                                other_keys[tag.attrib['k']] = 1
                            
    return keys    

#return 1 if key does not exist in dict
def key_value(type_value, keys):
    try:
        if keys[type_value] >= 1:
            return keys[type_value] + 1
    except:
        return 1

#Loop through tags and count number of unique tags and users and tag types
tags_dict = {}
unique_users = set()
keys = {}
other_keys = {}

for event, elem in ET.iterparse(osm_file):
    keys = key_type(elem, keys)

    if elem.tag in tags_dict.keys():
        tags_dict[elem.tag] += 1
        if elem.findall("[@uid]"):
            unique_users.add(elem.attrib['uid'])
        
    else:
        tags_dict[elem.tag] = 1
        if elem.findall("[@uid]"):
            unique_users.add(elem.attrib['uid'])
        
#Print number of unique users
print("Number of unique users","\n++++++++++++++++++++++++")
print(len(unique_users))
        
        
#Print results ordered by value
print("\n\nNumber of tags per tag type","\n++++++++++++++++++++++++")
s = [(k, tags_dict[k]) for k in sorted(tags_dict, key=tags_dict.get, reverse=True)]
pprint.pprint(s)

#Print possible issuees with k value
print("\n\nNumber of tag key types and other k values ","\n++++++++++++++++++++++++")
s = [(k, keys[k]) for k in sorted(keys, key=keys.get, reverse=True)]
pprint.pprint(s)

print("\n\nOther k values (Unique:",len(other_keys),")","\n++++++++++++++++++++++++")
s = [(k, other_keys[k]) for k in sorted(other_keys, key=other_keys.get, reverse=True)]
pprint.pprint(s)


# ### Clean up Street Names

# In[6]:


#Due to the unique names of streets in Singapore, the road name can be placed in the beginning or at the end so the usual Regex strings will not work
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons", "Jalan", "Lorong", "Way"]

#loop through list to create regex string
expected_re = "r\'("
for index,item in enumerate(expected):
    if index != len(expected)-1:
        expected_re += item
        expected_re += "|"
    else:
        expected_re += item
    
expected_re += ")\'"

street_type_re = re.compile(expected_re,re.IGNORECASE)


mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            "PKWY": "Parkway"
            }

#Code for auditing taken from Case Study
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r", encoding='utf8')
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types

#function to update names based on mapping
def update_name(name, mapping):
    m = street_type_re.search(name).group()
    name = name.replace(m,mapping[m])
    return name

pprint.pprint(dict(audit(OSM_PATH)))

