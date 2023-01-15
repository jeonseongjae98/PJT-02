import requests
sum = []

def popular_count():
    # 여기에 코드를 작성합니다.

    url = "https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-kr"
    response = requests.get(url).json()
    re = response["results"]
    return len(re)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
