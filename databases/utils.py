from databases.manager import CategoryManager




def get_category():
    name = ["Vivo","Matarolla"]
    category = CategoryManager.insert_category(name)