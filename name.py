# 分词
import re
stopwords = open('中文停用词表（比较全面，有1208个停用词）.txt','r').read()
stopwords = stopwords.split('\n')


texts = ''.join(dataall.name.tolist())
texts =''.join(re.findall(r'[\u4e00-\u9fa5]',texts))
result = jieba.cut(texts,cut_all=False)


allwords = [word for word in result if len(word)>1 and word not in stopwords]



result = pd.DataFrame(allwords)
result.columns =['word']
res = result.word.groupby(result.word).count()
res.index.name = 'text'
res = res.reset_index()
res = res.loc[res.word >= 10].reset_index(drop = True)

# 标题词云
name = res.text.tolist()
value = res.word.tolist()
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[10, 80])
wordcloud.render('游戏名称高频词.html')