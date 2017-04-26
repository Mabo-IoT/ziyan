# -*- coding: utf-8 -*-
from ziyan.ziyan_main import Command, Check, Handler


class MyCommand(Command):
    def __init__(self, configuration):
        super(MyCommand, self).__init__(configuration=configuration)

    def user_create_command(self):
        cmd = 1
        return cmd


class MyCheck(Check):
    def __init__(self, configuration):
        super(MyCheck, self).__init__(configuration=configuration)

    def user_check(self, command):
        if command == 1:
            return Check.data


class MyHandler(Handler):
    def __init__(self, configuration):
        super(MyHandler, self).__init__(configuration=configuration)

    def user_handle(self, raw_data):
        """
        用户须输出一个dict，可以填写一下键值，也可以不填写
        timestamp， 从数据中处理得到的时间戳（整形?）
        tags, 根据数据得到的tag
        data_value 数据拼成的list
        measurement 根据数据类型得到的 influxdb表明
        :param raw_data: 
        :return: 
        """
        # 数据经过处理之后生成 value_list
        data_value_list = [raw_data]

        tags = {'user_defined_tag': 'data_ralated_tag'}

        # user 可以在handle里自己按数据格式制定tags
        user_postprocessed = {'data_value': data_value_list,
                              'tags': tags, }
        return user_postprocessed