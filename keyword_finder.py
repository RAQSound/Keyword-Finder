import urllib.request as urlreq
import pandas as pd
import search_functions
from datetime import datetime


user_topic = "tipos de empanizados" #This string is the user topic where the keywords should be related.

number_iterations = 3
user_topic_list =[user_topic] 
count_words = 0
for i in range(0,number_iterations):
    
    for i2 in range(count_words,len(user_topic_list)):
        print(count_words)
        print(user_topic_list[count_words])
        recomendations = search_functions.googleKeywordSearch(user_topic_list[count_words])
        user_topic_list=user_topic_list+recomendations
        #print(recomendations)
        #print(len(user_topic_list))
        count_words=count_words+1
  
user_topic_list=list(set(user_topic_list))  


print('el resultado es:')
print(user_topic_list)

#search_functions.h1Checker(user_topic)
#Mejorar con multi threating

number_recommendations = len(user_topic_list)
print(number_recommendations)



info_keyword = pd.DataFrame(columns=['Topic', 'Keyword', 'h1 similitude percentage', 'Video Index'])


for i in range(0,number_recommendations):
# for i in range(0,2):
    print(i)
    similitude_percentage = search_functions.h1Checker(user_topic_list[i])
    print('La palabra clave es: "'+user_topic_list[i]+'" y tiene una similitud de '+str(similitude_percentage)+' porciento con el h1')
    info_keyword_add = pd.DataFrame([[user_topic,user_topic_list[i],similitude_percentage[0],similitude_percentage[1]]],columns = info_keyword.columns)
    info_keyword = pd.concat([info_keyword, info_keyword_add])
    
date = datetime.now()
date.strftime("%Y%B%d")

print(info_keyword)

info_keyword.to_csv(str(date.strftime("%Y%B%d"))+user_topic.replace(' ','_')+'00'+str(number_iterations)+'.csv',)
    
    



