from django.shortcuts import render, redirect, HttpResponse
from . import models
#
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

####################登录相关#####################
#没有登录直接访问的话，会根据settings.py中的LOGIN_URL="/login"跳转（有一个默认的）

def acc_login(request):
    error_msg=' '
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        print(username)
        password = request.POST.get("password")
        print(password)
        user = authenticate(username=username, password=password)  #只是验证功能，还没有登录
        if user:
            print(user)        #username
            print(type(user))  #<class 'django.contrib.auth.models.User'>
            login(request, user)   #验证通过，登录
            #内部有request.user=user     可以用模板{{request.user}}
            return redirect(request.GET.get("next", '/shop'))    #http://127.0.0.1:8080/login?next=/crm
            #登录成功默认跳转用户信息页面，如果是其他页面来的，登录后跳转到其他页面
        else:
            print(user)        #None
            print(type(user))  #<class 'NoneType'>
            error_msg = "帐号或密码错误"
        return render(request, "login.html", {"error_msg": error_msg})

def acc_logout(request):
    logout(request)
    return redirect('/login')

#######################首页#######################
@login_required
def shouye(request):
    return render(request, 'shouye.html')

#####################################关于进货的views#########################################
@login_required
def jinhuo_list(request):
    #展示清单
    #进货的所有货物
    shop_name = request.user.username
    all_goods = models.jinhuo.objects.filter(shop_name=shop_name)
    return render(request, 'jinhuo_list.html', {'all_goods': all_goods})

@login_required
def add_jinhuo(request):
    if request.method == 'POST':
        a = request.POST.get('number')
        if not a:
            return render(request, 'add_jinhuo.html', {'error': '输入不能为空'})
        # if models.jinhuo.objects.filter(number=a):
        #     return render(request, 'add_jinhuo.html', {'error': '款号已存在'})
        #
        shop_name = request.user.username
        #
        b = request.POST.get('sort')
        m = request.POST.get('m_total')
        l = request.POST.get('l_total')
        xl = request.POST.get('xl_total')
        xxl = request.POST.get('xxl_total')
        xxxl = request.POST.get('xxxl_total')
        xxxxl = request.POST.get('xxxxl_total')
        time = request.POST.get('c_time')
        color = request.POST.get('color')
        price = request.POST.get('price')
        c = int(m)+int(l)+int(xl)+int(xxl)+int(xxxl)+int(xxxxl)
        price_total = int(price)*int(c)
        models.jinhuo.objects.create(number=a, sort=b, total=c, m_total=m, l_total=l, xl_total=xl, xxl_total=xxl,
                                     xxxl_total=xxxl, xxxxl_total=xxxxl, c_time=time, color=color, price=price,
                                     price_total=price_total, shop_name=shop_name)
     #######################?库存自动增加?##################
        if not models.kucun.objects.filter(number=a, color=color, shop_name=shop_name):

            models.kucun.objects.create(number=a, sort=b, total=c, m_total=m, l_total=l, xl_total=xl, xxl_total=xxl,
                                        xxxl_total=xxxl, xxxxl_total=xxxxl, c_time=time, color=color, price=price,
                                        price_total=price_total, shop_name=shop_name)
        else:
            kucun_good = models.kucun.objects.filter(number=a, color=color, shop_name=shop_name)
            kucun_good = kucun_good[0]
            kucun_good.m_total = int(kucun_good.m_total)+int(m)
            kucun_good.l_total = int(kucun_good.l_total)+int(l)
            kucun_good.xl_total = int(kucun_good.xl_total)+int(xl)
            kucun_good.xxl_total = int(kucun_good.xxl_total)+int(xxl)
            kucun_good.xxxl_total = int(kucun_good.xxxl_total)+int(xxxl)
            kucun_good.xxxxl_total = int(kucun_good.xxxxl_total)+int(xxxxl)
            kucun_good.total = int(kucun_good.total)+int(c)
            #kucun_good.c_time = time
            kucun_good.price_total = int(kucun_good.price_total)+int(price)*int(c)
            kucun_good.save()
        return redirect('/shop/jinhuo')
    return render(request, 'add_jinhuo.html')

@login_required
def del_jinhuo(request):
    pk = request.GET.get('number')
    obj = models.jinhuo.objects.filter(number=pk)
    if not obj:
        return HttpResponse('要删除的款号不存在')
    obj.delete()
    return redirect('/shop/jinhuo')

@login_required
def eidt_jinhuo(request):
    pk = request.GET.get('number')
    obj = models.jinhuo.objects.filter(number=pk)
    if not obj:
        return HttpResponse('要编辑的款号不存在')
    obj = obj[0]

    if request.method == 'POST':
        number = request.POST.get('number')
        if not number:
            return render(request, 'edit_jinhuo.html', {'error': '输入不能为空'})
        if models.jinhuo.objects.filter(number=number):
            return render(request, 'edit_jinhuo.html', {'error': '款号已存在'})
        sort = request.POST.get('sort')
        total = request.POST.get('total')
        obj.number = number
        obj.sort = sort
        obj.total = total
        obj.save()
        return redirect('/shop/jinhuo')
    return render(request, 'edit_jinhuo.html', {'obj': obj})


@login_required
def search_jinhuo(request):
    number = request.GET.get('number')
    shop_name = request.user.username
    if not number:
        all_goods = models.jinhuo.objects.filter(shop_name=shop_name)
        return render(request, 'jinhuo_list.html', {'error_search': '搜索不能为空', 'all_goods': all_goods})
    if models.jinhuo.objects.filter(number=number, shop_name=shop_name):
        goods = models.jinhuo.objects.filter(number=number, shop_name=shop_name)
        return render(request, 'search_jinhuo.html', {'goods': goods})
    else:
        all_goods = models.jinhuo.objects.filter(shop_name=shop_name)
        return render(request, 'jinhuo_list.html', {'error_search': '该店款号不存在，请检查款号', 'all_goods': all_goods})

######################################关于销售的########################################
@login_required
def xiaoshou_list(request):
    shop_name = request.user.username
    all_goods = models.xiaoshou.objects.filter(shop_name=shop_name)
    return render(request, 'xiaoshou_list.html', {'all_goods': all_goods})


@login_required
def add_xiaoshou(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        shop_name = request.user.username
        if not number:
            return render(request, 'add_xiaoshou.html', {'error': '输入不能为空'})

        if not models.kucun.objects.filter(number=number, shop_name=shop_name):
            return render(request, 'add_xiaoshou.html', {'error': '该店库存中没有这个款号，请检查输入款号是否正确'})
        #b = request.POST.get('sort')
        color = request.POST.get('color')
        if not models.kucun.objects.filter(number=number, color=color, shop_name=shop_name):
            return render(request, 'add_xiaoshou.html', {'error': '该店库存中这个款号没有这款颜色，请检查输入颜色是否正确'})
        b = models.kucun.objects.filter(number=number, shop_name=shop_name)
        b = b[0]
        b = b.sort
        m = request.POST.get('m_total')
        l = request.POST.get('l_total')
        xl = request.POST.get('xl_total')
        xxl = request.POST.get('xxl_total')
        xxxl = request.POST.get('xxxl_total')
        xxxxl = request.POST.get('xxxxl_total')
        time = request.POST.get('c_time')
        c = int(m) + int(l) + int(xl) + int(xxl) + int(xxxl) + int(xxxxl)
        # models.xiaoshou.objects.create(number=number, sort=b, xiaoshou_total=c, m_total=m, l_total=l, xl_total=xl, xxl_total=xxl,
        #                              xxxl_total=xxxl, xxxxl_total=xxxxl, c_time=time, color=color)

        kucun_good = models.kucun.objects.filter(number=number, color=color, shop_name=shop_name)
        kucun_good = kucun_good[0]

        kucun_good.m_total = int(kucun_good.m_total)-int(m)
        ##
        if kucun_good.m_total < 0:
            return render(request, 'add_xiaoshou.html', {'error': 'M号当日销售件数输入有错误，库存中没有这么多件'})

        kucun_good.l_total = int(kucun_good.l_total)-int(l)
        ##
        if kucun_good.l_total < 0:
            return render(request, 'add_xiaoshou.html', {'error': 'L号当日销售件数输入有错误，库存中没有这么多件'})

        kucun_good.xl_total = int(kucun_good.xl_total)-int(xl)
        ##
        if kucun_good.xl_total < 0:
            return render(request, 'add_xiaoshou.html', {'error': 'XL号当日销售件数输入有错误，库存中没有这么多件'})

        kucun_good.xxl_total = int(kucun_good.xxl_total)-int(xxl)
        ##
        if kucun_good.xxl_total < 0:
            return render(request, 'add_xiaoshou.html', {'error': '2XL号当日销售件数输入有错误，库存中没有这么多件'})

        kucun_good.xxxl_total = int(kucun_good.xxxl_total)-int(xxxl)
        ##
        if kucun_good.xxxl_total < 0:
            return render(request, 'add_xiaoshou.html', {'error': '3XL号当日销售件数输入有错误，库存中没有这么多件'})

        kucun_good.xxxxl_total = int(kucun_good.xxxxl_total)-int(xxxxl)
        ##
        if kucun_good.xxxxl_total < 0:
            return render(request, 'add_xiaoshou.html', {'error': '4XL号当日销售件数输入有错误，库存中没有这么多件'})


        models.xiaoshou.objects.create(number=number, sort=b, xiaoshou_total=c, m_total=m, l_total=l, xl_total=xl, xxl_total=xxl,
                                     xxxl_total=xxxl, xxxxl_total=xxxxl, c_time=time, color=color, shop_name=shop_name)

        kucun_good.total = int(kucun_good.total)-int(c)
        price = models.jinhuo.objects.filter(number=number, color=color, shop_name=shop_name)
        price = price[0]
        price =price.price
        kucun_good.price_total = int(kucun_good.price_total) - int(price)*int(c)
        kucun_good.save()
        return redirect('/shop/xiaoshou')
    return render(request, 'add_xiaoshou.html')

@login_required
def search_xiaoshou(request):
    number = request.GET.get('number')
    shop_name = request.user.username
    if not number:
        all_goods = models.xiaoshou.objects.filter(shop_name=shop_name)
        return render(request, 'xiaoshou_list.html', {'error': '搜索不能为空', 'all_goods': all_goods})
    if models.xiaoshou.objects.filter(number=number, shop_name=shop_name):
        goods = models.xiaoshou.objects.filter(number=number, shop_name=shop_name)
        return render(request, 'search_xiaoshou.html', {'goods': goods})
    else:
        all_goods = models.xiaoshou.objects.filter(shop_name=shop_name)
        return render(request, 'xiaoshou_list.html', {'error': '款号不存在，请检查款号', 'all_goods': all_goods})


##############################库存#################################
@login_required
def kucun_list(request):
    all_goods = models.kucun.objects.all()
    total_price = 0
    total_goods = 0
    for good in all_goods:
        total_price = int(total_price) + int(good.price_total)
        total_goods = int(total_goods) + int(good.total)
    return render(request, 'kucun_list.html', {'all_goods': all_goods, 'total_price': total_price, 'total_goods':total_goods})

@login_required
def search_kucun(request):
    number = request.GET.get('number')
    if not number:
        all_goods = models.kucun.objects.all()
        return render(request, 'kucun_list.html', {'error': '输入款号不能为空', 'all_goods': all_goods})
    if models.kucun.objects.filter(number=number):
        goods = models.kucun.objects.filter(number=number)
        return render(request, 'search_kucun.html', {'goods': goods})
    else:
        all_goods = models.kucun.objects.all()
        return render(request, 'kucun_list.html', {'error': '库存中没有这个款号，请重新输入', 'all_goods': all_goods})


#####################################？调货返货？###################################
@login_required
def fanhuo_list(request):
    shop_name = request.user.username
    all_goods = models.fanhuo.objects.filter(shop_name=shop_name)
    return render(request, 'fanhuo_list.html', {'all_goods': all_goods})

@login_required
def add_fanhuo(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        shop_name = request.user.username
        if not number:
            return render(request, 'add_fanhuo.html', {'error': '输入不能为空'})

        if not models.kucun.objects.filter(number=number, shop_name=shop_name):
            return render(request, 'add_fanhuo.html', {'error': '库存中没有这个款号，请检查输入款号是否正确'})
        #b = request.POST.get('sort')
        color = request.POST.get('color')
        if not models.kucun.objects.filter(number=number, color=color, shop_name=shop_name):
            return render(request, 'add_fanhuo.html', {'error': '库存中这个款号没有这款颜色，请检查输入颜色是否正确'})
        b = models.kucun.objects.filter(number=number, color=color, shop_name=shop_name)
        b = b[0]

        #####自动获取商品名称b
        danjia = b.price
        b = b.sort
        m = request.POST.get('m_total')
        l = request.POST.get('l_total')
        xl = request.POST.get('xl_total')
        xxl = request.POST.get('xxl_total')
        xxxl = request.POST.get('xxxl_total')
        xxxxl = request.POST.get('xxxxl_total')
        time = request.POST.get('c_time')
        tips = request.POST.get('tips')
        c = int(m) + int(l) + int(xl) + int(xxl) + int(xxxl) + int(xxxxl)
        price_total = int(danjia)*int(c)

        # models.fanhuo.objects.create(number=number, sort=b, total=c, m_total=m, l_total=l, xl_total=xl, xxl_total=xxl,
        #                              xxxl_total=xxxl, xxxxl_total=xxxxl, c_time=time, color=color, price=danjia,
        #                              tips=tips, price_total=price_total)

        kucun_good = models.kucun.objects.filter(number=number, color=color, shop_name=shop_name)
        kucun_good = kucun_good[0]

        kucun_good.m_total = int(kucun_good.m_total)-int(m)
        ##
        if kucun_good.m_total < 0:
            return render(request, 'add_fanhuo.html', {'error': 'M号件数输入有错误，库存中没有这么多件'})

        kucun_good.l_total = int(kucun_good.l_total)-int(l)
        ##
        if kucun_good.l_total < 0:
            return render(request, 'add_fanhuo.html', {'error': 'L号件数输入有错误，库存中没有这么多件'})

        kucun_good.xl_total = int(kucun_good.xl_total)-int(xl)
        ##
        if kucun_good.xl_total < 0:
            return render(request, 'add_fanhuo.html', {'error': 'XL件数输入有错误，库存中没有这么多件'})

        kucun_good.xxl_total = int(kucun_good.xxl_total)-int(xxl)
        ##
        if kucun_good.xxl_total < 0:
            return render(request, 'add_fanhuo.html', {'error': '2XL号件数输入有错误，库存中没有这么多件'})

        kucun_good.xxxl_total = int(kucun_good.xxxl_total)-int(xxxl)
        ##
        if kucun_good.xxxl_total < 0:
            return render(request, 'add_fanhuo.html', {'error': '3XL件数输入有错误，库存中没有这么多件'})

        kucun_good.xxxxl_total = int(kucun_good.xxxxl_total)-int(xxxxl)
        ##
        if kucun_good.xxxxl_total < 0:
            return render(request, 'add_fanhuo.html', {'error': '4XL号件数输入有错误，库存中没有这么多件'})


        models.fanhuo.objects.create(number=number, sort=b, total=c, m_total=m, l_total=l, xl_total=xl, xxl_total=xxl,
                                     xxxl_total=xxxl, xxxxl_total=xxxxl, c_time=time, color=color, price=danjia,
                                     tips=tips, price_total=price_total, shop_name=shop_name)

        kucun_good.total = int(kucun_good.total)-int(c)
        price = models.jinhuo.objects.filter(number=number, color=color, shop_name=shop_name)
        price = price[0]
        price =price.price
        kucun_good.price_total = int(kucun_good.price_total) - int(price)*int(c)
        kucun_good.save()
        return redirect('/shop/fanhuo')
    return render(request, 'add_fanhuo.html')

@login_required
def search_fanhuo(request):
    number = request.GET.get('number')
    shop_name = request.user.username
    if not number:

        all_goods = models.fanhuo.objects.filter(shop_name=shop_name)
        return render(request, 'fanhuo_list.html', {'error': '款号输入不能为空', 'all_goods': all_goods})
    if not models.fanhuo.objects.filter(number=number, shop_name=shop_name):

        all_goods = models.fanhuo.objects.filter(shop_name=shop_name)
        return render(request, 'fanhuo_list.html', {'error': '该店此款号不存在，请重新输入', 'all_goods': all_goods})
    goods = models.fanhuo.objects.filter(number=number, shop_name=shop_name)
    return render(request, 'search_fanhuo.html', {'goods': goods})


#########################会员积分########################
@login_required
def vip_list(request):
    shop_name = request.user.username
    all_vip = models.vip.objects.filter(shop_name=shop_name)
    return render(request, 'vip_list.html', {'all_vip': all_vip})

@login_required
def add_vip(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        name = request.POST.get('name')
        jifen_total = request.POST.get('jifen_one')
        yucun = request.POST.get('yucun')
        yucun_if = request.POST.get('yucun_if')
        shop_name = request.user.username
######记录获得积分情况
        if not mobile:
            return render(request, 'add_vip.html', {'error': '手机号输入不能为空'})

        if len(mobile) != 11:
            return render(request, 'add_vip.html', {'error': '手机号长度错误，输入错误'})

        if not jifen_total.isdigit():
            return render(request, 'add_vip.html', {'error': '输入的积分不是纯数字，请输入纯数字'})

        if not models.vip.objects.filter(mobile=mobile, shop_name=shop_name):

            models.vip.objects.create(mobile=mobile, name=name, jifen_total=jifen_total, jifen_history=jifen_total)
            models.vip_detail.objects.create(mobile=mobile, name=name, jifen_get=jifen_total, shop_name=shop_name)
        else:
            ######生成会员详情的表
            #models.vip_detail.objects.create(mobile=mobile, name=name, jifen_get=jifen_total, )
            obj = models.vip.objects.filter(mobile=mobile, shop_name=shop_name)
            vip = obj[0]
            models.vip_detail.objects.create(mobile=mobile, name=vip.name, jifen_get=jifen_total, )
            #######预存次数减1
            if int(yucun_if) == 1:
                vip.yucun_total = int(vip.yucun_total) - int(1)
                vip.yucun = int(vip.yucun) - int(yucun)
            if vip.yucun_total < 0:
                return render(request, 'add_vip.html', {'error': '会员预存消费次数不足'})
            vip.jifen_total = int(vip.jifen_total)+int(jifen_total)
            vip.jifen_history = int(vip.jifen_history)+int(jifen_total)
            vip.save()
        return redirect('/shop/vip')
    return render(request, 'add_vip.html')

@login_required
def add_yucun(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        name = request.POST.get('name')
        yucun = request.POST.get('yucun')
        shop_name = request.user.username

        if not mobile:
            return render(request, 'add_yucun.html', {'error': '手机号输入不能为空'})

        if len(mobile) != 11:
            return render(request, 'add_yucun.html', {'error': '手机号长度错误，输入错误'})

        if not yucun.isdigit():
            return render(request, 'add_vip.html', {'error': '输入的预存金额不是纯数字，请输入纯数字'})

        if not models.vip.objects.filter(mobile=mobile, shop_name=shop_name):
            ############预存100元为标准
            yucun_total = int(int(yucun)//100)
            models.vip.objects.create(mobile=mobile, name=name, yucun=yucun, yucun_total=yucun_total,shop_name=shop_name)
        else:
            obj = models.vip.objects.filter(mobile=mobile, shop_name=shop_name)
            vip = obj[0]
            vip.yucun = int(vip.yucun)+int(yucun)
            vip.yucun_total = int(int(vip.yucun)//100)
            vip.save()
        return redirect('/shop/vip')
    return render(request, 'add_yucun.html')


@login_required
def jifen_duihuan(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        jifen = request.POST.get('jifen')
        shop_name = request.user.username
        ######记录积分兑换情况
        if not mobile:
            return render(request, 'jifen_duihuan.html', {'error': '手机号输入不能为空'})

        if len(mobile) != 11:
            return render(request, 'jifen_duihuan.html', {'error': '手机号长度错误，输入错误'})

        if not jifen.isdigit():
            return render(request, 'jifen_duihuan.html', {'error': '输入的兑换积分不是纯数字，请输入纯数字'})

        if not models.vip.objects.filter(mobile=mobile, shop_name=shop_name):
            return render(request, 'jifen_duihuan.html', {'error': '该店没有这个会员，请检查手机号'})
        #models.vip_detail.objects.create(mobile=mobile, jifen_use=jifen)
        obj = models.vip.objects.filter(mobile=mobile,shop_name=shop_name)
        vip = obj[0]
        models.vip_detail.objects.create(mobile=mobile, jifen_use=jifen, name=vip.name, shop_name=shop_name)
        vip.jifen_total = int(vip.jifen_total)-int(jifen)
        if vip.jifen_total < 0:
            return render(request, 'jifen_duihuan.html', {'error': '会员积分不足'})
        vip.save()
        return redirect('/shop/vip')
    return render(request, 'jifen_duihuan.html')

@login_required
def vip_detial(request):
    mobile = request.GET.get('mobile')
    shop_name = request.user.username
    all_vip = models.vip_detail.objects.filter(mobile=mobile, shop_name=shop_name)
    if not all_vip:
        return HttpResponse('要查看的会员不存在')
    return render(request, 'vip_detial.html', {'all_vip': all_vip})

@login_required
def search_vip(request):
    mobile = request.GET.get('mobile')
    shop_name = request.user.username
    if not mobile:
        all_vip = models.vip.objects.filter(shop_name=shop_name)
        return render(request, 'vip_list.html', {'error': '查询手机号不能为空', 'all_vip': all_vip})
    if not models.vip.objects.filter(mobile=mobile, shop_name=shop_name):
        all_vip = models.vip.objects.filter(shop_name=shop_name)
        return render(request, 'vip_list.html', {'error': '输入要查询的会员手机号不存在，请重新输入', 'all_vip': all_vip})
    vips = models.vip.objects.filter(mobile=mobile, shop_name=shop_name)
    return render(request, 'search_vip.html', {'vips':vips})