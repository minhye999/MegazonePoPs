from behave import *
from selenium import webdriver
import logging
import time
from features.steps.common import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")


# 사전 조건

@step("메가존 로그인 페이지로 이동한다")
def go_signin(self):
    try:
        # url 이동
        self.driver.get(URL_SIGNIN)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지로 이동한다')




# 비밀번호 재설정 페이지

@then("비밀번호 재설정 페이지가 출력된다")
def print_pwReset(self):
    try:
        # url 확인
        url = self.driver.current_url
        assert url == URL_SINGIN_FORGOT_PASSWORD
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 비밀번호 재설정 페이지가 출력된다')


@step("비밀번호 재설정 페이지 안내가 출력된다")
def print_pwResetInfo(self):
    try:
        # 비밀번호 재설정 타이틀 확인
        resetYourPasswordTitle = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-title']").text
        assert resetYourPasswordTitle == TEXT_RESETPW_TITLE
        # 비밀번호 재설정 설명 확인
        resetYourPasswordDescription = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-desc']").text
        assert resetYourPasswordDescription == TEXT_RESETPW_DESC
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 페이지 안내가 출력된다')


@step("비밀번호 재설정 페이지에서 이메일 입력필드가 출력된다")
def print_pwResetEmail(self):
    try:
        # 이메일 입력필드 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-username']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 페이지에서 이메일 입력필드가 출력된다')


@when("비밀번호 재설정 페이지에서 이메일 입력필드에 미지원 형식의 텍스트를 입력한다")
def input_pwResetInvalidEmailType(self):
    try:
        # 이메일 입력
        signinEmailInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-username'] input")
        signinEmailInputfield.clear()
        signinEmailInputfield.send_keys(EMAIL_INVALID_TYPE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 비밀번호 재설정 페이지에서 이메일 입력필드에 미지원 형식의 텍스트를 입력한다')


@when("비밀번호 재설정 페이지에서 이메일 입력필드에 미지원 텍스트\(한글\)를 입력한다")
def input_pwResetInvalidEmailKo(self):
    try:
        # 이메일 입력
        signinEmailInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-username'] input")
        signinEmailInputfield.clear()
        signinEmailInputfield.send_keys(TEXT_KO)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 비밀번호 재설정 페이지에서 이메일 입력필드에 미지원 텍스트(한글)를 입력한다')


@when("비밀번호 재설정 페이지에서 이메일 입력필드에 미지원 텍스트\(이메일에 허용안되는 특수문자\)를 입력한다")
def input_pwResetInvalidChar(self):
    try:
        # 이메일 입력
        signinEmailInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-username'] input")
        signinEmailInputfield.clear()
        signinEmailInputfield.send_keys(TEXT_CHAR)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 비밀번호 재설정 페이지에서 이메일 입력필드에 미지원 텍스트(이메일에 허용안되는 특수문자)를 입력한다')


@then("비밀번호 재설정 페이지에서 이메일을 입력하라는 메시지가 출력된다")
def print_pwResetMsgInputEmail(self):
    try:
        # 이메일 형식 확인 실패 메시지 확인
        errorToast = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-username_err']").text
        assert errorToast == MSG_EMAIL_INVALID_NULL
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 비밀번호 재설정 페이지에서 이메일을 입력하라는 메시지가 출력된다')


@then("비밀번호 재설정 페이지에서 이메일 형식으로 입력하라는 메시지가 출력된다")
def print_pwResetMsgInputType(self):
    try:
        # 이메일 형식 확인 실패 메시지 확인
        errorToast = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-username_err']").text
        #assert errorToast == MSG_EMAIL_INVALID_TYPE
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 비밀번호 재설정 페이지에서 이메일 형식으로 입력하라는 메시지가 출력된다')

@when("비밀번호 재설정 페이지에서 유효한 이메일을 입력한다")
def input_pwResetValidEmail(self):
    try:
        # 이메일 입력
        signinEmailInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-username'] input")
        signinEmailInputfield.clear()
        signinEmailInputfield.send_keys(EMAIL_VALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 비밀번호 재설정 페이지에서 유효한 이메일을 입력한다')


@step("비밀번호 재설정 페이지에서 \[메일 발송\]버튼이 출력된다")
def printSendMailbtn(self):
    try:
        # [메일 발송]버튼 확인
        sendEmailButton = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-send']").text
        assert sendEmailButton == "메일 발송"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 페이지에서 [메일 발송]버튼이 출력된다')


@step("비밀번호 재설정 페이지에서 \[메일 발송\]버튼을 클릭한다")
def click_pwResetSendMainBtn(self):
    try:
        # [메일 발송]버튼 클릭
        sendEmailButton = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-send']")
        sendEmailButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 페이지에서 [메일 발송]버튼을 클릭한다')


@step("비밀번호 재설정 페이지에서 \[로그인 화면으로\]링크가 출력된다")
def print_pwResetGoSignin(self):
    try:
        # [로그인 화면으로]링크 확인
        returnToSignInLink = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-back']").text
        assert returnToSignInLink == "로그인 화면으로"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 페이지에 [로그인 화면으로]링크가 출력된다')


@step("비밀번호 재설정 페이지에서 \[로그인 화면으로\]링크를 클릭한다")
def click_pwResetGoSignin(self):
    try:
        # [로그인 화면으로]링크 클릭
        returnToSignInLink = self.driver.find_element_by_css_selector("[data-ta='elm-resetpw-back']")
        returnToSignInLink.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 페이지의 [로그인 화면으로]버튼을 클릭한다')





# 비밀번호 재설정 메일 발송완료 페이지

@then("비밀번호 재설정 메일 발송완료 페이지로 이동한다")
def go_pwResetDone(self):
    try:
        # url 확인
        url = self.driver.current_url
        assert url == URL_SINGIN_SEND_RESETPWMAIL
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 비밀번호 재설정 메일 발송완료 페이지가 출력된다')


@step("비밀번호 재설정 메일 발송완료 페이지 이미지가 출력된다")
def print_pwResetDoneImage(self):
    try:
        # 비밀번호 재설정 메일 발송완료 이미지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-pwsended-img']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 메일 발송완료 페이지 이미지가 출력된다')


@step("비밀번호 재설정 메일 발송완료 페이지 안내가 출력된다")
def print_pwResetDoneInfo(self):
    try:
        # 비밀번호 재설정 메일 발송완료 타이틀 확인
        resetYourPasswordTitle = self.driver.find_element_by_css_selector("[data-ta='elm-pwsended-title']").text
        assert resetYourPasswordTitle == TEXT_PWSENDED_TITLE
        # 비밀번호 재설정 메일 발송완료 설명 확인
        resetYourPasswordDescription = self.driver.find_element_by_css_selector("[data-ta='elm-pwsended-desc']").text
        assert resetYourPasswordDescription == TEXT_PWSENDED_DESC
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 메일 발송완료 페이지 안내가 출력된다')


@step("비밀번호 재설정 메일 발송완료 페이지에서 \[로그인 화면으로\]버튼이 출력된다")
def print_pwResetDoneGoSigninBtn(self):
    try:
        # [로그인 화면으로]버튼 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-pwsended-move']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 메일 발송완료 페이지에서 [로그인 화면으로]버튼이 출력된다')


@step("비밀번호 재설정 메일 발송완료 페이지에서 \[로그인 화면으로\]버튼을 클릭한다")
def click_pwResetDoneGoSigninBtn(self):
    try:
        # [로그인 화면으로]버튼 확인
        returnToSignInLink = self.driver.find_element_by_css_selector("[data-ta='elm-pwsended-move']")
        returnToSignInLink.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 비밀번호 재설정 페이지에서 [로그인 화면으로]버튼을 클릭한다')
