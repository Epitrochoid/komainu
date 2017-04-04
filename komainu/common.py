from lxml import etree

# TODO: Look at using an interable parse to save memory
def load_xml_file(filename):
    handle = open(filename, 'rb')
    return etree.parse(handle)
