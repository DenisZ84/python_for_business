from rest_framework import viewsets
from rest_framework.decorators import action
import openpyxl
from openpyxl.writer.excel import save_virtual_workbook
from django.http import HttpResponse
from django.db.models import F

from api.serializers import UsCitySerializer, UsFuelSerializer
from api.services import get_enum_value, TimestampToIST, TimestampToStr
from us_fuels.models import UsFuel, USCity
from us_fuels.enums import Fuels


class UsFuelViewSet(viewsets.ModelViewSet):
    serializer_class = UsFuelSerializer
    queryset = UsFuel.objects

    def get_export_queryset(self):
        return self.queryset.annotate(
            fuel_name=get_enum_value(F('fuel'), Fuels),
            rus_date=TimestampToStr(TimestampToIST(F('date'))),             
        ).values_list('city_slug', 'fuel_name', 'price', 'rus_date' ).all()

    def create_excel(self):
        wb = openpyxl.Workbook()
        list_wb = wb.active
        list_wb.append(['Город', 'Топливо', 'Цена', 'Дата'])
        for row in self.get_export_queryset():
            list_wb.append(row)
        return save_virtual_workbook(wb)

    @action(detail=False, methods=['get'], url_path='export')
    def export_excel(self, request):
        response = HttpResponse(
            self.create_excel(), content_type='application/ms-excel',
        )
        response['Content-Disposition'] = 'attachment; filename=export.xlsx'
        return response


class UsCityViewSet(viewsets.ModelViewSet):
    serializer_class = UsCitySerializer
    queryset = USCity.objects.all()