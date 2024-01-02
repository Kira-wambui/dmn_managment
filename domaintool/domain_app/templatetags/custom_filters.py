from django import template
from datetime import datetime, timedelta, timezone

register = template.Library()

@register.filter(name='days_remaining')
def days_remaining(expiry_date):
    if isinstance(expiry_date, datetime):
        # If expiry_date is already a datetime object, no need to convert
        current_date = datetime.now(expiry_date.tzinfo)
    else:
        # Convert expiry_date to datetime object with timezone info
        expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        current_date = datetime.now(expiry_date.tzinfo)

    remaining_days = (expiry_date - current_date).days
    return remaining_days