# 各类型游戏数

num = len(dataall.name.unique())
result = dataall.groupby('type').count()['name'].reset_index().sort_values('name',ascending = False)


attr = list(result.type)
v = list(np.round(result.name/num,3)) 

pie = Pie()
style = Style()
pie_style = style.add(
label_pos="center",
is_label_show=True,
label_text_color=None,
is_legend_show = False
)
pie.add("",[attr[0],"其他"],[v[0],1-v[0]],radius=[18, 24],center = [10,20],**pie_style)
pie.add("",[attr[1],"其他"],[v[1],1-v[1]],radius=[18, 24],center = [30,20],**pie_style)
pie.add("",[attr[2],"其他"],[v[2],1-v[2]],radius=[18, 24],center = [50,20],**pie_style)
pie.add("",[attr[3],"其他"],[v[3],1-v[3]],radius=[18, 24],center = [70,20],**pie_style)
pie.add("",[attr[4],"其他"],[v[4],1-v[4]],radius=[18, 24],center = [90,20],**pie_style)

pie.add("",[attr[5],"其他"],[v[5],1-v[5]],radius=[18, 24],center = [10,50],**pie_style)
pie.add("",[attr[6],"其他"],[v[6],1-v[6]],radius=[18, 24],center = [30,50],**pie_style)
pie.add("",[attr[7],"其他"],[v[7],1-v[7]],radius=[18, 24],center = [50,50],**pie_style)
pie.add("",[attr[8],"其他"],[v[8],1-v[8]],radius=[18, 24],center = [70,50],**pie_style)
pie.add("",[attr[9],"其他"],[v[9],1-v[9]],radius=[18, 24],center = [90,50],**pie_style)

pie.add("",[attr[10],"其他"],[v[10],1-v[10]],radius=[18, 24],center = [10,80],**pie_style)
pie.add("",[attr[11],"其他"],[v[11],1-v[11]],radius=[18, 24],center = [30,80],**pie_style)
pie.add("",[attr[12],"其他"],[v[12],1-v[12]],radius=[18, 24],center = [50,80],**pie_style)
pie.add("",[attr[13],"其他"],[v[13],1-v[13]],radius=[18, 24],center = [70,80],**pie_style)
pie.add("",[attr[14],"其他"],[v[14],1-v[4]],radius=[18, 24],center = [90,80],**pie_style)


pie.render('各类型游戏数.html')


# 各类型游戏均分
c_schema= [( "乱斗/清版",10),
( "体育",10),
( "冒险",10),
( "动作",10),
( "即时战略",10),
( "射击",10),
( "格斗",10),
( "模拟",10),
( "横版过关",10),
( "益智",10),
( "竞速",10),
( "第一人称射击",10),
( "策略",10),
( "角色扮演",10),
( "音乐/旋律",10)]
result1 = dataall.rating.fillna(0).groupby(dataall.type).mean().reset_index()
result2 = dataall.rating.dropna().groupby(dataall.dropna().type).mean().reset_index()

v1 = [result1.rating.apply(lambda x:round(x,1)).tolist()]
v2 = [result2.rating.apply(lambda x:round(x,1)).tolist()]

radar = Radar()
radar.config(c_schema)
radar.add("游戏均分（无评分视为0）", v1, is_splitline=True, is_axisline_show=True,is_label_show = True)
radar.add("游戏均分（删除无评分）", v2, label_color=["#4e79a7"],item_color="#f9713c",is_label_show = True)
radar.render('各类型游戏评分.html')


# 各类型游戏评分人数

result1 = dataall.n_ratings.fillna(0).groupby(dataall.type).mean().reset_index()
result2 = dataall.n_ratings.dropna().groupby(dataall.dropna().type).mean().reset_index()

attr = result1.type.tolist()
v1 = np.round(result1.n_ratings.tolist(),1)
v2 = np.round(result2.n_ratings.tolist(),1)
line = Line()
#line.add(x_axis = attr,y_axis = xaxis_type = 'category')
line.add("包含无评分", attr, v1, mark_point=["max"],is_label_show = True)
line.add("不包含无评分", attr, v2, is_smooth=True, mark_point=["max"],is_label_show = True,xaxis_rotate = 30)
line.render('各类型游戏-评分人数.html')