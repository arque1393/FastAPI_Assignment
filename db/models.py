from sqlalchemy import (Column, ForeignKey, Integer, String,DateTime)
from sqlalchemy.orm import relationship
from datetime import datetime
from db._setup import Base

'''This module contains All the SQLAlchemy Database Schemas or Model
'''
class Admin(Base): 
    __tablename__ = "admin"
    admin_id = Column(Integer, primary_key= True)
    email = Column(String(100),unique=True, index= True, nullable= False )
    _password = Column(String(100), nullable=False)
    quiz= relationship('Quiz', back_populates='admin')

class Quiz(Base):
    __tablename__ = 'quiz'
    
    quiz_id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, ForeignKey('admin.admin_id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    # created_at = Column(DateTime, default=datetime.utcnow)
    admin = relationship('Admin', back_populates='quiz')
    question= relationship("Question", back_populates="quiz", cascade="all, delete-orphan")
    scores = relationship('Score', back_populates='quiz')
class Question(Base):
    __tablename__ = 'question'
    
    question_id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quiz.quiz_id'), nullable=False)
    text = Column(String, nullable=False)
    option1 = Column(String, nullable=False)
    option2 = Column(String, nullable=False)
    option3 = Column(String, nullable=False)
    option4 = Column(String, nullable=False)
    correct_option = Column(String, nullable=False)
    
    quiz = relationship('Quiz', back_populates='question')

class Participant(Base):
    __tablename__ = 'participant'
    
    participant_id = Column(Integer, primary_key=True)
    _password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    scores = relationship('Score', back_populates='participant')

class Score(Base):
    __tablename__ = 'score'
    
    score_id = Column(Integer, primary_key=True)
    participant_id = Column(Integer, ForeignKey('participant.participant_id'), nullable=False)
    quiz_id = Column(Integer, ForeignKey('quiz.quiz_id'), nullable=False)
    score = Column(Integer, nullable=False)
    
    participant = relationship('Participant', back_populates='scores')
    quiz = relationship('Quiz', back_populates='scores')


