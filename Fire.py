

from roboflow import Roboflow
rf = Roboflow(api_key="xBmQqK2pDYtvJDXn7q08")
project = rf.workspace().project("fire-8vzph")
model=project.version(1).model
model.predict("a.jpg", confidence=40).save("b.jpg")
