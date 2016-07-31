import datetime

from MailSend.ThreadClass import MultiThreadClass

class MailSendClass:
    def sendmain(self):
        # Given
        AllTestSuccess = 0  # 모든 테스트의 성공 값을 합쳐서 보여주기 위한 변수 선언
        AllTestFail = 0  # 모든 테스트의 실패 값을 합쳐서 보여주기 위한 변수 선언

        ### STEP-01: Input Setting
        print("IP를 정확하게 입력하십시오. (ex)175.115.94.214")
        HOST = input("사용할 서버 : ")
        THREAD = input("Thread 개수 : ")
        print("Second 단위입니다. 그냥 숫자만 입력하시면 진행됩니다.")
        DURINGTIME = input("발송 시간 : ")

        ### STEP-02: 입력받은 값을 이용한 설정 및 생성
        actionThread = []  # 입력 받은 개수만큼 thread를 List로 잡아주는 과정
        for i in range(int(THREAD)):  # thread 생성(생성자에는 HOST를 넣어줌)
            actionThread.append(MultiThreadClass(HOST))
        now = datetime.datetime.now()
        nowTime = datetime.datetime.now()  # 작업시작 시간
        finishTime = nowTime + datetime.timedelta(seconds=int(DURINGTIME))  # 끝나는 시간
        # 각 시간을 문자열로 바꿔주는 작업
        nowTime = nowTime.strftime('%Y-%m-%d %H:%M:%S')
        finishTime = str(finishTime.strftime('%Y-%m-%d %H:%M:%S'))

        ### STEP-03: 각 Thread 시작
        for i in actionThread:
            i.start()

        ### STEP-04: 발송시간부터 완료시간까지 while을 통해 확인 -> 시간이 일치하면 break로 빠져나옴
        while True:
            time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            if time == finishTime:
                break

        # STEP-05: 각 Thread를 중지하는 method
        #           추가적으로 stop을 명령했을때 이미 돌고 있던 실행은 완료하도록
        #           join() 이라는 method로 통제
        for i in actionThread:
            i.stop()
            i.join()

        ### STEP-06: 걀과 값을 나타내주는 method(각 Thread의 성공 실패, 전체 Thread의 성공 실패)
        print('\n시작시간 : ' + nowTime)
        print('종료시간 : ' + finishTime)
        print('작업시간 : ' + DURINGTIME + 's\n')

        for i in actionThread:
            AllTestSuccess += i.getSuccess()
            AllTestFail += i.getFail()
            print(i.getName() + " 성공 : " + str(i.getSuccess()) + "   실패 : " + str(i.getFail()))

        print("\n전체 성공 : " + str(AllTestSuccess) + "   전체 실패 : " + str(AllTestFail))
        print('성공률 : ' + str(float(AllTestSuccess / (AllTestFail + AllTestSuccess)) * 100) + '%   실패율 : ' + str(
            float(AllTestFail / (AllTestFail + AllTestSuccess)) * 100) + '%')


