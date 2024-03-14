class StateManager:
    def __init__(self):
        self.states = {}
        self.active_state = None

    def add_state(self, name, class_state):
        self.states[name] = class_state

    def change_state(self, name, reset=False):
        if reset or self.active_state is None:
            # Cria uma nova instância do estado se for para resetar ou se ainda não há um estado ativo
            self.active_state = self.states[name](self)
        else:
            if self.active_state:
                self.active_state.exit()
            self.active_state = self.states[name](self)
        self.active_state.enter()

    def update(self, dt):
        if self.active_state:
            self.active_state.update(dt)

    def draw(self, surface):
        if self.active_state:
            self.active_state.draw(surface)
