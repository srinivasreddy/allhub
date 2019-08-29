def massage_key(key):
    return key.replace("-", "_")


def transform(class_name, json_data):
    if isinstance(json_data, list):
        instance = type(class_name, (list,), {})()
        for item in json_data:
            instance.append(transform(class_name, item))
        return instance
    elif isinstance(json_data, dict):
        instance = type(class_name, (dict,), {})
        for key, value in json_data.items():
            key = massage_key(key)
            if isinstance(value, list):
                objs = []
                for item in value:
                    objs.append(transform(key[:-1], item))
                setattr(instance, key, objs)
                instance[key] = objs
            elif isinstance(value, dict):
                _transform = transform(key, value)
                setattr(instance, key, _transform)
                instance[key] = _transform
            else:
                setattr(instance, key, value)
                instance[key] = value
        return instance
