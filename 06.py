import requests
from pprint import pprint


def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}'
    response = requests.get(url).json()
    re = response["results"]
    
    try:
        a = re[0]["id"]
        url1 = f'https://api.themoviedb.org/3/movie/{a}/credits?api_key={API_KEY}&language=ko-KR'
        response1 = requests.get(url1).json()
        casts = response1['cast']
        crews = response1['crew']
        movie_credits = {
            'cast' : [],
            'crew' : []
        }
        for cast in casts:
            if cast['cast_id'] < 10:
                movie_credits['cast'].append(cast['name'])
        for crew in crews:
            if crew['department'] == 'Directing':
                movie_credits['crew'].append(crew['name'])

        return movie_credits
    
    except:
        return None




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
