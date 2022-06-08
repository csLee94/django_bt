from django import forms
from mbt.models import Inbound, Contract, InboundHistory

class InboundForm(forms.ModelForm):
    class Meta:
        model=Inbound
        fields = [
            'client_name',
            'requested_summary',
            'inbound_path',
            'inbound_dept',
            'budget',
            'client_manager',
            'client_manager_email',
            'client_manager_tel',
        ]
        # labels ={
        #     "client_name":"광고주 명",
        #     "budget":"예산",
        #     "requested_summary":"요청 브리프",
        #     "inbound_path":"인바운드 경로",
        #     "inbound_dept":"문의 대응 부서",
        #     'client_manager':"고객사 담당자",
        #     'client_manager_email':"담당자 이메일",
        #     'client_manager_tel':"담당자 번호",
        # }

class InboundToContractForm(forms.ModelForm):
    class Meta:
        model=Contract
        fields = ['contracted_title','person', 'contracted_value', 'description']
        labels = {
            'contracted_title':'계약 건 명',
            'person':'담당자',
            'contracted_value':'수주계약 총 금액',
            'description':"메모"
        }

class AddInboundHistory(forms.ModelForm):
    class Meta:
        model=InboundHistory
        fields = ['action_type', 'description', 'person']
        labels = {
            'action_type':'문의 대응(선택)',
            'description':"메모",
            'person':'담당자',
        }