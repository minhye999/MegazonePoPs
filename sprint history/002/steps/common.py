#### Test Data ####


# Web diver 경로
CHROME = "F:/PyCharm/Project/MegazonePoPs/venv/webdriver/chromedriver.exe"
#CHROME = 'executable_path="../Pops/venv/webdriver/chromedriver_v.0.86.exe'
#CHROME = 'executable_path="F:/PyCharm/Project/Pops/venv/webdriver/chromedriver_v.0.86.exe'
#CHROME = 'executable_path="F:/PyCharm/Project/Pops/venv/webdriver/chromedriver_v.0.87.0.exe'
Firefox = 'executable_path="F:/PyCharm/Project/Pops/venv/webdriver/geckodriver_v.0.28.0.exe"'
IE_11 = 'executable_path="F:/PyCharm/Project/Pops/venv/webdriver/iedriver.exe"'
IE_EDGE = 'executable_path="F:/PyCharm/Project/Pops/venv/webdriver/msedgedriver.exe"'

# Url (dev)
URL_POPS = "https://start.mzdev.com"  # POPS 앱 자동로그인하는 대시보드 = 메가존 런처 = PoPs는 앞으로 로그인, 어드민, 런처를 전체적으로 이야기할 때 사용
URL_SIGNIN = "https://login.mzdev.com/"  # 메가존 로그인 페이지
#URL_MYINFO = "https://my.mzdev.com"  "https://myaccount.mzdev.com"   "https://id.mzdev.com"   # 메가존 프로필 페이지 미정
URL_SINGIN_FORGOT_PASSWORD = "https://login.mzdev.com/password/reset/lookup"  # 비밀번호 재설정 페이지
URL_SINGIN_SEND_RESETPWMAIL ="https://login.mzdev.com/password/reset/done" #비밀번호 재설정 메일 발송완료 페이지
URL_MFAINFO = "https://login.mzdev.com/mfa/info"  # 2단계 인증 설정 안내 페이지
URL_OTPSET = "https://login.mzdev.com/mfa/set"  # OTP 설정 페이지
URL_GOOGLEPLAY = "https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2" # Google Play 페이지
URL_APPSTORE = "https://apps.apple.com/us/app/google-authenticator/id388497605"  # App Store 페이지
URL_MFADONE = "https://login.mzdev.com/mfa/done"  # 2단계 인증 설정완료 페이지
URL_MFA = "https://login.mzdev.com/mfa"  # 2단계 인증 페이지
URL_NOTFOUND =  "https://login.mzdev.com/zzz"  # 존재하지 않는 페니지
URL_CPD = "https://https://cad.megazoneauth.com/signin"  # 딜리버리 페이지
URL_DASHBOARD = "https://start.mzdev.com/"  # 대시보드 페이지
URL_SIGNOUT = "https://login.mzdev.com/logout?redirect=http://www.naver.com"  # 로그아웃
#URL_MZLUNCHER =  (apps.megazone.com or etc.)  start.login.mzdev.com # 메가존 런처 미정
URL_ACTIVE = "https://login.mzdev.com/activate?token=TKS-iDzwYSXdUmJsoP0mvsJZTJt99XMODh"  # 계정 활성화 페이지 (비밀번호 설정)
URL_ACTIVATED = "https://login.mzdev.com/activate/done"   # 계정 활성화 완료 페이지



# 메가존 어드민 페이지 (dev)
URL_ADMIN = "https://login.mzdev.com/?app=https://admin.mzdev.com"   # 메가존 어드민 로그인 페이지
URL_ADMIN2 = "https://admin.mzdev.com"  # 메가존 어드민 페이지
URL_USERS = "https://admin.mzdev.com/users"  # 사용자 > 사용자
URL_GROUPS = "https://admin.mzdev.com/users/groups"  # 사용자 > 그룹
URL_DIRECTORY = "https://admin.mzdev.com/users/directories"  # 사용자 > 디렉터리
URL_CUSTOMFIELDS = "https://admin.mzdev.com/users/custom-fields"  # 사용자 > 사용자 정의 필드
URL_APP = "https://admin.mzdev.com/apps"  # 앱
URL_ACCESSCONTROLS = "https://admin.mzdev.com/apps/policies"  # 앱 > 접근제어
URL_SECURITY_MANAGE_ONLINE_USERS = "https://admin.mzdev.com/securities/tokens"  # 보안 > 로그인 관리
URL_SECURITY_POLICIES = "https://admin.mzdev.com/apps/policies"  # 보안 > 보안 정책
URL_REPORTS = "https://admin.mzdev.com/apps/policies"  # 보고서


# Url (staging)

# Url (product)
#URL_POPS = "https://start.megazone.com" # POPS 앱 자동로그인하는 대시보드 = 메가존 런처 = PoPs는 앞으로 로그인, 어드민, 런처를 전체적으로 이야기할 때 사용
#URL_SIGNIN = "https://login.megazone.com/"  # 메가존 로그인 페이지
#URL_ADMIN = "https://admin.megazone.com" # 메가존 어드민 페이지
#URL_MYINFO = "https://my.megazone.com"  "https://myaccount.megazone.com"   "https://id.megazone.com"   # 메가존 프로필 페이지 미정
#URL_SINGIN_FORGOT_PASSWORD = "https://login.mzdev.com/password/reset/lookup"  # 비밀번호 재설정 페이지
#URL_SINGIN_SEND_RESETPWMAIL ="https://login.mzdev.com/password/reset/done" #비밀번호 재설정 메일 발송완료 페이지
#URL_MFAINFO = "https://login.mzdev.com/mfa/info"  # 2단계 인증 설정 안내 페이지
#URL_OTPSET = "https://login.mzdev.com/mfa/set"  # OTP 설정 페이지
#URL_GOOGLEPLAY = "https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2" # Google Play 페이지
#URL_APPSTORE = "https://apps.apple.com/us/app/google-authenticator/id388497605"  # App Store 페이지
#URL_MFADONE = "https://login.mzdev.com/mfa/done"  # 2단계 인증 설정완료 페이지
#URL_MFA = "https://login.mzdev.com/mfa"  # 2단계 인증 페이지
#URL_NOTFOUND =  "https://login.mzdev.com/zzz"  # 존재하지 않는 페니지
#URL_CPD = "https://https://cad.megazoneauth.com/signin"  # 딜리버리 페이지
#URL_DASHBOARD = "https://start.mzdev.com/"  # 대시보드 페이지
#URL_SIGNOUT = "https://login.mzdev.com/logout?redirect=http://www.naver.com"  # 로그아웃
#URL_MZLUNCHER =  (apps.megazone.com or etc.)  start.login.mzdev.com # 메가존 런처 미정



# Username & Password
USERNAME_INVALID = "winner@naver.com"
PASSWORD_INVALID = "Megazone1@"
USERNAME_UNNEEDMFA = "minhye9@megazone.com" # MFA 설정 필요없는 유저 (Default)
PASSWORD_UNNEEDMFA_USER = "Megazone1!" # MFA 설정 필요없는 유저의 비밀번호
USERNAME_NEEDMFA = "jhm@mz.co.kr" # MFA 설정 필요한 유저           wjdgkaud87!
PASSWORD_NEEDMFA_USER = "wjdgkaud87!" # MFA 설정 필요한 유저의 비밀번호
USERNAME_HADMFA = "minhye9@mz.co.kr" # MFA 설정 보유한 유저
PASSWORD_HADMFA_USER = "Megazone1!" # MFA 설정 보유한 유저의 비밀번호

# Group Name
GROUP_NAME_INVALID = "nogroupname"  # 유효하지 않은 그룹 이름
GROUP_NAME_DEFAULT = "Everyone"  # 기본 그룹 이름 (검색 기본 대상)
GROUP_DESC_DEFAULT = "기본 그룹입니다."  # 기본 그룹 설명 (설명 있음)
GROUP_DETAIL_DEFAULT = "https://admin.mzdev.com/groups/GRP-default"    # 기본 그룹 상세페이지

# 그룹1
GROUP1_NAME = "group1"  # 그룹 이름
GROUP1_NAME_PART = "oup1"  # 그룹 이름 부분
GROUP1_DESC = "-"  # 그룹 설명
GROUP1_NAME_EDIT = "group1♡"  # 그룹 이름
GROUP1_NAME_EDIT2 = "group1♡♡"  # 그룹 이름
GROUP1_DESC_EDIT = "group1 description♡"  # 그룹 설명

# 그룹2
GROUP2_NAME = "group2"  # 그룹 이름
GROUP2_NAME_PART = "oup2"  # 그룹 이름 부분
GROUP2_DESC = "group2 description"  # 그룹 설명
GROUP2_NAME_EDIT = "group2♡"  # 그룹 이름
GROUP2_DESC_EDIT = "group2 description♡"  # 그룹 설명


# MFA Code
MFACODE_VALID = "1234" # 유효한 인증 코드
MFACODE_INVALID = "1234" # 유효하지 않은 인증 코드

# EMAIL
EMAIL_VALID = "minhye9@mz.co.kr"
EMAIL_INVALID_TYPE = "test"

# PW
PW_INVALID_LIMIT_LESS = "1"

# 지원문자 확인을 위한 문자
TEXT_NUM = "1234"  # 숫자
TEXT_KO = "한글"  # 한글
TEXT_EN = "English"  # 영어
TEXT_CHAR = "`~!@#$%^&*()_+-=[]{}\|;':,./<>?"  # 특수문자


#### Resource ####
# 유효성 체크 메시지 (TEXT-대상-실패/성공)
MSG_SIGN_NULL_USERNAME = "필수 항목 입니다."  # 이메일 입력필드 미입력 > [로그인]버튼 클릭
MSG_SIGN_NULL_PW = "필수 항목 입니다."  # 비밀번호 입력필드 미입력 > [로그인]버튼 클릭
MSG_SIGNIN_INVALID_TYPE = "이메일 형식으로 입력해주세요."  # 이메일 입력필드 > 형식 틀리게 입력
MSG_SIGNIN_INVALID_TEXT = "이메일 또는 비밀번호를 정확히 입력해주세요."   # 이메일 입력필드 > 이메일 or 비밀번호 틀리게 입력
MSG_SIGNIN_INVALID_PW_LIMIT_LESS = "비밀번호는 최소 8자리 이상입니다."  # 비밀번호 입력필드 > 비밀번호 8자리 미만 입력

MSG_MFA_CODE_NULL = "필수 항목 입니다."  # OTP 설정 페이지 & 2단계 인증 페이지 > 인증 코드 미입력 > [로그인]버튼 클릭
MSG_MFA_INVALID_CHAR = "숫자만 입력해주세요."  # OTP 설정 페이지 & 2단계 인증 페이지 > 인증 코드 한글 입력 > [로그인]버튼 클릭
MSG_MFA_CODE_INVALID = "인증 코드를 정확하게 입력해주세요."  # OTP 설정 페이지 & 2단계 인증 페이지 > 인증 코드 틀리게 입력 > [로그인]버튼 클릭

MSG_EMAIL_INVALID_NULL = "필수 항목 입니다."  # 이메일 형식 확인 실패 메시지
MSG_EMAIL_INVALID_TYPE = "이메일 형식으로 입력해주세요."  # 이메일 형식 확인 실패 메시지
MSG_EMAIL_INVALID_TEXT = "이메일을 정확히 입력해주세요."  # 이메일 확인 실패 메시지

# 텍스트 (TEXT-페이지-항목)
TEXT_SINGIN_TITLE = "로그인" # 로그인 페이지 타이틀
TEXT_SINGIN_DESC = "MEGAZONE LAUNCHER(으)로 이동" #로그인 페이지 설명      # "to continue to MEGAZONE LAUNCHER"
TEXT_SINGIN_USERNAMEPLACEHOLDER = "이메일을 입력해주세요" # 로그인 페이지 Username Placeholder
TEXT_SINGIN_PWPLACEHOLDER = "비밀번호를 입력해주세요" # 로그인 페이지 Password Placeholder

TEXT_MFAINFO_TITLE = "2단계 인증 설정"
TEXT_MFAINFO_DESC = "이 조직에 로그인하려면 2단계 인증이 필요합니다.\n아래 버튼을 눌러 2단계 인증을 설정해주세요."

TEXT_OTPSET_TITLE = "OTP 설정"  # OTP 설정 타이틀
TEXT_OTPSET_DESC = "조직에 로그인할 때마다 OTP 앱에서 발급되는 일회용 인증 코드를 한번 더 입력해야 로그인이 완료되는 이중 보안 서비스입니다.\nOTP 앱이 없는 사용자는 하단 링크를 통해 설치해주세요." # OTP 설정 설명
TEXT_OTPSET_SCANTITLE = "1. 바코드 스캔"
TEXT_OTPSET_SCANDESC = "OTP 앱을 사용하여 바코드를 스캔해주세요."
TEXT_OTPSET_MFACODETITLE = "2. 인증 코드 입력"
TEXT_OTPSET_MFACODEDESC = "OTP 앱에 표시된 인증 코드를 입력해주세요."
TEXT_OTPSET_MFACODEPLACEHOLDER = "인증 코드를 입e력해주세요" # 인증 코드 입력필드 placeholder
TEXT_OTPSET_GOOGLEPLAY = "Google play" # Googl Play 텍스트
TEXT_OTPSET_APPSTORE = "App Store" # App Store 텍스트
TEXT_OTPSET_SECRETKEY = "표시된 비밀 키를 OTP 앱에 입력해주세요." # 비밀 키 설명

TEXT_MFA_TITLE = "2단계 인증" # 2단계 인증페이지 타이틀
TEXT_MFA_DESC = "OTP 앱에 표시된 인증 코드를 입력해주세요." # 2단계 인증페이지 설명
TEXT_MFA_CODEPLACEHOLDER = "인증 코드"  # 2단계 인증페이지 인증 코드 Palceholder

TEXT_RESETPW_TITLE = "비밀번호 재설정" # 비밀번호 재설정 페이지 타이틀
TEXT_RESETPW_DESC = "계정의 이메일 주소를 입력해주세요.\n비밀번호 재설정 링크가 포함된 메일이 계정의 이메일 주소로 발송됩니다." # 비밀번호 재설정 페이지 설명
TEXT_RESETPW_EMAILPLACEHOLDER = "이메일을 입력해주세요" # 비밀번호 재설정 페이지 Placeholder
TEXT_PWSENDED_TITLE = "비밀번호 재설정 메일 발송 완료"
TEXT_PWSENDED_DESC = "비밀번호 재설정 링크가 포함된 메일이 발송되었습니다.\n비밀번호 재설정 링크의 유효 시간은 1시간입니다.\n메일함을 확인해주세요."

TEXT_FOOTER_COPYRIGHT = "Copyright © MegazoneCloud Corp. All rights Reserved." #copyright
TEXT_FOOTER_KOREAN = "한국어"
TEXT_FOOTER_ENGLISH = "English"

TEXT_404_TITLE = "페이지가 존재하지 않습니다." #404 페이지 타이틀
TEXT_404_DESC = "죄송합니다.\n요청하신 페이지가 변경되었거나 더 이상 존재하지 않습니다." #404 페이지 설명

# TOAST (TOAST-페이지-대상)
TOAST_OTPSET_COPY = "복사했습니다."  # 비밀 키 복사완료 토스트
TOAST_MFACODE_SET = "2단계 인증이 설정되었습니다." # 2단계 인증 설정완료 토스트



# Admin Data
ID_NOPICTURE = "minhye9@mz.co.kr"  # 프로필 이미지를 미등록한 사용자 아이디
PW_NOPICTURE = "Megazone1!"  # 프로필 이미지를 미등록한 사용자 비밀번호
ID_HADPICTURE = "minhye9@megazone.com"  # 프로필 이미지를 등록한 사용자 아이디
PW_HADPICTURE = "Megazone1!"  # 프로필 이미지를 등록한 사용자 비밀번호
ID_PENDING = ""  # 대기 상태인 사용자 아이디 & 로그인 이력없는 사용자 아이디
PW_PENDING = ""  # 대기 상태인 사용자 비밀번호 & 로그인 이력없는 사용자 비밀번호
ID_HADSIGNIN = "minhye9@megazone.com"  # 로그인 이력있는 사용자 아이디
PW_HADSIGNIN = "Megazone1!"  # 로그인 이력있는 사용자 비밀번호

FAMILYNAME_UNNEEDMFA_DEACTIVE = ""  # 2단계 설정 필요없고, 비활성화 상태인 사용자 성
FIRSTNAME_UNNEEDMFA_DEACTIVE = ""  # 2단계 설정 필요없고, 비활성화 상태인 사용자 이름
ID_UNNEEDMFA_DEACTIVE = ""  # 2단계 설정 필요없고, 비활성화 상태인 사용자 아이디
PW_UNNEEDMFA_DEACTIVE = ""  # 2단계 설정 필요없고, 비활성화 상태인 사용자 비밀번호

FAMILYNAME_UNNEEDMFA_ACTIVE = "송"  # 2단계 설정 필요없고, 활성화 상태인 사용자 성
FIRSTNAME_UNNEEDMFA_ACTIVE = "민호"  # 2단계 설정 필요없고, 활성화 상태인 사용자 이름
FIRSTNAME_PART_UNNEEDMFA_ACTIVE = "호"  # 2단계 설정 필요없고, 활성화 상태인 사용자 부분 이름
ID_UNNEEDMFA_ACTIVE = "minhye9@megazone.com"  # 2단계 설정 필요없고, 활성화 상태인 사용자 아이디
ID_PART_UNNEEDMFA_ACTIVE = "hye9@mega"  # 2단계 설정 필요없고, 활성화 상태인 사용자 부분 아이디
PW_UNNEEDMFA_ACTIVE = "minhye9@megazone.com"  # 2단계 설정 필요없고, 활성화 상태인 사용자 비밀번호

FAMILYNAME_HADMFA_DEACTIVE = ""  # MFA 인증하고, 비활성화 상태인 사용자 성
FIRSTNAME_HADMFA_DEACTIVE = ""  #ID_HADMFA_ACTIVE MFA 인증하고, 비활성화 상태인 사용자 이름
ID_HADMFA_DEACTIVE = "user9@yopmail.com"  # MFA 인증하고, 비활성화 상태인 사용자 아이디
PW_HADMFA_DEACTIVE = ""  # MFA 인증하고, 비활성화 상태인 사용자 비밀번호

FAMILYNAME_HADMFA_ACTIVE = "구"  # MFA 인증하고, 활성화 상태인 사용자 성
FIRSTNAME_HADMFA_ACTIVE = "민혜"  # MFA 인증하고, 활성화 상태인 사용자 이름
ID_HADMFA_ACTIVE = "minhye9@mz.co.kr"  # MFA 인증하고, 활성화 상태인 사용자 아이디
PW_HADMFA_ACTIVE = "minhye9@mz.co.kr"  # MFA 인증하고, 활성화 상태인 사용자 비밀번호

FAMILYNAME_NEEDMFA_DEACTIVE = ""  # MFA 설정 필요하고, 비활성화 상태인 사용자 성
FIRSTNAME_NEEDMFA_DEACTIVE = ""  # MFA 설정 필요하고, 비활성화 상태인 사용자 이름
ID_NEEDMFA_DEACTIVE = ""  # MFA 설정 필요하고, 비활성화 상태인 사용자 아이디
PW_NEEDMFA_DEACTIVE = ""  # MFA 설정 필요하고, 비활성화 상태인 사용자 비밀번호

FAMILYNAME_NEEDMFA_ACTIVE = "jhm@mz.co.kr"  # MFA 설정 필요하고, 활성화 상태인 사용자 성
FIRSTNAME_NEEDMFA_ACTIVE = "jhm@mz.co.kr"  # MFA 설정 필요하고, 활성화 상태인 사용자 이름
ID_NEEDMFA_ACTIVE = "jhm@mz.co.kr"  # MFA 설정 필요하고, 활성화 상태인 사용자 아이디
PW_NEEDMFA_ACTIVE = "jhm@mz.co.kr"  # MFA 설정 필요하고, 활성화 상태인 사용자 비밀번호

ID_OWNER_ACTIVE = "hong@mz.co.kr"  # 주소유자 사용자 아이디
PW_OWNER_ACTIVE = "Megazone1!"  # 주소유자 사용자 비밀번호

ID_GROUP_NOTREQUIRED_CUSTOM = ""  # 사용자 정의 필드 필수값 아닌 그룹의 사용자 아이디
PW_GROUP_NOTREQUIRED_CUSTOM = ""  # 사용자 정의 필드 필수값 아닌 그룹의 사용자 비밀번호

ID_GROUP_REQUIRED_CUSTOME = ""  # 사용자 정의 필드 필수값인 그룹의 사용자 아이디
PW_GROUP_REQUIRED_CUSTOMOM = ""  # 사용자 정의 필드 필수값인 그룹의 사용자 비밀번호

ID_DELETE = "test1@yopmail.com"  # 생성하고 삭제할 사용자 아이디

PATH_USER_PROFILE_IMAGE = "C:/testdata/user_profile_image.gif"  # 사용자 프로필 이미지
PATH_USER_PROFILE_IMAGE_EDIT = "C:/testdata/user_profile_image_edit.gif"  # 사용자 프로필 이미지
PATH_USER_PROFILE_IMAGE_INVALID_EXTENSION = "C:/testdata/user_profile.txt"  # 사용자 프로필 이미지 (미지원 확장자)
PATH_USER_PROFILE_IMAGE_INVALID_SIZE = "C:/testdata/excess5MB.png"  # 사용자 프로필 이미지 (크기 5MB 초과)

# 사용자 1
USER1_ID = "user1@yopmail.com"  # 사용자1의 전체 아이디
USER1_ID_PART = "user1"  # 사용자1의 부분 아이디
USER1_FAMILYNAME = "강"  # 사용자1의 성
USER1_FAMILYNAME_EDIT = "♡강"  # 사용자1의 성 변경
USER1_FIRSTNAME = "승윤"  # 사용자1의 이름
USER1_FIRSTNAME_EDIT = "승윤♡"  # 사용자1의 이름 변경
USER1_NAME = "강승윤"  # 사용자1의 전체 이름
USER1_NAME_PART = "승윤"  # 사용자1의 부분 이름
USER1_PW = "Megazone1!"  # 사용자1의 비밀번호
USER1_PHONE = ""  # 사용자1의 폰 번호
USER1_DEPT = ""  # 사용자1의 부서
USER1_SUBMAIL = "user1sub@yopmail.com"  # 보조이메일
USER1_LASTLOGIN = "-"  # 사용자1의 최근 로그인 이력

# 사용자 2
USER2_ID = "user2@yopmail.com"  # 사용자2의 아이디 (부서없음)
USER2_ID_PART = "user2"  # 사용자2의 부분 아이디
USER2_FAMILYNAME = "송"  # 사용자2의 성
USER2_FIRSTNAME = "민호"  # 사용자2의 이름
USER2_NAME = "송민호"  # 사용자2의 전체 이름
USER2_NAME_PART = "민호"  # 사용자1의 부분 이름
USER2_PHONE = "010-1234-5678"  # 사용자2의 폰 번호
USER2_DEPT = "PDC"  # 사용자2의 부서
USER2_LASTLOGIN = "2020-11-21"  # 사용자2의 최근 로그인 이력

# 사용자 3
USER3_ID = "user3@yopmail.com"  # 사용자3의 아이디 (전화번호 없음)
USER3_ID_PART = "user3"  # 사용자2의 부분 아이디
USER3_FAMILYNAME = "김"  # 사용자3의 성
USER3_FIRSTNAME = "진우"  # 사용자3의 이름
USER3_NAME = "김진우"  # 사용자3의 전체 이름
USER3_PHONE = "010-1234-5678"  # 사용자3의 폰 번호
USER3_DEPT = "PDC"  # 사용자3의 부서

# 사용자 4
USER4_ID = "user4@yopmail.com"  # 사용자4의 아이디
USER4_FAMILYNAME = "이"  # 사용자3의 성
USER4_FIRSTNAME = "승훈"  # 사용자3의 이름
USER4_NAME = "이승훈"  # 사용자3의 전체 이름
USER4_PHONE = "010-1234-5678"  # 사용자3의 폰 번호
USER4_DEPT = "PDC"  # 사용자3의 부서


# 사용자 7
USER7_ID = "user7@yopmail.com"  # 사용자7의 아이디 MFA 인증하고, 활성화 상태인 사용자의 아이디
USER7_PW = "Megazone1!"  # 사용자7의 아이디 MFA 인증하고, 활성화 상태인 사용자의 비밀번호

# 사용자 9
USER9_ID = "user9@yopmail.com"  # 사용자9의 아이디 MFA 인증하고, 비활성화 상태인 사용자

# 사용자 10
USER10_ID = "user10@yopmail.com"  # 사용자10의 아이디

# 상태
USER_STATUS_PENDING = "대기"  # [대기] 상태
USER_STATUS_ACTIVE = "활성"  # [활성] 상태
USER_STATUS_DEACTIVE = "비활성"  # [비활성] 상태

# 상태별 유저 (사용자5 / 사용자6)
USER5_ID = "user5@yopmail.com"  # [활성] 상태의 유저 ★ 사전 데이터
USER5_ID_PART = "user5"  # 사용자5의 부분 아이디
USER5_PW = "Megazone1!"  # 사용자5의 패스워드

USER6_ID = "user6@yopmail.com"  # [비활성] 상태의 유저 ★ 사전 데이터
USER6_ID_PART = "user6"  # 사용자6의 부분 아이디

# 삭제할 유저
USER100_ID = "user100@yopmail.com"  # 사용자100의 아이디 (삭제할 유저)
USER100_ID_PART = "user100"  # 사용자100의 아이디 (삭제할 유저)

USER99_ID = "user99@yopmail.com"  # 사용자100의 아이디 (삭제할 유저)
USER99_ID_PART = "user99"  # 사용자99의 아이디 (삭제할 유저)

NEW_USER2_ID = "mino@yopmail.com"  # B사용자 아이디

NO_DATA = "-"  # 데이터 없는 경우, 하이픈(-) 표시

# Breadcrumb
BREADCRUMB_USER_DETAIL = "사용자 / 사용자 상세"  # 사용자 > 사용자 상세
BREADCRUMB_GROUP_DETAIL = "사용자 / 그룹 상세"  # 사용자 > 그룹 상세

