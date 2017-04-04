from lxml import etree

from komainu.common import load_xml_file

def get_entries(cpe_file):
    xml = load_xml_file(cpe_file)
    # Points to all config elements of the cpe document
    element_path = './/{http://cpe.mitre.org/dictionary/2.0}cpe-item[@name]'
    root = xml.getroot()
    return root.iterfind(element_path)
