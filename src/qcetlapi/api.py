import gsiqcetl
import pkg_resources
from flask import current_app


def cache_names():
    return [x.name for x in gsiqcetl.formats]


def etl_version():
    return pkg_resources.get_distribution('gsiqcetl').version


def cache_tables(name, version):
    cache = cache_object(name)
    if cache is None:
        return None, 404

    result = list(cache.get_tables(version).keys())
    if len(result) == 0:
        return None, 404
    else:
        return result, 200


def cache_versions(name):
    cache = cache_object(name)
    if cache is None:
        return None, 404

    return list(cache.schema_versions.keys()), 200


def get_json(name, version, table):
    cache = current_app.config['cache']
    try:
        loaded = cache.load(
            name,
            version,
            gsiqcetl.common.CleaningRules(), lambda x: None
        )
        return getattr(loaded, table).to_json(orient="records"), 200
    except KeyError:
        return None, 404


def cache_object(name):
    for f in gsiqcetl.formats:
        if f.name == name:
            return f

    return None
