# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

'''
수집 요청 상태를 확인합니다.
- 응답항목 관한 정보는 "[홈택스연동(전자세금계산서) API 연동매뉴얼]
  > 3.1.2. GetJobState(수집 상태 확인)" 을 참고하시기 바랍니다 .
'''

try:
    print("=" * 15 + " 수집 상태 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 수집요청(requestJob) 호출시 발급받은 작업아이디
    jobID = "019012912000000003"

    response = htTaxinvoiceService.getJobState(CorpNum, jobID, UserID)

    print("jobID (작업아이디) : %s" % response.jobID)
    print("jobState (수집상태) : %s" % response.jobState)
    print("queryType (수집유형) : %s" % response.queryType)
    print("queryDateType (수집 일자유형) : %s" % response.queryDateType)
    print("queryStDate (시작일자) : %s" % response.queryStDate)
    print("queryEnDate (종료일자) : %s" % response.queryEnDate)
    print("errorCode (오류코드) : %s" % response.errorCode)
    print("errorReason (오류메시지) : %s" % response.errorReason)
    print("jobStartDT (작업 시작일시) : %s" % response.jobStartDT)
    print("jobEndDT (작업 종료일시) : %s" % response.jobEndDT)
    print("collectCount (수집개수) : %s" % response.collectCount)
    print("regDT (수집 요청일시) : %s" % response.regDT)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
