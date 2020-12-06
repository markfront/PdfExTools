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
        print("\ntest_pdf1(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17, 7: 18, 8: 19, 9: 20, 10: 21, 11: 22, 12: 23}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf2(self):
        pdf_file = r"./sample-pdfs/2-col-pubmed-2.pdf"
        print("\ntest_pdf2(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 826, 1: 827, 2: 828, 3: 829, 4: 830, 5: 831, 6: 832, 7: 833, 8: 834, 9: 835}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf3(self):
        pdf_file = r"./sample-pdfs/ACL-P18-4005.pdf"
        print("\ntest_pdf3(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 25, 1: 26, 2: 27, 3: 28, 4: 29, 5: 30}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf4(self):
        pdf_file = r"./sample-pdfs/BTRR_Report.pdf"
        print("\ntest_pdf4(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf5(self):
        pdf_file = r"./sample-pdfs/ICML.pdf"
        print("\ntest_pdf5(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf6(self):
        pdf_file = r"./sample-pdfs/KDD.pdf"
        print("\ntest_pdf6(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 120, 1: 121, 2: 122, 3: 123, 4: 124, 5: 125, 6: 126, 7: 127, 8: 128, 9: 129}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf7(self):
        pdf_file = r"./sample-pdfs/NIH-Tech-Report_Aug2020.pdf"
        print("\ntest_pdf7(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = { 0: -1, 1: 0, 2: 1,3: 2,4: 3, 5: 4, 6: 5, 7: 6,8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29, 31: 30, 32: 31, 33: 32, 34: 33, 35: 34, 36: 35, 37: 36, 38: 37, 39: 38 }

        self.assertEqual(actual_page_numbers, extracted_page_numbers)
    
    def test_pdf8(self):
        pdf_file = r"./sample-pdfs/EMCM.pdf"
        print("\ntest_pdf8(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {0: 31, 1: 32, 2: 33, 3: 34}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf9(self):
        pdf_file = r"./sample-pdfs/BigDataSurvey2014.pdf"
        print("\ntest_pdf9(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {}
        for i in range(171, 210):
            actual_page_numbers[i-171] = i

        self.assertEqual(actual_page_numbers, extracted_page_numbers)

    def test_pdf10(self):
        pdf_file = r"./sample-pdfs/BioTextMining-Survey-2017.pdf"
        print("\ntest_pdf10(): " + pdf_file)
        extracted_page_numbers = self.extractor.process(pdf_file)
        actual_page_numbers = {}

        self.assertEqual(actual_page_numbers, extracted_page_numbers)    


if __name__ == '__main__':
    unittest.main()

# run tests from cmd-line:
# python test_pgn_extractor.py -v
