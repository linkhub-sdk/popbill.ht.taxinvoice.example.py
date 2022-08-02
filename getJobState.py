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
htTaxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
htTaxinvoiceService.UseStaticIP = testValue.UseStaticIP
htTaxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
수집 요청(RequestJob API) 함수를 통해 반환 받은 작업 아이디의 상태를 확인합니다.
- 수집 결과 조회(Search API) 함수 또는 수집 결과 요약 정보 조회(Summary API) 함수를 사용하기 전에
  수집 작업의 진행 상태, 수집 작업의 성공 여부를 확인해야 합니다.
- 작업 상태(jobState) = 3(완료)이고 수집 결과 코드(errorCode) = 1(수집성공)이면
  수집 결과 내역 조회(Search) 또는 수집 결과 요약 정보 조회(Summary) 를 해야합니다.
- 작업 상태(jobState)가 3(완료)이지만 수집 결과 코드(errorCode)가 1(수집성공)이 아닌 경우에는
  오류메시지(errorReason)로 수집 실패에 대한 원인을 파악할 수 있습니다.
- https://docs.popbill.com/httaxinvoice/python/api#GetJobState
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
