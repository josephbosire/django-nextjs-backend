from ninja import Router
from typing import List
from .schema import WaitlistEntryListSchema, ErrorWaitlistEntryCreateSchema, WaitlistEntryDetailSchema, WaitlistEntryCreateSchema
from .models import WaitlistEntry
from django.shortcuts import get_object_or_404
from ninja_jwt.authentication import JWTAuth
from .forms import WaitlistEntryCreateForm
import helpers
import json

router = Router()

@router.get("", response=List[WaitlistEntryListSchema], auth=helpers.api_auth_user_required)
def list_waitlist_entries(request):
    return WaitlistEntry.objects.filter(user=request.user)

@router.get("{entry_id}", response=WaitlistEntryDetailSchema, auth=helpers.api_auth_user_required)
def get_waitlist_entry(request, entry_id: int):
    return get_object_or_404(WaitlistEntry, id=entry_id, user=request.user)

@router.post("", response={200: WaitlistEntryDetailSchema, 400: ErrorWaitlistEntryCreateSchema}, auth=[JWTAuth(), helpers.api_auth_user_or_annonymous])
def create_waitlist_entry(request, data: WaitlistEntryCreateSchema):
    form = WaitlistEntryCreateForm(data.dict())
    if not form.is_valid():
        form_errors = json.loads(form.errors.as_json())
        return 400, form_errors
    new_waitlist_entry = form.save(commit=False)
    if request.user.is_authenticated:
        new_waitlist_entry.user = request.user
    new_waitlist_entry.save()
    return new_waitlist_entry

