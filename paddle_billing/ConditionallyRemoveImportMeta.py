from dataclasses import fields

from paddle_billing.RecursivelyRemoveKey import recursively_remove_key


def conditionally_remove_import_meta(entity_class, data: dict):
    """
    Paddle sends us import_meta in the data, but not all Entities support this, causing dynamic class instantiation
    to break. We selectively remove import_meta if the target Entity class doesn't define it.
    """
    import_meta_in_class = 'import_meta' in [field.name for field in fields(entity_class)]
    import_meta_in_data  = 'import_meta' in data['data']
    if not import_meta_in_class and import_meta_in_data:
        recursively_remove_key(data, 'import_meta')
