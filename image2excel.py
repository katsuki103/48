import sys
import os
import ocr
import draw
import xlrd
import xlwt
import yaml_class
from xlutils.copy import copy

pic_path = sys.argv[1]

pic_name = os.path.split(pic_path)[-1].split(".")[0]

print('doing')

# 使用ocr进行转换
config = yaml_class.get_yaml_data("config.yml")
jpg_name = './images_temp/'+pic_name+'/0.jpg'
trans = ocr.OCR()
path_excel = trans.img_to_excel(
    pic_name,
    image_path=pic_name,
    secret_id=config['secret_id'],
    secret_key=config['secret_key'],
)

old_excel = xlrd.open_workbook('output.xlsx')
new_excel = copy(old_excel)
ws = new_excel.get_sheet(0)
new_excel.save(pic_name+'.xls')
