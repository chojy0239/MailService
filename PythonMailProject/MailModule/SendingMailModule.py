# -*- coding: utf8 -*-
import datetime
import email
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from emaildata.text import Text
from MailModule.Method.decodeHeader import DecodeHeaderClass
from MailModule.Method.randomEmail import randomEmailClass


class SendEmailModule:
    def sendEmail(HOST , THREADNAME):
        ### Given
        PORT = 25
        SENDERADDR = randomEmailClass.selectEmail('sender')[0]  # Random으로 보내는 사람 정하기
        RECEIVERADDR = randomEmailClass.selectEmail('receiver')[0]  # Random으로 받는 사람 정하기

        # STEP-01: Read 'eml file'
        message = email.message_from_file(open('./Resources/EmlFile/message.eml'))

        # STEP-02: Decoding Process
        subjectCode = message['subject']                    # eml파일의 코드 중파일 중 subject(제목) 요소
        subject = DecodeHeaderClass.decodeHeader(subjectCode) # subject 부분을 decoding 해오는 과정
        html = Text.context_html(message)                    # html 부분을 decoding 하는 과정

        # STEP-03: Input element in MIMEText
        msg = MIMEText(html, _charset='utf8')               # 보내는 내용을 utf8로 정의
        msg['Subject'] = Header(subject, 'utf8')           # 보내는 내용제목을 utf-8로 정의
        msg['From'] = SENDERADDR                            # 보내는 사람
        msg['To'] = RECEIVERADDR                            # 받는 사람

        # STEP-04: Connect server using SMTP
        s = smtplib.SMTP(HOST, PORT)

        # STEP-05: Send Mail
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') # 현재시간을 String으로 받아줌
        s.sendmail(SENDERADDR, RECEIVERADDR, msg.as_string())
        print(THREADNAME + '  현재 시간' + time + '  Sender ID : ' + SENDERADDR +' Receiver ID : '
              + RECEIVERADDR + ' 전송완료 ')

        # STEP-06: FInish
        s.quit()



