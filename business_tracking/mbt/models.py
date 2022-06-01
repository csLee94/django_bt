from django.db import models

# Create your models here.

class Inbound(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField()
    inbound_title = models.CharField(max_length=50)
    client_name = models.CharField(max_length=20)
    client_contact_point = models.CharField(max_length=20)
    dept_lst = [
        ("CAM", "캠페인본부"),
        ("BX", "BX사업본부"),
        ("CNS", "전략컨설팅본부"),
        ("SLT", "더쏠트"),
        ("LCO", "로코옵티마이저스")
    ]
    dept = models.CharField(
        max_length=10,
        choices=dept_lst,
        default=None
    )
    def __str__(self):
        return self.inbound_title

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    inbound_id = models.ForeignKey(Inbound, on_delete=models.RESTRICT)
    created_at = models.DateTimeField()
    assignee = models.CharField(max_length=10)
    contracted_value = models.IntegerField()
    status = models.CharField(max_length=5)
    memo = models.TextField()
