from behave import *
import logging
from features.steps.common import *


use_step_matcher("re")


# 2단계 인증 설정 안내페이지

@then("2단계 인증 설정 안내페이지로 이동한다")
def go_mfaInfo(self):
    try:
        # url 확인
        url = self.driver.current_url
        assert url == URL_MFAINFO
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 2단계 인증 설정 안내페이지가 출력된다')


@step("2단계 인증 설정 안내페이지 안내가 출력된다")
def print_mfaInfoInfo(self):
    try:
        # 2단계 인증 설정 타이틀 확인
        mfaTitle = self.driver.find_element_by_css_selector("[data-ta='elm-mfainfo-title']").text
        assert mfaTitle == TEXT_MFAINFO_TITLE
        # 2단계 인증 설정 설명 확인
        mfaDescription = self.driver.find_element_by_css_selector("[data-ta='elm-mfainfo-desc']").text
        assert mfaDescription == TEXT_MFAINFO_DESC
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정 안내페이지 안내가 출력된다')


@step("2단계 인증 설정 안내페이지에서 \[설정하기\]버튼이 출력된다")
def print_mfaInfoSetupBtn(self):
    try:
        # [설정하기]버튼 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-mfainfo-move']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정 안내페이지에서 \[설정하기\]버튼이 출력된다')


@step("2단계 인증 설정 안내페이지에서 \[설정하기\]버튼을 클릭한다")
def click_mfaInfoSetupBtn(self):
    try:
        # [설정하기]버튼 클릭
        mfainfoActivateButton = self.driver.find_element_by_css_selector("[data-ta='elm-mfainfo-move']")
        mfainfoActivateButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정 안내페이지에서 [설정하기]버튼을 클릭한다')

@step("2단계 인증 설정 안내페이지에서 \[다른 계정으로 로그인\]링크가 출력된다")
def print_mfaInfoAnotherSignin(self):
    try:
        # [다른 계정으로 로그인]링크 확인
        AnotherAccountButton = self.driver.find_element_by_css_selector("[data-ta='elm-mfainfo-back']").text
        assert AnotherAccountButton == "다른 계정으로 로그인"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정 안내페이지에서 [다른 계정으로 로그인]링크가 출력된다')

@step("2단계 인증 설정 안내페이지에서 \[다른 계정으로 로그인\]링크를 클릭한다")
def click_mfaInfoAnotherSignin(self):
    try:
        # [다른 계정으로 로그인]링크 확인
        AnotherAccountButton = self.driver.find_element_by_css_selector("[data-ta='elm-mfainfo-back']")
        AnotherAccountButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정 안내페이지에서 [다른 계정으로 로그인]링크가 출력된다')


# OTP 설정 페이지

@then("OTP 설정 페이지로 이동한다")
def go_otpSetting(self):
    try:
        # url 확인
        url = self.driver.current_url
        assert url == URL_OTPSET
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then OTP 설정 페이지가 출력된다')


@step("OTP 설정 페이지 안내가 출력된다")
def print_otpSetting(self):
    try:
        # OTP 설정 타이틀 확인
        setupOTPtitle = self.driver.find_element_by_css_selector("[data-ta='elm-otp-title']").text
        assert setupOTPtitle == TEXT_OTPSET_TITLE
        # OTP 설정 설명 확인
        setupOTPdescription = self.driver.find_element_by_css_selector("[data-ta='elm-otp-desc']").text
        assert setupOTPdescription == TEXT_OTPSET_DESC
        # 바코드 스캔 타이틀 확인
        scanThisBarcodeTitle = self.driver.find_element_by_css_selector("[data-ta='elm-otp-barcodetitle']").text
        assert scanThisBarcodeTitle == TEXT_OTPSET_SCANTITLE
        # 바코드 스캔 설명 확인
        scanThisBarcodeDescription = self.driver.find_element_by_css_selector("[data-ta='elm-otp-barcodedesc']").text
        assert scanThisBarcodeDescription == TEXT_OTPSET_SCANDESC
        # 인증 코드 입력 타이틀 확인
        enterVerificationCodeTitle = self.driver.find_element_by_css_selector("[data-ta='elm-otp-codetitle']").text
        assert enterVerificationCodeTitle == TEXT_OTPSET_MFACODETITLE
        # 인증 코드 입력 설명 확인
        enterVerificationCodeDescription = self.driver.find_element_by_css_selector("[data-ta='elm-otp-codedesc']").text
        assert enterVerificationCodeDescription == TEXT_OTPSET_MFACODEDESC
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지 안내가 출력된다')


@step("OTP 설정 페이지에서 \[Google Play\]링크가 출력된다")
def print_otpSettingGooglePlay(self):
    try:
        # [Google Play]링크 확인
        googleplayLink = self.driver.find_element_by_css_selector("[data-ta='elm-otp-googleplay']").text
        assert googleplayLink == TEXT_OTPSET_GOOGLEPLAY
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [Google Play]링크가 출력된다')

@step("OTP 설정 페이지에서 \[Google Play\]링크를 클릭한다")
def click_otpSettingGooglePlay(self):
    try:
        # [Google Play]링크 클릭
        googleplayLink = self.driver.find_element_by_css_selector("[data-ta='elm-otp-googleplay']")
        googleplayLink.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [Google Play]링크를 클릭한다')


@then("Google Play 페이지로 이동한다")
def go_otpSettingGooglePlay(self):
    try:
        # Google Play 페이지로 새창 이동
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(10)
        # 이동한 페이지 url 확인 후, 새창 닫기
        url = self.driver.current_url
        assert url == URL_GOOGLEPLAY
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then Google Play 페이지가 출력된다')


@step("OTP 설정 페이지에서 \[App Store\]링크가 출력된다")
def print_otpSettingAppStore(self):
    try:
        # [App Store]링크 출력
        appstoreLink = self.driver.find_element_by_css_selector("[data-ta='elm-otp-appstore']").text
        assert appstoreLink == TEXT_OTPSET_APPSTORE
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 [App Store]링크가 출력된다')


@step("OTP 설정 페이지에서 \[App Store\]링크를 클릭한다")
def click_otpSettingAppStore(self):
    try:
        # [App Store]링크 클릭
        appstoreLink = self.driver.find_element_by_css_selector("[data-ta='elm-otp-appstore']")
        appstoreLink.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [App Store]링크를 클릭한다')


@then("App Store 페이지로 이동한다")
def go_otpSettingAppStore(self):
    try:
        # App Store 페이지로 새창 이동
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.implicitly_wait(10)
        # 이동한 페이지 url 확인 후, 새창 닫기
        url = self.driver.current_url
        assert url == URL_APPSTORE
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then App Store 페이지가 출력된다')


@step("OTP 설정 페이지에서 QR코드가 출력된다")
def print_otpSettingQrcode(self):
    try:
        # QR코드 출력 확인
        appstoreLink = self.driver.find_element_by_css_selector("[data-ta='elm-otp-appstore']")
        appstoreLink.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 QR코드가 출력된다')


@step("OTP 설정 페이지에서 \[스캔할 수 없나요\?\]버튼이 출력된다")
def print_otpSettingScanToggle(self):
    try:
        # [스캔할 수 없나요?]버튼 확인
        cannotScanItToggleButton = self.driver.find_element_by_css_selector("[data-ta='elm-otp-scantoggle']").text
        assert cannotScanItToggleButton == "스캔할 수 없나요?"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 [스캔할 수 없나요?]버튼이 출력된다')


@step("OTP 설정 페이지에서 \[스캔할 수 없나요\?\]버튼을 클릭한다")
def click_otpSettingScanToggle(self):
    try:
        # [스캔할 수 없나요?]버튼 클릭
        cannotScanItToggleButton = self.driver.find_element_by_css_selector("[data-ta='elm-otp-scantoggle']")
        cannotScanItToggleButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [스캔할 수 없나요?]버튼을 클릭한다')


@then("OTP 설정 페이지에서 비밀 키 정보가 출력된다")
def print_otpSettingSecretkey(self):
    try:
        # 비밀 키 확인 -> 영역만 체크 가능한데, 실제 키 값을 받아올 방법이 있을지?? api ???
        self.driver.find_element_by_css_selector("[data-ta='elm-otp-scantoggle']")
        # [복사]버튼 확인
        copyButton = self.driver.find_element_by_css_selector("[data-ta='elm-otp-secretcopy']").text
        assert copyButton == "복사"
        # 비밀 키 설명 확인 ------------------------------> data-ta 없음
        #secretkeyDescription = self.driver.find_element_by_css_selector("[data-ta='elm-otp-secretdesc']").text
        #assert secretkeyDescription == TEXT_OTPSET_SECRETKEY
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then OTP 설정 페이지에서 비밀 키 정보가 출력된다')


@step("OTP 설정 페이지에서 \[복사\]버튼을 클릭한다")
def click_otpSettingCopyBtn(self):
    try:
        # [복사]버튼 클릭
        copyButton = self.driver.find_element_by_css_selector("[data-ta='elm-otp-secretcopy']")
        copyButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 [복사]버튼을 클릭한다')


@then("OTP 설정 페이지에서 비밀 키가 복사되었다는 토스트가 출력된다")
def print_otpSettingToastCopySecretKey(self):
    try:
        # 토스트 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        # 문구체크 안하기로 함 : assert copyToast == TOAST_OTPSET_COPY
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then OTP 설정 페이지에서 비밀 키가 복사되었다는 토스트가 출력된다')

@step("OTP 설정 페이지에서 인증 코드 입력필드에 붙혀넣기한다")
def paste_otpSettingPasteQRcode(self):
    try:
        # 붙혀넣기 (키보드 조작)
        otpcode_inputfield = self.driver.find_element_by_css_selector("[data-ta='elm-otp-code']")
        #otpcode_inputfield.send_keys(Keys.CONTROL, 'v')
        pyperclip.paste()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
    raise NotImplementedError(u'STEP: And 인증 코드 입력필드에 붙혀넣기한다')


@then("OTP 설정 페이지에서 인증 코드 입력필드에 복사한 비밀 키가 붙혀넣기된다")
def print_otpSettingPasteQRcode(self):
    try:
        # 붙혀넣기 (키보드 조작)
        otpcode_inputfield = self.driver.find_element_by_css_selector("[data-ta='elm-otp-code']")
        print(otpcode_inputfield)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 복사한 비밀 키가 붙혀넣기된다')

@step("OTP 설정 페이지에서 발급받은 비밀 키를 OTP앱에 입력하고 인증을 받는다")
def print_otpSetting(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 발급받은 비밀 키를 OTP앱에 입력하고 인증을 받는다')


@step("OTP 설정 페이지에서 인증 코드 입력필드가 출력된다")
def print_otpSettingCodeInput(self):
    try:
        # 인증 코드 입력필드 확인
        verificationCodeInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-otp-code']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 인증 코드 입력필드가 출력된다')


@step("OTP 설정 페이지에서 유효하지 않은 인증 코드를 입력한다")
def input_otpSettingInvalidCode(self):
    try:
        # 인증 코드 입력
        # inputOtpCode = self.driver.find_element_by_css_selector("[data-ta='elm-otp-code'] input")
        otp_otpCodeInputfield = self.driver.find_element_by_name("code")  # data-ta로 입력필드 클릭안되는 이슈
        otp_otpCodeInputfield.click()
        otp_otpCodeInputfield.clear()
        otp_otpCodeInputfield.send_keys(MFACODE_INVALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 유효하지 않은 인증 코드를 입력한다')


@step("OTP 설정 페이지에서 유효한 인증 코드를 입력한다")
def input_otpSettingValidCode(self):
    try:
        # 인증 코드 입력
        input_otpcode_valid = self.driver.find_element_by_css_selector("[data-ta='elm-otp-code'] input")
        input_otpcode_valid.clear()
        input_otpcode_valid.send_keys(MFACODE_VALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 유효한 인증 코드를 입력한다')


@step("2단계 인증을 설정하였다는 토스트가 출력된다")
def print_otpSettingToastActivated(self):
    try:
        # 토스트 확인
        copyToast = self.driver.find_element_by_css_selector("[data-ta='elm-otp-copytoast']").text
        assert copyToast == TOAST_MFACODE_SET
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증을 설정하였다는 토스트가 출력된다')


@step("OTP 설정 페이지에서 인증 코드에 미지원 문자\(한글\)을 입력한다")
def input_otpSettingInvalidCodeKo(self):
    try:
        # 인증 코드 입력
        # inputmfacode_ko = self.driver.find_element_by_css_selector("[data-ta='elm-otp-code'] input")
        inputmfacode_ko = self.driver.find_element_by_name("code")  # data-ta로 입력필드 클릭안되는 이슈
        inputmfacode_ko.click()
        inputmfacode_ko.clear()
        inputmfacode_ko.send_keys(TEXT_NUM)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 인증 코드에 미지원 문자(한글)을 입력한다')


@step("OTP 설정 페이지에서 인증 코드에 미지원 문자\(영어\)를 입력한다")
def input_otpSettingInvalidCodeEn(self):
    try:
        # 인증 코드 입력
        # inputmfacode_en = self.driver.find_element_by_css_selector("[data-ta='elm-otp-code'] input")
        inputmfacode_en = self.driver.find_element_by_name("code")  # data-ta로 입력필드 클릭안되는 이슈
        inputmfacode_en.click()
        inputmfacode_en.clear()
        inputmfacode_en.send_keys(TEXT_EN)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 인증 코드에 미지원 문자(영어)를 입력한다')


@step("OTP 설정 페이지에서 인증 코드에 미지원 문자\(특수문자\)를 입력한다")
def input_otpSettingInvalidCodeChar(self):
    try:
        # 인증 코드 입력
        # inputmfacode_en = self.driver.find_element_by_css_selector("[data-ta='elm-otp-code'] input")
        inputmfacode_en = self.driver.find_element_by_name("code")  # data-ta로 입력필드 클릭안되는 이슈
        inputmfacode_en.click()
        inputmfacode_en.clear()
        inputmfacode_en.send_keys(TEXT_CHAR)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 인증 코드에 미지원 문자(특수문자)를 입력한다')


@then("OTP 설정 페이지에서 인증 코드를 입력하라는 메시지가 출력된다")
def print_otpSettingMsgNullCode(self):
    try:
        # 인증 코드 설정 실패 메시지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-otp-code_err']")
        # assert msg_failActicated == MSG_MFA_CODE_NULL
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then OTP 설정 페이지에서 인증 코드를 입력하라는 메시지가 출력된다')


@then("OTP 설정 페이지에서 숫자만 입력하라는 메시지가 출력된다")
def print_otpSettingMsgInvalidCodeType(self):
    try:
        # 인증 코드 설정 실패 메시지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-otp-code_err']")
        #assert msg_failActicated == MSG_MFA_INVALID_CHAR
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then OTP 설정 페이지에서 숫자만 입력하라는 메시지가 출력된다')

@then("OTP 설정 페이지에서 인증 코드를 정확하게 입력하라는 메시지가 출력된다")
def print_otpSettingMsgInvalidCode(self):
    try:
        # 인증 코드 설정 실패 메시지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-otp-code_err']")
        #assert msg_failActicated == MSG_MFA_CODE_INVALID
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then OTP 설정 페이지에서 인증 코드를 정확하게 입력하라는 메시지가 출력된다')


@step("OTP 설정 페이지에서 \[설정하기\]버튼이 출력된다")
def print_otpSettingActivatedBtm(self):
    try:
        # [설정하기]버튼 확인
        activateBtn = self.driver.find_element_by_css_selector("[data-ta='elm-otp-activate']").text
        assert activateBtn == "설정하기"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 [설정하기]버튼이 출력된다')


@step("OTP 설정 페이지에서 \[설정하기\]버튼을 클릭한다")
def click_otpSettingActivatedBtm(self):
    try:
        # [설정하기]버튼 클릭
        otpActivateBtn = self.driver.find_element_by_css_selector("[data-ta='elm-otp-activate']")
        otpActivateBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 [설정하기]버튼이 출력된다')


@step("OTP 설정 페이지에서 \[다른 계정으로 로그인\]링크가 출력된다")
def print_otpSettingAnotherSignin(self):
    try:
        # [다른 계정으로 로그인]링크 확인
        goSignin = self.driver.find_element_by_css_selector("[data-ta='elm-signin-forgot']").text
        assert goSignin == "다른 계정으로 로그인"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 [다른 계정으로 로그인]링크가 출력된다')


@step("OTP 설정 페이지에서 \[다른 계정으로 로그인\]링크를 클릭한다")
def click_otpSettingAnotherSignin(self):
    try:
        # [다른 계정으로 로그인]링크 클릭
        anotherSignin = self.driver.find_element_by_css_selector("[data-ta='elm-signin-forgot']")
        anotherSignin.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And OTP 설정 페이지에서 [다른 계정으로 로그인]링크를 클릭한다')





# 2단계 인증페이지

@then("2단계 인증 페이지가 출력된다")
def go_mfa(self):
    try:
        # url 확인
        url = self.driver.current_url
        assert url == URL_MFA
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 2단계 인증 페이지가 출력된다')


@step("2단계 인증 페이지 안내가 출력된다")
def print_mfaInfo(self):
    try:
        # 2단계 인증 페이지 타이틀 확인
        mfaTitle = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-title']").text
        assert mfaTitle == TEXT_MFA_TITLE
        # 2단계 인증 페이지 설명 확인
        mfaDescription = self.driver.find_element_by_css_selector(
                             "[data-ta='elm-mfa-desc']").text
        assert mfaDescription == TEXT_MFA_DESC
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 안내문구가 출력된다')


@step("2단계 인증페이지에서 인증 코드 입력필드가 출력된다")
def print_mfaCodeInput(self):
    try:
        # 인증 코드 입력필드 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 인증 코드 입력필드가 출력된다')


@step("2단계 인증페이지에서 유효한 인증 코드를 입력한다")
def input_mfaValidCode(self):
    try:
        # 비밀번호 입력
        signinPWInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code'] input")
        signinPWInputfield.clear()
        signinPWInputfield.send_keys(MFACODE_VALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 유효한 인증 코드를 입력한다')


@step("2단계 인증페이지에서 유효하지 않은 인증 코드를 입력한다")
def input_mfaInvalidCode(self):
    try:
        # 인증 코드 입력
        inputmfacode_invalid = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code'] input")
        inputmfacode_invalid.clear()
        inputmfacode_invalid.send_keys(MFACODE_INVALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 유효하지 않은 인증 코드를 입력한다')


@step("2단계 인증페이지에서 인증 코드에 미지원 문자\(한글\)를 입력한다")
def input_mfaInvalidCodeTypeKo(self):
    try:
        # 인증 코드 입력
        # inputmfacode_ko = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code'] input")
        inputmfacode_ko = self.driver.find_element_by_name("code")  # data-ta로 입력필드 클릭안되는 이슈
        inputmfacode_ko.click()
        inputmfacode_ko.clear()
        inputmfacode_ko.send_keys(TEXT_KO)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 인증 코드에 미지원 문자(한글)를 입력한다')

@step("2단계 인증페이지에서 인증 코드에 미지원 문자\(영어\)를 입력한다")
def input_mfaInvalidCodeTypeEn(self):
    try:
        # 인증 코드 입력
        # inputmfacode_en = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code'] input")
        inputmfacode_en = self.driver.find_element_by_name("code")  # data-ta로 입력필드 클릭안되는 이슈
        inputmfacode_en.click()
        inputmfacode_en.clear()
        inputmfacode_en.send_keys(TEXT_EN)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 인증 코드에 미지원 문자(영어)를 입력한다')


@step("2단계 인증페이지에서 인증 코드에 미지원 문자\(특수문자\)를 입력한다")
def input_mfaInvalidCodeTypeChar(self):
    try:
        # 인증 코드 입력
        # inputmfacode_en = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code'] input")
        inputmfacode_en = self.driver.find_element_by_name("code")  # data-ta로 입력필드 클릭안되는 이슈
        inputmfacode_en.click()
        inputmfacode_en.clear()
        inputmfacode_en.send_keys(TEXT_CHAR)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 인증 코드에 미지원 문자(특수문자)를 입력한다')

@then("2단계 인증페이지에서 인증 코드를 입력하라는 메시지가 출력된다")
def print_mfaMsgNullCodeInput(self):
    try:
        # 인증 코드 설정 실패 메시지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code_err']")
        #assert msg_failActicated == MSG_MFA_CODE_NULL
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 2단계 인증페이지에서 인증 코드를 입력하라는 메시지가 출력된다')

@then("2단계 인증페이지에서 숫자만 입력하라는 메시지가 출력된다")
def print_mfaMsgOnlyNumCode(self):
    try:
        # 인증 코드 설정 실패 메시지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code_err']")
        #assert msg_failActicated == MSG_MFA_INVALID_CHAR
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 2단계 인증페이지에서 숫자만 입력하라는 메시지가 출력된다')


@then("2단계 인증페이지에서 인증 코드를 정확하게 입력하라는 메시지가 출력된다")
def print_mfaMsgValidCode(self):
    try:
        # 인증 코드 설정 실패 메시지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-mfa-code_err']")
        #assert msg_failActicated == MSG_MFA_CODE_INVALID
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 2단계 인증페이지에서 인증 코드를 정확하게 입력하라는 메시지가 출력된다')


@step("2단계 인증페이지에서 \[로그인\]버튼이 출력된다")
def print_mfaSigninBtn(self):
    try:
        # [로그인]버튼 확인
        mfasigninButton = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-signin']").text
        assert mfasigninButton == "로그인"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에 [로그인]버튼이 출력된다')


@step("2단계 인증페이지에서 \[로그인\]버튼을 클릭한다")
def click_mfaSigninBtn(self):
    try:
        # [로그인]버튼 클릭
        anotherSignin = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-signin']")
        anotherSignin.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 [로그인]버튼을 클릭한다')


@step("2단계 인증페이지에서 \[다른 계정으로 로그인\]링크가 출력된다")
def print_mfaAnotherSignin(self):
    try:
        # [다른 계정으로 로그인]링크 확인
        AnotherAccountButton = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-back']").text
        assert AnotherAccountButton == "다른 계정으로 로그인"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 [다른 계정으로 로그인]링크가 출력된다')

@step("2단계 인증페이지에서 \[다른 계정으로 로그인\]링크를 클릭한다")
def click_mfaAnotherSignin(self):
    try:
        # [다른 계정으로 로그인]링크 클릭
        anotherSignin = self.driver.find_element_by_css_selector("[data-ta='elm-mfa-back']")
        anotherSignin.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증페이지에서 [다른 계정으로 로그인]링크를 클릭한다')






# 2단계 인증 설정완료 페이지

@then("2단계 인증 설정완료 페이지로 이동한다")
def goMfadone(self):
    try:
        # url 확인
        url = self.driver.current_url
        assert url == URL_MFADONE
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 2단계 인증 설정완료 페이지가 출력된다')


@step("2단계 인증 설정완료 페이지 안내가 출력된다")
def goMfadoneElm(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And 2단계 인증 설정완료 페이지 안내가 출력된다')


@step("2단계 인증 설정완료 페이지에서 \[확인\]버튼이 출력된다")
def printOkBtn(self):
    try:
        # [확인]버튼 확인
        okButton = self.driver.find_element_by_css_selector("[data-ta='elm-mfadone-ok']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정완료 페이지에서 [확인]버튼이 출력된다')


@step("2단계 인증 설정완료 페이지에서 \[확인\]버튼을 클릭한다")
def clickOkBtn(self):
    try:
        # [확인]버튼 클릭
        okButton = self.driver.find_element_by_css_selector("[data-ta='elm-mfadone-ok']")
        okButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정완료 페이지에서 [확인]버튼을 클릭한다')
