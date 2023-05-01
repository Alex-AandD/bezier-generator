from typing import Tuple, Type

class Vector2:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def to_tuple(self, v) -> Tuple[int, int]:
        return self.x, self.y

    def __mul__(self, other) -> Type["Vector2"]:
        if type(other) == int or type(other) == float:
            x = other * self.x
            y = other * self.y
            return Vector2(x, y)
        
        new_vx = self.x * other.x
        new_vy = self.y * other.y
        return Vector2(new_vx, new_vy)
    
    def __add__(self, other: Type["Vector2"]) -> Type["Vector2"]:
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"({self.x}, {self.y})"