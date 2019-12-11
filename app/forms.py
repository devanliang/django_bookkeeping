from django.forms import ModelForm, TextInput
from datetime import date
from .models import Record # 與model做連動

class RecordForm(ModelForm): # 繼承model form
    class Meta: # subclass
        model = Record # 用的model來連動
        fields = ['date','description','category','cash','balance_type']  # 用到的欄位
        widgets = { # 1.widgets屬性可針對某個欄位做特定處理
            'date': TextInput( # date是欄位選用 textinput格式 同html <input type="text">
                attrs={  # attrs 針對 textinput輸入資料做設定 可定義多種屬性
                    'id': 'datepicker1', # 利用key, value 值做設定
                    'value': date.today().strftime("%Y-%m-%d") # 給預設值用今天
                }
                )
        }