# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

'''
수집 요청 상태를 확인합니다.
- 응답항목 관한 정보는 "[홈택스 전자(세금)계산서 연계 API 연동매뉴얼
  > 3.2.2. GetJobState(수집 상태 확인)" 을 참고하시기 바랍니다 .
'''

try:
    print("=" * 15 + " 수집 상태 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob) 호출시 발급받은 작업아이디
    jobID = "016112315000000001"

    response = htTaxinvoiceService.getJobState(CorpNum, jobID, UserID)

    for key, value in response.__dict__.items():
        print("%s : %s" % (key, value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
