from vuex import Store

def increment(state):
    state.counter = state.counter + 1

def createStore():
    return Store(
      state={'counter': 0},
      mutations={'increment': increment}
    )

__default__ = createStore