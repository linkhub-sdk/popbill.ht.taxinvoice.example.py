# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID,testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 수집 상태 확인 " + "=" * 15)
    ''' JobState 구성
                jobID           (작업아이디)
                jobState        (수집상태)
                queryType       (수집유형)
                queryDateType   (일자유형)
                queryStDate     (시작일자)
                queryEnDate     (종료일자)
                errorCode       (오류코드)
                errorReason     (오류메시지)
                jobStartDT      (작업 시작일시)
                jobEndDT        (작업 종료일시)
                collectCount    (수집개수)
                regDT           (수집 요청일시)
    '''

    # 수집요청(requestJob) 호출시 발급받은 작업아이디
    jobID = "016080110000000007"

    response = htTaxinvoiceService.getJobState(testValue.testCorpNum, jobID, testValue.testUserID)

    for key, value in response.__dict__.items():
        print("%s : %s" % (key, value))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
