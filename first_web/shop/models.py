from django.db import models
from django.contrib.auth.models import User
# Create your models here.
##################进货##################

'''因为要用到它，所以要先导入'''
class UserInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    #和自带的User表一对一关联
    role=models.CharField(max_length=32)  #可以加扩展信息字段，比如年龄，性别，角色



class jinhuo(models.Model):
    number = models.CharField(max_length=10,  verbose_name='商品款号')
    sort = models.CharField(max_length=10, verbose_name='商品名称')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    m_total = models.IntegerField(default=0, verbose_name='M')
    l_total = models.IntegerField(default=0, verbose_name='L')
    xl_total = models.IntegerField(default=0, verbose_name='XL')
    xxl_total = models.IntegerField(default=0, verbose_name='2XL')
    xxxl_total = models.IntegerField(default=0, verbose_name='3XL')
    xxxxl_total = models.IntegerField(default=0, verbose_name='4XL')
    color = models.CharField(max_length=6, verbose_name='颜色', null=True)
    price = models.IntegerField(default=0, verbose_name='单价')
    price_total = models.IntegerField(default=0, verbose_name='总价')
    total = models.IntegerField(default=0, verbose_name='总数')

    shop_name = models.CharField(max_length=10, verbose_name='店名', null=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['-c_time']
        verbose_name = '进货'
        verbose_name_plural = '进货'

###################销售#################
class xiaoshou(models.Model):
    number = models.CharField(max_length=10,  verbose_name='商品款号')
    sort = models.CharField(max_length=10, verbose_name='商品名称')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='出售时间')
    m_total = models.IntegerField(default=0, verbose_name='M')
    l_total = models.IntegerField(default=0, verbose_name='L')
    xl_total = models.IntegerField(default=0, verbose_name='XL')
    xxl_total = models.IntegerField(default=0, verbose_name='2XL')
    xxxl_total = models.IntegerField(default=0, verbose_name='3XL')
    xxxxl_total = models.IntegerField(default=0, verbose_name='4XL')
    color = models.CharField(max_length=6, verbose_name='颜色', null=True)
    xiaoshou_total = models.IntegerField(default=0, verbose_name='总数')

    shop_name = models.CharField(max_length=10, verbose_name='店名', null=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['-c_time']
        verbose_name = '销售'
        verbose_name_plural = '销售'

###########################库存####################
class kucun(models.Model):
    number = models.CharField(max_length=8, verbose_name='商品款号')
    sort = models.CharField(max_length=10, verbose_name='商品名称')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='库存更新时间')
    m_total = models.IntegerField(default=0, verbose_name='M')
    l_total = models.IntegerField(default=0, verbose_name='L')
    xl_total = models.IntegerField(default=0, verbose_name='XL')
    xxl_total = models.IntegerField(default=0, verbose_name='2XL')
    xxxl_total = models.IntegerField(default=0, verbose_name='3XL')
    xxxxl_total = models.IntegerField(default=0, verbose_name='4XL')
    color = models.CharField(max_length=6, verbose_name='颜色', null=True)
    total = models.IntegerField(default=0, verbose_name='库存总数')
    price = models.IntegerField(default=0, verbose_name='单价')
    price_total = models.IntegerField(default=0, verbose_name='总价')

    shop_name = models.CharField(max_length=10, verbose_name='店名', null=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['-c_time']
        verbose_name = '库存'
        verbose_name_plural = '库存'


####################调货返货#######################
class fanhuo(models.Model):
    number = models.CharField(max_length=8, verbose_name='商品款号')
    sort = models.CharField(max_length=10, verbose_name='商品名称')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='返货调货时间')
    m_total = models.IntegerField(default=0, verbose_name='M')
    l_total = models.IntegerField(default=0, verbose_name='L')
    xl_total = models.IntegerField(default=0, verbose_name='XL')
    xxl_total = models.IntegerField(default=0, verbose_name='2XL')
    xxxl_total = models.IntegerField(default=0, verbose_name='3XL')
    xxxxl_total = models.IntegerField(default=0, verbose_name='4XL')
    color = models.CharField(max_length=6, verbose_name='颜色', null=True)
    total = models.IntegerField(default=0, verbose_name='库存总数')
    price = models.IntegerField(default=0, verbose_name='单价')
    price_total = models.IntegerField(default=0, verbose_name='总价')
    tips = models.CharField(max_length=8, verbose_name='备注')

    shop_name = models.CharField(max_length=10, verbose_name='店名', null=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['-c_time']
        verbose_name = '返货'
        verbose_name_plural = '返货'

######################会员积分#########################

class vip(models.Model):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='会员手机号')
    name = models.CharField(max_length=5, verbose_name='会员名字')
    jifen_total = models.IntegerField(default=0, verbose_name='总积分')
    jifen_history = models.IntegerField(default=0, verbose_name='历史消费总积分')
    yucun = models.IntegerField(default=0, verbose_name='预存总金额')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')
    yucun_total = models.IntegerField(default=0, verbose_name='预存总次数')

    shop_name = models.CharField(max_length=10, verbose_name='店名', null=True)

    def __str__(self):
        return self.mobile

    class Meta:
        ordering = ['-c_time']
        verbose_name = '会员积分管理'
        verbose_name_plural = '会员积分管理'

class vip_detail(models.Model):
    mobile = models.CharField(max_length=11, verbose_name='会员手机号')
    name = models.CharField(max_length=5, verbose_name='会员名')
    jifen_use = models.IntegerField(default=0, verbose_name='兑换积分')
    jifen_get = models.IntegerField(default=0, verbose_name='单次获得积分')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='时间')

    shop_name = models.CharField(max_length=10, verbose_name='店名', null=True)

    def __str__(self):
        return self.mobile

    class Meta:
        ordering = ['-c_time']
        verbose_name = '会员详情'
        verbose_name_plural = '会员详情'