from django.shortcuts import render, HttpResponse, redirect
from .models import Record, Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required # 以下function 要在使用這有登入才可使用
def hello(request):
    return render(request,'app/hello.html',{})

@login_required
def frontpage(request):
    #user = request.user # 有login_required request 會帶有user參數 
    record_form = RecordForm(initial={'balance_type':'支出'}) # initial參數給欄位預設值
    records = Record.objects.filter() # query all
    income_list = [record.cash for record in records if record.balance_type == '收入']
    outcome_list = [record.cash for record in records if record.balance_type == '支出']
    income = sum(income_list) if len(income_list) != 0 else 0
    outcome = sum(outcome_list) if len(outcome_list) != 0 else 0
    net = income - outcome
    return render(request, 'app/index.html', locals())

@login_required
def settings(request):
    categories = Category.objects.filter()
    return render(request, 'app/settings.html', locals())

@login_required
def add_Category(request):
    if request.method == 'POST':
        posted_data = request.POST # 類似dict
        category = posted_data['add_category'] # 取出add_category的值
        Category.objects.get_or_create(category=category) # 寫入資料庫欄位category, 沒有再創造
    return redirect('/settings') # 重新導向settings url 才會顯示輸入值（重作settings的function)

@login_required
def deleteCategory(request, category):
    Category.objects.filter(category=category).delete()
    return redirect('/settings')

@login_required
def addRecord(request):
    if request.method == 'POST':
        form = RecordForm(request.POST) # 傳入dict
        if form.is_valid():   # 確認輸入格式都符合規則
            form.save() # 存入資料庫
    return redirect('/') # 回到首頁

@login_required
def deleteRecord(request):
    if request.method == 'POST':
        id = request.POST['delete_val']
        Record.objects.filter(id=id).delete() # 利用ORM刪除
    return redirect('/')