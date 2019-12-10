import unittest
import pubmed_parser as pp

import os
DATA_DIR = os.path.dirname(os.path.realpath(__file__)) + "/../../data"


class TestMedlineExtract(unittest.TestCase):

    def test_parse_medline_xml(self):
        docs = pp.parse_medline_xml(DATA_DIR + "/pubmed19n0719_sample.xml")
        self.assertEqual("22369299", docs[0]['pmid'])


if __name__ == '__main__':
    unittest.main()
