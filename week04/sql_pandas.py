import pandas as pd
import random
import numpy as np
data=pd.DataFrame({'id':range(0,2000,100),'age':random.sample(range(10,60,2),20)})
#select * from data;
data
#select * from data limit 10;
data[:10]
#select id from data;
data.id
#select count(id) from data;
data.id.count()
#select * from data where id<1000 and age>30;
data[(data.id<1000) & (data.age>30)]

table1=pd.DataFrame({'id':np.random.randint(0,30,20),'order_id':np.random.randint(45305,54690,20),'income':np.random.randint(200,2000,20)})
table2=pd.DataFrame({'id':range(10,30),'product_id':np.random.randint(5305,5469,20),'user_id':np.random.randint(2001,2100,20)})
#select id,count(distinct order_id) from table1 group by id;
table1.groupby('id')['order_id'].nunique()
#select * from table1 t1 inner join table2 t2 on t1.id=t2.id;
pd.merge(table1,table2,on='id',how='inner')
#select * from table1 union select * from table2;
pd.concat([table1,table2]).drop_duplicates()
#delete from table1 where id=10;
table1=table1[table1.id!=10]
#alter table table1 drop column column_name;
table1=table1.drop('order_id',axis=1)



