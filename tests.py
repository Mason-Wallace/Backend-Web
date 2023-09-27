from app import app
import datetime

if __name__ == '__main__':
    with app.test_client() as client:
        date = datetime.datetime.today()
        second = str(date.second).encode('utf-8')
        hour = str(date.hour).encode('utf-8')
        year = str(date.year).encode('utf-8')

        response = client.get('/second')
        assert second in response.data
        
        response = client.get('/hour')
        assert hour in response.data

        response = client.get('/year')
        assert year in response.data