from bs4 import BeautifulSoup
import requests

url = "https://processoseletivo.ifrn.edu.br/"

try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        div_path = soup.find("div", class_="table-responsive")

        if div_path is not None:
            table = div_path.find("table")

            if table is not None:
                tbody = table.find("tbody")

                if tbody is not None:
                    tr = tbody.find_all("tr")
                    
                    if tr is None:
                        print("Elemento tr não encontradoo")              
                else:
                    print('Elemento "tbody" não encontrado')
            else:
                print('Elemento "table" não encontrado')
        else:
            print('Elemento "div.table-responsive" não encontrado')

    else:
        print(f"Falha ao acessar: {response.status_code} - {response.url}")

except requests.exceptions.ConnectionError:
    print("Falha na conexão")

except Exception as e:
    print(f"Erro inesperado: {e}")

selective_process_dict = {}

for i in range(len(tr)):
    selective_process_dict[i] = [tr[i].find("h3").text.strip()]

print(selective_process_dict[0])
