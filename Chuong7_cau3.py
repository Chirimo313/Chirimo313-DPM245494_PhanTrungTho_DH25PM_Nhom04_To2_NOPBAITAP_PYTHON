from xml.dom.minidom import parse

DOMTree = parse("employees.xml")
collection = DOMTree.documentElement

# Lấy tất cả các employee
employees = collection.getElementsByTagName("employee")

# Duyệt qua và in ra thông tin
for employee in employees:
    tag_id = employee.getElementsByTagName('id')[0]
    id = tag_id.childNodes[0].data
    tag_name = employee.getElementsByTagName('name')[0]
    name = tag_name.childNodes[0].data
    print(id, '\t', name)
