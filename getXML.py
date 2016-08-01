# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import HTTaxinvoiceService,PopbillException

htTaxinvoiceService =  HTTaxinvoiceService(testValue.LinkID,testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest

try:
    print("=" * 15 + "상세정보 확인 - XML" + "=" * 15)
    '''
        전자세금계산서 1건의 XML 문서를 조회합니다.
    '''

    # 전자세금계산서 국세청승인번호
    NTSConfirmNum = "201607274100002900000209"

    response = htTaxinvoiceService.getXML(testValue.testCorpNum, NTSConfirmNum, testValue.testUserID)

    print("ResultCode (응답코드) : %s " % response.ResultCode)
    print("Message (국세청승인번호) : %s " % response.Message)
    print("retObject (전자세금계산서 XML문서) : %s " % response.retObject)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
