data1 = dataall.loc[dataall.rating>=9.5]

result = data1.groupby('type').count()['name'].reset_index().sort_values('name',ascending = False).reset_index(drop = True)

attr = result.type
v1 = result.name
pie = Pie('9.5分以上游戏',title_pos = 'center',title_text_size = 20)
pie.add(
"",
attr,
v1,
radius=[40, 75],center = [50,60],
label_text_color=None,is_legend_show = False,
is_label_show=True
)
pie.render('高评分游戏-分类型.html')

data1['title'] = data1.name.apply(lambda x:str(x).split(':')[0].split(' ')[0])

# 9.5以上评分，评分人数超过1000
result = data1.loc[data1.n_ratings >= 100,['name','genres','content','platforms','rating','n_ratings']].drop_duplicates().reset_index(drop = True) 

result = result.sort_values(by = ['n_ratings','genres'],ascending = False).reset_index(drop = True)
result.to_excel('评分9.5以上游戏.xlsx')