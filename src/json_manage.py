import json

class MessageManage:
    @staticmethod
    def verify_selective_process_list(selective_process_lista):
        with open("src/selective_process.json", "r") as json_file:
            selective_process_json = json.load(json_file)["selective_process"]

        for i in selective_process_json:
            for j in selective_process_lista:
                if j in i:
                    print(j)
        
        with open("src/selective_process.json", "w") as json_file:
            json.dump(selective_process_json, json_file, indent=4)
        
    @staticmethod
    def send_selective_process_to_json(selective_process_lista):
        with open("src/selective_process.json", "r") as json_file:
            data = json.load(json_file)
            selective_process_json = data["selective_process"]

        print("Dados lidos do JSON:", selective_process_json)

        for i in selective_process_lista:
            selective_process_json.append(i)
        
        with open("src/selective_process.json", "w") as json_file:
            json.dump(selective_process_json, json_file, indent=4)
