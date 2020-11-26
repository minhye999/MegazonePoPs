from behave import *
import logging
from features.steps.common import *

use_step_matcher("re")


@step("메가존 어드민 페이지로 이동한다")
def go_admin(self):
    try:
        self.driver.get(URL_ADMIN)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 메가존 어드민 페이지로 이동한다')


# 헤더

@step("헤더에 프로필 이미지가 출력된다")
def print_profileImg(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-header-more']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 헤더에 프로필 이미지가 출력된다')


@when("헤더의 \[프로필 이미지\]를 클릭한다")
def click_profileImg(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='elm-header-more']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 헤더의 [프로필 이미지]를 클릭한다')

@step("헤더의 \[프로필 이미지\]를 클릭한다")
def step_impl(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='elm-header-more']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 헤더의 [프로필 이미지]를 클릭한다')

@then("헤더에 더보기 메뉴가 출력된다")
def print_moreMenu(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-header-more']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 헤더에 더보기 메뉴가 출력된다')


@step("더보기 메뉴에 이름이 출력된다")
def print_name(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-header-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        raise NotImplementedError(u'STEP: And 더보기 메뉴에 이름이 출력된다')


@step("더보기 메뉴에 아이디가 출력된다")
def print_id(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-header-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        raise NotImplementedError(u'STEP: And 더보기 메뉴에 아이디가 출력된다')


@step("더보기 메뉴에 \[로그아웃\]이 출력된다")
def print_signout(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-header-signout']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        raise NotImplementedError(u'STEP: And 더보기 메뉴에 [로그아웃]이 출력된다')


@step("더보기 메뉴의 \[로그아웃\]을 클릭한다")
def click_signout(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='elm-header-signout']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 더보기 메뉴의 [로그아웃]을 클릭한다')



# LNB

@when("LNB에서 최상위메뉴 \[사용자\]를 클릭한다")
def click_1depthUsers(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='nav-users']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When LNB에서 최상위메뉴 [사용자]를 클릭한다')


@step("LNB에서 하위메뉴 \[사용자\]를 클릭한다")
def click_2depthUsers(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='nav-users-users']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And LNB에서 하위메뉴 [사용자]를 클릭한다')


@then("사용자 페이지로 이동한다")
def go_users(self):
    try:
        # url 이동
        self.driver.get(URL_USERS)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 페이지로 이동한다')


@step("LNB에서 하위메뉴 \[그룹\]을 클릭한다")
def click_2depthGroups(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='nav-users-groups']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And LNB에서 하위메뉴 [그룹]을 클릭한다')


@then("그룹 페이지로 이동한다")
def go_groups(self):
    try:
        # url 이동
        self.driver.get(URL_GROUPS)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 페이지로 이동한다')


@step("LNB에서 하위메뉴 \[사용자 정의 필드\]를 클릭한다")
def click_2depthGroups(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='nav-users-customfields']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And LNB에서 하위메뉴 [사용자 정의 필드]를 클릭한다')


@then("사용자 정의 필드 페이지로 이동한다")
def go_customFields(self):
    try:
        # url 이동
        self.driver.get(URL_CUSTOMFIELDS)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 사용자 정의 필드 페이지로 이동한다')


@step("LNB에서 최상위메뉴 \[사용자\]를 클릭한다")
def step_impl(self):
    """
    :type self: behave.runner.self
    """
    raise NotImplementedError(u'STEP: And LNB에서 최상위메뉴 [사용자]를 클릭한다')
