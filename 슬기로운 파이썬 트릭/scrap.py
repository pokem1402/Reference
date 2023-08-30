# from web_scrapper/module/patent.py
# written by wonbin kim
# 2023.08.30. 14:00 Version
import argparse
import time
import traceback

class Scrapper_Patent(
    # Scrapper
    ):
    
    CONFIG = {
        'base_url' : "http://kpat.kipris.or.kr/kpat/{patent_number}.pdf?method=fullText&applno={patent_number}&pub_reg={pub_reg}&fileKind=undefined",
        'pub_reg' : [
            'R', # Registerd, 등록
            'P', # Public, 공개
        ]
    }
   
    # def __init__(self):
        # super().__init__("")

    @staticmethod
    def get_pdf_url(
        patent_number:int or str,
        pub_reg : str = "R"
    ) -> str:
        """Get the url of a patent pdf file."""
        if isinstance(patent_number, str):
            patent_number = patent_number.replace("-", "")
                        
        return Scrapper_Patent.CONFIG['base_url'].format(
            patent_number=patent_number,
            pub_reg = pub_reg,
        )

        
    @staticmethod
    def get_pdf_url_except(
        patent_number:int or str,
        pub_reg : str = "R"
    ) -> str:
        """Get the url of a patent pdf file, error handling with except"""
        
        if isinstance(patent_number, str):
            patent_number = patent_number.replace("-", "")
        
        if len(str(patent_number)) != 13:
            raise ValueError("특허번호는 13자리")
        
        if pub_reg not in Scrapper_Patent.CONFIG['pub_reg']:
            raise ValueError("타입은 P(공개) 혹은 R(등록)" )
        
        return Scrapper_Patent.CONFIG['base_url'].format(
            patent_number=patent_number,
            pub_reg = pub_reg,
        )
    
    @staticmethod
    def get_pdf_url_assert(
        patent_number:int or str,
        pub_reg : str = "R"
    ) -> str:
        """Get the url of a patent pdf file. error handling with assert"""
        
        if isinstance(patent_number, str):
            patent_number = patent_number.replace("-", "")
        
        assert len(str(patent_number)) == 13, "특허번호는 13자리"

        assert pub_reg in Scrapper_Patent.CONFIG['pub_reg'], "타입은 P(공개) 혹은 R(등록)"       
        
        return Scrapper_Patent.CONFIG['base_url'].format(
            patent_number=patent_number,
            pub_reg = pub_reg,
        )
    
    
        

if __name__ == '__main__':
    
    scrapper = Scrapper_Patent()
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "-p", "--patent", dest="patent", action='store', default="10-1972-0000009"
    ) 
    parser.add_argument(
        "-t", "--type", dest="type", action='store', default="R"
    ) 
    
    args = parser.parse_args()
    
    patent_number = args.patent
    print(f"입력한 번호 : {patent_number}")
    
    if __debug__:
        print("Debug run.")
    else:
        print("Release Run.")
    
    try:
        print("get_pdf_url")
        print(scrapper.get_pdf_url(patent_number, args.type))
    except (ValueError, AssertionError) as e:
        traceback.print_exc()
            
    try:
        print("get_pdf_url_assert:")
        print(scrapper.get_pdf_url_assert(patent_number, args.type))
    except (ValueError, AssertionError) as e:
        traceback.print_exc()
       
    try:
        print("get_pdf_url_except: ")
        print(scrapper.get_pdf_url_except(patent_number, args.type))
    except (ValueError, AssertionError) as e:
        traceback.print_exc()
        