# with open('여기다가 샘플 파일 주소 넣어 주시면 됩니다 호호', 'r') as f:
#     docs = f.readlines()    #라인단위로 docs에 집어넣는다
# for id, doc in enumerate(docs):
#     print('[{}] : {}...'.format(id, doc[:30]))  #30개씩만 출력
# print('00================================================================')
# from sklearn.feature_extraction.text import TfidfVectorizer
#
# #tfidf 벡터 메트릭스 생성
# tfidf = TfidfVectorizer()
# tfidf_matrix = tfidf.fit_transform(docs)
# print('type of tfidf_matrix {}'.format(type(tfidf_matrix)))
# print('shape of tfidf_matrix {}'.format(tfidf_matrix.shape))
# # 18개 문서의 279개의 단어집합
#
# print('11================================================================')
# vocab = sorted(tfidf.vocabulary_.items())
# print(vocab)
# print('================================================================')
# vocab[10:20]
#
# import pandas as pd
#                   #tfidf_matrix= crx매트릭스 toarray=ad array로 바꿈
# df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names())
# print('다섯개================================================================')
# print(df.head(5)) #다섯개만 뽑는다
#
# tfidf_table = tfidf_matrix.toarray()
#
# keywords = []
# for weight in tfidf_table:
#     w_vec = list(enumerate(weight))
#     w_vec = sorted(w_vec, key=lambda x : x[1], reverse=True)
#     print(w_vec[:3])
#     keywords.append(w_vec)
#
#     #1. (word_id, tfidf) 튜플의 리스트를 만든다.
#     #2. 리스트를 tfidf 값이 큰 순으로 정렬한다.
#     #3. 만들어진 리스트의 앞 3개 아이템을 출력한다.
#     #4. kewords 리스트에 추가한다.
#
#
# ##과제 부분입니다##
#
# num=int(input('찾을 단어 id값을 입력하시오:'))
# print('찾으신 id 값의 넘은 입니다:',vocab[num])
#
#
#
