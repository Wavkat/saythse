from django.db import models
from django.utils.safestring import mark_safe
class Contact(models.Model):
    def save(self, *args, **kwargs):
        if self.auto_number is None:
            oxirgi = Contact.objects.order_by('-auto_number').first()
            self.auto_number = 1 if not oxirgi else oxirgi.auto_number + 1
        super().save(*args, **kwargs)

    auto_number = models.PositiveIntegerField(
        verbose_name="№",
        null=True,
        blank=True,
        editable=True
    )


    name = models.CharField(max_length=100,default='0',verbose_name="Name")
    Job = models.CharField(max_length=100,default='0', verbose_name="Job/Должность" )
    Safety = models.CharField(max_length=100,default='0', verbose_name="Safety Induction\nВводный инструктаж AR" )
    Supervisor = models.CharField(max_length=100,default='0', verbose_name="Supervisor Leadership Training / BSP /\nТренинг лидерства для руководителей / BSP" )
    JSA = models.CharField(max_length=100,default='0', verbose_name="Awareness of Job Safety Analysis (JSA)\nОсведомленность о  Анализ безопасности работы (АБР)")
    Risk = models.CharField(max_length=100,default='0', verbose_name="Risk Management (HAZID. RAMS. JSA)\nУправление рисками")
    Loading = models.CharField(max_length=100,default='0', verbose_name="Loading & \nПогрузка и разгрузка")
    Emergency = models.CharField(max_length=100,default='0', verbose_name="Emergency Response\nЭкстренное реагирование")
    Incident = models.CharField(max_length=100,default='0', verbose_name="Incident Management\nУправление инцидентами")
    LOTO = models.CharField(max_length=100,default='0', verbose_name="LOTO")
    Safety1 = models.CharField(max_length=100,default='0', verbose_name="Вводный инструктаж EE" )
    Hazard = models.CharField(max_length=100,default='0', verbose_name="Hazard Communications/Use Hazardous Material \nОпасные связи/Использование опасных материалов")
    Fire = models.CharField(max_length=100,default='0', verbose_name="Fire Prevention\nПредотвращение пожаров")
    Electrical = models.CharField(max_length=100,default='0', verbose_name="Electrical Safety\nЭлектробезопасность")
    HotWork = models.CharField(max_length=100,default='0', verbose_name="Hotwork\nОгневые работы")
    CHMP = models.CharField(max_length=100,default='0', verbose_name="CHWP Receiver & Issuer\nПолучатель и Выдаватель CHWP")
    Ground = models.CharField(max_length=100,default='0', verbose_name="Ground Disturbance: Pilling. Excavation & Trenching\nРазрушение грунта: Пиллинг. раскопки и рытье траншей ер ишлари")
    Confined = models.CharField(max_length=100,default='0', verbose_name="Confined Space\nОграниченные пространства. Замккнутий пронс")
    Fall = models.CharField(max_length=100,default='0', verbose_name="Fall Protection & Dropped Objects\nРабота на высоте")
    Defensive = models.CharField(max_length=100,default='0', verbose_name="Defensive driving\nБезопасный вождение")
    Scaffold = models.CharField(max_length=100,default='0', verbose_name="Scaffold User\nСтроительные леса - Пользователь")
    Flagman = models.CharField(max_length=100,default='0', verbose_name="Flagman\nСигнальщик")
    Auto = models.CharField(max_length=100,default='0', verbose_name="Auto hydraulic lift / Авто гидро подемник")
    Certificate = models.CharField(max_length=100,default='0', verbose_name="Scaffolding-related Certificate\nСертификат по строительным лесам")
    Crane = models.CharField(max_length=100,default='0', verbose_name="Crane Operator Qualification Certificate\nКвалификационное удостоверение машиниста крана")
    Rigger = models.CharField(max_length=100,default='0', verbose_name="Rigger qualification certificate \nКвалификационное удостоверение стропальщика")
    Hoisting = models.CharField(max_length=100,default='0', verbose_name="Hoisting and Lifting supervisor qualification/certificate\nКвалификация/сертификат супервайзера по грузоподъемным машинам и подъемникам")
    Welder = models.CharField(max_length=100,default='0', verbose_name="Welder qualification\nКвалификация сварщика")
    Diesel = models.CharField(max_length=100,default='0', verbose_name="Training for diesel mechanics\nОбучение для дизелистов")
    PPE = models.CharField(max_length=100,default='0', verbose_name="Transportation of hazardous substances and distribution of fuel and lubricants\nПеревозка опасных веществ и раздача ГСМ")
    DrLicense = models.CharField(max_length=100,default='0', verbose_name="Driver's License / Водителская Удостореваная")
    Qualific = models.CharField(max_length=100,default='0', verbose_name="Abduction qualifications / Повищения кволификатсия")
    Heat = models.CharField(max_length=100,default='0', verbose_name="Heat Stress Campaign\nКампания потив теплового стресса")
    Load = models.CharField(max_length=100,default='0', verbose_name="Load Handling Campaign\nКампания по погрузке-разгрузке")
    GoldenRules = models.CharField(max_length=100,default='0', verbose_name="10 IIF/BSG Golden Rules\n10 Золотых правил охраны труда и техники безопасности")
    HAVS = models.CharField(max_length=100,default='0', verbose_name="Hand Safety Campaign HAVS\nКампания по безопасности рук")
    Dropped = models.CharField(max_length=100,default='0', verbose_name="Dropped Objects Campaign\nКампания Упавшие предметы")
    LOF = models.CharField(max_length=100,default='0', verbose_name="Line of Fire Campaign\nКампания Линия огня")
    med = models.CharField(max_length=100,default='0', verbose_name="Medical Certificate\nМедицинская справка")
    def __str__(self):
        return f"{self.auto_number}. {self.name}"
   

# Модель Training для формы TrainingForm
class Training(models.Model):
    auto_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    Job = models.CharField(max_length=100, default='')
    Safety = models.CharField(max_length=100, default='')
    Supervisor = models.CharField(max_length=100, default='')
    JSA = models.CharField(max_length=100, default='')
    Risk = models.CharField(max_length=100, default='')
    Loading = models.CharField(max_length=100, default='')
    Emergency = models.CharField(max_length=100, default='')
    Incident = models.CharField(max_length=100, default='')
    LOTO = models.CharField(max_length=100, default='')
    Safety1 = models.CharField(max_length=100, default='')
    Hazard = models.CharField(max_length=100, default='')
    Fire = models.CharField(max_length=100, default='')
    Electrical = models.CharField(max_length=100, default='')
    HotWork = models.CharField(max_length=100, default='')
    CHMP = models.CharField(max_length=100, default='')
    Ground = models.CharField(max_length=100, default='')
    Confined = models.CharField(max_length=100, default='')
    Fall = models.CharField(max_length=100, default='')
    Defensive = models.CharField(max_length=100, default='')
    Scaffold = models.CharField(max_length=100, default='')
    Flagman = models.CharField(max_length=100, default='')
    Auto = models.CharField(max_length=100, default='')
    Certificate = models.CharField(max_length=100, default='')
    Crane = models.CharField(max_length=100, default='')
    Rigger = models.CharField(max_length=100, default='')
    Hoisting = models.CharField(max_length=100, default='')
    Welder = models.CharField(max_length=100, default='')
    Diesel = models.CharField(max_length=100, default='')
    PPE = models.CharField(max_length=100, default='')
    DrLicense = models.CharField(max_length=100, default='')
    Qualific = models.CharField(max_length=100, default='')
    Heat = models.CharField(max_length=100, default='')
    Load = models.CharField(max_length=100, default='')
    GoldenRules = models.CharField(max_length=100, default='')
    HAVS = models.CharField(max_length=100, default='')
    Dropped = models.CharField(max_length=100, default='')
    LOF = models.CharField(max_length=100, default='')
    med = models.CharField(max_length=100, default='')

def save(self, *args, **kwargs):
    if self.auto_number is None:
        oxirgi = Contact.objects.order_by('-auto_number').first()
        self.auto_number = 1 if not oxirgi else oxirgi.auto_number + 1
    super().save(*args, **kwargs)


    
class Meta:
    verbose_name = "Worker"
    verbose_name_plural = "Workers"
    ordering = ['auto_number']