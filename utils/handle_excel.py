import xlrd
import xlwt

write_dict = {}
sheet_dict = {}
read_dict = {}

def writeRow(file_name, sheet_name, row, values, style=None):
    wb = None
    if (write_dict.__contains__(file_name)):
        wb = write_dict[file_name]
    else:
        wb = xlwt.Workbook(style_compression=2)
        write_dict[file_name] = wb
        sheet_dict[file_name] = {}
    
    sheet = None
    if (sheet_dict[file_name].__contains__(sheet_name)):
        sheet = sheet_dict[file_name][sheet_name]
    else:
        sheet = wb.add_sheet(sheet_name, cell_overwrite_ok=True)
        sheet_dict[file_name][sheet_name] = sheet
    
    if (style != None):
        created_style = createStyle() 
        
