from urllib import request, parse
import json
from datetime import datetime
import atexit
import sys
import traceback


class Notification:

    def __init__(self, normalMsg, errorMsg, code):
        self.normal = normalMsg
        self.error = errorMsg
        self.miaoCode = code
        self.hasSend = False
        atexit.register(self.__on_exit)
        sys.excepthook = self.__handle_exception

    def __notification(self, message):
        if not self.hasSend:
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

            miao_code = self.miaoCode
            message = message + '\n' + formatted_datetime

            page = request.urlopen(
                "http://miaotixing.com/trigger?" + parse.urlencode({"id": miao_code, "text": message, "type": "json"}))
            result = page.read()
            jsonObj = json.loads(result)
            if jsonObj["code"] == 0:
                print("EthaneHikeNotification-通知发送成功")
            else:
                print(
                    "EthaneHikeNotification-通知发送失败，错误代码：" + str(jsonObj["code"]) + "，描述：" + jsonObj["msg"])
            self.hasSend = True
        else:
            pass

    def __on_exit(self):
        self.__notification(self.normal)

    def __handle_exception(self, exc_type, exc_value, exc_traceback):
        if issubclass(exc_type, KeyboardInterrupt):
            print('EthaneHikeNotification-程序被用户中断')
            return
        print('EthaneHikeNotification-程序遇到异常')
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        self.__on_exception_exit()

    def __on_exception_exit(self):
        self.__notification(self.error)
