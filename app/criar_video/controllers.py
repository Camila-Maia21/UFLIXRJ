from app.criar_video.model import Video
from app.criar_disciplina.model import CriarDisciplina
from app.extensions import db
from flask import request, render_template, redirect
from flask.views import MethodView

class VideoDetails(MethodView): #/video/<int:id>
    def get(self, id):
        id_video = id
        videos = Video.query.filter_by(id = id_video).first()
        return render_template("video/video.html", videos = videos)


class VideoCreate(MethodView): #/video/create/<int:materia_id>
    def get(self, materia_id):
        return render_template("AdicionarVideo/adicionarvideo.html", materia = materia_id) 

    def post(self, materia_id): 
        data = request.form

        nome = data['nome']
        descricao = data['descricao']
        link = data['link']
        materia = materia_id

        if not isinstance(nome, str) or not isinstance(descricao, str):
            return {"error" : "Algum tipo invalido"}, 400
        
        linkcerto = link.replace("watch?v=", "embed/")
        video = Video(nome=nome, descricao=descricao , link=linkcerto, criardisciplina_id=materia)

        db.session.add(video)
        db.session.commit()

        print(video.criardisciplina_id)
        
        return redirect ("/materia/"+  str(materia_id))
        
class VideoEdit(MethodView): #/video/edit/<int:id>
    def get(self,id):
        video = Video.get_or_404(id)
        return video.json(),200

    def put(self,id):
        video = Video.get_or_404(id)
        data = request.json      
        nome = data['nome']
        descricao = data['descricao']
        link = data['link']
        
        video.nome = nome
        video.descricao = descricao
        video.link = link
        
        db.session.commit()
        return video.json() , 200

    def patch(self,id):
        video = Video.query.get_or_404(id)
        dados = request.json 

        data = request.json    

        nome = data['nome', video.nome]
        descricao = data['descricao', video.descricao]
        link = data['link', video.link]       

        video.nome = nome
        video.descricao = descricao
        video.link = link

        db.session.commit()
        return video.json() , 200

    def delete(self,id):
        video = Video.query.get_or_404(id)
        db.session.delete(video)
        db.session.commit()
        return video.json(), 200
