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
