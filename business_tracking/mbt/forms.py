from django import forms
from mbt.models import Inbound, Contract

class InboundForm(forms.ModelForm):
    class Meta:
        model=Inbound
        fields = [
            'client_name',
            'budget',
            'requested_summary',
            'inbound_path',
            'inbound_dept',
            'client_manager',
            'client_manager_email',
            'client_manager_tel',
        ]
        # widgets = {
        #     'inbound_title':forms.TextInput(attrs={'class':'form-control'}),
        #     'client_name':forms.TextInput(attrs={'class':'form-control'}),
        #     'inbound_path':forms.TextInput(attrs={'class':'form-control'}),
        #     'inbound_dept':forms.Select(attrs={"class":"form-control"}),
        # }
        labels ={
            "client_name":"광고주 명",
            "budget":"예산",
            "requested_summary":"요청 브리프",
            "inbound_path":"접촉경로",
            "inbound_dept":"문의 대응 부서",
            'client_manager':"고객사 담당자",
            'client_manager_email':"담당자 이메일",
            'client_manager_tel':"담당자 번호",
        }

class InboundToContractForm(forms.ModelForm):
    class Meta:
        model=Contract
        fields = ['person', 'contracted_value', 'description']
        labels = {
            'person':'담당자',
            'contracted_value':'수주계약 총 금액',
            'description':"메모"
        }