from home.models import Customer, Segments
from django.db.models.signals import pre_save, post_save, pre_init, post_init, pre_delete, post_delete, m2m_changed, class_prepared, pre_migrate, post_migrate  
from django.core.signals import request_started, request_finished, got_request_exception
from django.dispatch import receiver


# @receiver(signal=pre_save, sender=Customer)
# def customer_save_pre_handler(*args, **kwargs):
#     print("INSIDE PRE HANDLER")
   

# @receiver(signal=post_save, sender=Customer)
# def customer_save_post_handler(sender, instance, created, *args, **kwargs):
#     print("INSIDE POST HANDLER")
#     if created:
#         print(f"New record {instance.name} is created.")
#         segment = Segments.objects.filter(segment_class="A")[0]
#         segment.customers.add(instance)
#         print(f"{instance.name} added into {segment.segment_class}")
#     else:
#         print(instance.name, " is saved")

# @receiver(signal=pre_init, sender=Customer)
# def customer_init_pre_handler(*args, **kwargs):
#     print("INIT PRE HANDLER")
#     print(args, kwargs)

# @receiver(signal=post_init, sender=Customer)
# def customer_init_post_handler(*args, **kwargs):
#     print("INIT POST HANDLER")
#     print(args, kwargs)

# @receiver(signal=pre_delete, sender=Customer)
# def customer_delete_pre_handler(*args, **kwargs):
#     print("DELETE PRE HANDLER")
#     print(args, kwargs)

# @receiver(signal=post_delete, sender=Customer)
# def customer_delete_post_handler(*args, **kwargs):
#     print("DELETE POST HANDLER")
#     print(args, kwargs)

# @receiver(signal=m2m_changed, sender=Segments.customers.through)
# def handle_customer_change(*args,**kwargs):
#     print("INSIDE CUSTOMER CHANGE")
#     print(args, kwargs)

# @receiver(signal=class_prepared)
# def handle_class_prepared(*args, **kwargs):
#     print("INSIDE CLASS PREPARED")
#     print(args, kwargs)


# @receiver(signal=pre_migrate)
# def pre_migrate_handler(*args, **kwargs):
#     print("INSIDE PRE MIGRATE")
#     print(args, kwargs)

# @receiver(signal=post_migrate)
# def pre_migrate_handler(*args, **kwargs):
#     print("INSIDE POST MIGRATE")
#     print(args, kwargs)

@receiver(request_started)
def request_started_handler(*args, **kwargs):
    print("INSIDE REQUEST STARTED")
    print(args, kwargs)

@receiver(request_finished)
def request_started_handler(*args, **kwargs):
    print("INSIDE REQUEST FINISHED")
    print(args, kwargs)


@receiver(got_request_exception)
def request_started_handler(*args, **kwargs):
    print("INSIDE REQUEST EXCEPTION")
    print(args, kwargs)

#pre_save.connect(receiver=customer_save_pre_handler, sender=Customer)
#post_save.connect(receiver=customer_save_post_handler, sender=Customer)