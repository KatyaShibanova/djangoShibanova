from django.urls import path
from blog.views import index,by_dog,image_upload_view,get_deals,add_deal

urlpatterns = [
    path('', index, name='index'),
    path('<int:dog_id>', by_dog, name='by_dog'),
    path('dogs/', index, name='dogs'),
    path('add/', image_upload_view, name='add'),
    path('deals/', get_deals, name='deals'),
    path('<int:dog_id>/addDeal', add_deal, name='addDeal')
]