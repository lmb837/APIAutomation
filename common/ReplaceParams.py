class ReplaceParams:
    def replaceParams(data, keys, value):
        for key in keys:
            data = data.replace(key, value[key]);
        return data
