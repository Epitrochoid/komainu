from komainu.common import load_xml_file

import io
import pytest
import responses
import tempfile

def test_load_xml_file():
    load_xml_file('tests/samples/cpe.xml')

@responses.activate
def test_fetch_gz_file():
    url = 'http://example.com'
    in_filename = 'samples/gz_file.txt.gz'
    out_file = tempfile.NamedTemporaryFile()

    with io.open(filename, 'rb') as f:
        responses.add(
                responses.Response(
                    method='GET',
                    url='http://example.com',
                    body=f
                )
            )

    fetch_fz_file(url, out_file.name)

    out_file.seek(0)
    unzipped_text = out_file.read()

    assert unzipped_text == 'test'
