from notion.parser import board_parser
from notion.ms_word_writer import writer
from datetime import datetime
import sys

tdl_template_doc_dir = "/Users/billhan/Desktop/Dev/Notion/Notion-TDL-Parser/notion/ms_word_writer/tdl_template.docx"
doc_name = datetime.now().strftime("TDL_%y%m%d_%H%M%S")
print("Parsing " + doc_name + ".docx ...")

board_list = board_parser.parse_board()

write_dir = sys.argv[1]
writer.tdl_writer(tdl_template_doc_dir, write_dir+"/"+doc_name, board_list)
print("Done!")


