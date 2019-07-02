dataall['n_platforms'] = dataall.platforms.apply(lambda x:len(str(x).split('/')))
dataall['platform'] = dataall.platforms.apply(lambda x:str(x).split('/')[0].strip())

sns.pairplot(dataall,diag_kind = 'kde') 
plt.show()

data2 = dataall.dropna()
sns.pairplot(data2,diag_kind = 'kde') 
plt.show()