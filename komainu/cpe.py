# Copyright 2017 Mabry Cervin and all contributers listed in AUTHORS 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from lxml import etree

from komainu.common import load_xml_file

def load_entries_from_file(cpe_file):
    xml = load_xml_file(cpe_file)
    root = xml.getroot()
    namespace = root.nsmap[None]
    # Points to all config elements of the cpe document
    element_path = './/{{{0}}}cpe-item[@name]'.format(namespace)
    return root, root.iterfind(element_path)


def get_config(cpe_entry):
    return cpe_entry.get('name')


def make_get_nvdid(root):
    meta = root.nsmap['meta']
    def get_nvdid(cpe_entry):
        return cpe_entry.find('.//{{{0}}}item-metadata'.format(meta)).get('nvd-id')
    return get_nvdid
