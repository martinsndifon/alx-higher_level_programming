#!/usr/bin/python3

"""The base class for this project"""
import json
import csv
import turtle


class Base:
    """The base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if not list_objs:
            with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
                f.write("[]")
        else:
            res = []
            for obj in list_objs:
                res.append(obj.to_dictionary())
            with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(res))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the json string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        fake = None
        if cls.__name__ == "Rectangle":
            fake = cls(2, 2)
        else:
            fake = cls(3)
        fake.update(**dictionary)
        return fake

    @classmethod
    def load_from_file(cls):
        """Converts json file to list of instances"""
        instances = []
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                items = cls.from_json_string(f.read())
                for i in items:
                    instances.append(cls.create(**i))
            return instances
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""
        with open(cls.__name__ + ".csv", "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """converts csv file to list of objects"""
        try:
            with open(cls.__name__ + ".csv", "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the Rectangles and Squares using the turtle module"""
        tk = turtle.Turtle()
        tk.screen.bgcolor("#de912c")
        tk.pensize(3)
        tk.shape("turtle")

        tk.color("#f129f2")
        for rect in list_rectangles:
            tk.showturtle()
            tk.up()
            tk.goto(rect.x, rect.y)
            tk.down()
            for _ in range(2):
                tk.forward(rect.width)
                tk.left(90)
                tk.forward(rect.height)
                tk.left(90)
            tk.hideturtle()

        tk.color("#b7e328")
        for sq in list_squares:
            tk.showturtle()
            tk.up()
            tk.goto(sq.x, sq.y)
            tk.down()
            for _ in range(2):
                tk.forward(sq.width)
                tk.left(90)
                tk.forward(sq.height)
                tk.left(90)
            tk.hideturtle()

        turtle.exitonclick()
