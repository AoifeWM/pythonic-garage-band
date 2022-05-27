# Pythonic Garage band

This is a small script which served as an introduction to object oriented programming. It defines a variety of classes which allow structures of objects to be created. The classes are:

* `band`, which holds a variety of `musician` objects
* `musician` which is a parent class for the other 3 classes:
  * `Guitarist`
  * `Drummer`
  * `Bassist`

Each of the `musician` subclasses contains unique information about the musician, like their instrument, and what their solo sounds like. Each can be initialized with a name, and the rest is done automatically. The `band` class is initialized with a name and with a number of `musician` objects as its members.