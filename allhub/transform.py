def transform(class_name, json_data):
    if isinstance(json_data, list):
        instance = type(class_name, (list,), {})()
        for item in json_data:
            instance.append(transform(class_name[:-1], item))
        return instance
    elif isinstance(json_data, dict):
        instance = type(class_name, (dict,), {})()
        for key, value in json_data.items():
            if isinstance(value, list):
                objs = []
                for item in value:
                    objs.append(transform(key[:-1], item))
                setattr(instance, key, objs)
                instance[key] = objs
            elif isinstance(value, dict):
                _transform = transform(key, value)
                if "-" not in key:  # setting "name-key" fails on an object.
                    setattr(instance, key, _transform)
                instance[key] = _transform
            else:
                if "-" not in key:  # setting "name-key" fails on an object.
                    setattr(instance, key, value)
                instance[key] = value
        return instance
