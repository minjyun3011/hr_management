from django.views import generic
from .forms import SearchForm
from .models import Employee

class IndexView(generic.ListView):
    model=Employee
    template_name = 'employee/employee_list.html' 
    paginate_by=1

    def get_context_data(self):
        #テンプレートへ渡す辞書の作成
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET) #もとの辞書に、formを追加
        return context
    
    def get_queryset(self):
        form = SearchForm(self.request.GET)
        form.is_valid() 
        #これをしないと、cleaned_dataができない

        queryset = super().get_queryset()
        #まず、全社員を取得

        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department=department)
        #部署の選択があれば、サークルで絞り込み(filter)
            
        club = form.cleaned_data['club']
        if club:
            queryset = queryset.filter(club=club)
            # queryset = queryset.filter(family_name='吉田')
        return queryset
        #サークルの選択があれば、サークルで絞り込み(filter)

