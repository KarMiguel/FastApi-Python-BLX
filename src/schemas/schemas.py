from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


class ProdutoSimples (BaseModel):
    id:int 
    nome:str
    preco: float
    disponivel: bool
       
    class config():
        from_attributes = True

class Usuario (BaseModel):
    nome:str
    senha:str
    telefone:str
    produtos: List['ProdutoSimples'] = []
    
    class config():
        from_attributes = True

class UsuarioOut (Usuario):
    id: int 

class UsuarioSimples (BaseModel):
    id: int | None=None
    nome:str    
    telefone:str
    
    
    class config():
        from_attributes = True

class Produto (BaseModel):
    nome:str
    detalhes:str
    preco:float
    disponivel: bool = False
    usuario_id:int | None = None 
    
    class config():
        from_attributes = True

class ProdutoEditar (Produto):
    id:int | None=None

    class config():
        from_attributes = True  

class ProdutoOut (ProdutoEditar):
    usuario : UsuarioSimples
       
    class config():
        from_attributes = True


class Pedido (BaseModel):
    id:int | None = None
    quantidade:int
    tipo_entrega : str
    local_entrega: str | None = None
    observacao : str | str = 'Sem Observações'

    usuario_id:int | None = None 
    produto_id:int | None = None 

    usuario : UsuarioSimples  | None = None
    produto : ProdutoSimples  | None = None
    
    class config():
        from_attributes = True
        
class LoginData(BaseModel):
    senha:str
    telefone:str

class LoginSucesso(BaseModel):
    usuario: UsuarioSimples
    access_token: str

