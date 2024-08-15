from ninja import Router
from typing import List
from .schema import WaitlistEntryListSchema, WaitlistEntryDetailSchema
from .models import WaitlistEntry
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth

router = Router()

@router.get("", response=List[WaitlistEntryListSchema], auth=JWTAuth())
def list_waitlist_entries(request):
    return WaitlistEntry.objects.all()

@router.get("{entry_id}", response=WaitlistEntryDetailSchema)
def get_waitlist_entry(request, entry_id: int):
    return get_object_or_404(WaitlistEntry, id=entry_id)