# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue

from popbill import HTTaxinvoiceService, PopbillException

htTaxinvoiceService = HTTaxinvoiceService(testValue.LinkID, testValue.SecretKey)
htTaxinvoiceService.IsTest = testValue.IsTest
htTaxinvoiceService.IPRestrictOnOff = testValue.IPRestrictOnOff
htTaxinvoiceService.UseStaticIP = testValue.UseStaticIP
htTaxinvoiceService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
국세청 승인번호를 통해 수집한 전자세금계산서 1건의 상세정보를 XML 형태의 문자열로 반환합니다.
- https://developers.popbill.com/reference/httaxinvoice/python/api/search#GetXML
"""

try:
    print("=" * 15 + " 세금계산서 상세정보 확인 - XML " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 전자세금계산서 국세청승인번호
    NTSConfirmNum = "20161121410002030000079e"

    response = htTaxinvoiceService.getXML(CorpNum, NTSConfirmNum)

    print("ResultCode (요청에 대한 응답 상태코드) : %s " % response.ResultCode)
    print("Message (전자세금계산서 국세청승인번호) : %s " % response.Message)
    print("retObject (전자세금계산서 XML문서) : %s " % response.retObject)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
