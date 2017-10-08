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
import requests
import tempfile

# TODO: Look at using an interable parse to save memory
def load_xml_file(filename):
    handle = open(filename, 'rb')
    return etree.parse(handle)

def fetch_gz_file(url, filename):
    file_request = requests.get(url)
    with tempfile.TemporaryFile() as tf:
        for chunk in file_request.iter_content(chunk_size=1024):
            if chunk:
                tf.write(chunk)

        with gzip.open(tf, 'rb') as gf:
            unzipped_content = gf.read()

            with open(filename, 'wb') as of:
                of.write(gf)
