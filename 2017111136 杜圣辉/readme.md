## Read Me

- 本次爬取的数据文件比较多，但命名都是统一规范的，不会出现一个文件用不同的名字存储的情况
- 在这里，我会说明每一个文件的作用以及中文释义
- 所有文件的释义都会按照<u>获取顺序</u>进行解释：

|      | 文件名               | 作用                                                         | 何时何地得到                                                 |
| ---- | -------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 0    | anjuke_house_raw.csv | 安居客爬取到的原始数据                                       | 最开始爬取数据时<br>（1.1 Anjuke_cps.ipynb）                 |
| 1    | comm_table.csv       | 提取自anjuke_house_raw，记录房屋信息                         | 爬取完毕之后，经过字段选择和处理得到<br/>（1.1 Anjuke_cps.ipynb） |
| 2    | house_table.csv      | 提取自anjuke_house_raw，记录小区信息                         | 同上<br/>（1.1 Anjuke_cps.ipynb）                            |
| 3    | yangpu_house.csv     | 最初数据进入模型前留档的数据，此时已经经过简单的特征工程处理，包含小区、房子的信息 | 进入模型前<br>（2.1Attemptation.ipynb）                      |
| 4    | yangpu_business.csv  | 杨浦区商圈的名字、信息、经纬度                               | 查询地理坐标时<br/>（2.2GeoFeatures.ipynb）                  |
| 5    | yangpu_garden.csv    | 杨浦区公园的名字、信息、经纬度                               | 查询地理坐标时<br/>（2.2GeoFeatures.ipynb）                  |
| 6    | yangpu_hospital.csv  | 杨浦区医院的名字、信息、经纬度                               | 查询地理坐标时<br/>（2.2GeoFeatures.ipynb）                  |
| 7    | yangpu_school.csv    | 杨浦区学校的名字、信息、经纬度                               | 查询地理坐标时<br/>（2.2GeoFeatures.ipynb）                  |
| 8    | yangpu_subway.csv    | 杨浦区地铁站的名字、信息、经纬度                             | 查询地理坐标时<br/>（2.2GeoFeatures.ipynb）                  |
| 9    | comm_geoloc.csv      | 根据小区名，进入百度坐标拾取系统，扩充了小区地理坐标，以及小区周边最佳舒适距离半径以内各个生活设施的数目，如商圈、学校、地铁站、基础设施（医院、公园） | 查询地理坐标时<br>（2.2GeoFeatures.ipynb）                   |

- 接下来，对于每一个表单，我会对必要的表单-字段展示其意义和示例

  

### anjuke_house_raw.csv

| Feature           | Description        | Example                                                      |
| ----------------- | ------------------ | ------------------------------------------------------------ |
| title             | 售房主题           | 业主是我老客户，跟我定好一手房，急需首付，急售，随时看房     |
| house_price       | 房屋总价格（万元） | 350                                                          |
| house_info        | 房屋描述           | 所属小区：<br/>翔顺公寓<br/>房屋户型：<br/>2室 2厅 1卫<br/>房屋单价：<br/>48611 元/m²<br/>所在位置：<br/>杨浦区－ 黄兴－ 国顺东路26弄<br/><br/>建筑面积：<br/>72平方米<br/>参考首付：<br/>105.1万<br/>建造年代：<br/>1998年<br/>房屋朝向：<br/>南<br/>参考月供：<br/>13743元<br/>房屋类型：<br/>普通住宅<br/>所在楼层：<br/>中层(共6层)<br/>装修程度：<br/>简单装修<br/>产权年限：<br/>70年产权<br/>配套电梯：<br/>无<br/>房本年限：<br/>满二年<br/>产权性质：<br/>商品房<br/>唯一住房：<br/>暂无<br/>一手房源：<br/>否 |
| comm_area         | 小区面积           | 暂无                                                         |
| comm_households   | 小区户数           | 暂无                                                         |
| comm_plot_ratio   | 小区容积率         | 1.8                                                          |
| comm_parking_num  | 小区停车位数       | 暂无                                                         |
| comm_green_ratio  | 小区绿化率         | 25%                                                          |
| comm_property_fee | 小区物业费         | 0.60元/m²                                                    |
| item_district     | 所属区             | yangpu                                                       |
| adv               | 房屋优点           | 特色<br/>【小区户型】小区主要是以多层为主近83栋，一房朝南，50-60平。两房以双南厅朝北为主75平左右。<br/>【生活配套】小区出门口国顺东路路有菜场，农业银行等 以附近1公里五角场商圈长海医院，万达以及太苹洋生活广场。<br/>【轨道交通】地铁8号线翔殷路站1公里，公交1238、80、137、577、868等等，到中环高架0.3公里。<br/>【附近学校】【附近学校】翔殷路小学，为我区重点中学输送优秀生源。鞍山实验中学和复旦实验中学是市重点中学且轮换对口 |
| disadv            | 房屋缺点           | 不足<br/>距离地铁稍微远一点 车位有点紧张 绿化稍微少点        |
| core_point        | 房屋核心卖点       | 房源标签<br/>售房详情<br/>业主是置换的，诚意出售。看房提前约，**无要求。希望能尽量快**。<br/>税费解析<br/>满五税费少，产权的商品房。首套1个点契税，二套是3个点契税。<br/><br/>南北带大阳台，厅朝北，厨卫朝北。全明户型，采光好。一梯2户的。<br/>核心卖点<br/>满五，税费少。一梯2户，户型好。小区品质好，好停车。 |
| url               | 链接               | https://shanghai.anjuke.com/prop/view/A5071614777?from=filter&spread=commsearch&invalid=1&click_url=https://lego-click.anjuke.com/jump?target=pZwY0ZnlsztdraOWUvYKuadWm1NLujE1raYdrHE1sHwBujEVrjbOniYQnH03Py76PWnOuWmKPHnkPWTLn9DKnHNkPWNLPjnkP1bOnjNYnED3njTkTH9knjTKnikQnkDzsjDYnj0KnHNOnH9kPHcdnWEQrEDQTNujsRKjsN72iSilWrpFBSpcfSXVhShTBXyc-SB6Jrh6VEDQTHDKTiYQTEDQnWm3P191nW0QPj93njDvn19YTHmKTHDKryn3nAcdP19VP16hPzYYnhNQsH--PH9VnADdPhDdP1TkPWT1THDzPW9LrjnzP1DvnjbvPHDznjTKnHcvrj03n1cLnHEdrjmYn1bvrTDKTEDKTiYKTE7CIZwk01CfsLPCmyOMpA7Gsh78pMRouiOWUvYf0v7_uiqOmyOM0ZNf0jDfTNPKnbDYEH9QsNnkPWcVrNnvridDEYPDsHPaPH9OwjbvrNn1EEDznH98P1b8rjm8nHmkTHTKnTDKnikQnk7exEDQnjT1PEDQnjTQPWE3Tyu-nyEQnhDLsymvuyEVPjTdniYOrjEOsHNdnAmvP1uWPWmkrEDKPTDKTHnKnBkQPjTLsj0YPH9KnE78IyQ_TH0OP1RBm19kmWc3nvnLP19&uniqid=pc5ee10544dc6590.39798745&region_ids=9&position=1&kwtype=filter&now_time=1591805252 |



### comm_geoloc.csv

| Feature     | Description         | Example            |
| ----------- | ------------------- | ------------------ |
| loc         | 小区地址            | 文化佳园(公寓住宅) |
| lat         | 所在维度            | 31.29497           |
| lon         | 所在经度            | 121.5317           |
| trans       | 1.5km内地铁数       | 3                  |
| school      | 1.5km内学校数       | 7                  |
| business    | 1.5km内商圈数       | 2                  |
| fundamental | 1.5km内医院、公园数 | 2                  |

