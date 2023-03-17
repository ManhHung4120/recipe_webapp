# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Date,
    Boolean,
    ForeignKey,
    JSON,
    BigInteger,
    Text,
    Float,LargeBinary
)
from sqlalchemy.dialects import postgresql
from repo import db

class Category(db.Model):
    __tablename__ = 'category'

    category_id = Column(BigInteger, primary_key=True)
    category = Column(String, nullable=False)



class CategoryIngredient(db.Model):
    __tablename__ = 'category_ingredient'

    category_ingredient_id = Column(BigInteger, primary_key=True)
    category_id = Column(ForeignKey('category.category_id'))
    ingredient_id = Column(ForeignKey('ingredients.ingredient_id'))

    category = db.relationship('Category', primaryjoin='CategoryIngredient.category_id == Category.category_id', backref='category_ingredients')
    ingredient = db.relationship('Ingredient', primaryjoin='CategoryIngredient.ingredient_id == Ingredient.ingredient_id', backref='category_ingredients')



class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger)
    comment = Column(Text)
    rate = Column(Float)
    recipe_id = Column(BigInteger)



class FoodCategory(db.Model):
    __tablename__ = 'food_category'

    food_category_id = Column(BigInteger, primary_key=True)
    food_type = Column(String)



class Image(db.Model):
    __tablename__ = 'image'

    image_id = Column(BigInteger, primary_key=True)
    image = Column(LargeBinary)



class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    ingredient_id = Column(BigInteger, primary_key=True)
    ingredient_name = Column(String)
    image_id = Column(postgresql.ARRAY(String))
    nutritional_value_id = Column(BigInteger)



class MeasurementQuantity(db.Model):
    __tablename__ = 'measurement_quantities'

    measurement_qty_id = Column(BigInteger, primary_key=True)
    amount = Column(String)



class MeasurementUnit(db.Model):
    __tablename__ = 'measurement_units'

    measurement_unit_id = Column(BigInteger, primary_key=True)
    unit_name = Column(String)



class NutritionalValue(db.Model):
    __tablename__ = 'nutritional_value'

    carb = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    calories = Column(Float)
    measurement_unit_id = Column(BigInteger)
    measurement_qty_id = Column(BigInteger)
    nutritional_value_id = Column(String, primary_key=True)



class Recipe(db.Model):
    __tablename__ = 'recipe'

    recipe_id = Column(BigInteger, primary_key=True)
    recipe_name = Column(String)
    description = Column(Text)
    cuisine = Column(String)
    cook_time = Column(BigInteger)
    user_id = Column(BigInteger)



class RecipeCategory(db.Model):
    __tablename__ = 'recipe_category'

    recipe_category_id = Column(BigInteger, primary_key=True)
    food_category_id = Column(ForeignKey('food_category.food_category_id'))
    recipe_id = Column(ForeignKey('recipe.recipe_id'))

    food_category = db.relationship('FoodCategory', primaryjoin='RecipeCategory.food_category_id == FoodCategory.food_category_id', backref='recipe_categories')
    recipe = db.relationship('Recipe', primaryjoin='RecipeCategory.recipe_id == Recipe.recipe_id', backref='recipe_categories')



class RecipeIngredient(db.Model):
    __tablename__ = 'recipe_ingredients'

    recipe_ingredient_id = Column(db.BigInteger, primary_key=True)
    recipe_id = Column(ForeignKey('recipe.recipe_id'))
    ingredient_id = Column(ForeignKey('ingredients.ingredient_id'))
    measurement_unit_id = Column(ForeignKey('measurement_units.measurement_unit_id'))
    measurement_qty_id = Column(ForeignKey('measurement_quantities.measurement_qty_id'))

    ingredient = db.relationship('Ingredient', primaryjoin='RecipeIngredient.ingredient_id == Ingredient.ingredient_id', backref='recipe_ingredients')
    measurement_qty = db.relationship('MeasurementQuantity', primaryjoin='RecipeIngredient.measurement_qty_id == MeasurementQuantity.measurement_qty_id', backref='recipe_ingredients')
    measurement_unit = db.relationship('MeasurementUnit', primaryjoin='RecipeIngredient.measurement_unit_id == MeasurementUnit.measurement_unit_id', backref='recipe_ingredients')
    recipe = db.relationship('Recipe', primaryjoin='RecipeIngredient.recipe_id == Recipe.recipe_id', backref='recipe_ingredients')



class Step(db.Model):
    __tablename__ = 'step'

    step_id = Column(BigInteger, primary_key=True)
    recipe_id = Column(ForeignKey('recipe.recipe_id'))
    direction = Column(Text)
    step = Column(BigInteger)
    image_id = Column(BigInteger)

    recipe = db.relationship('Recipe', primaryjoin='Step.recipe_id == Recipe.recipe_id', backref='steps')



class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    role = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    image_id = Column(ForeignKey('image.image_id'))

    image = db.relationship('Image', primaryjoin='User.image_id == Image.image_id', backref='users')
