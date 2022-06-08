from django.db import models

# Create your models here.

class Inbound(models.Model):
    created_at = models.DateTimeField()
    inbound_dept = models.CharField(
        max_length=10,
        choices=[
            ("CAM", "캠페인본부"),
            ("NWB", "BX사업본부"),
            ("CNS", "전략컨설팅본부"),
            ("SLT", "더쏠트"),
            ("LCO", "로코옵티마이저스"),
        ]
    )
    inbound_path = models.CharField(max_length=20)
    inbound_title = models.CharField(max_length=20)
    client_name = models.CharField(max_length=20)
    budget = models.IntegerField(null=True)
    requested_summary = models.CharField(max_length=50)
    client_manager = models.CharField(max_length=5, null=True)
    client_manager_email =models.EmailField(max_length=30, null=True)
    client_manager_tel = models.CharField(max_length=13, null=True)
    status = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.inbound_title

class InboundHistory(models.Model):
    inbound = models.ForeignKey(Inbound, on_delete=models.CASCADE)
    action_type = models.CharField(
        max_length=10, 
        choices=[
            ("ACT1","응대회신"),
            ("ACT2","담당부서 이관"),
            ("ACT3","미팅확정"),
            ("ACT4","미팅완료"),
            ("ACT5", "기타"),
        ]
    )
    description = models.TextField()
    person = models.CharField(max_length=5)
    action_created_at = models.DateTimeField()

class Contract(models.Model):
    inbound_id = models.IntegerField()
    contracted_title = models.CharField(max_length=30)
    contracted_at = models.DateTimeField()
    contracted_value = models.IntegerField()
    contracted_dept = models.CharField(
        max_length=10,
        choices=[
            ("CAM", "캠페인본부"),
            ("NWB", "BX사업본부"),
            ("CNS", "전략컨설팅본부"),
            ("SLT", "더쏠트"),
            ("LCO", "로코옵티마이저스"),
        ]
    )
    person = models.CharField(max_length=10)
    client = models.CharField(max_length=30)
    client_type = models.CharField(
        max_length=10,
        choices=[
            ("ADV","광고주"), 
            ("AGN","대행사"), 
            ("LAB","랩사")
        ]
    )
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('progress','진행중'),
            ('end','종료')
        ],
        default="진행중"
    )