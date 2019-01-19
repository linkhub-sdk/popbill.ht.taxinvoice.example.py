# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService,PopbillException

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

'''
수집 요청건들에 대한 상태 목록을 확인합니다.
- 수집 요청 작업아이디(JobID)의 유효시간은 1시간 입니다.
- 응답항목에 관한 정보는 "[홈택스연동(전자세금계산서) API 연동매뉴얼]
  > 3.1.3. ListActiveJob (수집 상태 목록 확인)" 을 참고하시기 바랍니다.
'''

try:
    print("=" * 15 + " 수집 상태 목록 확인 " + "=" * 15 + "\n")

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = htTaxinvoiceService.listActiveJob(CorpNum, UserID)

    i = 1
    listLength = str(len(response))

    for info in response :
        print("수집상태 정보 [" + str(i) + "/" + listLength + "]")
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        print
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
