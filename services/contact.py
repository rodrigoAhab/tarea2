from flask import Blueprint, request, jsonify
from model.contact import Predio
from utils.db import db

predio= Blueprint('predio',__name__)

@predio.route('/predios/v1', methods=['GET'])
def getMensaje():
    result={}
    result["data"]='tarea2'
    return jsonify(result)

@predio.route('/predios/v1/listar', methods=['GET'])
def getContactos():
    result={}
    predios= Predio.query.all()
    result["data"]=predios
    result["status_code"]=200
    result["msg"]="Se recupero los datos sin inconvenientes"
    return jsonify(result),200

@predio.route('/predios/v1/insert', methods=['POST'])
def insert():
    result={}
    body=request.get_json()
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    id_persona=body.get('id_persona')
    url_imagen=body.get('url_imagen')

    if not id_tipo_predio or not descripcion or not ruc or not telefono or not correo or not direccion:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    predio=Predio(id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo, id_persona,url_imagen)
    db.session.add(predio)
    db.session.commit()
    result["data"]=predio
    result["status_code"]=201
    result["msg"]="Se agrego predio"
    return jsonify(result),201

@predio.route('/predios/v1/update', methods=['POST'])
def update():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')
    id_tipo_predio=body.get('id_tipo_predio')
    descripcion=body.get('descripcion')
    ruc=body.get('ruc')
    telefono=body.get('telefono')
    correo=body.get('correo')
    direccion=body.get('direccion')
    idubigeo=body.get('idubigeo')
    id_persona=body.get('id_persona')
    url_imagen=body.get('url_imagen')

    if not id_predio or not id_tipo_predio or not descripcion or not ruc or not telefono or not  correo or not direccion:
        result["status_code"]=400
        result["msg"]="Faltan datos"
        return jsonify(result),400
    
    predio=Predio.query.get(id_predio)
    if not predio:
        result["status_code"]=400
        result["msg"]="Predio no existe"
        return jsonify(result),400
    
    predio.id_tipo_predio= id_tipo_predio
    predio.descripcion= descripcion
    predio.ruc= ruc
    predio.telefono= telefono
    predio.correo= correo
    predio.direccion= direccion
    predio.idubigeo= idubigeo
    predio.id_persona= id_persona
    predio.url_imagen= url_imagen
    db.session.commit()


    result["data"]=predio
    result["status_code"]=202
    result["msg"]="Se modifico predio"
    return jsonify(result),202

@predio.route('/predios/v1/delete', methods=['DELETE'])
def delete():
    result={}
    body=request.get_json()
    id_predio=body.get('id_predio')
    if not id_predio :
        result["status_code"]=400
        result["msg"]="ID no valido"
        return jsonify(result),400
    
    predio=Predio.query.get(id_predio)
    if not predio:
        result["status_code"]=400
        result["msg"]="Contacto no existe"
        return jsonify(result),400
    
    db.session.delete(predio)
    db.session.commit()

    result["data"]=predio
    result["status_code"]=200
    result["msg"]="Se elimino el predio"
    return jsonify(result),200