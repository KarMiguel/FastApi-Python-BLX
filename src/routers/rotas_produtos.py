from fastapi import APIRouter,status,  Depends, HTTPException
from src.schemas.schemas import Produto, ProdutoOut,ProdutoEditar,ProdutoSimples, Usuario
from src.infra.sqlalchemy.repositorios.repositorioProduto import RepositorioProduto
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.config.database import get_db 
from src.routers.auth_utils import obter_usuario_logado

router = APIRouter()

@router.post('/produtos',status_code=status.HTTP_201_CREATED,response_model=ProdutoOut)
def criar_produto(produto: Produto,usuario = Depends(obter_usuario_logado), db:Session = Depends(get_db)):
    produto.usuario_id =usuario.id
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@router.get('/produtos',status_code=status.HTTP_200_OK, response_model=List[ProdutoOut])
def listar_produto(db:Session = Depends(get_db)):
   produto_listar  = RepositorioProduto(db).listar()
   return produto_listar

@router.put('/produtos/{id}',response_model=ProdutoSimples)
def atualizar_produto(id:int,produto: ProdutoEditar, session :Session = Depends(get_db)):
    RepositorioProduto(session).editar(id,produto)
    produto.id =id
    return produto

@router.delete('/produtos/{id}')
def remover_produto(id:int, session :Session = Depends(get_db)):
    RepositorioProduto(session).remover(id)
    return {"Produto":"Removido com Sucesso"}

@router.get('/meus_produtos',response_model=list[ProdutoOut])
def exibr_produto_Id(usuario: Usuario = Depends(obter_usuario_logado), session: Session=Depends(get_db)):
    produto_localizado = RepositorioProduto(session).buscarPorId(usuario.id)
    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'Não há um produto com id = {id}')
    return produto_localizado

