import urllib.request as urlreq
import urllib.parse
import numpy as np

import time
import pandas as pd

def prueba(user_topic):
    print('sirvió la prueba'+user_topic)
    
    
def similar_percetage(keyword,h1):
    comparison_list = keyword.split()
    number_words = len(comparison_list)
    #print(keyword)
    #print('El número de palabras en la palabra clave es: '+str(number_words))
    similar_percentaje = 0
    for i in range(0,number_words):
        #print(i)
        check_word = h1.count(comparison_list[i])        
        #print('la verificación es: '+str(check_word))
        if check_word>0:
            similar_percentaje = similar_percentaje+(1/number_words)
            #print(comparison_list[i])
            #print(similar_percentaje)
            
    return(similar_percentaje)
    
    
    
    
    
def tagsEliminator(text):
    number_tags = text.count('<')
    #print(number_tags)
    text=text.replace('->','')
    for i in range(0,number_tags):
        initial_position_tag = 0
        initial_position_tag = 0
        final_position_tag = 0
        
        initial_position_tag = text.index('<')
        final_position_tag = text.index('>')+1
        text2delete = text[initial_position_tag:final_position_tag] 
        #print(i)
        text = text.replace(text2delete,'')
    return(text)
def videoCheck(url):
    variable_check = 0
    count_video = url.count('youtube')
    count_video = count_video+url.count('tiktok')
    count_video = count_video+url.count('dailymotion')
    if count_video>0:
        variable_check = 1
    
        
    return(variable_check) 
    
    

def googleKeywordSearch(user_topic):
    user_topic = user_topic.replace(' ','+')
    yourUrl = "https://www.google.com/search?q="+urllib.parse.quote(user_topic)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    req = urlreq.Request(yourUrl, headers = headers)
    response = urlreq.urlopen(req)
    #body = urllib.parse.unquote(response.read()) 
    body = str(response.read(),encoding='utf-8') 
    #print(body.type)
    #body = body.decode('windows-1252')
    initial_word = '<span class="CVA68e qXLe6d">  <span class="qXLe6d FrIlee">  <span class="fYyStc">'
    length_initial_word = len(initial_word)
    final_word = '</span>'
    count_recomendations = body.count(initial_word)
    initial_pos = 0
    keyword_recommendations = ['']*count_recomendations
    for i in range(0,count_recomendations):
        #print(i)
        initial_pos = body.index(initial_word,int(initial_pos+1),len(body))
        final_pos = body.index(final_word,int(initial_pos+1),len(body))
        keyword_extracted = body[int(initial_pos+length_initial_word):int(final_pos)]
        # print(keyword_extracted)        
        keyword_encoded = keyword_extracted.encode('utf-8')
        # print(keyword_encoded)
        keyword_recommendations[i] = str(keyword_encoded,encoding='utf-8')
        # print(keyword_recommendations[i])
    #print(keyword_recommendations)
    #print(count_recomendations)
    return(keyword_recommendations)
    
    
    
    
    
def h1Checker(user_topic_original):
    
    user_topic = user_topic_original.replace(' ','+')
    yourUrl = "https://www.google.com/search?q="+urllib.parse.quote(user_topic)
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
    try:
        req = urlreq.Request(yourUrl, headers = headers)
        response = urlreq.urlopen(req)
    except:
        time.sleep(2)
    else:
        body = str(response.read())
        initial_word = 'sa=U&amp;url='
        final_word = '&amp;'
        length_initial_word = len(initial_word)
        count_recomendations = body.count(initial_word)
        # print(count_recomendations)
        url_verifications = ['']*count_recomendations
        initial_pos = 0
        h1 = '<h1'
        h1close = '>'
        h1end = '</h1>'
        sum_similitude = 0
        sum_count = 0
        video_count = 0
    
        for i in range(0,count_recomendations):
            #print(i)
            initial_pos = body.index(initial_word,int(initial_pos+length_initial_word),len(body))
            final_pos = body.index(final_word,int(initial_pos+length_initial_word),len(body))
            #print(initial_pos)
            #print(final_pos)
            url_verifications[i] = body[int(initial_pos+length_initial_word):int(final_pos)]
            video_count = video_count + videoCheck(url_verifications[i])
            print('la iteracion '+str(i)+' da como resultado un video_count igual a '+str(video_count))
    
        #print(url_verifications)
        for i in range(0,count_recomendations):
            # print(i)
            #headers = {'User-Agent':'abc-bot'+str(i)}
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
        
            ###############Entrar y ver la página de competencia SEO
            initial_pos_h1 = 0
            final_pos_h1 = 0
            try:
                req2 = urlreq.Request(url_verifications[i], headers = headers)
                response2 = urlreq.urlopen(req2, timeout=25)
                body2 = str(response2.read())
            except:
                i=i-1
                time.sleep(2)
            else:    
                #print(body2)
                count_h1 = body2.count(h1)
                count_h1end = body2.count(h1end)
                #print('este es el numero de h1: '+str(count_h1))
                #print('esta es la URL: '+url_verifications[i])
                #print(body2)
                if (count_h1>0) and (count_h1==count_h1end):
                    initial_pos_h1 = body2.index(h1,int(initial_pos_h1),len(body2))
                    final_pos_h1 = body2.index(h1end,int(initial_pos_h1+1),len(body2))
                    reference_h1 = body2[int(initial_pos_h1-1):int(final_pos_h1+5)]
                    #print('el h1 sucio es: "'+reference_h1+'"')
                    try:
                        h1_text = tagsEliminator(reference_h1)
                    except: 
                        print('un error con: '+reference_h1)
                    else:
                        h1_text = h1_text.replace('\\n',' ')
                        h1_text = h1_text.replace('  ','')
                        #h1_text = str("b'"+h1_text+"'",encoding='utf-8')
                        #print('el h1 es: "'+h1_text+'"')
                        similitude_percentage = similar_percetage(user_topic_original.lower(),h1_text.lower())
                        sum_similitude = sum_similitude+similitude_percentage
                        #print('el porcentaje de similitud es: '+str(similitude_percentage))
                        #print('La suma es: '+str(sum_similitude))
                        sum_count = sum_count+1
                        
                
            
        if sum_count > 0:
            similar_average = sum_similitude/sum_count
        else:    
            similar_average = np.nan
        if count_recomendations>0:
            video_percentage = video_count/count_recomendations    
        else:
            video_percentage = np.nan
        
        return([similar_average*100, video_percentage])
    