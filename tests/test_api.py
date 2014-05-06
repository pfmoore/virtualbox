from vbox import api

def test_found_vboxmanage():
    assert api.vboxmanage is not None
def test_found_sysprops():
    assert 'Default machine folder' in api.system_properties()

