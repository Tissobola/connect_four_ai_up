class Utils:
    def opponent(player):
        if player == 1:
            return 2
        elif player == 2:
            return 1
        
_inst = Utils
opponent = _inst.opponent