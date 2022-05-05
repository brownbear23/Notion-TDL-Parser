import requests, json

autherization = "secret_RySJ7IpnyDR3wbCk6rLG5MFxr263gxEPz1LbtQxhaLw"
database_id = "48e88dbf8cef4d01b7a47474c35e0f07"
block_id = "9eed2c03-6eb5-44b1-9b82-88969df6cdcb"
# block_id = "6029f117-c889-45fc-9e97-c5c83e719081"
url = "https://api.notion.com/v1/blocks/{block_id}/children?page_size=100".format(block_id=block_id)


headers = {
    "Accept": "application/json",
    "Notion-Version": "2021-08-16",
    "Content-Type": "application/json",
    "Authorization": "{autherization}".format(autherization=autherization)
}


response = requests.request("GET", url, headers=headers)

print(response.text)
# find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf


# def test_method(list):
#     list.append(5)
#
#
# list = [1, 2, 3, 4]
# test_method(list)
# print(list)


# from docx import Document

# document = Document()
# document.add_heading("TDL list", level=0)
# document.add_heading("TDL list", level=1)
# document.add_heading("TDL list", level=2)
# document.add_heading("current_tdl_field", level=3)
#
# document.add_paragraph('Lorem ipsum dolor sit amet.', style='ListBullet')

# paragraph = document.add_paragraph('Lorem ipsum dolor sit amet.')
# paragraph.style = 'List Bullet'
# document.add_paragraph(paragraph)


# from docx import Document
# from docx.shared import Pt
#
# document = Document("/Users/billhan/Desktop/Dev/Notion-TDL-Parser/ms_word_writer/tdl_template.docx")
#
# paragraph = document.add_paragraph()
# title = paragraph.add_run()
# title.text = "TDL list123123"
# title.bold = True
# title.font.size = Pt(28)
# title.font.name = "Times New Roman"
#
# paragraph = document.add_paragraph()
# title = paragraph.add_run()
# title.text = "TDL list"
# title.bold = True
# title.font.size = Pt(28)
# title.font.name = "Arial"
#
# paragraph = document.add_paragraph()
# title = paragraph.add_run()
# title.text = "TDL list"
# title.bold = True
# title.font.size = Pt(28)
# title.font.name = "Malgun Gothic"
#
# document.save('test' + '.docx')


# from ms_word_writer.util import time_util
#
# time_util.get_current_day_weekday()


# from docx import Document
# from docx.enum.text import WD_COLOR_INDEX
# from docx.shared import Pt
# document = Document("/Users/billhan/Desktop/Dev/Notion-TDL-Parser/notion/ms_word_writer/tdl_template.docx")
#
#
# paragraph = document.add_paragraph("HelosfdafasdfasdfasddddfsdHelosfdafasdfasdfasddddfsdHelosfdafasdfasdfasddddfsdHelosfdafasdfasdfasddddfsdHelosfdafasdfasdfasddddfsd")
# paragraph.style = 'List Bullet'
#
# paragraph = document.add_paragraph("Helo")
# paragraph.style = 'List Bullet 2'
#
# paragraph = document.add_paragraph("Helo")
# paragraph.style = 'List Bullet 3'
#
#
#
# paragraph = document.add_paragraph("•   asdfasd sdafasd fasdfasd asdfas dasdf ads adsf asd sadf adsf asdf sdf asdf dsf asfasdf asdasdf asdfadsfasd asdfasd asdf asdsdf asd")
# paragraph = document.add_paragraph("     •   asdfasd sdafasd fasdfasd asdfas dasdf ads adsf asd sadf adsf asdf sdf asdf dsf asfasdf asdasdf asdfadsfasd asdfasd asdf asdsdf asd")
# paragraph = document.add_paragraph("          •   asdfasd sdafasd fasdfasd asdfas dasdf ads adsf asd sadf adsf asdf sdf asdf dsf asfasdf asdasdf asdfadsfasd asdfasd asdf asdsdf asd")
#
#
#
# paragraph = document.add_paragraph("•   asdfasd sdafasd fasdfasd asdfas dasdf ads adsf asd sadf adsf asdf sdf asdf dsf asfasdf asdasdf asdfadsfasd asdfasd asdf asdsdf asd")
# paragraph.paragraph_format.left_indent = Pt(24)
#
# paragraph = document.add_paragraph("•   asdfasd sdafasd fasdfasd asdfas dasdf ads adsf asd sadf adsf asdf sdf asdf dsf asfasdf asdasdf asdfadsfasd asdfasd asdf asdsdf asd")
# paragraph.paragraph_format.left_indent = Pt(48)
#
# paragraph = document.add_paragraph("•   asdfasd sdafasd fasdfasd asdfas dasdf ads adsf asd sadf adsf asdf sdf asdf dsf asfasdf asdasdf asdfadsfasd asdfasd asdf asdsdf asd")
# paragraph.paragraph_format.left_indent = Pt(72)
# run = paragraph.add_run()
# run.text = "This is added"
# run.font.size = Pt(19)
# run.font.highlight_color = WD_COLOR_INDEX.YELLOW
# run = paragraph.add_run()
#
# run.text = "This is added222"
#
#
#
# document.save('test' + '.docx')
