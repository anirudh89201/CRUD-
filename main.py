from fastapi import FastAPI,Depends,HTTPException,status,Response
from alchemy import engine,Base,Session,User_cred,Create;
from schema import *;
from passlib.context import CryptContext;
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
app = FastAPI();
passwd_context = CryptContext(schemes=["Bcrypt"]);
@app.get("/create_table")
def create_table():
    Base.metadata.create_all(engine);
    return {"The table is successfully created"}
@app.post("/add_user")
def add_user(post:User,db: Session=Depends(get_db)):
    post = post.dict();
    new_post = User_cred(id=post['id'],Name=post['Name'],Content=post['Content']);
    db.add(new_post);
    db.commit();
    # print(new_post);
    return {"The post is sucessfully created"};
@app.get("/get_posts")
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(User_cred).all();
    return {"The posts are:" : posts};
@app.get("/get_posts/{id}")
def get_posts_id(id:int,db: Session = Depends(get_db)):
    posts = db.query(User_cred).filter(User_cred.id == id).first();
    if not posts:
        raise HTTPException(status_code=404,detail= f"The post with particular {id} does not found")
    return{f"The post with particular {id}" : posts};
@app.get("/robots.txt")
def robots_txt():
    raise HTTPException(status_code=404);
@app.delete("/delete/{id}")
def delete_id(id:int,db : Session = Depends(get_db)):
    posts = db.query(User_cred).filter(User_cred.id == id);
    if posts.first() == None:
        raise HTTPException(status_code=404,detail = f"The post with particular {id} does not exist");
    else:
        posts.delete()
        db.commit();    
        return Response(status_code=204);        
@app.put("/update/{id}",status_code=200)
def update_id(post:User,id:int,db:Session = Depends(get_db)):
    post_query = db.query(User_cred).filter(User_cred.id == id);
    posts = post_query.first();
    if not posts:
        raise HTTPException(status_code = 404,detail = f"The post with the particular {id} does not found")
    post_query.update(post.dict());
    db.commit();
    return {"The post is successfully updated"};
# @app.post("/create",response_model=UserOut)
# def signup(post:UserCreate,db:Session = Depends(get_db)):
#     post = post.dict();
#     post['password'] = passwd_context.hash(post['password']);
#     New_User = Create(email=post['email'],password=post['password']);
#     db.add(New_User);
#     db.commit();
#     return New_User
# @app.get("/Users/{id}",response_model = UserOut)
# def sigin(id:int,db : Session = Depends(get_db)):
#     New_Post = db.query(Create).filter(Create.id == id).first();
#     if not New_Post:
#         raise HTTPException(status_code=404,detail="There is no user with that particular id");
#     return New_Post;