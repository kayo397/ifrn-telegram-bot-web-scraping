from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, url):
        self.url = url
        self.response = None
        self.selective_process_list = []

    def url_request(self):
        try:
            self.response = requests.get(self.url)

            if self.response.status_code == 200:
                return True
            else:
                return False
        except requests.exceptions.ConnectionError:
            return False
        
        except Exception as e:
            return False
        
    def list_selective_process(self):
        soup = BeautifulSoup(self.response.text, "lxml")

        try:
            tbody_path = soup.find("div", class_="table-responsive").find("table").find("tbody")
            tr_elements = tbody_path.find_all("tr")  

            if tr_elements != []:
                for i in range(len(tr_elements)):
                    self.selective_process_list.append(tr_elements[i].find("h3").text.strip())
                return self.selective_process_list      
            else:
                return False
        except AttributeError:
            return False
