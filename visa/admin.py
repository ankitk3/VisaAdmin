from django.contrib import admin
from visa.models import Countries,Cities,BookingPassengers,BookingVisaDetails,BookingPricing,CountriesHasVendors,Documents
from visa.models import TypeOfVisas, TypeOfVisasDocuments,VendorRoe,Vendors,VisaBooking,VisaPrice,Visas

#Registering models here
class CountriesAdmin(admin.ModelAdmin):
    pass
class CitiesAdmin(admin.ModelAdmin):
    pass
class BookingPassengersAdmin(admin.ModelAdmin):
    pass
class BookingVisaDetailsAdmin(admin.ModelAdmin):
    pass
class BookingPricingAdmin(admin.ModelAdmin):
    pass
class CountriesHasVendorsAdmin(admin.ModelAdmin):
    pass
class DocumentsAdmin(admin.ModelAdmin):
    pass
class TypeOfVisasAdmin(admin.ModelAdmin):
    pass
class TypeOfVisasDocumentsAdmin(admin.ModelAdmin):
    pass
class VendorRoeAdmin(admin.ModelAdmin):
    pass
class VendorsAdmin(admin.ModelAdmin):
    pass
class VisaBookingAdmin(admin.ModelAdmin):
    pass
class VisaPriceAdmin(admin.ModelAdmin):
    pass
class VisasAdmin(admin.ModelAdmin):
    pass
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(BookingVisaDetails, BookingVisaDetailsAdmin)
admin.site.register(BookingPricing, BookingPricingAdmin)
admin.site.register(CountriesHasVendors, CountriesHasVendorsAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(TypeOfVisas, TypeOfVisasAdmin)
admin.site.register(TypeOfVisasDocuments, TypeOfVisasDocumentsAdmin)
admin.site.register(VendorRoe, VendorRoeAdmin)
admin.site.register(Vendors, VendorsAdmin)
admin.site.register(VisaBooking, VisaBookingAdmin)
admin.site.register(VisaPrice, VisaPriceAdmin)
admin.site.register(Visas, VisasAdmin)