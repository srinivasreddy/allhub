def massage_key(key):
    return key.replace("-", "_")


def transform(class_name, json_data):
    if isinstance(json_data, list):
        instance = type(class_name, (list,), {})()
        for index, item in enumerate(json_data):
            instance.append(transform(class_name, item))
        return instance
    elif isinstance(json_data, dict):
        instance = type(class_name, (), {})
        for key, value in json_data.items():
            key = massage_key(key)
            if isinstance(value, list):
                objs = []
                for item in value:
                    objs.append(transform(key[:-1], item))
                setattr(instance, key, objs)
            elif isinstance(value, dict):
                setattr(instance, key, transform(key, value))
            else:
                setattr(instance, key, value)
        return instance
