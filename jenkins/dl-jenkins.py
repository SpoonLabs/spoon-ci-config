#!/usr/bin/python3
# downloads the config of all Spoon jenkins jobs

import requests
from lxml import etree
import keyring
import os
import glob

login_keyring=keyring.get_keyring() 


doc = requests.get("https://ci.inria.fr/sos/api/xml").text

tree = etree.XML(doc)

jobs = []
for name in tree.xpath('//job/name/text()'):
  url = "https://ci.inria.fr/sos/job/"+name+"/config.xml"
  print(name)
  doc = requests.get(url, auth=requests.auth.HTTPBasicAuth('martin.monperrus@inria.fr', login_keyring.get_password('jenkins', 'martin.monperrus@inria.fr'))).text
  jobs.append("jobs/"+name+".xml")
  with open("jobs/"+name+".xml","w") as e:
    e.write(doc)

for i in glob.glob("jobs/*.xml"):
    if i not in jobs:
        os.system("git rm '"+i+"'")

# getting the list of plugins
plugins = requests.get("https://ci.inria.fr/sos/pluginManager/api/xml?depth=1&xpath=/*/*/shortName|/*/*/version&wrapper=plugins", auth=requests.auth.HTTPBasicAuth('martin.monperrus@inria.fr', login_keyring.get_password('jenkins', 'martin.monperrus@inria.fr'))).text
with open("plugins.xml","w") as e:
    e.write(plugins)

# to restore all plugins, see https://stackoverflow.com/questions/9765728/how-to-install-plugins-in-jenkins-with-the-help-of-jenkins-remote-access-api
