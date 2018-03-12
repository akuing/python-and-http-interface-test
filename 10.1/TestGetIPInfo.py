import unittest
import requests
import time


class TestGetIPInfo(unittest.TestCase):

    def testReturnGoodWhenGetIpInfoGivenNormalIPInBeijing(self):
        result = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip="+"106.120.105.62")
        self.assertEqual(0,result.json()["code"])
        self.assertEqual("中国",result.json()["data"]["country"])
        self.assertEqual("北京市",result.json()["data"]["city"])
    def testReturnErrorMsgWhenGetIpInfoGivenInvalidIP(self):
        time.sleep(5)
        result = requests.get("http://ip.taobao.com/service/getIpInfo.php?ip=" + "badip")
        self.assertEqual(1, result.json()["code"])
        self.assertEqual("invaild ip.", result.json()["data"])

if(__name__ == "__main__"):
    unittest.main(verbosity=2)