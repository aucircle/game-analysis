# 各平台游戏数

num = len(dataall.name.unique())
result = dataall.groupby('platform').count()['name'].reset_index()


name = result.platform.tolist()
value = result.name.tolist()
wordcloud = WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[20, 120])
wordcloud.render('游戏平台.html')


platforms = result.loc[result.name >100,'platform'].tolist()


dataall.platform = dataall.platform.apply(lambda x:x if x in platforms else '其他')
result = dataall.groupby('platform').count()['name'].reset_index().sort_values('name',ascending = False).reset_index(drop = True)


attr = result.platform
v1 = result.name
pie = Pie('各平台游戏数',title_pos = 'center',title_text_size = 20)
pie.add(
"",
attr,
v1,
radius=[40, 75],center = [50,60],
label_text_color=None,is_legend_show = False,
is_label_show=True
)
pie.render('各平台游戏数.html')






# 各平台游戏评分人数

result1 = dataall.n_ratings.fillna(0).groupby(dataall.platform).mean().reset_index()
result2 = dataall.n_ratings.dropna().groupby(dataall.dropna().platform).mean().reset_index()

attr = result1.platform.tolist()
v1 = np.round(result1.n_ratings.tolist(),1)
v2 = np.round(result2.n_ratings.tolist(),1)
line = Line()
#line.add(x_axis = attr,y_axis = xaxis_type = 'category')
line.add("包含无评分", attr, v1, mark_point=["max"],is_label_show = True)
line.add("不包含无评分", attr, v2, is_smooth=True, mark_point=["max"],is_label_show = True,xaxis_rotate = 70)
line.render('各平台游戏-评分人数.html')


# 各平台游戏均分

result1 = dataall.rating.fillna(0).groupby(dataall.platform).mean().reset_index()
result2 = dataall.rating.dropna().groupby(dataall.dropna().platform).mean().reset_index()

attr = result1.platform.tolist()
v1 = np.round(result1.rating.tolist(),1)
v2 = np.round(result2.rating.tolist(),1)
line = Line()
#line.add(x_axis = attr,y_axis = xaxis_type = 'category')
line.add("包含无评分", attr, v1, mark_point=["max"],is_label_show = True)
line.add("不包含无评分", attr, v2, is_smooth=True, mark_point=["max"],is_label_show = True,xaxis_rotate = 70)
line.render('各平台游戏-均分.html')