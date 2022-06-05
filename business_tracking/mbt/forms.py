from django import forms
from mbt.models import Inbound, Contract

class InboundForm(forms.ModelForm):
    class Meta:
        model=Inbound
        fields = ['inbound_title', 'client_name', 'client_contact_point', 'dept']
        widgets = {
            'inbound_title':forms.TextInput(attrs={'class':'form-control'}),
            'client_name':forms.TextInput(attrs={'class':'form-control'}),
            'client_contact_point':forms.TextInput(attrs={'class':'form-control'}),
            'dept':forms.Select(attrs={"class":"form-control"}),
        }
        labels ={
            "inbound_title":"인바운드 문의 건",
            "client_name":"광고주 명",
            "client_contact_point":"접촉경로",
            "dept":"문의 대응 부서",
        }

class InboundToContractForm(forms.ModelForm):
    class Meta:
        model=Contract
        fields = ['assignee', 'contracted_value', 'memo']
        labels = {
            'assignee':'담당자',
            'contracted_value':'수주계약 총 금액',
            'memo':"메모"
        }