import xlrd
import random

class randomEmailClass:
    # 해당 Excel 파일에서 Sender와 Receiver을 뽑아오기 위한 Class
    def selectEmail(type):
        i = random.randrange(0, 30)
        workbook = xlrd.open_workbook("./Resources/DB_SenderReceiverEmail/sendEmail.xlsx")
        if type == 'sender':
            worksheet = workbook.sheet_by_index(0)
        elif type == 'receiver':
            worksheet = workbook.sheet_by_index(1)
        else:
            return 'fail'
        SENDERADDR = worksheet.row_values(i)
        return SENDERADDR;
