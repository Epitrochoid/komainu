from komainu.common import load_xml_file

import pytest

def test_load_xml_file():
    load_xml_file('tests/samples/cpe.xml')
