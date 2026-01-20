import requests
import threading
import yaml 
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from deepdiff import DeepDiff

class Spider():
    """
    Spider call. Handles
    logining into a site and finding
    pages a user can see via screen scraping
    """ 
    pages = {}
    base_url = ""
    user = ""
    password = ""
    urls_file = "user_pages.yaml"
    session = {}

    def __init__(self, base_url, user, password):
        """
        Populate class vars for the URL we are spidering
        the user, and the passwordword.
        Setup a dict to store the pages we find.
        """
        self.base_url = base_url
        self.pages[user] = []
        self.user = user
        self.password = password
        self.login()

    def login(self):
        """
        Handles login/session creation
        Calls the page spiderer
        Calls the function to output findings
        """
        headers = {"Content-Type": "application/json"}
        data={
            'username': self.user,
            'password': self.password
        }
        with requests.Session() as self.session:
            login_request = self.session.post(self.base_url+"/login",data=json.dumps(data), headers=headers)
            if login_request.status_code == 200:
                self.spider_pages(self.base_url)
                self.write_findings()

    def spider_pages(self, page):
        """
        Find a page and add to
        pages object. Recursively called,
        uses threads.
        """
        urls = []
        if "logout" not in page:
            page = self.session.get(page)
            html_content = page.content 
            parser = BeautifulSoup(html_content, 'html.parser') 
    
            for anchor_tag in parser.find_all('a', href=True):
                href = anchor_tag.get('href')
                if self.base_url not in href:
                    urls.append(urljoin(self.base_url, href))
                else:
                    urls.append(href)

            for url in urls:
                if url not in self.pages[self.user]:
                    self.pages[self.user].append(url)
                    try:
                        result = threading.Thread(target=self.spider_pages, args=(url,))
                        result.start()
                        result.join()
                    except:
                        print("Error")
    
    def write_findings(self):
        """
        Write the URLs we find to 
        our YAML document
        """ 
        pages_found = WriteToYAML(self.urls_file, self.user)
        pages_found.write_to_file(self.pages[self.user]) 


class TestPages():
    """
    Tests one user against a list of 
    URLs a second user can see.
    If it finds an IDOR, write to
    an output file
    """ 
    urls_file = "user_pages.yaml" #turn to commandline input so not duped in code
    pages_diff = []
    idor_file = "idors.yaml"
    process_urls = []
    session = {}

    base_url = ""
    user1 = ""
    user1_password = ""
    user2 = ""
    user2_password = ""

    def __init__(self, base_url, user1, user1_password, user2, user2_password):
        self.base_url = base_url
        self.user1 = user1
        self.user1_password = user1_password     
        self.user2 = user2
        self.user2_password = user2_password
        self.test_for_idor()

    def test_for_idor(self):
        self.process_urls = ReadFromYaml(self.urls_file)
        self.process_urls = self.process_urls.read_file()
        self.diff_urls()
        self.login()

    def diff_urls(self):
        """
        """
        diff = DeepDiff(self.process_urls[self.user1], self.process_urls[self.user2])
        if 'values_changed' in diff:
            for path,change in diff['values_changed'].items():
                self.pages_diff.append(change['new_value'])

    def login(self):
        """
        Handles login/session creation
        Calls the IDOR checker
        Calls the function to output findings
        """
        headers = {"Content-Type": "application/json"}
        data={
            'username': self.user1,
            'password': self.user1_password
        }
        with requests.Session() as self.session:
            login_request = self.session.post(self.base_url+"/login",data=json.dumps(data), headers=headers)

            if login_request.status_code == 200:
                self.test_urls()
            

    def test_urls(self):
        """
        check for IDORs
        """
        for url in self.pages_diff:
            test = self.session.get(url)
            if test.status_code == 200:
                print("***IDOR FOUND****") 
                print(url)
            else:
                pass

class ReadFromYaml():
    """
    Read a YAML file 
    return a dict 
    """ 
    file = ""
    def __init__(self, file):
        self.file = file

    def read_file(self):
        url_dict = {}
        with open(self.file, 'r') as file:
            url_dict = yaml.safe_load(file)
        return url_dict


class WriteToYAML():
      """
      Class to write to YAML file
      """
      urls_file = ""
      url_dict = {}
      user = ""

      def __init__(self, urls_file, user):
          print ("Writing to YAML file")
          self.user = user
          self.url_dict[user] = []
          self.urls_file = urls_file
          self.generate_dict()

      def generate_dict(self):
          """
          Read in YAML file, and convert to a dict
          we will then update the relevant object 
          with pages found, or add it if it is 
          not present
          """
          with open(self.urls_file, 'r') as file:
              file_contents = yaml.safe_load(file)
              if file_contents is not None:
                  self.url_dict = file_contents

      def write_to_file(self,pages):
          """
          Append/add to the dict 
          and write back to the
          YAML file
          """
          self.url_dict[self.user] = pages
          with open(self.urls_file, "w") as file_handler:
              yaml.dump(self.url_dict, file_handler, sort_keys=False, default_flow_style=False)

Spider("<url>", "<username 1>","<password 1>")
TestPages("<url>", "<username 1>","<password 1>", "<username 2>", "<password 2>")
