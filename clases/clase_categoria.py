class clsCategoria:
    id = 0
    categoria = ""
    diccategoria = {}

    def __init__(self,p_id,p_categoria):
        self.id = p_id
        self.categoria = p_categoria
        self.diccategoria={
            "id": p_id,
            "categoria"  : p_categoria
        } 