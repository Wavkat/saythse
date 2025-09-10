import openpyxl
from main.core.models import Contact

def import_contacts_from_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    contacts = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if len(row) < 36:
            print(f"⚠️ Qator yetarli ustun emas: {row}")
            continue

        (
            name, Job, Safety, Supervisor, JSA, Risk, Loading, Emergency, Incident,
            LOTO, Safety1, Hazard, Fire, Electrical, HotWork, CHMP, Ground, Confined,
            Fall, Defensive, Scaffold, Flagman, Auto, Certificate, Crane, Rigger, Hoisting,
            Welder, Diesel, PPE, DrLicense, Qualific, Heat, Load, GoldenRules, HAVS, Dropped, LOF, med
        ) = row[:39]

        # Bo‘sh ism yoki lavozim bo‘lsa, o‘tkazib yuborish
        if not name or not Job:
            continue

        contacts.append(Contact(
            name=name,
            Job=Job,
            Safety=Safety,
            Supervisor=Supervisor,
            JSA=JSA,
            Risk=Risk,
            Loading=Loading,
            Emergency=Emergency,
            Incident=Incident,
            LOTO=LOTO,
            Safety1=Safety1,
            Hazard=Hazard,
            Fire=Fire,
            Electrical=Electrical,
            HotWork=HotWork,
            CHMP=CHMP,
            Ground=Ground,
            Confined=Confined,
            Fall=Fall,
            Defensive=Defensive,
            Scaffold=Scaffold,
            Flagman=Flagman,
            Auto=Auto,
            Certificate=Certificate,
            Crane=Crane,
            Rigger=Rigger,
            Hoisting=Hoisting,
            Welder=Welder,
            Diesel=Diesel,
            PPE=PPE,
            DrLicense=DrLicense,
            Qualific=Qualific,
            Heat=Heat,
            Load=Load,
            GoldenRules=GoldenRules,
            HAVS=HAVS,
            Dropped=Dropped,
            LOF=LOF,
            med=med
        ))

    for contact in contacts:
        contact.save()
    print(f"✅ {len(contacts)} ta kontakt yuklandi.")