import re
import sys
import pdfplumber

"""
assumption: 
(1) each page (other than the 1st page) should have a page number printed in header or footer.
(2) the page number might not start from 1, but should be in ascending order.
(3) sometimes the 1st page might have meta info about the document that often not appear in other pages.
"""

class PageNumberExtractor:
    def process(self, input_pdf):
        """
        entry method of the class
        return a map of logical page number to physical ones (aka. the # printed on page)
        """
        
        header_lines = []   # the 1st line of each page
        footer_lines = []   # the last line of each page
        header_lines2 = []  # the 2nd line of each page
        footer_lines2 = []  # the 2nd last line of each page
        with pdfplumber.open(input_pdf) as pdf:
            for page in pdf.pages:
                text = page.extract_text() 
                #print("page %s: %s" % (str(page.page_number), str(len(text))))

                lines = text.split('\n')

                header_lines.append(lines[0])   # first line
                footer_lines.append(lines[-1])  # last line
                header_lines2.append(lines[1])   # second line
                footer_lines2.append(lines[-2])  # second last line

        result = {}
        candidates = [header_lines, footer_lines, header_lines2, footer_lines2]
         
        for cand_lines in candidates:
            result = self.find_page_numbers(cand_lines)
            if len(result)>0:
                return result
                
        return result
        
    def ascending_order(self, num_list):
        """ check if the given list of numbers are in ascending order """
        result = True
        prev_num = num_list[0]
        for k in range(1, len(num_list)):
            if prev_num >= num_list[k]:
                return False
            else:
                prev_num = num_list[k]
        return result

    def find_page_numbers(self, lines):
        """
        return a dictionary of logical page # to physical ones.
        e.g., {0: 11, 1: 12, 2: 13, 3: 14, 4: 15, 5: 16, 6: 17}
        """

        # step 1: assume each line is a line from a page
        # here to find all numbers in each line
        candidates = []
        for line in lines:
            #print(line)
            numbers = re.findall(r"\d+", line)
            if (numbers):
                # all numbers in this line
                candidates.append(numbers)

        #print(candidates)

        # step 2: find common lenghs of the number lists
        # ignore the 1st list, which is extracted from the 1st page
        min_len = len(candidates[0])
        for k in range(1, len(candidates)):
            min_len = min(min_len, len(candidates[k]))

        #print("min_len = %d" % min_len)

        # step 3: go through the numbers across all pages 
        # to see if they appear to be page numbers 
        result = {}   
        for i in range(min_len):
            cand_pages = []
            # check from candidates of the 2nd page
            for k in range(1, len(candidates)):
                cand_pages.append(candidates[k][i])

            #print(cand_pages)

            if self.ascending_order(cand_pages):
                result[0] = int(cand_pages[0]) - 1
                for j in range(0, len(cand_pages)):
                    result[j+1] = int(cand_pages[j])

        return result

if __name__ == "__main__":
    pdf_file = sys.argv[1]

    print("pdf_file: " + pdf_file)

    extractor = PageNumberExtractor()
    page_numbers = extractor.process(pdf_file)

    print(page_numbers)
