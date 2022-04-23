from sklearn.metrics.pairwise import cosine_similarity  # 코사인 유사도 모듈
from sklearn.metrics.pairwise import linear_kernel  # 코사인 빠르게해주는거

with open('/Users/dclab/PycharmProjects/pythonProject4/venv/sample.txt', 'r') as f:
    docs = f.readlines()    #라인단위로 docs에 집어넣는다
for id, doc in enumerate(docs):
    print('[{}] : {}...'.format(id, doc[:30]))  #30개씩만 출력
print('00================================================================')
from sklearn.feature_extraction.text import TfidfVectorizer

#tfidf 벡터 메트릭스 생성
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(docs)
print('type of tfidf_matrix {}'.format(type(tfidf_matrix)))
print('shape of tfidf_matrix {}'.format(tfidf_matrix.shape))

def cosine_sim_rank(tfidf_matrix):
    # 1. 코사인 유사도 계산
    cos_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    # cos_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    print('shape of cos_sim table {}'.format(cos_sim.shape))

    # 2. 유사도가 높은 문서 쌍 순으로 정렬
    sim_scores = []
    for idx, sim in enumerate(cos_sim):
        sim = list(enumerate(sim))
        sim = sorted(sim, key=lambda x: x[1], reverse=True)
        sim_scores.append(((idx, sim[1][0]), sim[1][1]))

    sim_scores.sort(key=lambda x: x[1], reverse=True)
    return sim_scores


sim_scores = cosine_sim_rank(tfidf_matrix)
print(sim_scores)

test = ['first korean artist']
test_matrix = tfidf.transform(test) #퍼스트 꼬리아 아티스트를 벡터화함
print(test_matrix)

sim=cosine_similarity(test_matrix,tfidf_matrix)
print(sim.shape)
sim=sim[0]
sim=[(id, cos) for id, cos in enumerate(sim)]
sim= sorted(sim, key=lambda x: x[1], reverse=True)
print(sim)