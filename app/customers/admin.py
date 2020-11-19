import csv
from datetime import datetime
from io import TextIOWrapper
from django import forms
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect

from .models import Order, Customer

admin.site.register(Order)


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    change_list_template = "customers/customers_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            form = CsvImportForm(request.POST, request.FILES)
            if form.is_valid():
                file = TextIOWrapper(request.FILES["csv_file"].file, encoding='UTF-8')
                records = csv.reader(file)
                next(records)
                for line in records:
                    input_data = Customer()
                    input_data.first_name = line[0]
                    input_data.last_name = line[1]
                    input_data.birth_date = datetime.strptime(line[2], "%Y/%m/%d")
                    input_data.registration_date = datetime.strptime(line[3], "%Y/%m/%d")
                    input_data.save()

            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "customers/csv_form.html", payload
        )
