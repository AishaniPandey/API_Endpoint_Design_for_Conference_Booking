# from pydantic import BaseModel
# from datetime import datetime
# from typing import List

# class ConferenceBase(BaseModel):
#     name: str
#     location: str
#     topics: List[str]
#     start_time: datetime
#     end_time: datetime
#     available_slots: int

# class ConferenceCreate(ConferenceBase):
#     pass

# class Conference(ConferenceBase):
#     id: int

# class UserBase(BaseModel):
#     user_id: str
#     interested_topics: List[str]

# class UserCreate(UserBase):
#     pass

# class User(UserBase):
#     id: int

from pydantic import BaseModel
from datetime import datetime
from typing import List

class ConferenceBase(BaseModel):
    name: str
    location: str
    topics: List[str]
    start_time: datetime
    end_time: datetime
    available_slots: int

class ConferenceCreate(ConferenceBase):
    pass

class Conference(ConferenceBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    user_id: str
    interested_topics: List[str]

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
