from docx.shared import Pt


### Notion related constants
class NotionConstants:
    authorization = "{your_authorization_token}"
    database_id = "{your_db_id}"


### Word document related constants
class DocConstants:
    font_name = "Times New Roman"
    # font_name = "Dotum"
    paragraph_space_before = Pt(0)
    paragraph_space_after = Pt(5)
    line_space = 1.0

    left_indent_num = 24
