import threading

from MailModule.SendingMailModule import SendEmailModule


class MultiThreadClass(threading.Thread):
    # Given
    success = 0
    fail = 0
    action = True

    # 생성자 method : host의 값을 받아서 mailModule로 넘겨주기 위해 값을 받아줌
    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host

    # run method : 실질적으로 동작을 하는 method
    def run(self):
        # stop() method 를 통해 중지 하기 위해 self.action을 조건으로 걸어줌
        while self.action:
            try:
                # mailModule과 연결되는 부분
                SendEmailModule.sendEmail(self.host, self.getName())
                self.success += 1
            except:
                self.fail += 1
                print(self.getName() + " 전송 실패")

    # Thread를 멈추는 method
    def stop(self):
        self.action = False

    # 해당 Thread의 성공 값을 넘겨줌
    def getSuccess(self):
        return self.success

    # 해당 Thread의 실패 값을 넘겨줌
    def getFail(self):
        return self.fail