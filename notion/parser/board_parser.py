import requests, json
from notion import constants
from notion.structure.board_page import BoardPage

def parse_board(database_id):
    board_list = []

    board_json = __request_board(database_id)
    results = board_json.get("results")

    # print(json.dumps(board_json))

    if not isinstance(results, list):
        raise RuntimeError("Key \"results\" not found in board json.")

    for page in results:
        if not page.get("object") == "page":
           raise RuntimeError("Object is not \"page\".") 

        id = page.get("id")

        if len(page.get("properties").get("Name").get("title")) == 0:
            raise RuntimeError("Object has no title.") 
        title = page.get("properties").get("Name").get("title")[0].get("plain_text")


        if page.get("properties").get("TDL field").get("select") == None:
            tdl_field = "Other"
        else:
            tdl_field = page.get("properties").get("TDL field").get("select").get("name")


        if page.get("properties").get("Urgency").get("select") == None:
            urgency = None
        else:
            urgency = page.get("properties").get("Urgency").get("select").get("name")


        if page.get("properties").get("Due date").get("date") == None:
            due_date = None
        else:
            due_date = page.get("properties").get("Due date").get("date").get("start")

        temp_board_page = BoardPage(id, tdl_field, urgency, due_date, title)

        board_list.append(temp_board_page)

    return board_list






def __request_board(database_id):
    url = "https://api.notion.com/v1/databases/{database_id}/query".format(database_id=database_id)

    payload = {
        "page_size": 100,
        "sorts": [
            {
                "property": "TDL field",
                "direction": "ascending"
            },
            {
                "property": "Due date",
                "direction": "ascending"
            }
        ]
    }

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "{autherization}".format(autherization=constants.autherization)
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    return json.loads(response.text)





if __name__ == "__main__":
    pass 





