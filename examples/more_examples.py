import dataclasses
import time
from copy import copy

from stf.base import BaseTransform

TRANSFORM_MAP = {
            'hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                            'extract': 'name', 'distinct': True},
            'non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                'extract': 'name'},
            'bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                         'extract': '*'},
            '1hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                            'extract': 'name', 'distinct': True},
            '1non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                'extract': 'name'},
            '1bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                         'extract': '*'},
            '2hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                            'extract': 'name', 'distinct': True},
            '2non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                'extract': 'name'},
            '2bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                         'extract': '*'},
            '5hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                            'extract': 'name', 'distinct': True},
            '5non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                'extract': 'name'},
            '5bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                         'extract': '*'},
            '51hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                             'extract': 'name', 'distinct': True},
            '51non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                 'extract': 'name'},
            '51bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                          'extract': '*'},
            '52hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                             'extract': 'name', 'distinct': True},
            '52non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                 'extract': 'name'},
            '52bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                          'extract': '*'},
            '53hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                            'extract': 'name', 'distinct': True},
            '53non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                'extract': 'name'},
            '53bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                         'extract': '*'},
            '21hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                             'extract': 'name', 'distinct': True},
            '21non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                 'extract': 'name'},
            '21bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                          'extract': '*'},
            '22hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                             'extract': 'name', 'distinct': True},
            '22non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                 'extract': 'name'},
            '22bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                          'extract': '*'},
            '3hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                            'extract': 'name', 'distinct': True},
            '3non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                'extract': 'name'},
            '3bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                         'extract': '*'},
            '31hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                             'extract': 'name', 'distinct': True},
            '31non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                 'extract': 'name'},
            '31bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                          'extract': '*'},
            '32hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                             'extract': 'name', 'distinct': True},
            '32non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                 'extract': 'name'},
            '32bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1',
                          'extract': '*'},
        }


async def amain():
    start_time = time.time()
    p = Parse()
    p.categories = []
    p.categories.append({'sortkey': 'DMG', 'hidden': '', 'name': 'DEF'})
    p.categories.append({'sortkey': 'DMG', 'hidden': '', 'name': 'ABC'})
    p.categories.append({'sortkey': 'DMG', 'name': 'GHI'})
    t = T()
    t.parse = p

    cf = BaseTransform.get_transformer_for_type(t)
    c_data = await cf.atransform(
        {
            'hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""', 'extract': 'name', 'distinct': True},
            'non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""', 'extract': 'name'},
            'bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1', 'extract': '*'},
        }
    )
    print(c_data)
    print("Async 1 time: ", time.time() - start_time)

    c_data = await cf.atransform(
        {
            'hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""',
                            'extract': 'name', 'distinct': True},
            'non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""',
                                'extract': 'name'},
            'bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1', 'extract': '*'},
        }
    )
    print(c_data)
    print("Async 2 time: ", time.time() - start_time)


def main():
    start_time = time.time()
    p = Parse()
    p.categories = []
    p.categories.append({'sortkey': 'DMG', 'hidden': '', 'name': 'DEF'})
    p.categories.append({'sortkey': 'DMG', 'hidden': '', 'name': 'ABC'})
    p.categories.append({'sortkey': 'DMG', 'name': 'GHI'})
    t = T()
    t.parse = p

    cf = BaseTransform.get_transformer_for_type(t)
    c_data = cf.single_transform(copy(TRANSFORM_MAP))
    print(c_data)
    print("Sync time", time.time() - start_time)


def threaded_main():
    start_time = time.time()
    p = Parse()
    p.categories = []
    p.categories.append({'sortkey': 'DMG', 'hidden': '', 'name': 'DEF'})
    p.categories.append({'sortkey': 'DMG', 'hidden': '', 'name': 'ABC'})
    p.categories.append({'sortkey': 'DMG', 'name': 'GHI'})
    t = T()
    t.parse = p

    cf = BaseTransform.get_transformer_for_type(t)
    c_data = cf.transform(copy(TRANSFORM_MAP))
    print(c_data)
    print("Threaded time", time.time() - start_time)

# with open(sys.argv[1]) as jfp, open(sys.argv[2]) as xfp:
    #     jf = JSONTransform(jfp.read())
    #     json_data = {
    #         'hidden_keys': jf.select('parse.categories', 'hidden == ""', 'sortkey', distinct=True),
    #         'non_hidden_keys': jf.select('parse.categories', 'hidden != ""', '*'),
    #         'bad_keys': jf.select('parse.categories', 'hidden > 1', '*'),
    #     }
    #     print(json_data)
    #
    #     j_data = jf.transform(
    #         {
    #             'hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""', 'extract': 'sortkey', 'distinct': True},
    #             'non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""', 'extract': '*'},
    #             'bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1', 'extract': '*'},
    #         }
    #     )
    #     print(j_data)
    #     print(json_data == j_data)
    #
    #     jf.set_output('xml')
    #     j_data = jf.transform(
    #         {
    #             'HiddenKeys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""', 'extract': 'sortkey', 'distinct': True},
    #             'NonHiddenKeys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""', 'extract': '*'},
    #             'BadKeys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1', 'extract': '*'},
    #         }
    #     )
    #     print(j_data)
    #
    #     jy_data = jf.transform(
    #         {
    #             'HiddenKeys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""', 'extract': 'sortkey', 'distinct': True},
    #             'NonHiddenKeys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""', 'extract': '*'},
    #             'BadKeys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1', 'extract': '*'},
    #         },
    #         output='yaml'
    #     )
    #     print(jy_data)
    #
    #     tc = TestClass()
    #     tc_data = jf.transform(
    #         {
    #             'hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden == ""', 'extract': 'sortkey', 'distinct': True},
    #             'non_hidden_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden != ""', 'extract': '*'},
    #             'bad_keys': {'action': 'select', 'filter': 'parse.categories', 'criteria': 'hidden > 1', 'extract': '*'},
    #         },
    #         output=tc
    #     )
    #     print(tc)
    #
    #     xf = XMLTransform(xfp.read())
    #
    #     xml_data = {
    #         'hidden_keys': xf.select('api.parse.categories.cl', '@hidden == ""', '@sortkey', distinct=True),
    #         'non_hidden_keys': xf.select('api.parse.categories.cl', '@hidden != ""', '#text'),
    #         'bad_keys': xf.select('api.parse.categories.cl', '@hidden > 1', '*'),
    #         'non_existent_keys': xf.select('parse.api', '@hidden == ""'),
    #         'non_existent_extract': xf.extract('parse.api'),
    #     }
    #     print(xml_data)
    #
    #     print(json_data == xml_data)
    #
    #     xfp.seek(0)
    #     xfx = XMLTransform(xfp.read())
    #
    #     xml_data = {
    #         'HiddenKeys': xfx.select('api.parse.categories.cl', '@hidden == ""', '@sortkey', distinct=True),
    #         'NonHiddenKeys': xfx.select('api.parse.categories.cl', '@hidden != ""', '#text'),
    #         'BadKeys': xfx.select('api.parse.categories.cl', '@hidden > 1', '*'),
    #     }
    #     print(dicttoxml(xml_data))
    #
    #     print(dicttoxml(xml_data) == j_data)
    #
    #     print(yaml.dump(xml_data))


if __name__ == '__main__':
    @dataclasses.dataclass(slots=True)
    class TestClass:
        hidden_keys: list[str] = dataclasses.field(default_factory=list)
        non_hidden_keys: list[str] = dataclasses.field(default_factory=list)
        bad_keys: list[str] = dataclasses.field(default_factory=list)

    class Parse:
        categories = dataclasses.field(default_factory=list)

    class T:
        parse = None

    # asyncio.run(amain())

    # main()
    threaded_main()