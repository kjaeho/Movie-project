import pymysql
import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:ssafy@127.0.0.1:3306/ssafyweb", encoding='utf-8-sig')

# 1
# table0 = pd.read_excel('last_data/last_movie.xlsx', encoding='utf-8-sig')
# table1 = pd.read_excel('last_data/last_genre_data.xlsx', encoding='utf-8-sig')
# table2 = pd.read_excel('last_data/last_actor_data.xlsx', encoding='utf-8-sig')
# table3 = pd.read_excel('last_data/last_keyword_data.xlsx', encoding='utf-8-sig')

# table0.to_sql(name='movies_movie', con=engine, if_exists='append', index=False)
# table1.to_sql(name='movies_genre',con=engine, if_exists='append', index=False)
# table2.to_sql(name='movies_actor',con=engine, if_exists='append', index=False)
# table3.to_sql(name='movies_keyword',con=engine, if_exists='append', index=False)


# # 2
# table4 = pd.read_excel('last_data/last_genre.xlsx', encoding='CP949')
# table4.to_sql(name='movies_movie_genres',con=engine, if_exists='append', index=False)

# # 3
# table5 = pd.read_excel('last_data/last_actor.xlsx', encoding='CP949')
# table5.to_sql(name='movies_movie_actors',con=engine, if_exists='append', index=False)

# # 4
# table7 = pd.read_excel('last_data/last_keyword.xlsx', encoding='CP949')
# table7.to_sql(name='movies_movie_keywords',con=engine, if_exists='append', index=False)


# 이건 하지마!!!
# table6 = pd.read_excel('last_data/last_reviews.csv', encoding='CP949')
# table6.to_sql(name='reviews_review',con=engine, if_exists='append', index=False)
