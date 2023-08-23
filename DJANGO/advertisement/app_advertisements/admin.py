from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price", "created_at", "auction"]
    list_filter = ["auction", "created_at"]
    actions = ["make_auction_as_false", "make_auction_as_true"]
    fieldsets = (
        ("Общие", {"fields": ("title", "description")}),
        ("Финансы", {"fields": ("price", "auction")})
    )

    @admin.action(description="Убрать возможность тогра")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность тогра")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisements, AdvertisementAdmin)