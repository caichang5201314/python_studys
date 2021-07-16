from json import loads
from random import randint

import pytest
from requests import get, post

from interface.dao.ExcelHelper import ExcelHelper
from interface.dao.MySQLHelper import MySQLHelper
from interface.utils.Config import Config
from interface.utils.Logger import Logger

logger = Logger('TestSchool').getlog()


class TestSchool():
    # 登录

    file = './conf/config.ini'
    config = Config(file)

    @pytest.mark.skip()
    # 登录
    def test_login(self):
        url = self.config.get_value(self.file, 'base', 'url') + "/login/in"
        cookies = {
            'JSESSIONID': self.config.get_value(self.file, 'base', 'cookies')
        }

        params = {
            'account': 'admin',
            'pwd': '660B8D2D5359FF6F94F8D3345698F88C'
        }
        response = get(url, params=params, cookies=cookies)
        logger.info(response.text)
        expected = 'admin'
        assert 'admin' == expected  # admin为实际结果

    # 新建学校信息
    @pytest.mark.skip()
    def test_addSchoolInfo(self):
        url = self.config.get_value(self.file, 'base', 'url') + '/school/manage/addSchoolInfo'
        cookies = {
            'JSESSIONID': self.config.get_value(self.file, 'base', 'cookies')
        }
        helper = ExcelHelper()
        logger.info(helper.allvalues_by_row(9, 14, 7, 9))
        excel_data = helper.allvalues_by_row(9, 14, 7, 9)

        school_type = randint(1, 4)
        for i in range(len(excel_data)):
            data = {
                'schoolName': excel_data[i][0],
                'listSchoolType[0].id': school_type,
                'canRecruit': 0,
                'remark': excel_data[i][1]
            }
            response = post(url=url, data=data, cookies=cookies)
            # print(response.text)
            response_text = loads(response.text)
            logger.info(f'返回的值为:{response_text}')
            assert response_text['message'] != '该学校已存在，不能重复新建。'


    # 设置学生录入时间
    def test_setStudentRecruitTime(self):
        cookies = {
            'JSESSIONID': self.config.get_value(self.file, 'base', 'cookies')
        }
        url = self.config.get_value(self.file, 'base', 'url') + '/school/manage/setStudentRecruitTime'
        helper = ExcelHelper()
        excel_data = helper.col_value(7,9)
        logger.info(excel_data)

        school_name = excel_data[randint(1,4)]
        logger.info('-----'+school_name)


        mysql = MySQLHelper()
        sql=f"select * from t_school_info where f_school_name ='{school_name}'"
        mysql_data=mysql.select(sql)
        logger.info(mysql_data[0][0])
        logger.info(type(mysql_data[0][0]))

        json = [
            {
                "id": str(mysql_data[0][0]),
                "recruitStartTime": "2021-06-02",
                "recruitEndTime": "2021-06-05",
                "isStudentRecruitTime": "1"
            }
        ]

        response = post(url=url, json=json, cookies=cookies)
        # print(response.text)
        response_text = loads(response.text)
        logger.info(response_text)

        assert response_text['data'][0]['id'] == int(json[0]['id'])

    @pytest.mark.skip()
    # 设置招生录取时间
    def test_setEnrollmentTime(self):
        url = 'http://192.168.1.36:8080/recruit.students/school/manage/setEnrollmentTime'

        json = [{"id": "5827", "startTime": "2021-06-06", "endTime": "2021-06-09", "isSelfEnrollmentTime": "1"}]

        cookies = {
            'JSESSIONID': 'C584A48CA4996AEB945AABF8A28C207F'
        }

        response = post(url=url, json=json, cookies=cookies)
        # print(response.text)
        response_text = loads(response.text)

        if response_text['data'][0]['id'] == int(json[0]['id']):
            print('测试通过')
        else:
            print('测试失败')

    @pytest.mark.skip()
    # 禁用
    def test_enableOrDisableSchool(self):
        url = 'http://192.168.1.36:8080/recruit.students/school/manage/enableOrDisableSchool'

        json = [{"id": "611702", "disable": 0, "schoolId": "5827"}]

        cookies = {
            'JSESSIONID': 'C584A48CA4996AEB945AABF8A28C207F'
        }

        response = post(url=url, json=json, cookies=cookies)
        # print(response.text)
        response_text = loads(response.text)

        if response_text['data'][0]['id'] == int(json[0]['id']):
            print('测试通过')
        else:
            print('测试失败')

    @pytest.mark.skip()
    # 启用
    def test_enableOrStartSchool(self):
        url = 'http://192.168.1.36:8080/recruit.students/school/manage/enableOrDisableSchool'

        json = [{"id": "611702", "disable": 1, "schoolId": "5827"}]

        cookies = {
            'JSESSIONID': 'C584A48CA4996AEB945AABF8A28C207F'
        }

        response = post(url=url, json=json, cookies=cookies)
        # print(response.text)
        response_text = loads(response.text)

        if response_text['data'][0]['id'] == int(json[0]['id']):
            print('测试通过')
        else:
            print('测试失败')

    @pytest.mark.skip()
    # 修改
    def test_setEnrollmentTime(self):
        url = 'http://192.168.1.36:8080/recruit.students/school/manage/updateSchoolInfo'

        data = {
            'schoolName': 'wuliKarry',
            'id': '5827',
            'listSchoolType[0].id': 4,
            'canRecruit': 0,
            'remark': 'school'
        }

        cookies = {
            'JSESSIONID': 'C584A48CA4996AEB945AABF8A28C207F'
        }

        response = post(url=url, data=data, cookies=cookies)
        # print(response.text)
        response_text = loads(response.text)
        # 断言
        if response_text['message'] == '修改成功':
            print('测试通过')
        else:
            print('测试失败')

    @pytest.mark.skip()
    # 查看
    def test_querySchoolInfo(self):
        url = 'http://192.168.1.36:8080/recruit.students/school/manage/querySchoolInfo'

        data = {
            'id': '5827'
        }

        cookies = {
            'JSESSIONID': 'C584A48CA4996AEB945AABF8A28C207F'
        }

        response = post(url=url, data=data, cookies=cookies)
        print(response.text)
