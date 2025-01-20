# -*- coding: utf-8 -*-

"""
팝빌 홈택스수집 전자세금계산서 API Python SDK Example

Python 연동 튜토리얼 안내 : https://developers.popbill.com/guide/httaxinvoice/python/getting-started/tutorial
업데이트 일자 : 2025-01-20
연동 기술지원 연락처 : 1600-9854
연동 기술지원 이메일 : code@linkhubcorp.com

<테스트 연동개발 준비사항>
1) API Key 변경 (연동신청 시 메일로 전달된 정보)
    - LinkID : 링크허브에서 발급한 링크아이디
    - SecretKey : 링크허브에서 발급한 비밀키
2) SDK 환경설정 옵션 설정
    - IsTest : 연동환경 설정, True-테스트, False-운영(Production), (기본값:True)
    - IPRestrictOnOff : 인증토큰 IP 검증 설정, True-사용, False-미사용, (기본값:True)
    - UseStaticIP : 통신 IP 고정, True-사용, False-미사용, (기본값:False)
    - UseLocalTimeYN : 로컬시스템 시간 사용여부, True-사용, False-미사용, (기본값:True)
3) 홈택스수집 로그인 인증정보를 등록합니다. (부서사용자등록 / 공동인증서 등록)
    - 팝빌로그인 > [홈택스수집] > [환경설정] > [인증 관리] 메뉴
    - 홈택스수집 인증 관리 팝업 URL(GetCertificatePopUpURL API) 반환된 URL을 이용하여
      홈택스수집 인증 처리를 합니다.
"""

# 링크아이디
LinkID = "TESTER"

# 비밀키
SecretKey = "SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I="

# 연동환경 설정, True-테스트, False-운영(Production), (기본값:True)
IsTest = True

# 인증토큰 IP 검증 설정, True-사용, False-미사용, (기본값:True)
IPRestrictOnOff = True

# 통신 IP 고정, True-사용, False-미사용, (기본값:False)
UseStaticIP = False

# 로컬시스템 시간 사용여부, True-사용, False-미사용, (기본값:True)
UseLocalTimeYN = True

# 팝빌회원 사업자번호
testCorpNum = "1234567890"

# 팝빌회원 아아디
testUserID = "testkorea"
