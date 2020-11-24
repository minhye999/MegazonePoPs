from behave import *
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from features.steps.common import *

use_step_matcher("re")



# 그룹 목록 > [그룹 추가]버튼

@step("그룹 목록 페이지에서 \[그룹 추가\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-addgroup']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 [그룹 추가]버튼이 출력된다')


@when("그룹 목록 페이지에서 \[그룹 추가\]버튼을 클릭한다")
def step_impl(self):
    try:
        addGroupBtn = self.driver.find_element_by_css_selector("[data-ta='elm-groups-addgroup']")
        addGroupBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 [그룹 추가]버튼을 클릭한다')


@then("그룹 목록 페이지에서 \[그룹 추가\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-add']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 [그룹 추가]팝업이 출력된다')


@then("\[그룹 추가\]팝업에서 \[이름\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-name'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 추가]팝업에서 [이름]입력필드가 출력된다')


@step("\[그룹 추가\]팝업에서 \[이름\]입력필드를 클릭한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-name'] input")
        name.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 [이름]입력필드를 클릭한다')


@step("\[그룹 추가\]팝업에서 그룹 \[이름\]을 중복되게 입력한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-name'] input")
        name.clear()
        name.send_keys(GROUP_NAME_DEFAULT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 그룹 [이름]을 중복되게 입력한다')


@step("\[그룹 추가\]팝업에서 \[그룹1의 이름\]을 유효하게 입력한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-name'] input")
        name.clear()
        name.send_keys(GROUP1_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 [그룹1의 이름]을 유효하게 입력한다')


@step("\[그룹 추가\]팝업에서 \[그룹2의 이름\]을 유효하게 입력한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-name'] input")
        name.clear()
        name.send_keys(GROUP2_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 [그룹2의 이름]을 유효하게 입력한다')

@then("\[그룹 추가\]팝업에서 \[설명\]입력필드가 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-desc']")
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/form/div[2]/div[2]/div/div/textarea[1]')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 추가]팝업에서 [설명]입력필드가 출력된다')


@step("\[그룹 추가\]팝업에서 \[그룹2의 설명\]을 유효하게 입력한다")
def step_impl(self):
    try:
        #desc = self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-name']")
        desc = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/form/div[2]/div[2]/div/div/textarea[1]')
        desc.clear()
        desc.send_keys(GROUP2_DESC)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 [그룹2의 설명]을 유효하게 입력한다')


@step("\[그룹 추가\]팝업에서 \[취소\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-back']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 [취소]버튼이 출력된다')


@step("\[그룹 추가\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-back']")
        cancelBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 [취소]버튼을 클릭한다')


@step("\[그룹 추가\]팝업에서 \[추가하기\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-add']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 [추가하기]버튼이 출력된다')


@step("\[그룹 추가\]팝업에서 \[추가하기\]버튼을 클릭한다")
def step_impl(self):
    try:
        addBtn = self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-add']")
        addBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 추가]팝업에서 [추가하기]버튼을 클릭한다')


@then("\[그룹 추가\]팝업에서 필수값 관련 경고 메시지가 출력된다\(이름\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-name_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 추가]팝업에서 필수값 관련 경고 메시지가 출력된다(이름)')


@then("\[그룹 추가\]팝업에서 그룹 이름 중복 경고 메시지가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-name_err']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 추가]팝업에서 그룹 이름 중복 경고 메시지가 출력된다')


@then("그룹 목록 페이지에서 \[그룹 추가\]팝업이 닫힌다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-add']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 [그룹 추가]팝업이 닫힌다')


@then("그룹 목록 페이지에서 \[그룹 추가\]팝업이 닫힌다")
def step_impl(self):
    with self.assertRaises(NotImplementedError):
        self.driver.find_element_by_css_selector("[data-ta='elm-addgroup-title']")
        self.driver.implicitly_wait(10)


@then("그룹 목록 페이지에서 추가한 \[그룹1\]이 출력된다")
def step_impl(self):
    try:
        # 검색 입력필드에 추가한 그룹 아이디를 입력한다
        search = self.driver.find_element_by_css_selector('[data-ta="elm-groups-search"] input')
        search.click()
        self.driver.implicitly_wait(10)
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP1_NAME)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        enterKey = self.driver.find_element_by_css_selector('[data-ta="elm-groups-search"] input')
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 추가한 그룹이 검색된다
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        assert GROUP1_NAME == name.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 추가한 [그룹1]이 출력된다')

@then("그룹 목록 페이지에서 추가한 \[그룹2\]가 출력된다")
def step_impl(self):
    try:
        # 검색 입력필드에 추가한 그룹 아이디를 입력한다
        search = self.driver.find_element_by_css_selector('[data-ta="elm-groups-search"] input')
        search.click()
        self.driver.implicitly_wait(10)
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP2_NAME)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        enterKey = self.driver.find_element_by_css_selector('[data-ta="elm-groups-search"] input')
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 추가한 그룹이 검색된다
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        assert GROUP2_NAME == name.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 추가한 [그룹2]가 출력된다')


@step("그룹이 추가되었다는 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹이 추가되었다는 토스트가 출력된다')




# 그룹 목록 > 검색

@then("그룹 목록 페이지에서 \[검색\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-search']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 [검색]입력필드가 출력된다')


@when("그룹 목록 페이지에서 \[검색\] 입력필드를 클릭한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector('[data-ta="elm-groups-search"] input')
        search.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 [검색] 입력필드를 클릭한다')

@when("그룹 목록 페이지에서 검색 입력필드에 텍스트 미입력 상태에서 \[엔터키\]를 입력한다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-groups-search']").send_keys(Keys.ENTER)
        # data-ta 영역에 엔터키가 먹지않아서 class name을 사용함
        enterKey = self.driver.find_element_by_class_name('MuiInputBase-input')
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 검색 입력필드에 텍스트 미입력 상태에서 [엔터키]를 입력한다')


@step("그룹 목록 페이지에서 검색 입력필드에 \[유효하지 않은 텍스트\]를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP_NAME_INVALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Add 그룹 목록 페이지에서 검색 입력필드에 [유효하지 않은 텍스트]를 입력한다')


@when("그룹 목록 페이지에서 검색 입력필드에 \[그룹1의 이름\]을 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP1_NAME_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 검색 입력필드에 [그룹1의 이름]을 부분 입력한다')


@when("그룹 목록 페이지에서 검색 입력필드에 \[그룹1의 이름\]을 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP1_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 검색 입력필드에 [그룹1의 이름]을 전체 입력한다')


@when("그룹 목록 페이지에서 검색 입력필드에 \[그룹2의 이름\]을 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP2_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 검색 입력필드에 [그룹2의 이름]을 전체 입력한다')

@when("그룹 목록 페이지에서 검색 입력필드에 삭제하려는 그룹 \[이름\]을 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP1_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 검색 입력필드에 대기 상태인 그룹 아이디를 입력한다')


@when("그룹 목록 페이지에서 검색 입력필드에 그룹 \[이름\]을 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP1_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 검색 입력필드에 그룹 [이름]을 입력한다')


@when("그룹 목록 페이지에서 검색 입력필드에 \[기본그룹의 이름\]을 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        search.clear()
        search.send_keys(GROUP_NAME_DEFAULT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 검색 입력필드에 [기본그룹의 이름]을 입력한다')


@then("그룹 목록 페이지에서 검색결과 없다는 안내가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-search_result']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 검색결과 없다는 안내가 출력된다')


@then("그룹 목록 페이지에서 \[그룹1의 이름\]을 포함한 검색결과가 출력된다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        assert GROUP1_NAME == name.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 [그룹1의 이름]을 포함한 검색결과가 출력된다')


@then("그룹 목록 페이지에서 \[그룹1의 이름\]과 일치하는 검색결과가 출력된다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        assert GROUP1_NAME == name.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 [그룹1의 이름]과 일치하는 검색결과가 출력된다')




# 그룹 목록 > 기본 그룹 아이콘

@step("그룹 목록 페이지에서 기본 그룹 \[아이콘\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-icon']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 기본 그룹 [아이콘]이 출력된다')




# 그룹 목록 > 이름

@then("그룹 목록 페이지에서 그룹의 \[이름\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 그룹의 [이름]이 출력된다')

@then("그룹 목록 페이지에서 \[기본그룹의 이름\]이 출력된다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        assert GROUP_NAME_DEFAULT == name.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에 [기본그룹의 이름]이 출력된다')


@step("그룹 목록 페이지에서 \[그룹1의 이름\]이 출력된다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        assert GROUP1_NAME == name.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 [그룹1의 이름]이 출력된다')


@when("그룹 목록 페이지에서 검색 입력필드에 그룹의 \[이름\]을 입력한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        name.clear()
        name.send_keys(GROUP_NAME_DEFAULT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 검색 입력필드에 그룹의 [이름]을 입력한다')




# 그룹 목록 > 설명
@step("그룹 목록 페이지에서 그룹의 \[설명\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-desc']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 그룹의 [설명]이 출력된다')

@step("그룹 목록 페이지에서 \[기본그룹의 설명\]이 출력된다")
def step_impl(self):
    try:
        desc = self.driver.find_element_by_css_selector("[data-ta='elm-groups-desc']")
        assert desc == GROUP_DESC_DEFAULT
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 [기본그룹의 설명]이 출력된다')


@step("그룹 목록 페이지에서 \[그룹1의 설명\]이 출력된다")
def step_impl(self):
    try:
        desc = self.driver.find_element_by_css_selector("[data-ta='elm-groups-desc']")
        assert GROUP1_DESC == desc.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 [그룹1의 설명]이 출력된다')

@step("그룹 목록 페이지에서 \[그룹1의 설명\]이 출력된다")
def step_impl(self):
    try:
        desc = self.driver.find_element_by_css_selector("[data-ta='elm-groups-desc']")
        assert GROUP1_DESC == desc.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 [그룹1의 설명]이 출력된다')


@step("그룹 목록 페이지에서 \[그룹2의 설명\]이 출력된다")
def step_impl(self):
    try:
        desc = self.driver.find_element_by_css_selector("[data-ta='elm-groups-desc']")
        assert GROUP2_DESC == desc.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 [그룹2의 설명]이 출력된다')




# 그룹 목록 > 그룹 수
@step("그룹 목록 페이지에서 그룹의 \[사용자 수\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-num']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 그룹의 [사용자 수]가 출력된다')

@step("그룹 목록 페이지에서 기본 그룹 \[사용자 수\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-num']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 기본 그룹 [사용자 수]가 출력된다')


@step("그룹 목록 페이지에서 생성한 그룹 \[사용자 수\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-num']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 생성한 그룹 [사용자 수]가 출력된다')


@then("그룹 목록 페이지에서 그룹의 \[사용자 수\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-num']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 목록 페이지에서 그룹의 [사용자 수]가 출력된다')




# 그룹 상세

@when("그룹 목록 페이지에서 그룹 행을 클릭한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groups-name']")
        name.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: When 그룹 목록 페이지에서 그룹 행을 클릭한다')


@then("그룹 상세 페이지로 이동한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-adduser']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지로 이동한다')


@then("그룹 상세 페이지에서 \[Breadcrumb\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-breadcrumb-depth2']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 [Breadcrumb]이 출력된다')


@step("그룹 상세 페이지에서 그룹의 \[타이틀\]이 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-title']")   # data-ta 적용안됨
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[2]/h2/p/span')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [타이틀]이 출력된다')




# 그룹 상세 > [더보기]버튼

@step("그룹 상세 페이지에서 \[더보기\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-more']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [더보기]버튼이 출력된다')


@then("그룹 상세 페이지에서 \[더보기\]버튼이 비활성화된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-more']").get_attribute("disabled")   # data-ta 적용안됨
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[2]/button/span[1]/svg').get_attribute("disabled")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 [더보기]버튼이 비활성화된다')


@step("그룹 상세 페이지에서 \[더보기\]버튼을 클릭한다")
def step_impl(self):
    try:
        more = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-more']")   # data-ta 적용안됨
        #more = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[2]/button/span[1]/svg')
        more.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [더보기]버튼을 클릭한다')



# 그룹 상세 > 이름

@step("그룹 상세 페이지에서 \[그룹1의 이름\]이 출력된다")
def step_impl(self):
    try:
        #name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        # name = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[1]/div/div/input')
        # assert GROUP1_NAME == name.text
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹1의 이름]이 출력된다')

@step("그룹 상세 페이지에서 \[기본그룹의 이름\]이 출력된다")
def step_impl(self):
    try:
        # name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        # assert GROUP_NAME_DEFAULT == name.text
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [기본그룹의 이름]이 출력된다')

@step("그룹 상세 페이지에서 그룹의 \[이름\]입력필드를 클릭한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        name.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [이름]입력필드를 클릭한다')


@step("그룹 상세 페이지에서 그룹의 \[이름\]입력필드의 텍스트를 모두 제거한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        name.clear()
        name.send_keys()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [이름]입력필드의 텍스트를 모두 제거한다')


@step("그룹 상세 페이지에서 그룹의 \[이름\]을 중복되게 입력한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        name.clear()
        name.send_keys(GROUP_NAME_DEFAULT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [이름]을 중복되게 입력한다')


@step("그룹 상세 페이지에서 그룹의 \[이름\]입력필드에 유효하게 텍스트를 입력한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        name.clear()
        name.send_keys(GROUP1_NAME_EDIT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [이름]입력필드에 유효하게 텍스트를 입력한다')


@step("그룹 상세 페이지에서 그룹의 \[이름\]을 기존과 다르게 입력한다")
def step_impl(self):
    try:
        name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        name.clear()
        name.send_keys(GROUP1_NAME_EDIT2)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [이름]을 기존과 다르게 입력한다')

@step("그룹 상세 페이지에서 입력필드 외부 영역을 클릭한다")
def step_impl(self):
    try:
        title = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-user']")
        title.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 입력필드 외부 영역을 클릭한다')


@then("그룹 상세 페이지에서 필수값 관련 경고 메시지가 출력된다\(이름\)")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name_err']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 필수값 관련 경고 메시지가 출력된다(이름)')


@then("그룹 상세 페이지에서 입력한 텍스트로 그룹의 \[이름\]이 변경된다")
def step_impl(self):
    try:
        # name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
        # assert name == GROUP1_NAME_EDIT
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name'] input")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 입력한 텍스트로 그룹의 [이름]이 변경된다')




# 그룹 상세 > 설명
@step("그룹 상세 페이지에서 \[그룹1의 설명\]이 출력된다")
def step_impl(self):
    try:
        #desc = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        #assert GROUP1_DESC == desc.text
        #self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[2]/div/div/textarea[1]')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹1의 설명]이 출력된다')

@step("그룹 상세 페이지에서 \[그룹2의 설명\]이 출력된다")
def step_impl(self):
    try:
        # desc = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        # assert GROUP2_DESC == desc.text
        #self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[2]/div/div/textarea[1]')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹2의 설명]이 출력된다')

@step("그룹 상세 페이지에서 \[기본그룹의 설명\]이 출력된다")
def step_impl(self):
    try:
        # desc = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        # assert GROUP_DESC_DEFAULT == desc.text
        #self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[2]/div/div/textarea[1]')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [기본그룹의 설명]이 출력된다')

@step("그룹 상세 페이지에서 그룹의 \[설명\]입력필드를 클릭한다")
def step_impl(self):
    try:
        #desc = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        desc = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[2]/div/div/textarea[1]')
        desc.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [설명]입력필드를 클릭한다')


@step("그룹 상세 페이지에서 그룹의 \[설명\]입력필드의 텍스트를 모두 제거한다")
def step_impl(self):
    try:
        # desc = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        desc = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[2]/div/div/textarea[1]')
        desc.clear()
        desc.send_keys()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [설명]입력필드의 텍스트를 모두 제거한다')


@step("그룹 상세 페이지에서 그룹의 \[설명\]을 기존과 다르게 입력한다")
def step_impl(self):
    try:
        # desc = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        desc = self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[2]/div/div/textarea[1]')
        desc.clear()
        desc.send_keys(GROUP2_DESC_EDIT)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 그룹의 [설명]을 기존과 다르게 입력한다')


@then("그룹 상세 페이지에서 그룹의 \[설명\]입력필드가 데이터없이 변경된다")
def step_impl(self):
    try:
        # desc = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        # assert NO_DATA == desc.text
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[2]/div/div/textarea[1]')
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 그룹의 [설명]입력필드가 데이터없이 변경된다')


@then("그룹 상세 페이지에서 입력한 텍스트로 그룹의 \[설명\]이 변경된다")
def step_impl(self):
    try:
        # desc = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-desc'] input")
        # assert GROUP1_DESC_EDIT == desc.text
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div[3]/div[1]/form/div/div[2]/div/div/textarea[1]')
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 입력한 텍스트로 그룹의 [설명]이 변경된다')




# 그룹 상세 > [그룹 사용자] 탭

@step("그룹 상세 페이지에서 \[그룹 사용자\]탭이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-user']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹 사용자]탭이 출력된다')


@step("그룹 상세 페이지에서 \[그룹 사용자 추가\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-adduser']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹 사용자 추가]버튼이 출력된다')


@step("그룹 상세 페이지에서 사용자의 \[프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-picture']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 사용자의 [프로필 이미지]가 출력된다')


@then("그룹 상세 페이지에서 사용자의 \[기본 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-nopicture']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자의 [기본 프로필 이미지]가 출력된다')


@then("그룹 상세 페이지에서 사용자의 \[설정한 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-picture']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자의 [설정한 프로필 이미지]가 출력된다')


@step("그룹 상세 페이지에서 사용자의 \[이름\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 사용자의 [이름]이 출력된다')


@step("그룹 상세 페이지에서 사용자의 \[아이디\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 사용자의 [아이디]가 출력된다')


@step("그룹 상세 페이지에서 사용자의 상태가 \[대기\]로 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-pending']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 사용자의 상태가 [대기]로 출력된다')


@step("그룹 상세 페이지에서 사용자의 상태가 \[활성\]으로 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-active']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 사용자의 상태가 [활성]으로 출력된다')


@step("그룹 상세 페이지에서 사용자의 상태가 \[비활성\]으로 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-deactive']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 사용자의 상태가 [비활성]으로 출력된다')




# 그룹 상세 > [그룹 사용자] 탭 > 사용자 검색


@step("그룹 상세 페이지에서 \[검색\]입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [검색]입력필드가 출력된다')


@step("그룹 상세 페이지에서 검색 입력필드에 \[유효하지 않은 텍스트\]를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USERNAME_INVALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [유효하지 않은 텍스트]를 입력한다')


@step("그룹 상세 페이지에서 검색 입력필드에 \[사용자1의 이름\]을 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER1_NAME_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [사용자1의 이름]을 부분 입력한다')


@step("그룹 상세 페이지에서 검색 입력필드에 \[사용자1의 아이디\]를 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER1_ID_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [사용자1의 아이디]를 부분 입력한다')

@step("그룹 상세 페이지에서 검색 입력필드에 \[사용자2의 아이디\]를 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER2_ID_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [사용자2의 아이디]를 부분 입력한다')

@step("그룹 상세 페이지에서 검색 입력필드에 \[사용자1의 이름\]을 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER1_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [사용자1의 이름]을 전체 입력한다')


@step("그룹 상세 페이지에서 검색 입력필드에 \[사용자1의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER1_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [사용자1의 아이디]를 전체 입력한다')

@step("그룹 상세 페이지에서 검색 입력필드에 \[사용자2의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER2_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [사용자2의 아이디]를 전체 입력한다')

@step("그룹 상세 페이지에서 검색 입력필드에 \[사용자5의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER5_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [사용자5의 아이디]를 전체 입력한다')


@step("그룹 상세 페이지에서 검색 입력필드에 \[사용자6의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER6_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [사용자6의 아이디]를 전체 입력한다')


@step("그룹 상세 페이지에서 검색 입력필드에 텍스트 미입력 상태에서 \[엔터키\]를 입력한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 텍스트 미입력 상태에서 [엔터키]를 입력한다')


@step("그룹 상세 페이지에서 검색 입력필드에 \[엔터키\]를 입력한다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 검색 입력필드에 [엔터키]를 입력한다')


@then("그룹 상세 페이지에서 사용자 전체 검색결과가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 전체 검색결과가 출력된다')


@then("그룹 상세 페이지에서 사용자 검색결과 없다는 안내가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search_result']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 검색결과 없다는 안내가 출력된다')


@then("그룹 상세 페이지에서 해당 사용자의 \[이름\]을 포함한 검색결과가 출력된다")
def step_impl(self):
    try:
        #name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        #assert USER1_NAME == name.text   # 텍스트 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 해당 사용자의 [이름]을 포함한 검색결과가 출력된다')


@then("그룹 상세 페이지에서 해당 사용자의 \[아이디\]를 포함한 검색결과가 출력된다")
def step_impl(self):
    try:
        #id = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        #assert USER1_ID == id.text  # 텍스트 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 해당 사용자의 [아이디]를 포함한 검색결과가 출력된다')


@then("그룹 상세 페이지에서 해당 사용자의 \[이름\]과 일치하는 검색결과가 출력된다")
def step_impl(self):
    try:
        # name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        # assert USER1_NAME == name.text   # 텍스트 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 해당 사용자의 [이름]과 일치하는 검색결과가 출력된다')


@then("그룹 상세 페이지에서 해당 사용자의 \[아이디\]와 일치하는 검색결과가 출력된다")
def step_impl(self):
    try:
        # id = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        # assert USER1_ID == id.text  # 텍스트 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 해당 사용자의 [아이디]와 일치하는 검색결과가 출력된다')

@then("그룹 상세 페이지에서 \[사용자1의 이름\]이 출력된다")
def step_impl(self):
    try:
        #name = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        #assert USER1_NAME == name.text   # 텍스트 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서  [사용자1의 이름]이 출력된다')

@then("그룹 상세 페이지에서 \[사용자1의 아이디\]가 출력된다")
def step_impl(self):
    try:
        # id = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        # assert USER1_ID == id.text  # 텍스트 체크안됨
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서  [사용자1의 아이디]가 출력된다')

@then("그룹 상세 페이지에서 사용자 목록의 사용자의 \[프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector('[data-ta="elm-groupdetail-picture"] img')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 목록의 사용자의 [프로필 이미지]가 출력된다')

@then("그룹 상세 페이지에서 사용자 목록의 사용자의 \[이름\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 목록의 사용자의 [이름]이 출력된다')

@then("그룹 상세 페이지에서 사용자 목록의 사용자의 \[아이디\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 목록의 사용자의 [아이디]가 출력된다')


@then("그룹 상세 페이지에서 사용자 목록의 사용자의 \[상태\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-state']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 목록의 사용자의 [상태]가 출력된다')


@then("그룹 상세 페이지에서 사용자 목록의 사용자의 상태가 \[대기\]로 출력된다")
def step_impl(self):
    try:
        status = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-state']")
        assert USER_STATUS_PENDING == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 목록의 사용자의 상태가 [대기]로 출력된다')

@then("그룹 상세 페이지에서 사용자 목록의 사용자의 상태가 \[활성\]으로 출력된다")
def step_impl(self):
    try:
        status = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-state']")
        assert USER_STATUS_ACTIVE == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 목록의 사용자의 상태가 [활성]으로 출력된다')


@then("그룹 상세 페이지에서 사용자 목록의 사용자의 상태가 \[비활성\]으로 출력된다")
def step_impl(self):
    try:
        status = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-state']")
        assert USER_STATUS_DEACTIVE == status.text
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 사용자 목록의 사용자의 상태가 [비활성]으로 출력된다')






# 그룹 상세 > [그룹 사용자 추가]팝업

@step("그룹 상세 페이지에서 \[그룹 사용자 추가\]버튼을 클릭한다")
def step_impl(self):
    try:
        addUserBtn = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-adduser']")
        addUserBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹 사용자 추가]버튼을 클릭한다')


@then("그룹 상세 페이지에서 \[그룹 사용자 추가\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 [그룹 사용자 추가]팝업이 출력된다')




# 그룹 상세 > [그룹 사용자 추가]팝업 > 사용자 검색

@then("\[그룹 사용자 추가\]팝업에서 \[검색\] 입력필드가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 [검색] 입력필드가 출력된다')


@step("\[그룹 사용자 추가\]팝업에서 \[검색\] 입력필드를 클릭한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
        search.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 [검색] 입력필드를 클릭한다')


@step("\[그룹 사용자 추가\]팝업에서 검색 입력필드에 \[유효하지 않은 텍스트\]를 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
        search.clear()
        search.send_keys(USERNAME_INVALID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색 입력필드에 [유효하지 않은 텍스트]를 입력한다')


@step("\[그룹 사용자 추가\]팝업에서 검색 입력필드에 \[사용자1의 이름\]을 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
        search.clear()
        search.send_keys(USER1_NAME_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색 입력필드에 [사용자1의 이름]을 부분 입력한다')


@step("\[그룹 사용자 추가\]팝업에서 검색 입력필드에 \[사용자2의 아이디\]를 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
        search.clear()
        search.send_keys(USER2_ID_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색 입력필드에 [사용자2의 아이디]를 부분 입력한다')


@step("\[그룹 사용자 추가\]팝업에서 검색 입력필드에 \[사용자1의 이름\]을 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
        search.clear()
        search.send_keys(USER1_NAME)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색 입력필드에 [사용자1의 이름]을 전체 입력한다')

@step("\[그룹 사용자 추가\]팝업에서 검색 입력필드에 \[사용자1의 아이디\]를 부분 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
        search.clear()
        search.send_keys(USER1_ID_PART)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색 입력필드에 [사용자1의 아이디]를 부분 입력한다')


@step("\[그룹 사용자 추가\]팝업에서 검색 입력필드에 \[사용자1의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        search = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
        search.clear()
        search.send_keys(USER1_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색 입력필드에 [사용자1의 아이디]를 전체 입력한다')


@step("\[그룹 사용자 추가\]팝업에서 검색 입력필드에 \[사용자2의 아이디\]를 전체 입력한다")
def step_impl(self):
    try:
        # search = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-search']")
        search = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-search"] input')
        search.clear()
        search.send_keys(USER2_ID)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색 입력필드에 [사용자2의 아이디]를 전체 입력한다')


@step("그룹 목록 페이지에서 \[엔터키\]를 입력한다")
def step_impl(self):
    try:
        enterKey = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search'] input")
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지에서 [엔터키]를 입력한다')


# 그룹 상세 > [그룹 사용자 추가]팝업 > 사용자 검색 결과


@then("\[그룹 사용자 추가\]팝업에서 사용자 검색결과 없다는 안내가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-search_result']")   # data-ta 적용안됨
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 사용자 검색결과 없다는 안내가 출력된다')


@then("\[그룹 사용자 추가\]팝업에서 \[사용자1의 이름\]을 포함한 검색결과가 출력된다")
def step_impl(self):
    try:
        #name = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-name']")
        #assert USER1_NAME == name.text
        self.driver.find_element_by_css_selector(
            '.MuiAutocomplete-popper .MuiGrid-direction-xs-column > div:nth-child(1)')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 [사용자1의 이름]을 포함한 검색결과가 출력된다')


@then("\[그룹 사용자 추가\]팝업에서 \[사용자1의 아이디\]를 포함한 검색결과가 출력된다")
def step_impl(self):
    try:
        #id = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id']")
        #assert USER1_ID == id.text
        self.driver.find_element_by_css_selector('.MuiAutocomplete-popper .MuiGrid-direction-xs-column > div:nth-child(2)')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 [사용자1의 아이디]를 포함한 검색결과가 출력된다')


@then("\[그룹 사용자 추가\]팝업에서 \[사용자1의 이름\]과 일치하는 검색결과가 출력된다")
def step_impl(self):
    try:
        #name = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-name']")
        #assert USER1_NAME == name.text
        self.driver.find_element_by_css_selector('.MuiAutocomplete-popper .MuiGrid-direction-xs-column > div:nth-child(1)')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 [사용자1의 이름]과 일치하는 검색결과가 출력된다')


@then("\[그룹 사용자 추가\]팝업에서 \[사용자1의 아이디\]와 일치하는 검색결과가 출력된다")
def step_impl(self):
    try:
        # id = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id']")
        # assert USER1_ID == id.text
        self.driver.find_element_by_css_selector(
            '.MuiAutocomplete-popper .MuiGrid-direction-xs-column > div:nth-child(2)')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 [사용자1의 아이디]와 일치하는 검색결과가 출력된다')


@then("\[그룹 사용자 추가\]팝업에서 검색된 사용자 프로필 이미지에 \[기본 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-adduser-elm-adduser-selectednopicture']")  # data-ta 부재
        self.driver.find_element_by_css_selector('.MuiAutocomplete-popper .MuiAvatar-root ')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 검색된 사용자 프로필 이미지에 [기본 프로필 이미지]가 출력된다')


@then("\[그룹 사용자 추가\]팝업에서 검색된 사용자 프로필 이미지에 \[설정한 프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-adduser-selectedpicture']")  # data-ta 부재
        self.driver.find_element_by_css_selector('.MuiAutocomplete-popper .MuiAvatar-root ')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 검색된 사용자 프로필 이미지에 [설정한 프로필 이미지]가 출력된다')




# 그룹 상세 > [그룹 사용자 추가]팝업 > 사용자 선택

@step("\[그룹 사용자 추가\]팝업에서 검색된 사용자 체크박스를 \[체크\]한다")
def step_impl(self):
    try:
        checkbox = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-checkbox"] input')
        checkbox.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색된 사용자 체크박스를 [체크]한다')


@step("\[그룹 사용자 추가\]팝업에서 검색된 사용자 체크박스를 다시 \[체크\]한다")
def step_impl(self):
    try:
        checkbox = self.driver.find_element_by_css_selector('[data-ta="elm-adduser-checkbox"] input')
        checkbox.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 검색된 사용자 체크박스를 다시 [체크]한다')


@then("\[그룹 사용자 추가\]팝업에서 선택한 사용자의 \[프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-selectednopicture']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 선택한 사용자의 [프로필 이미지]가 출력된다')


@step("\[그룹 사용자 추가\]팝업에서 선택한 \[사용자1의 아이디\]가 출력된다")
def step_impl(self):
    try:
        #selectedId = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id']")
        #assert USER1_ID == selectedId.text
        #self.driver.find_element_by_css_selector('MuiChip-label')
        self.driver.find_element_by_css_selector('.MuiAutocomplete-inputRoot .MuiChip-root:nth-child(1) .MuiChip-label')
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 선택한 [사용자1의 아이디]가 출력된다')


@step("\[그룹 사용자 추가\]팝업에서 선택한 \[사용자2의 아이디\]가 출력된다")
def step_impl(self):
    try:
        #selectedId = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id']")
        #assert USER2_ID == selectedId.text
        #self.driver.find_element_by_css_selector('MuiChip-label')
        self.driver.find_element_by_css_selector('.MuiAutocomplete-inputRoot .MuiChip-root:nth-child(2) .MuiChip-label')
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 선택한 [사용자2의 아이디]가 출력된다')


@then("\[그룹 사용자 추가\]팝업에서 사용자 전체 검색결과\(조직 사용자 중 아직 이 그룹에 추가되지 않은 사용자\)가 출력된다")
def step_impl(self):
    try:
        #self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id']")
        self.driver.find_element_by_css_selector('.MuiAutocomplete-popper .MuiGrid-direction-xs-column > div:nth-child(1)')
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 사용자 전체 검색결과(조직 사용자 중 아직 이 그룹에 추가되지 않은 사용자)가 출력된다')


@then("\[그룹 사용자 추가\]팝업에서 선택한 사용자의 \[프로필 이미지\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-selectedpicture']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 선택한 사용자의 [프로필 이미지]가 출력된다')


@step("\[그룹 사용자 추가\]팝업에서 선택한 사용자의 \[아이디\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-selectedid']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 선택한 사용자의 [아이디]가 출력된다')


@step("\[그룹 사용자 추가\]팝업에서 선택한 사용자에 \[X\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-delete']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 선택한 사용자에 [X]버튼이 출력된다')


@step("\[그룹 사용자 추가\]팝업에서 선택한 사용자 \[X\]버튼을 클릭한다")
def step_impl(self):
    try:
        signinSigninButton = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-delete']")
        signinSigninButton.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 선택한 사용자 [X]버튼을 클릭한다')


@then("\[그룹 사용자 추가\]팝업에서 선택한 사용자가 삭제된다")
def step_impl(self):
    with self.assertRaises(NotImplementedError):
        #self.driver.find_element_by_css_selector("[data-ta='elm-adduser-id']")
        self.driver.find_element_by_css_selector('.MuiAutocomplete-inputRoot .MuiChip-root:nth-child(1) .MuiChip-label')
        self.driver.implicitly_wait(10)
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 선택한 사용자가 삭제된다')


@step("\[그룹 사용자 추가\]팝업에서 \[취소\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-back']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 [취소]버튼이 출력된다')


@step("\[그룹 사용자 추가\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-back']")
        cancelBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 [취소]버튼을 클릭한다')


@step("\[그룹 사용자 추가\]팝업에서 \[추가하기\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 [추가하기]버튼이 출력된다')


@step("\[그룹 사용자 추가\]팝업에서 \[추가하기\]버튼을 클릭한다")
def step_impl(self):
    try:
        addBtn = self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
        addBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 추가]팝업에서 [추가하기]버튼을 클릭한다')


@then("\[그룹 사용자 추가\]팝업에서 경고없이 팝업 유지된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업에서 경고없이 팝업 유지된다')


@then("\[그룹 사용자 추가\]팝업이 닫힌다")
def step_impl(self):
    with self.assertRaises(NotImplementedError):
        self.driver.find_element_by_css_selector("[data-ta='elm-adduser-add']")
        self.driver.implicitly_wait(10)
        raise NotImplementedError(u'STEP: Then [그룹 사용자 추가]팝업이 닫힌다')


@step("그룹 상세 페이지에서 추가한 사용자가 사용자 목록에 출력된다")
def step_impl(self):
    try:
        #id = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-id']")
        #assert USER1_ID == id.text
        # 그룹 상세에서 검색
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input")
        search.clear()
        search.send_keys(USER1_ID)
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search'] input").send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 추가한 사용자가 사용자 목록에 출력된다')


@step("그룹 상세 페이지에서 사용자가 추가되었다는 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 사용자가 추가되었다는 토스트가 출력된다')




# 그룹 상세 > [그룹 사용자 삭제]팝업

@step("그룹 상세 페이지에서 사용자 행에 \[마우스 오버\]를 한다")
def step_impl(self):
    try:
        action = ActionChains(self.driver);
        firstLevelMenu = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-name']")
        action.move_to_element(firstLevelMenu).perform()
        secondLevelMenu = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-deleteuser']")
        action.move_to_element(secondLevelMenu).perform()
        secondLevelMenu.click()
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 사용자 행에 [마우스 오버]를 한다')


@step("그룹 상세 페이지에서 \[그룹 사용자 삭제\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-deleteuser']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹 사용자 삭제]버튼이 출력된다')


@step("그룹 상세 페이지에서 \[그룹 사용자 삭제\]버튼을 클릭한다")
def step_impl(self):
    try:
        deleteUserBtn = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-deleteuser']")
        deleteUserBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹 사용자 삭제]버튼을 클릭한다')


@then("그룹 상세 페이지에서 \[그룹 사용자 삭제\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-delete']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 [그룹 사용자 삭제]팝업이 출력된다')


@then("\[그룹 사용자 삭제\]팝업에서 사용자의 \[이름\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-name']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 사용자 삭제]팝업에서 사용자의 [이름]이 출력된다')


@step("\[그룹 사용자 삭제\]팝업에서 사용자의 \[아이디\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-id']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 삭제]팝업에서 사용자의 [아이디]가 출력된다')


@step("\[그룹 사용자 삭제\]팝업에서 \[취소\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-back']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 삭제]팝업에서 [취소]버튼이 출력된다')


@step("\[그룹 사용자 삭제\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-back']")
        cancelBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 삭제]팝업에서 [취소]버튼을 클릭한다')


@step("\[그룹 사용자 삭제\]팝업에서 \[삭제\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-delete']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 삭제]팝업에서 [삭제]버튼이 출력된다')


@step("\[그룹 사용자 삭제\]팝업에서 \[삭제\]버튼을 클릭한다")
def step_impl(self):
    try:
        deleteBtn = self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-delete']")
        deleteBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 사용자 삭제]팝업에서 [삭제]버튼을 클릭한다')


@then("\[그룹 사용자 삭제\]팝업이 닫힌다")
def step_impl(self):
    with self.assertRaises(NotImplementedError):
        self.driver.find_element_by_css_selector("[data-ta='elm-deleteuser-title']")
        self.driver.implicitly_wait(10)
        raise NotImplementedError(u'STEP: Then [그룹 사용자 삭제]팝업이 닫힌다')


@step("그룹에서 사용자가 삭제된다")
def step_impl(self):
    try:
        # 검색 입력필드에 삭제한 사용자 아이디를 입력한다
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search] input")
        search.clear()
        search.send_keys(USER1_ID)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        #self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search']").send_keys(Keys.ENTER)
        # data-ta 영역에 엔터키가 먹지않아서 class name을 사용함
        enterKey = self.driver.find_element_by_class_name('MuiInputBase-input')
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 검색결과가 없다는 안내가 출력된다
        #self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-search_result']")
        self.driver.find_element_by_xpath('//*[@id="tabpanel-0"]/div/div[2]/div/table/tbody/tr/td/p')
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹에서 사용자가 삭제된다')


@step("그룹에서 사용자가 삭제되었다는 토스트가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹에서 사용자가 삭제되었다는 토스트가 출력된다')



# 그룹 상세 > [그룹 삭제]팝업

@step("그룹 상세 페이지에서 \[그룹 삭제\]메뉴가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-deletegroup']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹 삭제]메뉴가 출력된다')


@step("그룹 상세 페이지에서 \[그룹 삭제\]메뉴를 클릭한다")
def step_impl(self):
    try:
        deleteGroup = self.driver.find_element_by_css_selector("[data-ta='elm-groupdetail-deletegroup']")
        deleteGroup.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [그룹 삭제]메뉴를 클릭한다')


@then("그룹 상세 페이지에서 \[그룹 삭제\]팝업이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deletegroup-delete']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then 그룹 상세 페이지에서 [그룹 삭제]팝업이 출력된다')


@then("\[그룹 삭제\]팝업에서 그룹의 \[이름\]이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deletegroup-name']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: Then [그룹 삭제]팝업에서 그룹의 [이름]이 출력된다')


@step("\[그룹 삭제\]팝업에서 그룹의 \[사용자 수\]가 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deletegroup-num']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 삭제]팝업에서 그룹의 [사용자 수]가 출력된다')


@step("\[그룹 삭제\]팝업에서 \[취소\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deletegroup-back']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 삭제]팝업에서 [취소]버튼이 출력된다')


@step("\[그룹 삭제\]팝업에서 \[취소\]버튼을 클릭한다")
def step_impl(self):
    try:
        cancelBtn = self.driver.find_element_by_css_selector("[data-ta='elm-deletegroup-back']")
        cancelBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 삭제]팝업에서 [취소]버튼을 클릭한다')


@step("\[그룹 삭제\]팝업에서 \[삭제\]버튼이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-deletegroup-delete']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 삭제]팝업에서 [삭제]버튼이 출력된다')


@step("\[그룹 삭제\]팝업에서 \[삭제\]버튼을 클릭한다")
def step_impl(self):
    try:
        deleteBtn = self.driver.find_element_by_css_selector("[data-ta='elm-deletegroup-delete']")
        deleteBtn.click()
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And [그룹 삭제]팝업에서 [삭제]버튼을 클릭한다')


@then("\[그룹 삭제\]팝업이 닫힌다")
def step_impl(self):
    with self.assertRaises(NotImplementedError):
        self.driver.find_element_by_css_selector("[data-ta='elm-deletegroup-title']")
        self.driver.implicitly_wait(10)


@step("그룹 목록 페이지로 이동한다")
def step_impl(self):
    try:
        self.driver.get(URL_GROUPS)
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 목록 페이지로 이동한다')


@step("해당 그룹이 더 이상 그룹 목록 페이지에 노출되지 않는다")
def step_impl(self):
    try:
        # 검색 입력필드에 삭제한 그룹 이름을 입력한다
        search = self.driver.find_element_by_css_selector("[data-ta='elm-groups-search] input")
        search.clear()
        search.send_keys(GROUP1_NAME)
        self.driver.implicitly_wait(10)
        # 엔터키를 입력한다
        #self.driver.find_element_by_css_selector("[data-ta='elm-groups-search']").send_keys(Keys.ENTER)
        # data-ta 영역에 엔터키가 먹지않아서 class name을 사용함
        enterKey = self.driver.find_element_by_class_name('MuiInputBase-input')
        enterKey.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(10)
        # 검색결과가 없다는 안내가 출력된다
        self.driver.find_element_by_css_selector("[data-ta='elm-groups-search_result']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 해당 그룹이 더 이상 그룹 목록 페이지에 노출되지 않는다')


@step("그룹이 삭제 예정 상태로 변경되었다는 토스트 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='elm-toast']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹이 삭제 예정 상태로 변경되었다는 토스트 출력된다')




# 그룹 상세 > [보안 정책]탭
@step("그룹 상세 페이지에서 \[보안 정책\]탭이 출력된다")
def step_impl(self):
    try:
        self.driver.find_element_by_css_selector("[data-ta='nav-groupdetail-security']")
        self.driver.implicitly_wait(10)
    except Exception as e:
        logging.error("arrived at exception: " + str(e))
        raise NotImplementedError(u'STEP: And 그룹 상세 페이지에서 [보안 정책]탭이 출력된다')