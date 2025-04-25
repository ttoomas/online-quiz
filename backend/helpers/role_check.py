from helpers.socketio import sio

def only_admin(func):
    def wrapper(sid, *args, **kwargs):
        role = sio.get_session(sid)["role"]

        if role == "admin":
            func(sid, *args, **kwargs)
        else:
            raise Exception("Unauthorized")
            
    return wrapper

def only_player(func):
    def wrapper(sid, *args, **kwargs):
        role = sio.get_session(sid)["role"]

        if role == "player":
            func(sid, *args, **kwargs)
        else:
            raise Exception("Unauthorized")
            
    return wrapper
    
def get_role(sid):
    role = sio.get_session(sid)["role"]

    return role