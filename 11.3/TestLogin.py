import requests
from bs4 import BeautifulSoup
import  unittest
class TestLogin(unittest.TestCase):
    def testLoginSuccess(self):
        session = requests.session()
        result = session.get("http://127.0.0.1:5000/login")

        soup = BeautifulSoup(result.text, "html.parser")
        inputs = soup.find_all("input", id="csrf_token")
        csrf_token =  inputs[0].attrs["value"]
        data={"csrf_token":csrf_token,"email":"a_kui@163.com","password":"111111"}
        result = session.post("http://127.0.0.1:5000/login",data=data)

        self.assertEqual(200,result.status_code)
        self.assertIn("Logged in successfully",result.text)
        print(BeautifulSoup(result.text, "html.parser").prettify())

if(__name__ == "__main__"):
    unittest.main()

