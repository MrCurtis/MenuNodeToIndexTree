from pprint import pprint
from collections import defaultdict

menu_nodes = [{
  u'title': u'Artist interview: Doroth\xe9e Selz',
  u'nid': u'349289',
  u'parents': [{
    u'id': u'300355',
    u'level': 1,
    u'title': u'The World Goes Pop',
    u'weight': u'0'
    },{
    u'id': u'351775',
    u'level': 2,
    u'title': u'Artist interviews',
    u'weight': u'-12'}]
},
{
  u'title': u'Raimo Reinikainen',
  u'nid': u'349187',
  u'parents': [{
    u'id': u'300355',
    u'level': 1,
    u'title': u'The World Goes Pop',
    u'weight': u'0'
    },{
    u'id': u'351795',
    u'level': 2,
    u'title': u'Artist biographies',
    u'weight': u'-13'}]
},
{
  u'title': u'Artist interview: Ushio Shinohara',
  u'nid': u'351761',
  u'parents': [{
    u'id': u'300355',
    u'level': 1,
    u'title': u'The World Goes Pop',
    u'weight': u'0'
    },{
    u'id': u'351775',
    u'level': 2,
    u'title': u'Artist interviews',
    u'weight': u'-12'}]
},
{
  u'title': u'Glauco Rodrigues',
  u'nid': u'348623',
  u'parents': [{
    u'id': u'300355',
    u'level': 1,
    u'title': u'The World Goes Pop',
    u'weight': u'0'
    },{
    u'id': u'351795',
    u'level': 2,
    u'title': u'Artist biographies',
    u'weight': u'-13'}]
},
{
  u'title': u'Artist interview: Teresinha Soares',
  u'nid': u'349395',
  u'parents': [{
    u'id': u'300355',
    u'level': 1,
    u'title': u'The World Goes Pop',
    u'weight': u'0'
    },{
    u'id': u'351775',
    u'level': 2,
    u'title': u'Artist interviews',
    u'weight': u'-12'}]
},
{
  u'title': u'Peter Roehr',
  u'nid': u'349183',
  u'parents': [{
    u'id': u'300355',
    u'level': 1,
    u'title': u'The World Goes Pop',
    u'weight': u'0'
    },{
    u'id': u'351795',
    u'level': 2,
    u'title': u'Artist biographies',
    u'weight': u'-13'}]
}]

index_tree = [{
  u'title': u'The World Goes Pop',
  u'id': u'300355',
  u'level': 1,
  u'weight': u'0',
  u'children': [{
    u'id': u'351775',
    u'level': 2,
    u'title': u'Artist interviews',
    u'weight': u'-12',
    u'children': [{
      u'title': u'Artist interview: Ushio Shinohara',
      u'nid': u'351761'
      },{
      u'title': u'Artist interview: Teresinha Soares',
      u'nid': u'349395'
      }]
    },{
    u'id': u'351795',
    u'level': 2,
    u'title': u'Artist biographies',
    u'weight': u'-13',
    u'children': [{
      u'title': u'Raimo Reinikainen',
      u'nid': u'349187'
      },{
      u'title': u'Glauco Rodrigues',
      u'nid': u'348623'
      },{
      u'title': u'Peter Roehr',
      u'nid': u'349183'
      }]
    }]
  }]

def create_lookup_dict(menu_nodes):
    lookup_dict = dict()
    for node in menu_nodes:
        for parent in node["parents"]:
            lookup_dict[parent["id"]] = parent
    return lookup_dict


def make_index_dict(menu_nodes):
    index_dict = defaultdict(list)
    for node in menu_nodes:
        key = tuple(parent["id"] for parent in node["parents"])
        value = {key: val for key, val in node.items() if key != "parents"}
        index_dict[key].append(value)
    return index_dict


def merge(lookup_dict, parent_id, children):
    new_dict = lookup_dict[parent_id].copy()
    new_dict["children"] = children
    return new_dict


def merge_recurse(lookup_dict, index_dict):
    if len(index_dict) == 1:
        return index_dict
    new_index_dict = defaultdict(list)
    new_index_dict[tuple()] = index_dict[tuple()]
    for key, val in index_dict.items():
        if key != tuple():
            new_index_dict[key[:-1]].append(merge(lookup_dict, key[-1], val))
    return merge_recurse(lookup_dict, new_index_dict)



lookup_dict = create_lookup_dict(menu_nodes)
initial_index_dict = make_index_dict(menu_nodes)
processed_index_dict = merge_recurse(lookup_dict, initial_index_dict)
pprint(processed_index_dict[tuple()])

