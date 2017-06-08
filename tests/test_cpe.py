from komainu.cpe import check_for_cve, load_entries_from_file, get_config, make_get_nvdid
from komainu.common import load_xml_file

def test_load_entries():
    load_entries_from_file('tests/samples/cpe.xml')


def test_get_nvdid_for_name():
    root, configs = load_entries_from_file('tests/samples/cpe.xml')
    get_nvdid = make_get_nvdid(root)
    found = False

    for element in configs:
        if get_config(element) == 'cpe:/a:python:pillow:2.2.2':
            assert get_nvdid(element) == "266775"
            found = True
            break

    if not found:
        raise Exception('Expected entry not found in test file')

def test_check_for_cve():
    config = 'cpe:/a:python:pillow:2.2.2'
    name = 'pillow'
    correct_vers = '2.2.2'
    wrong_vers = '2.2.1'

    assert check_for_cve(config, name, correct_vers)
    assert not check_for_cve(config, name, wrong_vers)
