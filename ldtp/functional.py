import client

def whoismyhost():
    return client._client._ServerProxy__host

def launchapp(cmdline):
    return client._client.launchapp(cmdline)

def guiexist(gui_name, object_name=''):
    return client._client.guiexist(gui_name, object_name)

def waittillguiexist(gui_name, object_name='', timeout=5):
    return client._client.waittillguiexist(gui_name, object_name, timeout)

def waittillguinotexist(gui_name, timeout=5):
    return client._client.waittillguinotexist(gui_name, timeout)

def selectmenuitem(gui_name, heirarchy):
    return client._client.selectmenuitem(gui_name, heirarchy)

def click(gui_name, obj_name):
    return client._client.click(gui_name, obj_name)

def getobjectlist(window_name):
    return client._client.getobjectlist(window_name)

def getobjectinfo(gui_name, obj_name):
    return client._client.getobjectinfo(gui_name, obj_name)

def getobjectproperty(gui_name, obj_name, prop):
    return client._client.getobjectproperty(gui_name, obj_name, prop)
