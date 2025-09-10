from django.contrib import admin
from django import forms
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User, Group
from django.contrib.admin.models import LogEntry
from .models import Contact, Training
from .forms import TrainingForm
from django.contrib.admin import AdminSite
# Foydalanuvchilarni admin paneldan olib tashlash
admin.site.unregister(User)
admin.site.unregister(Group)
try:
    admin.site.unregister(LogEntry)
except admin.sites.NotRegistered:
    pass
    



class ContactAdmin(admin.ModelAdmin):
    list_display = ('auto_number', 'name',)
    search_fields = ('auto_number', 'name',)
    ordering = ['auto_number']
    
    # search bar faqat raqam bo‘yicha bo‘lsa
    def get_search_results(self, request, queryset, search_term):
        if search_term.isdigit():
            queryset = queryset.filter(auto_number=search_term)
            return queryset, False
        return super().get_search_results(request, queryset, search_term)
    

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['name'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#D412B473",
            'Name/Имя')
        form.base_fields['Job'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#D412B473",
            'Job/Должность')
        form.base_fields['Safety'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#DAFBFCFF",
            'Safety Induction\nВводный инструктаж AR')
        form.base_fields['Supervisor'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#DAFBFCFF",
            'Supervisor Leadership Training / BSP /\nТренинг лидерства для руководителей / BSP')
        form.base_fields['JSA'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#DAFBFCFF",
            'Awareness of Job Safety Analysis (JSA)\nОсведомленность о  Анализ безопасности работы (АБР)')
        form.base_fields['Risk'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#DAFBFCFF",
            'Risk Management (HAZID. RAMS. JSA)\nУправление рисками')
        form.base_fields['Loading'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#DAFBFCFF",
            'Loading & \nПогрузка и разгрузка')
        form.base_fields['Emergency'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#DAFBFCFF",
            'Emergency Response\nЭкстренное реагирование')
        form.base_fields['Incident'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#DAFBFCFF",
            'Incident Management\nУправление инцидентами')
        form.base_fields['LOTO'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#DAFBFCFF",
            'LOTO')
        form.base_fields['Safety1'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Вводный инструктаж EE')
        form.base_fields['Hazard'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Hazard Communications/Use Hazardous Material \nОпасные связи/Использование опасных материалов')
        form.base_fields['Fire'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Fire Prevention\nПредотвращение пожаров')
        form.base_fields['Electrical'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Electrical Safety\nЭлектробезопасность')
        form.base_fields['HotWork'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Hotwork\nОгневые работы')
        form.base_fields['CHMP'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'CHWP Receiver & Issuer\nПолучатель и Выдаватель CHWP')
        form.base_fields['Ground'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Ground Disturbance: Pilling. Excavation & Trenching\nРазрушение грунта: Пиллинг. раскопки и рытье траншей ер ишлари')
        form.base_fields['Confined'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Confined Space\nОграниченные пространства. Замккнутий пронс')
        form.base_fields['Fall'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Fall Protection & Dropped Objects\nРабота на высоте')
        form.base_fields['Defensive'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Defensive driving\nБезопасный вождение')
        form.base_fields['Scaffold'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Scaffold User\nСтроительные леса - Пользователь')
        form.base_fields['Flagman'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Flagman\nСигнальщик')
        form.base_fields['Auto'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgb(229, 254, 226)",
            'Auto hydraulic lift / Авто гидро подемник')
        form.base_fields['Certificate'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Scaffolding-related Certificate\nСертификат по строительным лесам')
        form.base_fields['Crane'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Crane Operator Qualification Certificate\nКвалификационное удостоверение машиниста крана')
        form.base_fields['Rigger'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Rigger qualification certificate \nКвалификационное удостоверение стропальщика')
        form.base_fields['Hoisting'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Hoisting and Lifting supervisor qualification/certificate\nКвалификация/сертификат супервайзера по грузоподъемным машинам и подъемникам')
        form.base_fields['Welder'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Welder qualification\nКвалификация сварщика')
        form.base_fields['Diesel'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Training for diesel mechanics\nОбучение для дизелистов')
        form.base_fields['PPE'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Transportation of hazardous substances and distribution of fuel and lubricants\nПеревозка опасных веществ и раздача ГСМ')
        form.base_fields['DrLicense'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Driver\'s License / Водителская Удостореваная')
        form.base_fields['Qualific'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 18, 255, 0.637)",
            'Abduction qualifications / Повищения кволификатсия')
        form.base_fields['Heat'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 255, 91, 0.801)",
            'Heat Stress Campaign\nКампания потив теплового стресса')
        form.base_fields['Load'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 255, 91, 0.801)",
            'Load Handling Campaign\nКампания по погрузке-разгрузке')
        form.base_fields['GoldenRules'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 255, 91, 0.801)",
            '10 IIF/BSG Golden Rules\n10 Золотых правил охраны труда и техники безопасности')
        form.base_fields['HAVS'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 255, 91, 0.801)",
            'Hand Safety Campaign HAVS\nКампания по безопасности рук')
        form.base_fields['Dropped'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 255, 91, 0.801)",
            'Dropped Objects Campaign\nКампания Упавшие предметы')
        form.base_fields['LOF'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "rgba(255, 255, 91, 0.801)",
            'Line of Fire Campaign\nКампания Линия огня')
        form.base_fields['med'].label = format_html(
            '<button style="background:{};color:black;width: 155px;padding:5px;border-radius:5px;">{}</button>',
            "#8DB0FDAC",
            'Medical Certificate\nМедицинская справка')
        
        return form
        

admin.site.register(Contact, ContactAdmin)

