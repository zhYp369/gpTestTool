import base64
from utils.edit_date.edit_json import type_to_json

yuanfile = r"C:\Users\zhangyp\Desktop\100条蓝票.ofd"
newfile = r"C:\Users\zhangyp\Desktop\%s.jpg"


def get_file_base64(file):
    sFile = open(file, "rb").read()
    encodeStr = base64.b64encode(sFile)
    decodestr = str(encodeStr, "utf-8")
    print(decodestr)


def get_base64_file(value, file):
    img = base64.b64decode(value)
    fh = open(file, "wb")
    fh.write(img)
    fh.close()


with open(r'.\test.xml', "r", encoding='utf-8') as f:
    res_xml = f.read()
    f.close()
res_json = type_to_json(res_xml)
res_list = res_json.get("DATAS").get("DATA")
for i in range(len(res_list)):
    jpg_date = res_list[i].get("IMG")
    file = newfile % str(i+1)
    get_base64_file(jpg_date, file)

