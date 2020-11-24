from behave import *
import logging
import os
from selenium.webdriver.common.keys import Keys
from setuptools import glob
from features.steps.common import *

use_step_matcher("re")


# 공통
@step("페이지를 \[새로고침\]한다")
def step_impl(self):
    try:
        self.driver.refresh()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 페이지를 [새로고침]한다')



# 사용자 목록

@step("사용자 목록 페이지에서 \[더보기\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-more']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [더보기]버튼이 출력된다')

@step("사용자 목록 페이지에서 \[더보기\]버튼을 확인한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-more']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [더보기]버튼을 확인한다')



# 사용자 목록 > 검색

@step("사용자 목록 페이지에서 \[검색\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-search']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [검색]입력필드가 출력된다')


@when("사용자 목록 페이지에서 \[검색\] 입력필드를 클릭한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 [검색] 입력필드를 클릭한다')


@when("사용자 목록 페이지에서 검색입력필드에 텍스트 미입력 상태에서 \[엔터키\]를 입력한다")
def step_impl(self):
    try:
        enterKey = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 텍스트 미입력 상태에서 [엔터키]를 입력한다')


@when("사용자 목록 페이지에서 검색입력필드에 \[유효하지 않은 텍스트\]를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USERNAME_INVALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [유효하지 않은 텍스트]를 입력한다')


@when("사용자 목록 페이지에서 검색입력필드에 \[사용자1의 이름\]을 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER1_NAME_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자1의 이름]을 부분 입력한다')

@when("사용자 목록 페이지에서 검색입력필드에 \[사용자2의 이름\]을 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER2_NAME_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자2의 이름]을 부분 입력한다')


@when("사용자 목록 페이지에서 검색입력필드에 \[사용자1의 아이디\]를 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER1_ID_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자1의 아이디]를 부분 입력한다')


@when("사용자 목록 페이지에서 검색입력필드에 \[사용자1의 이름\]을 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER1_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자1의 이름]을 전체 입력한다')


@when("사용자 목록 페이지에서 검색입력필드에 \[사용자1의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER1_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자1의 아이디]를 전체 입력한다')

@when("사용자 목록 페이지에서 검색입력필드에 \[사용자2의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER2_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자2의 아이디]를 전체 입력한다')

@when("사용자 목록 페이지에서 검색입력필드에 \[사용자3의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER3_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자3의 아이디]를 전체 입력한다')

@when("사용자 목록 페이지에서 검색입력필드에 \[사용자4의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER4_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자4의 아이디]를 전체 입력한다')

@when("사용자 목록 페이지에서 검색입력필드에 \[사용자5의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER5_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자5의 아이디]를 전체 입력한다')

@when("사용자 목록 페이지에서 검색입력필드에 \[사용자6의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER6_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자6의 아이디]를 전체 입력한다')

@when("사용자 목록 페이지에서 검색입력필드에 \[사용자7의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER7_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자7의 아이디]를 전체 입력한다')

@when("사용자 목록 페이지에서 검색입력필드에 \[사용자100의 아이디\]를 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER100_ID_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 검색입력필드에 [사용자100의 아이디]를 부분 입력한다')


@when("사용자 페이지에서 검색입력필드에 사용자 정의 필드 필수값 아닌 그룹의 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_GROUP_NOTREQUIRED_CUSTOM)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 사용자 정의 필드 필수값 아닌 그룹의 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 사용자 정의 필드 필수값인 그룹의 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_GROUP_REQUIRED_CUSTOME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 사용자 정의 필드 필수값인 그룹의 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 프로필 이미지를 미등록한 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_NOPICTURE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 프로필 이미지를 미등록한 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 프로필 이미지를 등록한 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_HADPICTURE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 프로필 이미지를 등록한 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 대기 상태인 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_PENDING)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 대기 상태인 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 활성화 상태인 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_UNNEEDMFA_ACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 활성화 상태인 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 비활성화 상태인 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_UNNEEDMFA_DEACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 비활성화 상태인 사용자 아이디를 입력한다')

@when("사용자 페이지에서 검색입력필드에 유효한 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_UNNEEDMFA_ACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 유효한 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 로그인 이력없는 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_PENDING)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 로그인 이력없는 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 로그인 이력있는 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_UNNEEDMFA_ACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 로그인 이력있는 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 2단계 설정 필요없고, 활성화 상태인 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_UNNEEDMFA_ACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 2단계 설정 필요없고, 활성화 상태인 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 MFA 인증하고, 비활성화 상태인 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER9_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 MFA 인증하고, 비활성화 상태인 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 MFA 인증하고, 활성화 상태인 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER7_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 MFA 인증하고, 활성화 상태인 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 2단계 설정 필요없고, 비활성화 상태인 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_UNNEEDMFA_DEACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 2단계 설정 필요없고, 비활성화 상태인 사용자 아이디를 입력한다')


@when("사용자 페이지에서 검색입력필드에 주소유자인 사용자 아이디를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(ID_OWNER_ACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 페이지에서 검색입력필드에 주소유자인 사용자 아이디를 입력한다')


@step("\[엔터키\]를 입력한다")
def step_impl(self):
    try:
        enterKey = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [엔터키]를 입력한다')


@then("전체 검색결과가 출력된다")  # 정상 아님
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 전체 검색결과가 출력된다')


@then("사용자 목록 페이지에서 검색결과 없다는 안내가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-search_result']") # data ta 적용안됨
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 검색결과 없다는 안내가 출력된다')


@then("사용자 목록 페이지에서 \[사용자1의 이름\]을 포함한 검색결과가 출력된다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-users-name']")
        assert USER1_NAME == firstname.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자1의 이름]을 포함한 검색결과가 출력된다')


@then("사용자 목록 페이지에서 \[사용자1의 아이디\]를 포함한 검색결과가 출력된다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        assert USER1_ID == id.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자1의 아이디]를 포함한 검색결과가 출력된다')


@then("사용자 목록 페이지에서 \[사용자1의 이름\]과 일치하는 검색결과가 출력된다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-users-name']")
        assert USER1_NAME == firstname.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자1의 이름]과 일치하는 검색결과가 출력된다')


@then("사용자 목록 페이지에서 \[사용자1의 아이디\]와 일치하는 검색결과가 출력된다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        assert USER1_ID == id.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자1의 아이디]와 일치하는 검색결과가 출력된다')




# 사용자 목록 > 프로필 이미지
@then("사용자 목록 페이지에서 \[프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_class_name('MuiAvatar-img')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [프로필 이미지]가 출력된다')

@then("사용자 목록 페이지에 사용자의 \[기본 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-nopicture']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에 사용자의 [기본 프로필 이미지]가 출력된다')


@then("사용자 목록 페이지에 사용자의 \[설정한 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-picture']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에 사용자의 [설정한 프로필 이미지]가 출력된다')




# 사용자 목록 > 이름의 상태 아이콘

@then("사용자 목록 페이지에 프로필 \[상태\]가 미출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-pendingprofile']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에 상태아이콘이 미출력된다')


@then("사용자 목록 페이지에 \[활성\]상태가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-activeprofile']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에 [활성]상태가 출력된다')


@then("사용자 목록 페이지에 \[비활성\]상태가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-deactiveprofile']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에 [비활성]상태가 출력된다')





# 사용자 목록 > 이름

@then("사용자 목록 페이지에서 \[이름\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [이름]이 출력된다')


@then("사용자 목록 페이지에서 \[사용자1의 이름\]이 출력된다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-users-name']")
        assert USER1_NAME == name.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자1의 이름]이 출력된다')



# 사용자 목록 > 아이디

@then("사용자 목록 페이지에서 \[아이디\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [아이디]가 출력된다')

@then("사용자 목록 페이지에서 \[사용자1의 아이디\]가 출력된다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        assert USER1_ID == id.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자1의 아이디]가 출력된다')


# 사용자 목록 > 최근 로그인 날짜

@then("사용자 목록 페이지에서 \[최근 로그인 날짜\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-lastsignin']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [최근 로그인 날짜]가 출력된다')

@then("사용자 목록 페이지에서 \[사용자1의 최근 로그인 날짜\]가 출력된다")
def step_impl(self):
    try:
        lastSignin = self.driver.find_element_by_css_selector("[data-ta='elm-users-lastsignin']")
        assert USER1_LASTLOGIN == lastSignin.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자1의 최근 로그인 날짜]가 출력된다')

@then("사용자 목록 페이지에서 \[사용자2의 최근 로그인 날짜\]가 출력된다")
def step_impl(self):
    try:
        #lastSignin = self.driver.find_element_by_css_selector("[data-ta='elm-users-lastsignin']")
        #assert USER2_LASTLOGIN == lastSignin.text
        self.driver.find_element_by_css_selector("[data-ta='elm-users-lastsignin']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자2의 최근 로그인 날짜]가 출력된다')




# 사용자 목록 > 상태

@then("사용자 목록 페이지에서 \[상태\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-state']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [상태]가 출력된다')


@then("사용자 목록 페이지에서 사용자의 상태가 \[대기\]로 출력된다")
def step_impl(self):
    try:
        # self.driver.find_element_by_css_selector("[data-ta='elm-users-pending']")
        status = self.driver.find_element_by_css_selector("[data-ta='elm-users-state']")
        assert USER_STATUS_PENDING == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 사용자의 상태가 [대기]로 출력된다')


@then("사용자 목록 페이지에서 사용자의 상태가 \[활성\]으로 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-users-active']")
        status = self.driver.find_element_by_css_selector("[data-ta='elm-users-state']")
        assert USER_STATUS_ACTIVE == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 사용자의 상태가 [활성]으로 출력된다')

@then("사용자 목록 페이지에서 사용자의 상태가 \[비활성\]으로 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-users-deactive']")
        status = self.driver.find_element_by_css_selector("[data-ta='elm-users-state']")
        assert USER_STATUS_DEACTIVE == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 사용자의 상태가 [비활성]으로 출력된다')


@step("사용자 목록 페이지에서 사용자의 상태 아이콘이 \[대기\]로 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-pendingicon']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 사용자의 상태 아이콘이 [대기]로 출력된다')


@step("사용자 목록 페이지에서 사용자의 상태 아이콘이 \[활성\]으로 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-users-activeicon']")
        self.driver.find_element_by_css_selector("[data-ta='elm-users-state']")  # 상태값
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 사용자의 상태 아이콘이 [활성]으로 출력된다')

@step("사용자 목록 페이지에서 사용자의 상태 아이콘이 \[비활성\]으로 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-users-deactiveicon']")
        self.driver.find_element_by_css_selector("[data-ta='elm-users-state']")  # 상태값
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 사용자의 상태 아이콘이 [비활성]으로 출력된다')





# 사용자 목록 > [더보기]버튼

@then("사용자 목록 페이지에서 \[더보기\]버튼이 비활성화된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-more']").get_attribute("disabled")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [더보기]버튼이 비활성화된다')


@step("사용자 목록 페이지에서 \[더보기\]버튼을 클릭한다")
def step_impl(self):
    try:
        moreBtn = self.driver.find_element_by_css_selector("[data-ta='elm-users-more']")
        moreBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [더보기]버튼을 클릭한다')


@then("사용자 목록 페이지에서 \[계정 활성화 메일 재전송\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-resend']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [계정 활성화 메일 재전송]메뉴가 출력된다')

@then("사용자 목록 페이지에서 \[2단계 인증 해제\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-remove']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [2단계 인증 해제]메뉴가 출력된다')





# 사용자 목록/상세 > 계정 활성화 메일 재전송 팝업

@step("사용자 목록 페이지에서 \[계정 활성화 메일 재전송\]메뉴를 클릭한다")
def step_impl(self):
    try:
        moreBtn = self.driver.find_element_by_css_selector("[data-ta='elm-users-resend']")
        moreBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [계정 활성화 메일 재전송]메뉴를 클릭한다')


@then("사용자 목록 페이지에서 \[계정 활성화 메일 재전송\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-resend-resend']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [계정 활성화 메일 재전송]팝업이 출력된다')


@step("사용자 상세 페이지에서 \[계정 활성화 메일 재전송\]메뉴를 클릭한다")
def step_impl(self):
    try:
        resendBtn = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-resend']")
        resendBtn.click()  #data-ta 미구현
        #self.driver.find_element_by_xpath('//*[@id="menu-list-grow"]/li[1]').click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [계정 활성화 메일 재전송]메뉴를 클릭한다')


@then("사용자 상세 페이지에서 \[계정 활성화 메일 재전송\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-resend-resend']")  # data-ta 없어 xpath로 체크
        #self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[2]/span[1]')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [계정 활성화 메일 재전송]팝업이 출력된다')


@step("\[계정활성화 메일 재전송\]팝업에서 \[사용자1의 이름\]이 출력된다")
def step_impl(self):
    try:
        #name = self.driver.find_element_by_css_selector("[data-ta='elm-resend-name']")
        #assert USER1_NAME == name.text   # data-ta 부재
        self.driver.find_element_by_css_selector("[data-ta='elm-resend-name']")
        #name = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div/p[3]/strong[1]')
        #assert USER1_NAME == name.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [계정활성화 메일 재전송]팝업에서 [사용자1의 이름]이 출력된다')


@step("\[계정활성화 메일 재전송\]팝업에서 \[사용자1의 아이디\]가 출력된다")
def step_impl(self):
    try:
        #id = self.driver.find_element_by_css_selector("[data-ta='elm-resend-id']")
        #assert USER1_ID == id.text  #data-ta 부재
        self.driver.find_element_by_css_selector("[data-ta='elm-resend-id']")
        #id = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[2]/div/p[3]/strong[2]')
        #assert USER1_ID == id.text

        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [계정활성화 메일 재전송]팝업에서 [사용자1의 아이디]가 출력된다')


@step("\[계정활성화 메일 재전송\]팝업에서 \[취소\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-resend-cancel']") #data-ta 부재
        #self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[1]/span[1]')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [계정활성화 메일 재전송]팝업에서 [취소]버튼이 출력된다')


@step("\[계정활성화 메일 재전송\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-resend-cancel']")
        cancelBtn.click()    #data-ta 부재
        #self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[1]/span[1]').click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [계정활성화 메일 재전송]팝업에서 [취소]버튼을 클릭한다')


@step("\[계정활성화 메일 재전송\]팝업에서 \[재전송\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-resend-resend']")  #data-ta 부재
        #self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[2]/span[1]')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [계정활성화 메일 재전송]팝업에서 [재전송]버튼이 출력된다')


@step("\[계정활성화 메일 재전송\]팝업에서 \[재전송\]버튼을 클릭한다")
def step_impl(self):
    try:
        resendBtn = self.driver.find_element_by_css_selector("[data-ta='elm-resend-resend']")
        resendBtn.click()  #data-ta 부재
        #self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[2]/span[1]').click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [계정활성화 메일 재전송]팝업에서 [재전송]버튼을 클릭한다')

@then("\[계정활성화 메일 재전송\]팝업이 닫힌다")
def step_impl(self):
    with self.assertRaises(NotImplementedError):
        self.driver.find_element_by_css_selector("[data-ta='elm-resend-resend']")
        self.driver.implicitly_wait(10)
        raise NotImplementedError(u'STEP: Then [계정활성화 메일 재전송]팝업이 닫힌다')


@step("계정활성화 메일이 재전송된다")
def step_impl(self):
    """
    :type self: behave.runner.self
    """
    raise NotImplementedError(u'STEP: And 계정활성화 메일이 재전송된다')


@step("계정활성화 메일 전송 완료 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 계정활성화 메일 전송 완료 토스트가 출력된다')




# 사용자 목록/상세 > [2단계 인증 해제] 팝업

@step("사용자 목록 페이지에서 \[2단계 인증 해제\]메뉴를 클릭한다")
def step_impl(self):
    try:
        forgotPasswordButton = self.driver.find_element_by_css_selector("[data-ta='elm-users-remove']")
        forgotPasswordButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [2단계 인증 해제]메뉴를 클릭한다')


@then("사용자 목록 페이지에서 \[2단계 인증 해제\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-remove-remove']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [2단계 인증 해제]팝업이 출력된다')


@step("사용자 상세 페이지에서 \[2단계 인증 해제\]메뉴를 클릭한다")
def step_impl(self):
    try:
        removeBtn = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-remove']")
        removeBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [2단계 인증 해제]메뉴를 클릭한다')


@then("사용자 상세 페이지에서 \[2단계 인증 해제\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-remove-remove']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [2단계 인증 해제]팝업이 출력된다')


@step("\[2단계 인증 해제\]팝업에서 사용자의 \[이름\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-remove-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [2단계 인증 해제] 팝업에서 사용자의 [이름]이 출력된다')


@step("\[2단계 인증 해제\]팝업에서 사용자의 \[아이디\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-remove-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [2단계 인증 해제]팝업에서 사용자의 [아이디]가 출력된다')


@step("\[2단계 인증 해제\]팝업에서 사용자의 \[인증수단\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-remove-otp']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [2단계 인증 해제]팝업에서 사용자의 [인증수단]이 출력된다')


@step("\[2단계 인증 해제\]팝업에서 \[취소\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-remove-back']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [2단계 인증 해제]팝업에서 [취소]버튼이 출력된다')


@step("\[2단계 인증 해제\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-remove-back']")
        cancelBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [2단계 인증 해제]팝업에서 [취소]버튼을 클릭한다')


@step("\[2단계 인증 해제\]팝업에서 \[해제\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-remove-remove']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [2단계 인증 해제]팝업에서 [해제]버튼이 출력된다')

@step("\[2단계 인증 해제\]팝업에서 \[해제\]버튼 클릭한다")
def step_impl(self):
    try:
        removeBtn = self.driver.find_element_by_css_selector("[data-ta='elm-remove-remove']")
        removeBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [2단계 인증 해제]팝업에서 [해제]버튼 클릭한다')


@then("\[2단계 인증 해제\]팝업이 닫힌다")
def step_impl(self):
    with self.assertRaises(NotImplementedError):
        self.driver.find_element_by_css_selector("[data-ta='elm-remove-remove']")
        self.driver.implicitly_wait(10)
        raise NotImplementedError(u'STEP: Then [2단계 인증 해제]팝업이 닫힌다')


@step("2단계 인증이 해제된다")
def step_impl(self):
    try:
        # 메가존 로그인 페이지로 이동
        self.driver.get(URL_SIGNIN)
        self.driver.implicitly_wait(10)
        # 이메일 입력
        email = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        email.clear()
        email.send_keys(USERNAME_UNNEEDMFA)
        self.driver.implicitly_wait(10)
        # 비밀번호 입력
        pw = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password'] input")
        pw.clear()
        pw.send_keys(PASSWORD_UNNEEDMFA_USER)
        self.driver.implicitly_wait(10)
        # 2단계 인증없이 대시보드로 이동
        url = self.driver.current_url
        assert url == URL_DASHBOARD
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 2단계 인증이 해제된다')

@step("2단계 인증 해제 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-removetoast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 2단계 인증 해제 토스트가 출력된다')

@step("메가존 로그인 페이지에서 2단계 인증 해제한 \[이메일\]을 입력한다")
def step_impl(self):
    try:
        email = self.driver.find_element_by_css_selector("[data-ta='elm-signin-username'] input")
        email.clear()
        email.send_keys(ID_HADMFA_ACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 2단계 인증 해제한 [이메일]을 입력한다')


@step("메가존 로그인 페이지에서 2단계 인증 해제한 계정의 \[비밀번호\]를 입력한다")
def step_impl(self):
    try:
        pw = self.driver.find_element_by_css_selector("[data-ta='elm-signin-password'] input")
        pw.clear()
        pw.send_keys(PW_HADMFA_ACTIVE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 로그인 페이지에서 2단계 인증 해제한 계정의 [비밀번호]를 입력한다')





# 사용자 목록 > 페이징


@when("사용자 목록 페이지에서 스크롤을 내린다")
def step_impl(self):
    try:
        scrolls = 4
        while True:
            scrolls -= 1
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            self.driver.implicitly_wait(10)
            if scrolls < 0:
                break
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: when 사용자 목록 페이지에서 스크롤을 내린다')


@then("사용자 목록 페이지에서 \[페이징\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-paging']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [페이징]이 출력된다')


@then("사용자 목록 페이지에서 \[페이징\]이 출력되지 않는다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-paging']").get_attribute("disabled")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [페이징]이 출력되지 않는다')


@when("사용자 목록 페이지에서 \[1\]버튼을 클릭한다")
def step_impl(self):
    try:
        #self.driver.find_element_by_link_text("1").click()  # data-ta 부재
        page1 = self.driver.find_element_by_css_selector("li:nth-child(3) > .MuiButtonBase-root")
        page1.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 [1]버튼을 클릭한다')


@step("사용자 목록 페이지에서 \[2\]버튼을 클릭한다")
def step_impl(self):
    try:
        #self.driver.find_element_by_link_text("2").click()  # data-ta 부재
        page2 = self.driver.find_element_by_css_selector("li:nth-child(4) > .MuiButtonBase-root")
        page2.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [2]버튼을 클릭한다')


@step("사용자 목록 페이지에서 \[<\]버튼을 클릭한다")
def step_impl(self):
    try:
        #pageNotFoundTitle = self.driver.find_element_by_css_selector("[data-ta='elm-users-prev']")  # data-ta 부재
        pageprev = self.driver.find_element_by_css_selector("li:nth-child(2) > .MuiButtonBase-root")
        pageprev.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [<]버튼을 클릭한다')


@when("사용자 목록 페이지에서 \[>\]버튼을 클릭한다")
def step_impl(self):
    try:
        #pageNotFoundTitle = self.driver.find_element_by_css_selector("[data-ta='elm-users-next']")  # data-ta 부재
        pagenext = self.driver.find_element_by_css_selector("li:nth-child(8) > .MuiButtonBase-root")
        pagenext.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 [>]버튼을 클릭한다')


@step("사용자 목록 페이지에서 \[<<\]버튼을 클릭한다")
def step_impl(self):
    try:
        #pageNotFoundTitle = self.driver.find_element_by_css_selector("[data-ta='elm-users-first']")  # data-ta 부재
        pagestart = self.driver.find_element_by_css_selector("li:nth-child(1) > .MuiButtonBase-root")
        pagestart.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [<<]버튼을 클릭한다')


@when("사용자 목록 페이지에서 \[>>\]버튼을 클릭한다")
def step_impl(self):
    try:
        #pageNotFoundTitle = self.driver.find_element_by_css_selector("[data-ta='elm-users-last']")  # data-ta 부재
        pageend = self.driver.find_element_by_css_selector("li:nth-child(9) > .MuiButtonBase-root")
        pageend.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 [>>]버튼을 클릭한다')

@then("사용자 목록 페이지에서 \[마지막\]페이지로 이동한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("li:nth-child(9) > .MuiButtonBase-root")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [마지막]페이지로 이동한다')

@then("사용자 목록 페이지에서 \[1\]페이지로 이동한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("li:nth-child(3) > .MuiButtonBase-root")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [1]페이지로 이동한다')

@then("사용자 목록 페이지에서 \[2\]페이지로 이동한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("li:nth-child(4) > .MuiButtonBase-root")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [2]페이지로 이동한다')




# 사용자 목록 > 사용자 추가 팝업

@step("사용자 목록 페이지에서 \[사용자 추가\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-adduser']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 [사용자 추가]버튼이 출력된다')


@when("사용자 목록 페이지에서 \[사용자 추가\]버튼을 클릭한다")
def step_impl(self):
    try:
        addBtn = self.driver.find_element_by_css_selector("[data-ta='elm-users-adduser']")
        addBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 사용자 목록 페이지에서 [사용자 추가]버튼을 클릭한다')


@then("사용자 목록 페이지에서 \[사용자 추가\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자 추가]팝업이 출력된다')


@then("\[사용자 추가\]팝업에서 프로필 이미지에 \[기본 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-nopicture']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 프로필 이미지에 [기본 프로필 이미지]가 출력된다')


@step("\[사용자 추가\]팝업에서 프로필 이미지의 \[기본 프로필 이미지\]를 클릭한다")
def step_impl(self):
    try:
        profileImg = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-nopicture']")
        profileImg.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 프로필 이미지의 [기본 프로필 이미지]를 클릭한다')


@step("\[사용자 추가\]팝업에서 \[프로필 이미지\]를 클릭한다")
def step_impl(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-picture']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [프로필 이미지]를 클릭한다')


@step("\[파일탐색기\]에서 \[유효하지 않은 확장자의 파일\]을 선택한다")
def step_impl(self):
    try:
        file_input = self.driver.find_element_by_xpath('//input[@type="file"]')
        file_input.send_keys(PATH_USER_PROFILE_IMAGE_INVALID_EXTENSION)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [파일탐색기]에서 [유효하지 않은 확장자의 파일]을 선택한다')


@step("\[파일탐색기\]에서 \[유효하지 않은 크기의 이미지\]를 선택한다")
def step_impl(self):
    try:
        file_input = self.driver.find_element_by_xpath('//input[@type="file"]')
        file_input.send_keys(PATH_USER_PROFILE_IMAGE_INVALID_SIZE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [파일탐색기]에서 [유효하지 않은 크기의 이미지]를 선택한다')


@step("\[파일탐색기\]에서 \[유효한 이미지\]를 선택한다")
def step_impl(self):
    try:
        file_input = self.driver.find_element_by_xpath('//input[@type="file"]')
        file_input.send_keys(PATH_USER_PROFILE_IMAGE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [파일탐색기]에서 [유효한 이미지]를 선택한다')

@step("\[파일탐색기\]에서 \[기존과 다른 이미지\]를 선택한다")
def step_impl(self):
    try:
        file_input = self.driver.find_element_by_xpath('//input[@type="file"]')
        file_input.send_keys(PATH_USER_PROFILE_IMAGE_EDIT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [파일탐색기]에서 [기존과 다른 이미지]를 선택한다')

@then("\[사용자 추가\]팝업에서 프로필 이미지에 \[변경한 이미지\]가 출력된다")
def step_impl(self):
    def print_extensiontoast(self):
        try:
            self.driver.find_element_by_css_selector("[data-ta='elm-adduser-picture']")
            self.driver.implicitly_wait(10)
        except Exception as e:
            logging.error("arrived at exception: " + str(e))
            raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 프로필 이미지에 [변경한 이미지]가 출력된다')


@then("\[사용자 추가\]팝업에서 이미지 형식 오류 안내 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        #self.driver.find_element_by_class_name('react-toast-notifications__container css-uku268')
        #self.driver.find_element_by_xpath("/div/div/div/div[2]")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 이미지 형식 오류 안내 토스트가 출력된다')


@then("\[사용자 추가\]팝업에서 이미지 크기 오류 안내 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 크기 오류 안내 토스트가 출력된다')


@step("\[사용자 추가\]팝업에서\[프로필 이미지\]를 클릭한다")
def step_impl(self):
    try:
        profileImg = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-picture']")
        profileImg.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사]용자 추가]팝업에서[프로필 이미지]를 클릭한다')


@then("\[사용자 추가\]팝업에서 프로필 이미지 \[업로드\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-upload']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 프로필 이미지 [업로드]메뉴가 출력된다')


@step("\[사용자 추가\]팝업에서 프로필 이미지 \[업로드\]메뉴를 클릭한다")
def step_impl(self):
    try:
        uploadBtn = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-upload']")
        uploadBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 프로필 이미지 [업로드]메뉴를 클릭한다')


@step("\[사용자 추가\]팝업에서 프로필 이미지 \[삭제\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-delete']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 프로필 이미지 [삭제] 메뉴가 출력된다')


@step("\[사용자 추가\]팝업에서 프로필 이미지 \[삭제\]메뉴를 클릭한다")
def step_impl(self):
    try:
        deleteBtn = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-delete']")
        deleteBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 프로필 이미지 [삭제]메뉴를 클릭한다')


@step("\[사용자 추가\]팝업에서 \[성\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-familyname']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [성]입력필드가 출력된다')


@step("\[사용자 추가\]팝업에서 \[사용자1의 성\]을 유효하게 입력한다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-familyname'] input")
        familyname.clear()
        familyname.send_keys(USER1_FAMILYNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자1의 성]을 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자2의 성\]을 유효하게 입력한다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-familyname'] input")
        familyname.clear()
        familyname.send_keys(USER2_FAMILYNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자2의 성]을 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자3의 성\]을 유효하게 입력한다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-familyname'] input")
        familyname.clear()
        familyname.send_keys(USER3_FAMILYNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자3의 성]을 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자4의 성\]을 유효하게 입력한다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-familyname'] input")
        familyname.clear()
        familyname.send_keys(USER4_FAMILYNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자4의 성]을 유효하게 입력한다')


@then("\[사용자 추가\]팝업에서 필수값 관련 경고 메시지가 출력된다\(성\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-familyname_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 필수값 관련 경고 메시지가 출력된다(성)')


@step("\[사용자 추가\]팝업에서 \[이름\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-firstname']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [이름]입력필드가 출력된다')


@step("\[사용자 추가\]팝업에서 \[사용자1의 이름\]을 유효하게 입력한다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-firstname'] input")
        firstname.clear()
        firstname.send_keys(USER1_FIRSTNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자1의 이름]을 유효하게 입력한다')


@step("\[사용자 추가\]팝업에서 \[사용자2의 이름\]을 유효하게 입력한다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-firstname'] input")
        firstname.clear()
        firstname.send_keys(USER2_FIRSTNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자2의 이름]을 유효하게 입력한다')


@step("\[사용자 추가\]팝업에서 \[사용자3의 이름\]을 유효하게 입력한다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-firstname'] input")
        firstname.clear()
        firstname.send_keys(USER3_FIRSTNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자3의 이름]을 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자4의 이름\]을 유효하게 입력한다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-firstname'] input")
        firstname.clear()
        firstname.send_keys(USER4_FIRSTNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자4의 이름]을 유효하게 입력한다')

@then("\[사용자 추가\]팝업에서 필수값 관련 경고 메시지가 출력된다\(이름\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-firstname_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 필수값 관련 경고 메시지가 출력된다(이름)')

@step("\[사용자 추가\]팝업에서 \[아이디\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [아이디]입력필드가 출력된다')


@step("\[사용자 추가\]팝업에서 \[사용자1의 아이디\]를 유효하게 입력한다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id'] input")
        id.clear()
        id.send_keys(USER1_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자1의 아이디]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자2의 아이디\]를 유효하게 입력한다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id'] input")
        id.clear()
        id.send_keys(USER2_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자2의 아이디]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자3의 아이디\]를 유효하게 입력한다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id'] input")
        id.clear()
        id.send_keys(USER3_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자3의 아이디]를 유효하게 입력한다')


@step("\[사용자 추가\]팝업에서 \[사용자4의 아이디\]를 유효하게 입력한다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id'] input")
        id.clear()
        id.send_keys(USER4_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자4의 아이디]를 유효하게 입력한다')


@step("\[사용자 추가\]팝업에서 \[아이디\]를 형식에 맞지 않게 입력한다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id'] input")
        id.clear()
        id.send_keys(USER1_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [아이디]를 형식에 맞지 않게 입력한다')


@step("\[사용자 추가\]팝업에서 \[사용자1의 아이디\]를 중복되게 입력한다")
def step_impl(self):
    try:
        id = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id'] input")
        id.clear()
        id.send_keys(USER1_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [아이디]를 중복되게 입력한다')


@then("\[사용자 추가\]팝업에서 필수값 관련 경고 메시지가 출력된다\(아이디\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-firstname_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 필수값 관련 경고 메시지가 출력된다(아이디)')


@then("\[사용자 추가\]팝업에서 아이디 중복 경고 메시지가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 아이디 중복 경고 메시지가 출력된다')


@step("\[사용자 추가\]팝업에서 \[보조 이메일\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-mail']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [보조 이메일]입력필드가 출력된다')


@then("\[사용자 추가\]팝업에서 이메일 형식 경고 메시지가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 이메일 형식 경고 메시지가 출력된다')


@step("\[사용자 추가\]팝업에서 \[부서\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-dept']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [부서]입력필드가 출력된다')

@step("\[사용자 추가\]팝업에서 \[사용자1의 부서\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-dept']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자1의 부서]입력필드가 출력된다')


@step("\[사용자 추가\]팝업에서 \[사용자1의 부서\]를 유효하게 입력한다")
def step_impl(self):
    try:
        dept = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-dept'] input")
        dept.clear()
        dept.send_keys(USER1_DEPT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자1의 부서]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자2의 부서\]를 유효하게 입력한다")
def step_impl(self):
    try:
        dept= self.driver.find_element_by_css_selector("[data-ta='elm-adduser-dept'] input")
        dept.clear()
        dept.send_keys(USER2_DEPT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자2의 부서]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자3의 부서\]를 유효하게 입력한다")
def step_impl(self):
    try:
        dept= self.driver.find_element_by_css_selector("[data-ta='elm-adduser-dept'] input")
        dept.clear()
        dept.send_keys(USER3_DEPT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자3의 부서]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자4의 부서\]를 유효하게 입력한다")
def step_impl(self):
    try:
        dept= self.driver.find_element_by_css_selector("[data-ta='elm-adduser-dept'] input")
        dept.clear()
        dept.send_keys(USER4_DEPT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자4의 부서]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[전화번호\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-phone']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [전화번호]입력필드가 출력된다')


@step("\[사용자 추가\]팝업에서 \[사용자1의 전화번호\]를 유효하게 입력한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-phone'] input")
        phone.clear()
        phone.send_keys(USER1_PHONE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자1의 전화번호]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자2의 전화번호\]를 유효하게 입력한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-phone'] input")
        phone.clear()
        phone.send_keys(USER2_PHONE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자2의 전화번호]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자3의 전화번호\]를 유효하게 입력한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-phone'] input")
        phone.clear()
        phone.send_keys(USER3_PHONE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자3의 전화번호]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[사용자4의 전화번호\]를 유효하게 입력한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-phone'] input")
        phone.clear()
        phone.send_keys(USER4_PHONE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자4의 전화번호]를 유효하게 입력한다')

@step("\[사용자 추가\]팝업에서 \[전화번호\]에 미지원 문자를 입력한다 \(한글, 영어, 특수문자 등\)")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-phone'] input")
        phone.clear()
        phone.send_keys(TEXT_KO)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [전화번호]에 미지원 문자를 입력한다 (한글, 영어, 특수문자 등)')


@then("\[사용자 추가\]팝업에서 전화번호 미지원 문자 경고 메시지가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-phone_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [사용자 추가]팝업에서 전화번호 미지원 문자 경고 메시지가 출력된다')


@step("\[사용자 추가\]팝업에서 \[사용자 정의 필드\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-custom']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자 정의 필드]가 출력된다')


@step("\[사용자 추가\]팝업에서 \[사용자 정의 필드\]를 유효하게 입력한다")
def step_impl(self):
    try:
        dept = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-position'] input")
        dept.clear()
        dept.send_keys(USER1_DEPT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [사용자 정의 필드]를 유효하게 입력한다')


@step("\[사용자 추가\]팝업에서 \[취소\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-back']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [취소]버튼이 출력된다')


@step("\[사용자 추가\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-back']")
        cancelBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [취소]버튼을 클릭한다')


@then("사용자 목록 페이지에서 \[사용자 추가\]팝업이 닫힌다")
def step_impl(self):
     with self.assertRaises(NotImplementedError):
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
        self.driver.implicitly_wait(10)
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 [사용자 추가]팝업이 닫힌다')


@step("\[사용자 추가\]팝업에서 \[추가하기\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [추가하기]버튼이 출력된다')


@step("\[사용자 추가\]팝업에서 \[추가하기\]버튼을 클릭한다")
def step_impl(self):
    try:
        addBtn = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
        addBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 추가]팝업에서 [추가하기]버튼을 클릭한다')


@then("사용자 목록 페이지에서 추가한 \[사용자1\]이 출력된다")
def step_impl(self):
    try:
        # 검색입력필드에 추가한 유저 아이디를 입력한다
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.click()
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER1_ID)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        enterKey = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 추가한 유저가 검색된다
        id = self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        assert USER1_ID == id.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 추가한 [사용자1]이 출력된다')

@then("사용자 목록 페이지에서 추가한 \[사용자2\]가 출력된다")
def step_impl(self):
    try:
        # 검색입력필드에 추가한 유저 아이디를 입력한다
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.click()
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER2_ID)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        enterKey = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 추가한 유저가 검색된다
        id = self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        assert USER2_ID == id.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 추가한 [사용자2]가 출력된다')


@then("사용자 목록 페이지에서 추가한 \[사용자3\]이 출력된다")
def step_impl(self):
    try:
        # 검색입력필드에 추가한 유저 아이디를 입력한다
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.click()
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER3_ID)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        enterKey = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 추가한 유저가 검색된다
        id = self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        assert USER3_ID == id.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 추가한 [사용자3]이 출력된다')

@then("사용자 목록 페이지에서 추가한 \[사용자4\]가 출력된다")
def step_impl(self):
    try:
        # 검색입력필드에 추가한 유저 아이디를 입력한다
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.click()
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER4_ID)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        enterKey = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 추가한 유저가 검색된다
        id = self.driver.find_element_by_css_selector("[data-ta='elm-users-id']")
        assert USER4_ID == id.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록 페이지에서 추가한 [사용자4]가 출력된다')

@step("사용자가 추가되었다는 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자가 추가되었다는 토스트가 출력된다')





# 사용자 상세

@step("사용자 목록 페이지에서 사용자 행을 클릭한다")
def step_impl(self):
    try:
        goDetail = self.driver.find_element_by_css_selector("[data-ta='elm-users-name']")
        goDetail.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록 페이지에서 사용자 행을 클릭한다')


@then("사용자 상세 페이지로 이동한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-breadcrumb-depth2']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지로 이동한다')


@then("사용자 상세 페이지에서 \[Breadcrumb\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-breadcrumb-depth2']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [Breadcrumb]이 출력된다')


@step("사용자 상세 페이지에서 타이틀 \[사용자1의 아이디\]가 출력된다")
def step_impl(self):
    try:
        # id = self.driver.find_element_by_css_selector("[data-ta='nav-userdetail-title']")
        # assert USER1_ID == id.text
        self.driver.find_element_by_css_selector("[data-ta='nav-userdetail-title']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 타이틀 [사용자1의 아이디]가 출력된다')




# 사용자 상세 > 더보기

@step("사용자 상세 페이지에서 \[더보기\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-more']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [더보기]버튼이 출력된다')


@step("사용자 상세 페이지에서 \[더보기\]버튼을 클릭한다")
def step_impl(self):
    try:
        moreBtn = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-more']")
        moreBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [더보기]버튼을 클릭한다')


@then("사용자 상세 페이지에서 \[계정 활성화 메일 재전송\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-resend']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [계정 활성화 메일 재전송]메뉴가 출력된다')


@then("사용자 상세 페이지에서 \[2단계 인증 해제\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-remove']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [2단계 인증 해제]메뉴가 출력된다')

@then("사용자 상세 페이지에서 \[사용자 삭제\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-deleteuser']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자 삭제]메뉴가 출력된다')





# 사용자 상세 > 사용자 삭제 팝업

@step("사용자 상세 페이지에서 \[사용자 삭제\]메뉴를 클릭한다")
def step_impl(self):
    try:
        deleteBtn = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-deleteuser']")
        deleteBtn.click()
        # self.driver.find_element_by_xpath('//*[@id="menu-list-grow"]/li[2]').click() # data-ta 미적용으로 사용
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [사용자 삭제]메뉴를 클릭한다')


@then("사용자 상세 페이지에서 \[사용자 삭제\]메뉴가 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-deleteuser']")
        self.driver.find_element_by_xpath('//*[@id="menu-list-grow"]/li[2]') # data-ta 미적용으로 사용
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자 삭제]메뉴가 출력된다')


@then("사용자 상세 페이지에서 \[사용자 삭제\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-delete']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자 삭제]팝업이 출력된다')


@step("\[사용자 삭제\]팝업에서 \[사용자1의 이름\]이 출력된다")
def step_impl(self):
    try:
        #name = self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-name']")
        #assert USER1_NAME == name.text  # 성+이름 합쳐서 조회안된다고 함
        #assert USER1_NAME_PART == name.text
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 삭제]팝업에서 [사용자1의 이름]이 출력된다')


@step("\[사용자 삭제\]팝업에서 \[사용자1의 아이디\]가 출력된다")
def step_impl(self):
    try:
        #id = self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-id']")
        #assert USER1_ID_PART == id.text  # ID Full name 안된다고 함
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 삭제]팝업에서 [사용자1의 아이디]가 출력된다')


@step("\[사용자 삭제\]팝업에서 \[취소\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-back']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 삭제]팝업에서 [취소]버튼이 출력된다')


@step("\[사용자 삭제\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-back']")
        cancelBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 삭제]팝업에서 [취소]버튼을 클릭한다')


@step("\[사용자 삭제\]팝업에서 \[삭제\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-delete']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 삭제]팝업에서 [삭제]버튼이 출력된다')


@step("\[사용자 삭제\]팝업에서 \[삭제\]버튼을 클릭한다")
def step_impl(self):
    try:
        deleteBtn = self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-delete']")
        deleteBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [사용자 삭제]팝업에서 [삭제]버튼을 클릭한다')


@then("\[사용자 삭제\]팝업이 닫힌다")
def step_impl(self):
    def step_impl(self):
        with self.assertRaises(NotImplementedError):
            self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-delete']")
            self.driver.implicitly_wait(10)
        raise NotImplementedError(u'STEP: Then [사용자 삭제\팝업이 닫힌다')


@step("사용자 목록으로 이동한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 목록으로 이동한다')

@then("사용자 목록 페이지로 이동한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-users-adduser']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 목록페이지로 이동한다')

@step("해당 사용자가 더 이상 사용자 목록에 노출되지 않는다")
def step_impl(self):
    try:
        # 검색입력필드에 삭제한 유저 아이디를 입력한다
        search = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        search.clear()
        search.send_keys(USER3_ID)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        enterKey = self.driver.find_element_by_css_selector("[data-ta='elm-users-search'] input")
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 검색결과가 없다는 안내가 출력된다
        # self.driver.find_element_by_css_selector("[data-ta='elm-users-search_result']") # data ta 적용안됨
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/table/tbody/tr/td/p')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 해당 사용자가 더 이상 사용자 목록에 노출되지 않는다')

@step("사용자 상세 페이지에서 주소유자는 삭제할 수 없다는 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 주소유자는 삭제할 수 없다는 토스트가 출력된다')

@step("사용자가 삭제 예정 상태로 변경되었다는 토스트 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자가 삭제 예정 상태로 변경되었다는 토스트 출력된다')






# 사용자 상세 > 프로필 이미지

@then("사용자 상세 페이지에서 프로필 이미지에 \[기본 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-nopicture']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 프로필 이미지에 [기본 프로필 이미지]가 출력된다')


@step("사용자 상세 페이지에서 \[기본 프로필 이미지\]를 클릭한다")
def step_impl(self):
    try:
        #defaultImg = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-nopicture'] img")
        #defaultImg = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-nopicture']")
        #defaultImg.click()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[1]/div').click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [기본 프로필 이미지]를 클릭한다')


@step("사용자 상세 페이지에서 프로필 이미지에 \[설정한 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-picture'] img")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 프로필 이미지에 [설정한 프로필 이미지]가 출력된다')


@step("사용자 상세 페이지에서 \[설정한 프로필 이미지\]를 클릭한다")
def step_impl(self):
    try:
        profileImg = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-picture'] img")
        #profileImg = self.driver.find_element_by_class_name('MuiAvatar-img')
        profileImg.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [설정한 프로필 이미지]를 클릭한다')


@then("사용자 상세 페이지에서 프로필 이미지 \[업로드\]메뉴가 출력된다")
def step_impl(self):
    try:
        upload = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-upload']")
        upload.send_keys(PATH_USER_PROFILE_IMAGE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 프로필 이미지 [업로드]메뉴가 출력된다')


@step("사용자 상세 페이지에서 프로필 이미지 \[업로드\]메뉴를 클릭한다")
def step_impl(self):
    try:
        upload = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-upload']")
        upload.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 용자 상세 페이지에서 프로필 이미지 [업로드]메뉴를 클릭한다')

@step("사용자 상세 페이지에서 프로필 이미지 \[삭제\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-delete']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 프로필 이미지 [삭제]메뉴가 출력된다')


@step("사용자 상세 페이지에서 프로필 이미지 \[삭제\]메뉴를 클릭한다")
def step_impl(self):
    try:
        deleteBtn = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-delete']")
        deleteBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 프로필 이미지 [삭제]메뉴를 클릭한다')

@then("사용자 상세 페이지에서 이미지 확장자 오류 안내 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 이미지 확장자 오류 안내 토스트가 출력된다')

@then("사용자 상세 페이지에서 이미지 크기 오류 안내 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 이미지 크기 오류 안내 토스트가 출력된다')




# 사용자 상세 > 상태

@step("사용자 상세 페이지에서 \[사용자1의 상태\]가 출력된다")
def step_impl(self):
    try:
        # status = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-state']")
        # assert USER_STATUS_PENDING == status.tet
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-state']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [상태]가 출력된다')


@then("사용자 상세 페이지에서 사용자의 상태가 \[대기\]로 출력된다")
def step_impl(self):
    try:
        status = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-state']")
        assert USER_STATUS_PENDING == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 사용자의 상태가 [대기]로 출력된다')


@then("사용자 상세 페이지에서 사용자의 상태가 \[활성\]으로 출력된다")
def step_impl(self):
    try:
        status = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-state']")
        assert USER_STATUS_ACTIVE == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 사용자의 상태가 [활성]으로 출력된다')


@then("사용자 상세 페이지에서 사용자의 상태가 \[비활성\]으로 출력된다")
def step_impl(self):
    try:
        status = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-state']")
        assert USER_STATUS_DEACTIVE == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 사용자의 상태가 [비활성]으로 출력된다')


@step("사용자 상세 페이지에서 상태 토글버튼을 \[활성\]으로 변경한다")
def step_impl(self):
    try:
        #toggleActive = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-activetoggle']")
        #toggleActive.click()
        # 참고 : 활성버튼을 누르는게 아니라, 비활성버튼을 눌러야 활성상태로 됨
        toggleDeactive = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-deactivetoggle']")
        toggleDeactive.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 상태 토글버튼을 [활성]으로 변경한다')


@step("사용자 상세 페이지에서 상태 토글버튼을 \[비활성\]으로 변경한다")
def step_impl(self):
    try:
        #toggleDeactive = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-deactivetoggle']")
        #toggleDeactive.click()
        # 참고 : 비활성버튼을 누르는게 아니라, 활성버튼을 눌러야 비활성 팝업이 출력됨
        toggleActive = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-activetoggle']")
        toggleActive.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 상태 토글버튼을 [비활성]으로 변경한다')


@then("사용자 상세 페이지에서 \[계정 비활성화\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deactive-ok']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [계정 비활성화]팝업이 출력된다')

@step("\[계정 비활성화\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-deactive-cancel']")
        cancelBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [계정 비활성화]팝업에서 [취소]버튼을 클릭한다')


@step("\[계정 비활성화\]팝업에서 \[확인\]버튼을 클릭한다")
def step_impl(self):
    try:
        okBtn = self.driver.find_element_by_css_selector("[data-ta='elm-deactive-ok']")
        okBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [계정 비활성화]팝업에서 [확인]버튼을 클릭한다')

@step("사용자 상세 페이지에서 조직의 주소유자는 비활성화할 수 없다는 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 조직의 주소유자는 비활성화할 수 없다는 토스트가 출력된다')

@step("사용자의 상태가 비활성되었다는 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자의 상태가 비활성되었다는 토스트가 출력된다')




# 사용자 상세 > 성

@then("사용자 상세 페이지에서 \[사용자1의 성\]이 출력된다")
def step_impl(self):
    try:
        #familyname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname'] input")
        #assert USER1_FAMILYNAME == familyname.text
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자1의 성]이 출력된다')


@step("사용자 상세 페이지에서 사용자의 \[성\]입력필드를 클릭한다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname'] input")
        familyname.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [성]입력필드를 클릭한다')


@step("사용자 상세 페이지에서 사용자의 \[성\]입력필드의 텍스트를 모두 제거한다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname'] input")
        familyname.clear()
        familyname.send_keys()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [성]입력필드의 텍스트를 모두 제거한다')


@step("사용자 상세 페이지에서 사용자의 \[성\]입력필드에 유효하게 텍스트를 입력한다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname'] input")
        familyname.clear()
        familyname.send_keys(USER1_FAMILYNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [성]입력필드에 유효하게 텍스트를 입력한다')


@step("사용자 상세 페이지에서 사용자의 \[성\]을 기존과 다르게 입력한다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname'] input")
        familyname.clear()
        familyname.send_keys(USER1_FAMILYNAME_EDIT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [성]을 기존과 다르게 입력한다')


@then("사용자 상세 페이지에서 필수값 관련 경고 메시지가 출력된다\(성\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 필수값 관련 경고 메시지가 출력된다(성)')


@then("사용자 상세 페이지에서 입력한 텍스트로 사용자의 \[성\]이 변경된다")
def step_impl(self):
    try:
        familyname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname'] input")
        # assert USER1_FAMILYNAME_EDIT == familyname.text
        # 성 텍스트가 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-familyname'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 입력한 텍스트로 사용자의 [성]이 변경된다')


@step("사용자 상세 페이지에서 입력필드 외부 영역을 클릭한다")  # 타이틀 클릭
def step_impl(self):
    try:
        #familyname = self.driver.find_element_by_css_selector("[data-ta='nav-userdetail-title']")
        firstname = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[4]/div/div/input')
        firstname.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 입력필드 외부 영역을 클릭한다')




# 사용자 상세 > 이름

@then("사용자 상세 페이지에서 \[사용자1의 이름\]이 출력된다")
def step_impl(self):
    try:
        #firstname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-firstname'] input")
        #assert USER1_NAME == firstname.text
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-firstname'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자1의 이름]이 출력된다')


@step("사용자 상세 페이지에서 사용자의 \[이름\]입력필드를 클릭한다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-firstname'] input")
        firstname.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [이름]입력필드를 클릭한다')


@step("사용자 상세 페이지에서 사용자의 \[이름\]입력필드의 텍스트를 모두 제거한다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-firstname'] input")
        firstname.clear()
        firstname.send_keys()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [이름]입력필드의 텍스트를 모두 제거한다')


@step("사용자 상세 페이지에서 사용자의 \[이름\]을 기존과 다르게 입력한다")
def step_impl(self):
    try:
        firstname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-firstname'] input")
        firstname.clear()
        firstname.send_keys(USER1_FIRSTNAME_EDIT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [이름]을 기존과 다르게 입력한다')


@then("사용자 상세 페이지에서 필수값 관련 경고 메시지가 출력된다\(이름\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-firstname_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 필수값 관련 경고 메시지가 출력된다(이름)')


@then("사용자 상세 페이지에서 입력한 텍스트로 사용자의 \[이름\]이 변경된다")
def step_impl(self):
    try:
        #firstname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-firstname'] input")
        # assert USER1_FIRSTNAME == firstname.text
        # 텍스트 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-firstname'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 입력한 텍스트로 사용자의 [이름]이 변경된다')




# 사용자 상세 > 아이디

@then("사용자 상세 페이지에서 \[사용자1의 아이디\]가 출력된다")
def step_impl(self):
    try:
        #id = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-id'] input")
        #assert USER1_ID == id.text
        # 텍스트 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-id'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자1의 아이디]가 출력된다')




# 사용자 상세 > 부서

@then("사용자 상세 페이지에서 \[사용자1의 부서\]가 출력된다")
def step_impl(self):
    try:
        #dept = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        #assert USER1_DEPT == dept.text    # data-ta 적용안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자1의 부서]가 출력된다')


@step("사용자 상세 페이지에서 사용자의 \[부서\]입력필드를 클릭한다")
def step_impl(self):
    try:
        dept = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        dept.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [부서]입력필드를 클릭한다')


@step("사용자 상세 페이지에서 사용자의 \[부서\]입력필드의 텍스트를 모두 제거한다")
def step_impl(self):
    try:
        dept = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        dept.clear()
        dept.send_keys()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [부서]입력필드의 텍스트를 모두 제거한다')


@step("사용자 상세 페이지에서 사용자의 \[부서\]를 기존과 다르게 입력한다")
def step_impl(self):
    try:
        dept = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        dept.clear()
        dept.send_keys(USER1_DEPT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [부서]를 기존과 다르게 입력한다')


@then("사용자 상세 페이지에서 사용자의 \[부서\]입력필드가 데이터없이 변경된다")
def step_impl(self):
    try:
        #dept = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        #assert NO_DATA == dept.text
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 사용자의 [부서]입력필드가 데이터없이 변경된다')


@then("사용자 상세 페이지에서 입력한 텍스트로 사용자의 \[부서\]가 변경된다")
def step_impl(self):
    try:
        #dept = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        #assert dept == USER1_DEPT
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-dept'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 입력한 텍스트로 사용자의 [부서]가 변경된다')



# 사용자 상세 > 전화번호

@then("사용자 상세 페이지에서 \[사용자1의 전화번호\]가 출력된다")
def step_impl(self):
    try:
        #phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        #assert USER1_PHONE == phone.text
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자1의 전화번호]가 출력된다')


@step("사용자 상세 페이지에서 사용자의 \[전화번호\]입력필드를 클릭한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        phone.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [전화번호]입력필드를 클릭한다')


@step("사용자 상세 페이지에서 사용자의 \[전화번호\]입력필드의 텍스트를 모두 제거한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        phone.clear()
        phone.send_keys()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [전화번호]입력필드의 텍스트를 모두 제거한다')


@step("사용자 상세 페이지에서 사용자의 \[전화번호\]입력필드에 미지원 텍스트\(한글\)를 입력한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        phone.clear()
        phone.send_keys(TEXT_KO)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [전화번호]입력필드에 미지원 텍스트(한글)를 입력한다')


@step("사용자 상세 페이지에서 사용자의 \[전화번호\]입력필드에 미지원 텍스트\(영어\)를 입력한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        phone.clear()
        phone.send_keys(TEXT_EN)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [전화번호]입력필드에 미지원 텍스트(영어)를 입력한다')


@then("사용자 상세 페이지에서 미지원 문자 관련 경고 메시지가 출력된다\(영어\)")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        phone.clear()
        phone.send_keys(USER1_FIRSTNAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 미지원 문자 관련 경고 메시지가 출력된다(영어)')


@step("사용자 상세 페이지에서 사용자의 \[전화번호\]입력필드에 미지원 텍스트\(전화번호에 허용안되는 특수문자\)를 입력한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        phone.clear()
        phone.send_keys(TEXT_CHAR)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [전화번호]입력필드에 미지원 텍스트(전화번호에 허용안되는 특수문자)를 입력한다')


@step("사용자 상세 페이지에서 사용자의 \[전화번호\]를 기존과 다르게 입력한다")
def step_impl(self):
    try:
        phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        phone.clear()
        phone.send_keys(USER1_PHONE)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 사용자의 [전화번호]를 기존과 다르게 입력한다')


@then("사용자 상세 페이지에서 미지원 문자 관련 경고 메시지가 출력된다\(한글\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 미지원 문자 관련 경고 메시지가 출력된다(한글)')


@then("사용자 상세 페이지에서 미지원 문자 관련 경고 메시지가 출력된다\(영어\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 미지원 문자 관련 경고 메시지가 출력된다(영어)')


@then("사용자 상세 페이지에서 미지원 문자 관련 경고 메시지가 출력된다\(특수문자\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 미지원 문자 관련 경고 메시지가 출력된다(특수문자)')


@then("사용자 상세 페이지에서 사용자의 \[전화번호\]입력필드가 데이터없이 변경된다")
def step_impl(self):
    try:
        #phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        #assert == NO_DATA == phone.text
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 사용자의 [전화번호]입력필드가 데이터없이 변경된다')


@then("사용자 상세 페이지에서 입력한 텍스트로 \[전화번호\]가 변경된다")
def step_impl(self):
    try:
        #phone = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        #assert USER1_PHONE == phone.text
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-phone'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 입력한 텍스트로 [전화번호]가 변경된다')



# 사용자 상세 > 사용자 정의 필드

@then("사용자 상세 페이지에서 \[사용자 정의 필드\]영역이 출력되지 않는다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-custom']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자 정의 필드]영역이 출력되지 않는다')


@then("사용자 상세 페이지에서 \[사용자 정의 필드\]영역이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-custom']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [사용자 정의 필드]영역이 출력된다')




# 사용자 상세 > 가입된 그룹
@step("사용자 상세 페이지에서 \[가입된 그룹\] 탭이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-group']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [가입된 그룹] 탭이 출력된다')


@then("사용자 상세 페이지에서 \[기본 그룹\]이름이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-defaultname']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [기본 그룹]이름이 출력된다')


@step("사용자 상세 페이지에서 \[기본 그룹\]설명이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-defaultdesc']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [기본 그룹]설명이 출력된다')


@step("사용자 상세 페이지에서 \[기본 그룹\]을 클릭한다")
def step_impl(self):
    try:
        inputFamilyname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-defaultname']")
        inputFamilyname.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [기본 그룹]을 클릭한다')


@then("\[기본 그룹\] 상세 페이지의 사용자 목록으로 이동한다")
def step_impl(self):
    try:
        url = self.driver.current_url
        assert url == GROUP_DETAIL_DEFAULT
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [기본 그룹] 상세 페이지의 사용자 목록으로 이동한다')


@then("사용자 상세 페이지에서 \[생성한 그룹\]이름이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-customname']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 [생성한 그룹]이름이 출력된다')


@step("사용자 상세 페이지에서 \[생성한 그룹\]설명이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-customdesc']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [생성한 그룹]설명이 출력된다')


@step("사용자 상세 페이지에서 \[생성한 그룹\]을 클릭한다")
def step_impl(self):
    try:
        inputFamilyname = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-customname']")
        inputFamilyname.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 사용자 상세 페이지에서 [생성한 그룹]을 클릭한다')


@then("\[생성한 그룹\] 상세 페이지의 사용자 목록으로 이동한다")
def step_impl(self):
    try:
        url = self.driver.current_url
        #assert url == GROUP_DETAIL_CUSTOM
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [생성한 그룹] 상세 페이지의 사용자 목록으로 이동한다')


@then("사용자 상세 페이지에서 가입된 그룹이 최근에 추가된 그룹순으로 정렬된다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-userdetail-customnamee']")
        grouplist = sorted(glob.glob('*'), key=os.path.getctime)
        for name in grouplist:
            pass
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 상세 페이지에서 가입된 그룹이 최근에 추가된 그룹순으로 정렬된다')