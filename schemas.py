"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
Each Pydantic model represents a collection in your database.
Class name lowercased -> collection name (Lead -> "lead").
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    name: str = Field(..., description="Full name")
    email: EmailStr = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")


class Product(BaseModel):
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in EUR")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")


# Lead schema for quiz + contact capture
class Lead(BaseModel):
    metri: Optional[str] = Field(None, description="Metri quadri da ristrutturare (testo libero)")
    stanze: Optional[str] = Field(None, description="Numero stanze principali (testo libero)")
    livello: Optional[str] = Field(None, description="Livello finiture desiderato")
    nome: str = Field(..., description="Nome e cognome")
    email: EmailStr = Field(..., description="Email")
    telefono: str = Field(..., description="Numero di telefono")
    stima: Optional[str] = Field(None, description="Stima calcolata lato frontend in EUR formattati")
