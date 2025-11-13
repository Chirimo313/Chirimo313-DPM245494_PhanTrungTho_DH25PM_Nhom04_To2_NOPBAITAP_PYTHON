import xlsxwriter

workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# Thiết lập các cột cho file
worksheet.set_column('A:A', 5)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 20)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)

# Định dạng tiêu đề cột in đậm
bold = workbook.add_format({'bold': True})

# Thêm dòng tiêu đề và định dạng in đậm
worksheet.write('A1', 'STT', bold
