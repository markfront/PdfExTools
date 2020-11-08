import unittest

import importlib.util

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

target_module = module_from_file("page_number_extractor", "../PdfExTools/page_number_extractor.py")

class TestPageNumberExtractor(unittest.TestCase):
    """
    Test PageNumberExtractor
    """
    def setUp(self):
        self.extractor = target_module.PageNumberExtractor()

    def tearDown(self):
        return

    def test_pdf1(self):
        pdf_file = r"./sample-pdfs/2-col-pubmed.pdf"
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18, 8: 19, 9: 20, 10: 21, 11: 22, 12: 23}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf2(self):
        pdf_file = r"./sample-pdfs/2-col-pubmed-2.pdf"
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 826, 1: 827, 2: 828, 3: 829, 4: 830, 5: 831, 6: 832, 7: 833, 8: 834, 9: 835}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf3(self):
        pdf_file = r"./sample-pdfs/ACL-P18-4005.pdf"
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 25, 1: 26, 2: 27, 3: 28, 4: 29, 5: 30}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

if __name__ == '__main__':
    unittest.main()

# run tests from cmd-line:
# python test_pgn_extractor.py -v
