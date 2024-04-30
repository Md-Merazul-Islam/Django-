
from django.urls import path
from . import views

urlpatterns = [
    # path('add/',views.add_post, name = 'add_post'),
    path('add/',views.AddPostCreateViews.as_view(), name = 'add_post'),
    # path('edit/<int:id>',views.edit_post, name = 'edit_post'),
    path('edit/<int:id>',views.EditPostView.as_view(), name = 'edit_post'),
    # path('delete_post/<int:id>',views.delete_post, name = 'delete_post'),
    path('delete_post/<int:id>',views.DeletePost.as_view(), name = 'delete_post'),

]