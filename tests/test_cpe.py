from komainu.cpe import load_entries_from_file, get_config, make_get_nvdid
from komainu.common import load_xml_file

def test_load_entries():
    load_entries_from_file('tests/samples/cpe.xml')


def test_get_nvdid_for_name():
    root, configs = load_entries_from_file('tests/samples/cpe.xml')
    get_nvdid = make_get_nvdid(root)
    found = False

    for element in configs:
        if get_config(element) == "cpe:/a:1024cms:1024_cms:0.7":
            assert get_nvdid(element) == "121218"
            found = True
            break

    if not found:
        raise Exception('Expected entry not found in test file')
