#!/usr/bin/python3
# downloads the config of all Spoon jenkins jobs

import requests
from lxml import etree
import keyring
login_keyring=keyring.get_keyring() 


doc = requests.get("https://ci.inria.fr/sos/api/xml").text

tree = etree.XML(doc)

for name in tree.xpath('//job/name/text()'):
  url = "https://ci.inria.fr/sos/job/"+name+"/config.xml"
  print(name)
  doc = requests.get(url, auth=requests.auth.HTTPBasicAuth('martin.monperrus@inria.fr', login_keyring.get_password('jenkins', 'martin.monperrus@inria.fr'))).text
  with open("config/"+name+".xml","w") as e:
    e.write(doc)

