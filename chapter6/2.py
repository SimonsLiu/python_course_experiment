"""
@author:Liushihao
@time:2020/4/20:11:23
@email:Liushihao_1224@163.com
@describe:
设计一个“超市进销存管理系统”，要求如下：
(1)系统包括7种操作，分别是：1.查询所有商品；2.添加商品；3.修改商品；4.删除商品；5.卖出端口；6.汇总；-1.退出系统。
(2)选择操作序号“1”，显示所有商品。
(3)选择操作序号“2”，添加新的商品(包括商品名称、数量和进货价格)。
(4)选择操作序号“3”，修改商品。
(5)选择操作序号“4”，删除商品。
(6)选择操作序号“5”，卖出商品(包括商品名称、数量和售出价格)。
(7)选择操作序号“6”，汇总当天卖出商品，包括每种销售商品名称、数量、进货总价、销售总价等。
(8)选择操作序号“-1”，退出系统。
"""
# 定义商品类
import prettytable as pt
class Commodity:
    # 构造方法
    def __init__(self, Name, Numbers, inputPrice):
        self.Name = Name                # 商品名称.
        self.Numbers = Numbers          # 商品数量.
        self.inputPrice = inputPrice    # 商品进价.
        # self.outputPrice = outputPrice  # 商品售价.(商品的售价是变动的)
        self.count = 0                  # 此商品的销量
        self.AlloutputPrice = 0         # 商品的总销售额
        self.AllinputPrice = self.Numbers*self.inputPrice # 商品的总进价额
    # 商品销售
    def sale(self, outputPrice, num):
        if num <= self.Numbers:
            self.outputPrice = outputPrice  # 商品售价.
            self.count += num
            self.Numbers -= num
            self.AlloutputPrice += num * outputPrice
            return True
        else:
            print("库存不够，需要进货！")
            return False
class SaleManager:
    # 商品列表 commodities，每一个元素都是一个商品对象
    commodities = []
    # 构造方法
    def init(self):
        self.commodities.append(Commodity('怡宝纯净水', 100, 1.3))
        self.commodities.append(Commodity('富光水杯', 100, 4.3))
        self.commodities.append(Commodity('英雄牌钢笔', 100, 18))
    # 菜单
    def Menu(self):
        self.init()
        print('\"超市进销存管理系统\"菜单:')
        print('1.显示所有商品')
        print('2.添加新的商品(包括商品名称、数量和进货价格)')
        print('3.修改商品')
        print('4.删除商品')
        print('5.卖出商品(包括商品名称、数量和售出价格)')
        print('6.汇总当天卖出商品，包括每种销售商品名称、数量、进货总价、销售总价')
        print('-1.退出系统')
        while (True):
            menu_item = input('******请输入菜单编号: ')
            if menu_item == '1':
                self.show_all_commodities()
            elif menu_item == '2':
                self.add_commodities()
            elif menu_item == '3':
                self.modify_commodities()
            elif menu_item == '4':
                self.del_commodities()
            elif menu_item == '5':
                self.sale_commodities()
            elif menu_item == '6':
                self.Summarize_sales()
            elif menu_item == '-1':
                print('谢谢使用!')
                break
            else:
                print("请输入-1，1~6范围的菜单项编号！")

    # 1. 显示所有商品
    def show_all_commodities(self):
        for commodity in self.commodities:
            print('名称: %s,  数量: %d,  进价: %.2f' % (commodity.Name, commodity.Numbers, commodity.inputPrice))

    # 2. 添加新商品
    def add_commodities(self):
        commodity_name = input("请输入添加商品的名称：")
        ret = self.check_commodities(commodity_name)
        if ret != None:
            print('商品已经存在！')
        else:
            num = int(input("请输入商品进货数量："))
            inprice = int(input("请输入商品进货价格："))
            new_commodity = Commodity(commodity_name, num, inprice)
            self.commodities.append(new_commodity)
            print("添加商品成功！")

    # 3. 修改商品
    def modify_commodities(self):
        commodity_name = input("请输入修改商品的名称：")
        ret = self.check_commodities(commodity_name)
        if ret == None:
            print('商品不存在！')
        else:
            num = int(input("请输入修改商品的数量："))
            inprice = float(input("请输入修改商品的单价："))
            ret.Numbers = num
            ret.inputPrice = inprice
            print("修改商品成功！")

    # 4. 删除商品
    def del_commodities(self):
        commodity_name = input("请输入删除商品的名称：")
        ret = self.check_commodities(commodity_name)
        if ret == None:
            print('商品不存在！')
        else:
            self.commodities.remove(ret)
            print("删除商品成功！")

    # 5. 卖出商品(包括商品名称、数量和售出价格)
    def sale_commodities(self):
        commodity_name = input("请输入卖出商品的名称：")
        ret = self.check_commodities(commodity_name)
        if ret == None:
            print('商品不存在！')
        else:
            num = int(input("请输入销售数量："))
            outprice = float(input("请输入售出价格："))
            if ret.sale(outprice, num):
                print("卖出商品成功！")
            else:
                print("卖出商品失败")

    # 6. 汇总当天卖出商品，包括每种销售商品名称、数量、进货总价、销售总价')
    def Summarize_sales(self):
        print("今天销售情况汇总：")
        tb = pt.PrettyTable()
        tb.field_names = ["商品名称", "数量", "进货总价", "销售总价"]
        for commodity in self.commodities:
            if commodity.count!=0:
                tb.add_row([commodity.Name, commodity.count, commodity.inputPrice*commodity.count, commodity.AlloutputPrice])
        print(tb)

    # 检查商品是否存在，根据商品名称查找
    def check_commodities(self, Name):
        for commodity in self.commodities:
            if commodity.Name == Name:
                return commodity
        return None

if __name__ == "__main__":
    manager = SaleManager()
    manager.Menu()