import sys
import os
import ocr
import draw
import xlrd
import xlwt
import yaml_class
from xlutils.copy import copy

pdf_path = sys.argv[1]

pdf_name = os.path.split(pdf_path)[-1].split(".")[0]

print('doing')

# PDF按每页转为JPG文件
draw.pdf2jpg(pdf_path, './images_temp/'+pdf_name+'/')

# 使用ocr进行转换
config = yaml_class.get_yaml_data("config.yml")
jpg_name = './images_temp/'+pdf_name+'/0.jpg'
trans = ocr.OCR()
path_excel = trans.img_to_excel(
    pdf_name,
    image_path=jpg_name,
    secret_id=config['secret_id'],
    secret_key=config['secret_key'],
)

old_excel = xlrd.open_workbook(pdf_name+'.xlsx')
new_excel = copy(old_excel)
ws = new_excel.get_sheet(0)
new_excel.save(pdf_name+'.xls')
