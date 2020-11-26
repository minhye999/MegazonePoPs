from behave import *
from selenium import webdriver
import logging
import time
from features.steps.common import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

use_step_matcher("re")

# 사전조건

@given("Chrome 브라우저를 실행한다")
def open_ChromeBrowser(self):
    self.driver = webdriver.Chrome(executable_path="F:/PyCharm/Project/Pops/venv/webdriver/chromedriver_v.0.86.exe")
    #self.driver = webdriver.Chrome(executable_path="../Pops/venv/webdriver/chromedriver_v.0.86.exe")
    self.driver.implicitly_wait(5)
    self.driver.maximize_window()


@given("IE 11 브라우저를 실행한다")
def open_IE11Browser(self):
    self.driver = webdriver.Chrome(executable_path="../Pops/venv/webdriver/iedriver.exe")
    self.driver.implicitly_wait(5)
    self.driver.maximize_window()
    raise NotImplementedError(u'STEP: Given 웹 브라우저를 실행한다')


@given("IE Edge 브라우저를 실행한다")
def open_IEedgeBrowser(self):
    self.driver = webdriver.Chrome(executable_path="../Pops/venv/webdriver/msedgedriver.exe")
    self.driver.implicitly_wait(5)
    self.driver.maximize_window()
    raise NotImplementedError(u'STEP: Given 웹 브라우저를 실행한다')


@given("Firefox 브라우저를 실행한다")
def open_FirefoxBrowser(self):
    self.driver = webdriver.Chrome(executable_path="../Pops/venv/webdriver/geckodriver.exe")
    self.driver.implicitly_wait(5)
    self.driver.maximize_window()
    raise NotImplementedError(u'STEP: Given 웹 브라우저를 실행한다')




# 로그인 페이지

@when("메가존 로그인 페이지로 이동한다")
def go_singin(self):
    try:
        # url 이동
        self.driver.get(URL_SIGNIN)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 메가존 로그인 페이지로 이동한다')


@then("메가존 로그인 페이지가 출력된다")
def print_singin(self):
    try:
        # url 확인
        url = self.driver.current_url
        assert url == URL_SIGNIN
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 메가존 로그인 페이지가 출력된다')


@step("메가존 로그인 페이지에서 안내가 출력된다")
def print_singinInfo(self):
    try:
        # 로그인 타이틀 확인
        singinTitle = self.driver.find_element_by_css_selector("[data-ta='elm-signin-title']").text
        assert singinTitle == TEXT_SINGIN_TITLE
        # 로그인 설명 확인
        singinDescription = self.driver.find_element_by_css_selector("[data-ta='elm-signin-desc']").text
        assert singinDescription == TEXT_SINGIN_DESC
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 안내가 출력된다')


@step("메가존 로그인 페이지에서 이메일 입력필드가 출력된다")
def print_singinEmailInput(self):
    try:
        # 이메일 입력필드 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-signin-username']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 이메일 입력필드가 출력된다')


@then("메가존 로그인 페이지에서 이메일 & 비밀번호가 필수 항목이라는 메시지가 출력된다")
def print_singinMsgNullEmailPW(self):
    try:
        # 로그인 실패 메시지 확인
        self.driver.implicitly_wait(10)
        msgFailSigninNull = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username_err']")
        assert MSG_SIGN_NULL_USERNAME == msgFailSigninNull.text
        msgFailSigninNull = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password_err']")
        assert MSG_SIGN_NULL_PW == msgFailSigninNull.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 메가존 로그인 페이지에서 이메일 & 비밀번호가 필수 항목이라는 메시지가 출력된다')

@then("메가존 로그인 페이지에서 이메일 필수 항목이라는 메시지가 출력된다")
def print_singinMsgNullEmail(self):
    try:
        # 로그인 실패 메시지 확인
        self.driver.implicitly_wait(10)
        msgFailSigninNull = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username_err']")
        assert MSG_SIGN_NULL_USERNAME == msgFailSigninNull.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 메가존 로그인 페이지에서 이메일 필수 항목이라는 메시지가 출력된다')


@when("메가존 로그인 페이지에서 이메일 입력필드에 미지원 형식의 텍스트를 입력한다")
def input_singinMsgInvalidEmailType(self):
    try:
        # 이메일 입력
        signinUsernameInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        signinUsernameInputfield.clear()
        signinUsernameInputfield.send_keys(EMAIL_INVALID_TYPE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 메가존 로그인 페이지에서 이메일 입력필드에 미지원 형식의 텍스트를 입력한다')


@step("메가존 로그인 페이지에서 이메일 입력필드에 미지원 텍스트\(한글\)을 입력한다")
def input_singinMsgInvalidEmailKo(self):
    try:
        # 이메일 입력
        signinUsernameInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        signinUsernameInputfield.clear()
        signinUsernameInputfield.send_keys(TEXT_KO)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 이메일 입력필드에 미지원 텍스트(한글)을 입력한다')

@when("메가존 로그인 페이지에서 이메일 입력필드에 미지원 텍스트\(이메일에 허용안되는 특수문자\)를 입력한다")
def input_singinMsgInvalidEmailChar(self):
    try:
        # 이메일 입력
        signinUsernameInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        signinUsernameInputfield.clear()
        signinUsernameInputfield.send_keys(TEXT_CHAR)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 메가존 로그인 페이지에서 이메일 입력필드에 미지원 텍스트(이메일에 허용안되는 특수문자)를 입력한다')


@then("메가존 로그인 페이지에서 이메일 형식으로 입력하라는 메시지가 출력된다")
def print_singinMsgInvalidEmailType(self):
    try:
        # 로그인 실패 메시지 확인
        self.driver.implicitly_wait(10)
        msgFailSigninNull = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username_err']")
        #assert MSG_SIGNIN_INVALID_TYPE == msgFailSigninNull.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 메가존 로그인 페이지에서 이메일 형식으로 입력하라는 메시지가 출력된다')


@step("메가존 로그인 페이지에서 유효하지 않은 이메일을 입력한다")
def input_singinMsgInvalidEmail(self):
    try:
        # 이메일 입력
        signinUsernameInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        signinUsernameInputfield.clear()
        signinUsernameInputfield.send_keys(USERNAME_INVALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 유효하지 않은 이메일을 입력한다')


@step("2단계 인증 필요없는 계정의 이메일을 입력한다")
def input_singinUnneedMfa(self):
    try:
        # 이메일 입력
        signinUsernameInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        signinUsernameInputfield.clear()
        signinUsernameInputfield.send_keys(USERNAME_UNNEEDMFA)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 필요없는 계정의 이메일을 입력한다')


@step("2단계 인증 필요한 계정의 이메일을 입력한다")
def input_singinNeedMfa(self):
    try:
        # 이메일 입력
        signinUsernameInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        signinUsernameInputfield.clear()
        signinUsernameInputfield.send_keys(USERNAME_NEEDMFA)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 필요한 계정의 이메일을 입력한다')


@step("2단계 인증 설정된 계정의 이메일을 입력한다")
def input_singinHadMfa(self):
    try:
        # 이메일 입력
        signinUsernameInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        signinUsernameInputfield.clear()
        signinUsernameInputfield.send_keys(USERNAME_HADMFA)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정된 계정의 이메일을 입력한다')


@step("메가존 로그인 페이지에서 비밀번호 입력필드가 출력된다")
def print_singinPWInput(self):
    try:
        # 비밀번호 입력필드 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-signin-password'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 비밀번호 입력필드가 출력된다')


@then("메가존 로그인 페이지에서 비밀번호 필수 항목이라는 메시지가 출력된다")
def print_singinMsgNullPW(self):
    try:
        # 로그인 실패 메시지 확인
        self.driver.implicitly_wait(10)
        msgFailSigninNull = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password_err']")
        assert MSG_SIGN_NULL_PW == msgFailSigninNull.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 메가존 로그인 페이지에서 비밀번호 필수 항목이라는 메시지가 출력된다')


@step("메가존 로그인 페이지에서 유효하지 않은 비밀번호를 입력한다")
def input_singinInvalidPW(self):
    try:
        # 비밀번호 입력
        signinPWInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password'] input")
        signinPWInputfield.clear()
        signinPWInputfield.send_keys(PASSWORD_INVALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 유효하지 않은 비밀번호를 입력한다')


@when("메가존 로그인 페이지에서 비밀번호 입력필드에 최소 길이 미만의 텍스트를 입력한다")
def input_singinPWMinLess(self):
    try:
        # 비밀번호 입력
        signinPWInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password'] input")
        signinPWInputfield.clear()
        signinPWInputfield.send_keys(PW_INVALID_LIMIT_LESS)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 메가존 로그인 페이지에서 비밀번호 입력필드에 최소 길이 미만의 텍스트를 입력한다')


@step("2단계 인증 필요없는 계정의 비밀번호를 입력한다")
def input_singinPWUneedMfa(self):
    try:
        # 비밀번호 입력
        signinPWInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password'] input")
        signinPWInputfield.clear()
        signinPWInputfield.send_keys(PASSWORD_UNNEEDMFA_USER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 필요없는 계정의 비밀번호를 입력한다')


@step("2단계 인증 필요한 계정의 비밀번호를 입력한다")
def input_singinPWNeedMfa(self):
    try:
        # 비밀번호 입력
        signinPWInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password'] input")
        signinPWInputfield.clear()
        signinPWInputfield.send_keys(PASSWORD_NEEDMFA_USER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 필요한 계정의 비밀번호를 입력한다')


@step("2단계 인증 설정된 계정의 비밀번호를 입력한다")
def input_singinPWHadMfa(self):
    try:
        # 비밀번호 입력
        signinPWInputfield = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password'] input")
        signinPWInputfield.clear()
        signinPWInputfield.send_keys(PASSWORD_UNNEEDMFA_USER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증 설정된 계정의 비밀번호를 입력한다')


@then("메가존 로그인 페이지에서 비밀번호 최소 글자 수 이상으로 입력하라는 메시지가 출력된다")
def print_singinMsgMinPW(self):
    try:
        # 로그인 실패 메시지 확인
        self.driver.implicitly_wait(10)
        msgFailSigninMinLess = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password_err']")
        #assert MSG_SIGNIN_INVALID_PW_LIMIT_LESS == msgFailSigninMinLess.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 메가존 로그인 페이지에서 비밀번호 최소 글자 수 이상으로 입력하라는 메시지가 출력된다')


@then("메가존 로그인 페이지에서 이메일 또는 비밀번호를 정확하게 입력하라는 메시지가 출력된다")
def print_singinMsgInvalidUsernamePW(self):
    try:
        # 로그인 실패 메시지 확인
        self.driver.implicitly_wait(10)
        msgFailSignin = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password_err']")
        assert MSG_SIGNIN_INVALID_TEXT == msgFailSignin.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 메가존 로그인 페이지에서 이메일 또는 비밀번호를 정확하게 입력하라는 메시지가 출력된다')


@step("메가존 로그인 페이지에서 \[로그인\]버튼이 출력된다")
def print_singinSigninBtn(self):
    try:
        # [로그인]버튼 확인
        signinButton = self.driver.find_element_by_css_selector("[data-ta='elm-signin-signin']").text
        assert signinButton == "로그인"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 [로그인]버튼이 출력된다')


@step("메가존 로그인 페이지에서 \[로그인\]버튼을 클릭한다")
def click_singinSigninBtn(self):
    try:
        # [로그인]버튼 클릭
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='elm-signin-signin']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 [로그인]버튼을 클릭한다')


@then("대시보드 페이지로 이동한다")
def go_dashboard(self):
    try:
        # 대시보드 url 확인
        url = self.driver.current_url
        assert url == URL_DASHBOARD
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 로그인되고 대시보드로 이동한다')


@step("메가존 로그인 페이지에서 \[비밀번호를 잃어버리셨나요\?\]버튼이 출력된다")
def print_forgotPWBtn(self):
    try:
        # [비밀번호를 잃어버리셨나요?]버튼 확인
        forgotPasswordButton = self.driver.find_element_by_css_selector("[data-ta='elm-signin-forgot']").text
        assert forgotPasswordButton == "비밀번호를 잃어버리셨나요?"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 [비밀번호를 잃어버리셨나요?]버튼이 출력된다')


@step("메가존 로그인 페이지에서 \[비밀번호를 잃어버리셨나요\?\]버튼을 클릭한다")
def click_forgotPWBtn(self):
    try:
        # [비밀번호를 잃어버리셨나요?]버튼 클릭
        forgotPasswordButton = self.driver.find_element_by_css_selector("[data-ta='elm-signin-forgot']")
        forgotPasswordButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 [비밀번호를 잃어버리셨나요?]버튼을 클릭한다')







# 페이지 공통

@step("Megazone Cloud 로고가 출력된다")
def print_logo(self):
    try:
        # logo 확인
        self.driver.find_element_by_css_selector("img[data-ta='elm-header-logo']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And Megazone Cloud 로고가 출력된다')


@step("\[이용약관\]텍스트가 출력된다")
def print_terms(self):
    try:
        # 이용약관 확인
        terms = self.driver.find_element_by_css_selector("[data-ta='elm-footer-terms']").text
        assert terms == "이용약관"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [이용약관]텍스트가 출력된다')


@step("\[개인정보처리방침\]텍스트가 출력된다")
def print_private(self):
    try:
        # 개인정보처리방침 확인
        privacyPolicy = self.driver.find_element_by_css_selector("[data-ta='elm-footer-private']").text
        assert privacyPolicy == "개인정보처리방침"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [개인정보처리방침]텍스트가 출력된다')


@step("Copyright가 출력된다")
def print_copyright(self):
    try:
        # copyright 확인
        copyright = self.driver.find_element_by_css_selector("[data-ta='elm-footer-copyright']").text
        assert copyright == TEXT_FOOTER_COPYRIGHT
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And Copyright가 출력된다')


@then("브라우저에서 설정한 언어가 출력된다")
def print_lang(self):
    try:
        # 적용된 언어 확인
        language = self.driver.find_element_by_css_selector("[data-ta='elm-footer-lang']").text
        assert language == "한국어"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 브라우저에서 설정한 언어가 출력된다')


@step("다국어 설정이 출력된다")
def print_langSet(self):
    try:
        # 다국어 설정 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-footer-lang']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 다국어 설정이 출력된다')


@step("다국어 설정영역을 클릭한다")
def click_langSet(self):
    try:
        # 다국어 설정영역 클릭
        language = self.driver.find_element_by_css_selector("[data-ta='elm-footer-lang']")
        language.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 다국어 설정영역을 클릭한다')


@step("설정메뉴에 \[한국어\]가 출력된다")
def click_langSet(self):
    try:
        # 다국어 설정영역 클릭
        korean = self.driver.find_element_by_css_selector("[data-ta='elm-footer-langko']").text
        assert korean == TEXT_FOOTER_KOREAN
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 설정메뉴에 [한국어]가 출력된다')


@step("설정메뉴에 \[영어\]가 출력된다")
def click_langSet(self):
    try:
        # 다국어 설정영역 클릭
        english = self.driver.find_element_by_css_selector("[data-ta='elm-footer-langen']").text
        assert english == TEXT_FOOTER_ENGLISH
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 설정메뉴에 [영어]가 출력된다')


@step("\[한국어\]를 선택한다")
def click_langKo(self):
    try:
        # 한국어 선택
        korean = self.driver.find_element_by_css_selector("[data-ta='elm-footer-langko']")
        korean.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [한귝어]를 선택한다')


@step("\[영어\]를 선택한다")
def click_langEn(self):
    try:
        # 영어 선택
        english = self.driver.find_element_by_css_selector("[data-ta='elm-footer-langen']")
        english.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [영어]를 선택한다')


@then("\[한국어\]로 페이지가 출력된다")
def print_Langko(self):
    try:
        # 선택한 한국어 적용 확인
        language = self.driver.find_element_by_css_selector("[data-ta='elm-footer-lang']").text
        assert language == "한국어"
        singinTitle = self.driver.find_element_by_css_selector("[data-ta='elm-signin-title']").text
        assert singinTitle == TEXT_SINGIN_TITLE
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then \[한국어\]로 페이지가 출력된다')


@then("\[영어\]로 페이지가 출력된다")
def print_LangEn(self):
    try:
        # 선택한 한국어 적용 확인
        language = self.driver.find_element_by_css_selector("[data-ta='elm-footer-lang']").text
        assert language == "ENGLISH"
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then \[영어\]로 페이지가 출력된다')






# 기타

@step("브라우저에 로그아웃 url을 입력한다")
def go_logout(self):
    try:
        # 로그아웃 url 이동
        self.driver.get("http://login.mzdev.com/logout?redirect=http://www.naver.com")
        print(URL_SIGNOUT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 브라우저에 로그아웃 url을 입력한다')


@when("앱으로 이동한다")
def go_anotherApp(self):
    try:
        # 다른 앱 url 이동
        self.driver.get(URL_CPD)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 앱으로 이동한다')


@step("앱\[로그인\]버튼을 클릭한다")
def click_appSinginBtn(self):
    try:
        # 다른 앱에서 [로그인]버튼 클릭하여 메가존 로그인 페이지로 이동
        self.driver.find_element_by_link_text(u"메가존 계정 로그인").click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [로그인]버튼을 클릭한다')


@when("존재하지 않는 페이지로 이동한다")
def go_notFound(self):
    try:
        # url 이동
        self.driver.get(URL_NOTFOUND)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 존재하지 않는 페이지로 이동한다')


@then("존재하지 않는 페이지가 출력된다")
def print_notFound(self):
    try:
        # url 확인
        url = self.driver.current_url
        assert url == URL_NOTFOUND
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 페이지를 찾을 수 없다고 출력된다')


@step("존재하지 않는 페이지 안내가 출력된다")
def print_notFoundInfo(self):
    try:
        # 존재하지 않는 페이지 이미지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-err-img']")
        # 존재하지 않는 페이지 타이틀 확인
        pageNotFoundTitle = self.driver.find_element_by_css_selector("[data-ta='elm-err-title']").text
        assert pageNotFoundTitle == TEXT_404_TITLE
        # 존재하지 않는 페이지 설명 확인
        pageNotFoundDescription = self.driver.find_element_by_css_selector("[data-ta='elm-err-desc']").text
        assert pageNotFoundDescription == TEXT_404_DESC
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 존재하지 않는 페이지 안내가 출력된다')


@step("존재하지 않는 페이지 \[확인\]버튼이 출력된다")
def print_notFoundOkBtn(self):
    try:
        # [확인]버튼 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-err-ok']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 존재하지 않는 페이지 [확인]버튼이 출력된다')


@step("존재하지 않는 페이지 \[확인\]버튼을 클릭한다")
def click_notFoundOkBtn(self):
    try:
        # [확인]버튼 클릭
        pageNotFoundTitle = self.driver.find_element_by_css_selector("[data-ta='elm-err-ok']")
        pageNotFoundTitle.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 존재하지 않는 페이지 [확인]버튼을 클릭한다')


@step("존재하지 않는 페이지 이미지가 출력된다")
def print_notFoundImg(self):
    try:
        # 이미지 확인
        self.driver.find_element_by_css_selector("[data-ta='elm-err-img']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 존재하지 않는 페이지 이미지가 출력된다')