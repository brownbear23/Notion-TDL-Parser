from unittest import result
import requests, json
from notion.constants import NotionConstants
from notion.structure.bulleted_block import BulletedBlock




def parse_all_bulleted_blocks(parent_block):

    block_children_json = __request_bulleted_block(parent_block.id)
    results = block_children_json.get("results")

    if not isinstance(results, list):
        raise RuntimeError("Key \"results\" not found in block children json.")

    for block_json in results:
        if not block_json.get("type") == "bulleted_list_item":
            continue
        
        block_object = __parse_bulleted_block(block_json)

        if block_object.has_children:
            parent_block.insert(parse_all_bulleted_blocks(block_object))
        else:
            parent_block.insert(block_object)

    return parent_block





def __parse_bulleted_block(block_json):
    id = block_json.get("id")
    has_children = block_json.get("has_children")

    if len(block_json.get("bulleted_list_item").get("text")) == 0:
        text = "-"
    else:
        text = "- " + block_json.get("bulleted_list_item").get("text")[0].get("plain_text")

    return BulletedBlock(False, id, has_children, text)





def __request_bulleted_block( block_id):
    url = "https://api.notion.com/v1/blocks/{block_id}/children?page_size=100".format(block_id=block_id)


    headers = {
        "Accept": "application/json",
        "Notion-Version": "2021-08-16",
        "Content-Type": "application/json",
        "Authorization": "{autherization}".format(autherization=NotionConstants.autherization)
    }


    response = requests.request("GET", url, headers=headers)


    return json.loads(response.text)



if __name__ == "__main__":
    pass 