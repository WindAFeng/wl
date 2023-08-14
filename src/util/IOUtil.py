import json
import yaml


def readJsonFileToDict(path: str) -> dict:
    """
    读取文本文件,文件内容应该符合JSON格式,方法会返回一个dict对象

    参数:
    path (str): 文件相对于主程序(main)的路径

    返回:
    data (dict): 从文件中读取出的dict对象
    """
    with open(path, 'r', encoding='utf-8') as f:
        tmp = json.load(f)
    return tmp


def saveDictDataToJson(path: str, data: dict):
    """
    把dict对象转变成json格式的文本字符串,存入到指定的文件中(.json)

    参数:
    path (str): 文件相对于主程序(main)的路径
    data (dict): 要保存的字典对象
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    return


def readYamlFileToDict(path: str) -> dict:
    """
    读取文本文件,文件内容应该符合YAML格式,方法会返回一个dict对象

    参数:
    path (str): 文件相对于主程序(main)的路径

    返回:
    data (dict): 从文件中读取出的dict对象
    """
    with open(path, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


def saveDictDataToYaml(path: str, data: dict):
    """
    把dict对象转变成yaml格式的文本字符串,存入到指定的文件中(.yml)

    参数:
    path (str): 文件相对于主程序(main)的路径
    data (dict): 要保存的字典对象
    """
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)
