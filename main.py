import xlrd
import json

# xlrd版本需要是1.2.0
data = xlrd.open_workbook("Book1.xlsx")
table = data.sheets()[0]
n = table.nrows
stu = []
for i in range(n):
    if i == 0:
        continue
    stu.append(table.row_values(i))
json_data = json.dumps(stu)
with open('stu_json.json','w') as f :
    f.write(json_data)

with open('stu_json.json','r') as f:
    d = json.load(f)
    print(d)
    r = list(filter(lambda j: j[2] > 5, d))
    print("亲密度大于5的人有:",r)
