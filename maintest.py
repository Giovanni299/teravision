try:
    from main import app
    import unittest
    from http import HTTPStatus
except Exception as e:
    print(f'Some modules are missing, {e}')

nested = '/nested'

class MainTest(unittest.TestCase):
    def test_server_is_up_and_running(self):
        tester = app.test_client(self)
        response = tester.get('/').status_code
        self.assertEqual(response, HTTPStatus.OK)

    def test_function_nested_running(self):
        tester = app.test_client(self)
        response = tester.get(nested, json={'items':[1, 2, [3, 4, [5, 6], 7], 8]}).status_code
        self.assertEqual(response, HTTPStatus.OK)

        response = tester.get( nested, json={"items": []}).status_code
        self.assertEqual(response, HTTPStatus.NOT_FOUND)

    def test_check_content_type(self):
        tester = app.test_client(self)
        response = tester.get(nested, json={'items':'qwe'})
        self.assertEqual(response.content_type, 'application/json')

    def test_check_content_data(self):
        tester = app.test_client(self)
        response = tester.get(nested, json={'items':'qwe'})
        self.assertTrue(b'Error' in response.data)

        response = tester.get(nested, json={'items':123})
        self.assertTrue(b'Error' in response.data)

        response = tester.get( nested, json={"items": [1, 2, [3, 4, [5, 6], 7], 8]})
        self.assertTrue(b'result' in response.data)        
        self.assertTrue(b'[1,2,3,4,5,6,7,8]' in response.data)

    def test_check_succesful_result(self):        
        tester = app.test_client(self)
        response = tester.get( nested, json={"items": [1, 2, [3, 4]]})
        self.assertTrue(b'[1,2,3,4]' in response.data)
        
        response = tester.get( nested, json={"items": [1]})
        self.assertTrue(b'[1]' in response.data)

if __name__ == '__main__':
    unittest.main()