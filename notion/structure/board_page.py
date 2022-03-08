from notion.structure.bulleted_block import BulletedBlock
from notion.parser import block_parser

class BoardPage:
    

    def __init__(self, id, tdl_field, urgency, due_date, title):
        self.__id = id
        self.__tdl_field = tdl_field
        self.__urgency = urgency
        self.__due_date = due_date
        self.__title = title

        self.root_bulleted_block = self.__get_content()
       


    def __get_content(self):
        root_bulleted_block = BulletedBlock(True, self.__id, True, None)
        return block_parser.parse_all_bulleted_blocks(root_bulleted_block)

        


    def block_to_string(self, bulleted_block, level):
        if not bulleted_block.root:
            temp = ""
            for n in range(level):
                temp += "   "

            print(temp + bulleted_block.text)

            level += 1
        
        if not len(bulleted_block.children) == 0:
            for child_bulleted_block in bulleted_block.children:
                self.block_to_string(child_bulleted_block, level)




    def to_string(self):
        # print(self.__id)
        print("Field:", self.__tdl_field)
        print("Title:", self.__title)
        print("Urgency:", self.__urgency)

        if self.__due_date == None:
            print("Due date:", self.__due_date)
        else:
            if "T" in self.__due_date:
                date = self.__due_date.split("T")[0]
                time = self.__due_date.split("T")[1].split(".")[0]
                print("Due date:", date, "/", time)
            else:    
                print("Due date:", self.__due_date)
        
        print("Content: ")
        self.block_to_string(self.root_bulleted_block, 0)

        



if __name__ == "__main__":
    pass 