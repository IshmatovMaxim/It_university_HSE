
# coding: utf-8

# In[2]:


from rutermextract import TermExtractor


# In[65]:


term_extractor = TermExtractor()
file = open('text_input.txt', 'r') # На вход подается сказака о рыбаке и рыбке
text = file.read()

word = [] # Пустой список для ключевых слов
value = [] # Пустой список для количества повторений


'''
В цикле term_extractor извлекает ключевые фразы из TXT-файла,
аргумент nested=True дополнительно извлекает ключевые слова из словосочетаний
'''


for term in term_extractor(text, nested=True):
    word.append(term.normalized) # Добавляет в список слова в нормализованной форме
    value.append(term.count) # Добавляет в список количество вхождений
    #print(term.normalized, term.count) 


# In[27]:


import pandas as pd


# In[61]:


df = pd.DataFrame({
    'Word': word,
    'Value': value
})


# In[63]:


df

# In[64]:

df.to_excel('text_output.xls') #Экспорт

