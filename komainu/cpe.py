from lxml import etree

from komainu.common import load_xml_file

def load_entries_from_file(cpe_file):
    xml = load_xml_file(cpe_file)
    # Points to all config elements of the cpe document
    element_path = './/{http://cpe.mitre.org/dictionary/2.0}cpe-item[@name]'
    root = xml.getroot()
    return root, root.iterfind(element_path)

def get_config(cpe_entry):
    return cpe_entry.get('name')

def get_nvdid(cpe_entry):
    return cpe_entry.find('.//{http://scap.nist.gov/schema/cpe-dictionary-metadata/0.2}item-metadata').get('nvd-id')
