from django.urls import path
from backend.views import GetImg
from backend.views import UploadCsv
from backend.views import FilterOutlier
from backend.views import ConditionSearch
from backend.views import SendMail

urlpatterns = [
    #path('对应url', 模块名.as_view({'请求类型': 'views.py中对应的函数名'})
    path('saveimage/', GetImg.as_view({'post': 'save_image'})),
    path('vibration/uploadCsv/', UploadCsv.as_view({'post':'save_csv'})),
    path('vibration/filterOutlier/', FilterOutlier.as_view({'post':'filter_outlier'})),
    path('vibration/conditionSearch/', ConditionSearch.as_view({'post':'condition_search'})),
    path('vibration/sendMail/', SendMail.as_view({'post': 'send_mail'}))
]
