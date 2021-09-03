from django.contrib.auth.models import User

def reg(request):
    email = request.GET.get("email") or ""
    if email:
        email = email.lower()
    user = User.objects.create_user(
                email=email,
                defaults=dict(
                    membership_platform_type=User.MEMBERSHIP_PLATFORM_DIRECT,
                    full_name=email[:email.find("@")],
                    created_at=now,
                    updated_at=now,
                    moderation_status=User.MODERATION_STATUS_INTRO,
                ),
            )

    # At this point, user is a User object that has already been saved
    # to the database. You can continue to change its attributes
    # if you want to change other fields.
    user.save()

    return HttpResponse("[ok]", status=200)
